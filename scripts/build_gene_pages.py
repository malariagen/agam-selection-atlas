# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
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

    template = env.get_template('gene.rst')

    features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    genes = features[features['type'] == 'gene']

    signals = pd.read_csv('docs/_static/data/signals.csv')

    for _, gene in genes.iterrows():

        # TODO this doesn't properly handle overlapping signals spanning a
        # centromere
        overlapping_signals = signals[
            (signals.epicenter_arm == gene.seqid) &
            (signals.focus_start <= gene.end) &
            (signals.focus_stop >= gene.start)
        ]

        # TODO this doesn't properly handle overlapping signals spanning a
        # centromere
        adjacent_signals = signals[
            (signals.epicenter_arm == gene.seqid) &
            ((gene.end < signals.focus_start) |
             (gene.start > signals.focus_stop)) &
            ((signals.focus_start - 50000) <= gene.end) &
            ((signals.focus_stop + 50000) >= gene.start)
        ]

        gene_report = {
            'gene': {
                'id': gene.ID,
                'name': gene.Name,
                'description': gene.description,
                'seqid': gene.seqid,
                'start': gene.start,
                'end': gene.end,
            },
            'overlapping_signals':
                overlapping_signals.to_dict(orient='records'),
            'adjacent_signals':
                adjacent_signals.to_dict(orient='records'),
        }

        out_path = os.path.join('docs', 'gene', gene.ID + '.rst')
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(template.render(**gene_report), file=f)
