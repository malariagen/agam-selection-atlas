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
              'epicenter_arm',
              'epicenter_start',
              'epicenter_stop',
              'focus_arm',
              'focus_start',
              'focus_stop',
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

    for path in sorted(glob('docs/signal/*/*/*/*/report.yml')):

        # load the basic signal report
        with open(path, mode='rb') as f:
            report = yaml.load(f)

        # augment report with gene information
        focus = report['focus']
        overlapping_genes = genes[(
                (genes.seqid == focus['arm']) &
                (genes.start <= focus['stop']) &
                (genes.end >= focus['start'])
        )]
        overlapping_genes = ' '.join(
            [g.ID for _, g in overlapping_genes.iterrows()]
        )

        row = [
            report['population']['id'],
            report['statistic']['id'],
            report['chromosome'],
            report['rank'],
            report['epicenter']['arm'],
            report['epicenter']['start'],
            report['epicenter']['stop'],
            report['focus']['arm'],
            report['focus']['start'],
            report['focus']['stop'],
            report['peak']['arm'],
            report['peak']['start'],
            report['peak']['stop'],
            report['minor_delta_aic'],
            report['sum_delta_aic'],
            overlapping_genes,
        ]
        table += [row]

    table = etl.wrap(table).sort(key='sum_delta_aic', reverse=True)
    table.tocsv('docs/signals.csv')
