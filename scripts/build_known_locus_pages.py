# -*- coding: utf-8 -*-
from setup import *


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    # make the populations index page
    loci_template = env.get_template('known-loci.rst')
    data = dict(loci=known_loci)
    with open('docs/known-loci.rst', mode='w') as f:
        f.write(loci_template.render(loci=known_loci))

    # make the per-population pages
    locus_template = env.get_template('known-locus.rst')

    # load signals
    df_signals = pd.read_csv('docs/_static/data/signals.csv')

    os.makedirs('docs/known-locus', exist_ok=True)

    for locus in known_loci:

        locus_data = dict()
        locus_data['locus'] = locus

        # find overlapping genes
        overlapping_genes = genes[(
            (genes.seqid == locus['seqid']) &
            (genes.start <= locus['end_coord']) &
            (genes.end >= locus['start_coord'])
        )]
        locus_data['genes'] = [
            {'id': gene.ID,
             'name': gene.Name,
             'description': gene.description.split('[Source:')[0].strip()}
            for _, gene in overlapping_genes.iterrows()
        ]

        # find overlapping signals
        overlapping_signals = df_signals[(
            (df_signals.focus_start_seqid == locus['seqid']) &
            (df_signals.focus_end_seqid == locus['seqid']) &
            (df_signals.focus_start_coord <= (locus['end_coord'] + 50000)) &
            (df_signals.focus_end_coord >= (locus['start_coord'] - 50000))
        )].to_dict(orient='records')
        print(locus['short_name'], len(overlapping_signals))
        locus_data['signals'] = overlapping_signals

        # render the report
        out_path = 'docs/known-locus/{}.rst'.format(locus['short_name'].lower())
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(locus_template.render(**locus_data), file=f)
