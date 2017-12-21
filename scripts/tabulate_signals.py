# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import yaml
from glob import glob
import os
import allel
import petl as etl
import sys
sys.path.insert(0, 'agam-report-base/src/python')
from ag1k import phase1_ar3
# setup data sources
ag1k_dir = 'ngs.sanger.ac.uk/production/ag1000g/phase1'
phase1_ar3.init(os.path.join(ag1k_dir, 'AR3'))
genome = phase1_ar3.genome
chromosomes = '2R', '2L', '3R', '3L', 'X'


if __name__ == '__main__':

    table = [['population',
              'statistic',
              'chromosome',
              'rank',
              'epicenter_arm',
              'epicenter_start',
              'epicenter_stop',
              'focus_start_arm',
              'focus_stop_arm',
              'focus_start',
              'focus_stop',
              'peak_start_arm',
              'peak_stop_arm',
              'peak_start',
              'peak_stop',
              'minor_delta_aic',
              'sum_delta_aic',
              'delta_aic_left',
              'delta_aic_right',
              'overlapping_genes',
              ]]

    features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    genes = features[features['type'] == 'gene']

    for path in sorted(glob('docs/_static/data/signal/*/*/*/*/report.yml')):
        print('reading', path)

        # load the basic signal report
        with open(path, mode='rb') as f:
            report = yaml.load(f)

        # figure out what chromosome arm
        epicenter = report['epicenter']
        # check epicenter does not span centromere - not sure how to handle that
        # case
        assert epicenter['start'][0] == epicenter['stop'][0]
        epicenter_arm = epicenter['start'][0]
        epicenter_start = epicenter['start'][1]
        epicenter_stop = epicenter['stop'][1]

        # obtain focus
        focus = report['focus']
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
        overlapping_genes = ' '.join(
            [g.ID for _, g in overlapping_genes.iterrows()]
        )

        row = [
            report['population']['id'],
            report['statistic']['id'],
            report['chromosome'],
            report['rank'],
            report['epicenter']['start'][0],
            report['epicenter']['start'][1],
            report['epicenter']['stop'][1],
            # focus may start and stop on different arms, preserve this info
            report['focus']['start'][0],
            report['focus']['stop'][0],
            report['focus']['start'][1],
            report['focus']['stop'][1],
            # peak may start and stop on different arms, preserve this info
            report['peak']['start'][0],
            report['peak']['stop'][0],
            report['peak']['start'][1],
            report['peak']['stop'][1],
            report['minor_delta_aic'],
            report['sum_delta_aic'],
            report['delta_aic'][0],
            report['delta_aic'][1],
            overlapping_genes,
        ]
        table += [row]

    table = etl.wrap(table).sort(key='sum_delta_aic', reverse=True)
    table.tocsv('docs/_static/data/signals.csv')
