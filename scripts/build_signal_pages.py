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

    for path in sorted(glob('docs/signals/*/*/*/*/signal_report.yml')):

        # load the basic signal report
        with open(path, mode='rb') as f:
            signal_report = yaml.load(f)
        signal = signal_report['signal']

        # augment report with gene information
        overlapping_genes = genes[(
                (genes.seqid == signal['arm']) &
                (genes.start <= signal['stop']) &
                (genes.end >= signal['start'])
        )]
        signal_report['overlapping_genes'] = [
            {'id': gene.ID,
             'name': gene.Name,
             'description': gene.description.split('[Source:')[0].strip()}
            for _, gene in overlapping_genes.iterrows()
        ]
        adjacent_genes = genes[(
                (genes.seqid == signal['arm']) &
                ((genes.end < signal['start']) | (genes.start > signal['stop'])) &
                (genes.start <= (signal['stop'] + 40000)) &
                (genes.end >= (signal['start'] - 40000))

        )]
        signal_report['adjacent_genes'] = [
            {'id': gene.ID,
             'name': gene.Name,
             'description': gene.description.split('[Source:')[0].strip()}
            for _, gene in adjacent_genes.iterrows()
        ]

        # augment report with related signals information
        overlapping_signals = signals[(
                (signals.signal_arm == signal['arm']) &
                (signals.signal_start <= signal['stop']) &
                (signals.signal_stop >= signal['start']) &
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
