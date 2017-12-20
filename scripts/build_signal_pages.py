# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
import yaml
from glob import glob
import os
import allel
import pandas as pd
import sys
sys.path.insert(0, 'agam-report-base/src/python')
from ag1k import phase1_ar3
# setup data sources
ag1k_dir = 'ngs.sanger.ac.uk/production/ag1000g/phase1'
phase1_ar3.init(os.path.join(ag1k_dir, 'AR3'))
genome = phase1_ar3.genome
chromosomes = '2R', '2L', '3R', '3L', 'X'


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    template = env.get_template('signal.rst')

    features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    genes = features[features['type'] == 'gene']

    signals = pd.read_csv('docs/signals.csv')

    for path in sorted(glob('docs/signal/*/*/*/*/report.yml')):

        # load the basic signal report
        with open(path, mode='rb') as f:
            signal_report = yaml.load(f)

        # figure out what chromosome arm
        epicenter = signal_report['epicenter']
        # check epicenter does not span centromere - not sure how to handle that
        # case
        assert epicenter['start'][0] == epicenter['stop'][0]
        epicenter_arm = epicenter['start'][0]

        # obtain focus
        focus = signal_report['focus']
        focus_start_arm = focus['start'][0]
        focus_stop_arm = focus['stop'][0]
        focus_start = focus['start'][1]
        focus_stop = focus['stop'][1]

        # crude way to deal with rare case where focus spans centromere
        if focus_start_arm != epicenter_arm:
            focus_start = 1
        if focus_stop_arm != epicenter_arm:
            focus_stop = len(genome[epicenter_arm])

        # augment report with gene information
        overlapping_genes = genes[(
            (genes.seqid == epicenter_arm) &
            (genes.start <= focus_stop) &
            (genes.end >= focus_start)
        )]

        signal_report['overlapping_genes'] = [
            {'id': gene.ID,
             'name': gene.Name,
             'description': gene.description.split('[Source:')[0].strip()}
            for _, gene in overlapping_genes.iterrows()
        ]

        adjacent_genes = genes[(
                (genes.seqid == epicenter_arm) &
                ((genes.end < focus_start) | (genes.start > focus_stop)) &
                (genes.start <= (focus_stop + 50000)) &
                (genes.end >= (focus_start - 50000))

        )]
        signal_report['adjacent_genes'] = [
            {'id': gene.ID,
             'name': gene.Name,
             'description': gene.description.split('[Source:')[0].strip()}
            for _, gene in adjacent_genes.iterrows()
        ]

        # augment report with related signals information
        # TODO this doesn't properly handle overlapping signals spanning a
        # centromere
        overlapping_signals = signals[(
                (signals.epicenter_arm == epicenter_arm) &
                (signals.focus_start <= focus_stop) &
                (signals.focus_stop >= focus_start) &
                # don't include self
                ((signals.population != signal_report['population']['id']) |
                 (signals.statistic != signal_report['statistic']['id']))
        )]
        signal_report['overlapping_signals'] = overlapping_signals.to_dict(
            orient='records')

        # render the report
        out_path = os.path.join(os.path.dirname(path), 'index.rst')
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(template.render(**signal_report), file=f)
