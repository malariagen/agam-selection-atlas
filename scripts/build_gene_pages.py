# -*- coding: utf-8 -*-
from setup import *


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
            (signals.epicenter_seqid == gene.seqid) &
            (signals.focus_start <= gene.end) &
            (signals.focus_end >= gene.start)
        ]

        # TODO this doesn't properly handle overlapping signals spanning a
        # centromere
        adjacent_signals = signals[
            (signals.epicenter_seqid == gene.seqid) &
            ((gene.end < signals.focus_start) |
             (gene.start > signals.focus_end)) &
            ((signals.focus_start - 50000) <= gene.end) &
            ((signals.focus_end + 50000) >= gene.start)
        ]

        gene_report = {
            'gene': {
                'id': gene.ID,
                'name': gene.Name,
                'description': gene.description.split('[Source:')[0].strip(),
                'seqid': gene.seqid,
                'start': int(gene.start),
                'end': int(gene.end),
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
