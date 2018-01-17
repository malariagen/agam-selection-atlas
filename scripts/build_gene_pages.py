# -*- coding: utf-8 -*-
from setup import *


if __name__ == '__main__':

    # setup jinja templates
    loader = jinja2.FileSystemLoader('templates')
    env = jinja2.Environment(loader=loader)
    template = env.get_template('gene.rst')

    # input data sources
    signals = pd.read_csv('docs/_static/data/signals.csv')

    # ensure output directory exists
    os.makedirs(os.path.join('docs', 'gene'), exist_ok=True)

    for _, gene in genes.iterrows():

        # # DEVELOPMENT shortcut
        # if gene.ID != 'AGAP004707':
        #     continue

        # TODO this doesn't properly handle overlapping signals spanning a centromere
        overlapping_signals = signals[
            (signals.epicenter_seqid == gene.seqid) &
            (signals.focus_start_coord <= gene.end) &
            (signals.focus_end_coord >= gene.start)
        ]

        # TODO this doesn't properly handle overlapping signals spanning a centromere
        adjacent_signals = signals[
            (signals.epicenter_seqid == gene.seqid) &
            ((gene.end < signals.focus_start_coord) |
             (gene.start > signals.focus_end_coord)) &
            ((signals.focus_start_coord - 50000) <= gene.end) &
            ((signals.focus_end_coord + 50000) >= gene.start)
        ]

        overlapping_loci = [locus for locus in known_loci
                            if (locus['seqid'] == gene.seqid and
                                locus['start_coord'] <= gene.end and
                                locus['end_coord'] >= gene.start)]
        overlapping_loci_names = set([locus['short_name'] for locus in overlapping_loci])
        adjacent_loci = [locus for locus in known_loci
                         if (locus['seqid'] == gene.seqid and
                             locus['start_coord'] <= (gene.end + 50000) and
                             locus['end_coord'] >= (gene.start - 50000) and
                             locus['short_name'] not in overlapping_loci_names)]

        gene_report = {
            'gene': {
                'id': gene.ID,
                'name': gene.Name,
                'description': gene.description.split('[Source:')[0].strip(),
                'seqid': gene.seqid,
                'start': int(gene.start),
                'end': int(gene.end),
            },
            'overlapping_signals': overlapping_signals.to_dict(orient='records'),
            'adjacent_signals': adjacent_signals.to_dict(orient='records'),
            'overlapping_loci': overlapping_loci,
            'adjacent_loci': adjacent_loci,
        }

        out_path = os.path.join('docs', 'gene', gene.ID + '.rst')
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(template.render(**gene_report), file=f)
