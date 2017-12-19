# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import yaml
from glob import glob
import os
import allel
import petl as etl


if __name__ == '__main__':

    table = [['population',
              'statistic',
              'chromosome',
              'rank',
              'focus_arm',
              'focus_start',
              'focus_stop',
              'signal_arm',
              'signal_start',
              'signal_stop',
              'peak_arm',
              'peak_start',
              'peak_stop',
              'minor_delta_aic',
              'sum_delta_aic',
              'overlapping_genes',
              ]]

    features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    genes = features[features['type'] == 'gene']

    for path in sorted(glob('docs/signals/*/*/*/*/signal_report.yml')):

        # load the basic signal report
        with open(path, mode='rb') as f:
            signal_report = yaml.load(f)

        # augment report with gene information
        signal = signal_report['signal']
        overlapping_genes = genes[(
                (genes.seqid == signal['arm']) &
                (genes.start <= signal['stop']) &
                (genes.end >= signal['start'])
        )]
        overlapping_genes = ' '.join(
            [g.ID for _, g in overlapping_genes.iterrows()]
        )

        row = [
            signal_report['population']['id'],
            signal_report['statistic']['id'],
            signal_report['chromosome'],
            signal_report['rank'],
            signal_report['focus']['arm'],
            signal_report['focus']['start'],
            signal_report['focus']['stop'],
            signal_report['signal']['arm'],
            signal_report['signal']['start'],
            signal_report['signal']['stop'],
            signal_report['peak']['arm'],
            signal_report['peak']['start'],
            signal_report['peak']['stop'],
            signal_report['minor_delta_aic'],
            signal_report['sum_delta_aic'],
            overlapping_genes,
        ]
        table += [row]

    table = etl.wrap(table).sort(key='sum_delta_aic', reverse=True)
    table.tocsv('docs/signals.csv')
