# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
import os
import allel


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    template = env.get_template('gene_report.rst')

    features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    genes = features[features['type'] == 'gene']

    for _, gene in genes.iterrows():

        gene_report = {
            'gene': {
                'id': gene.ID,
                'name': gene.Name,
                'description': gene.description,
            },
        }

        out_path = os.path.join('docs', 'genes', gene.ID + '.rst')
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(template.render(**gene_report), file=f)
