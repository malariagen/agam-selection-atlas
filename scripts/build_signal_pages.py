# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
import yaml
from glob import glob
import os
import allel
import pandas as pd


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
        focus = signal_report['focus']

        # augment report with gene information
        overlapping_genes = genes[(
                (genes.seqid == focus['arm']) &
                (genes.start <= focus['stop']) &
                (genes.end >= focus['start'])
        )]
        signal_report['overlapping_genes'] = [
            {'id': gene.ID,
             'name': gene.Name,
             'description': gene.description.split('[Source:')[0].strip()}
            for _, gene in overlapping_genes.iterrows()
        ]
        adjacent_genes = genes[(
                (genes.seqid == focus['arm']) &
                ((genes.end < focus['start']) | (genes.start > focus['stop'])) &
                (genes.start <= (focus['stop'] + 40000)) &
                (genes.end >= (focus['start'] - 40000))

        )]
        signal_report['adjacent_genes'] = [
            {'id': gene.ID,
             'name': gene.Name,
             'description': gene.description.split('[Source:')[0].strip()}
            for _, gene in adjacent_genes.iterrows()
        ]

        # augment report with related signals information
        overlapping_signals = signals[(
                (signals.focus_arm == focus['arm']) &
                (signals.focus_start <= focus['stop']) &
                (signals.focus_stop >= focus['start']) &
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
