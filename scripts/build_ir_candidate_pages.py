# -*- coding: utf-8 -*-
from setup import *


def count_signals(gene, df_signals):

    overlapping_signals = df_signals[
        (df_signals.epicenter_seqid == gene.seqid) &
        (df_signals.focus_start <= gene.end) &
        (df_signals.focus_end >= gene.start)
    ]

    # TODO this doesn't properly handle overlapping signals spanning a
    # centromere
    adjacent_signals = df_signals[
        (df_signals.epicenter_seqid == gene.seqid) &
        ((gene.end < df_signals.focus_start) |
         (gene.start > df_signals.focus_end)) &
        ((df_signals.focus_start - 50000) <= gene.end) &
        ((df_signals.focus_end + 50000) >= gene.start)
    ]

    return len(overlapping_signals), len(adjacent_signals)


def build_candidate_page(template, df_genes, df_signals, title, slug):

    df_candidates = pd.read_csv(
        'docs/_static/data/ir-candidate-genes/{}.csv'.format(slug),
        index_col='ID'
    )
    df_candidate_genes = df_genes.join(df_candidates, how='inner')
    counts = [count_signals(gene, df_signals)
              for _, gene in df_candidate_genes.iterrows()]
    df_candidate_genes['n_signals_overlapping'] = np.array([c[0] for c in counts])
    df_candidate_genes['n_signals_adjacent'] = np.array([c[1] for c in counts])
    df_candidate_genes['n_signals'] = np.array([sum(c) for c in counts])
    df_sorted = (
        df_candidate_genes
        .sort_values(by='n_signals_overlapping', ascending=False, kind='mergesort')
        .sort_values(by='n_signals', ascending=False, kind='mergesort')
    )

    data = {
        'title': title,
        'slug': slug,
        'genes': [
            {'id': id_,
             'name': gene.Name,
             'description': gene.description.split('[Source:')[0].strip(),
             'n_signals': gene.n_signals,
             'n_signals_overlapping': gene.n_signals_overlapping,
             'n_signals_adjacent': gene.n_signals_adjacent,
             'start': gene.start,
             'end': gene.end,
             'seqid': gene.seqid,
             }
            for id_, gene in df_sorted.iterrows()
        ]
    }

    page_path = os.path.join('docs', 'ir-candidate', '{}.rst'.format(slug))
    print('rendering', page_path)
    with open(page_path, mode='w') as f:
        print(template.render(**data), file=f)


def main():

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    template = env.get_template('ir-candidate.rst')

    df_features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    df_genes = df_features[df_features['type'] == 'gene'].set_index('ID')

    df_signals = pd.read_csv('docs/_static/data/signals.csv')

    for slug, title in zip(['metabolic', 'target_site', 'behavioural', 'cuticular'],
                           ['Metabolic genes', 'Target-site genes',
                            'Behavioural genes', 'Cuticular genes']):
        build_candidate_page(template=template, slug=slug, df_genes=df_genes,
                             df_signals=df_signals, title=title)

    #
    # df_candidates = pd.read_csv(
    #     'docs/_static/data/ir-candidate-genes/type1_metabolic.txt',
    #     names=['ID', 'transcript'],
    #     sep='\t', index_col='ID'
    # )
    # df_candidate_genes = df_genes.join(df_candidates, how='inner')
    # counts = [count_signals(gene, df_signals)
    #           for _, gene in df_candidate_genes.iterrows()]
    # df_candidate_genes['n_signals_overlapping'] = np.array([c[0] for c in counts])
    # df_candidate_genes['n_signals_adjacent'] = np.array([c[1] for c in counts])
    # df_candidate_genes['n_signals'] = np.array([sum(c) for c in counts])
    # df_candidate_genes.sort_values(by='n_signals', ascending=False, inplace=True)
    #
    # data = {
    #     'title': 'Metabolic resistance candidate genes',
    #     'slug': 'metabolic',
    #     'genes': [
    #         {'id': id_,
    #          'name': gene.Name,
    #          'description': gene.description.split('[Source:')[0].strip(),
    #          'n_signals': gene.n_signals,
    #          'n_signals_overlapping': gene.n_signals_overlapping,
    #          'n_signals_adjacent': gene.n_signals_adjacent,
    #          'start': gene.start,
    #          'end': gene.end,
    #          'seqid': gene.seqid,
    #          }
    #         for id_, gene in df_candidate_genes.iterrows()
    #     ]
    # }
    #
    # page_path = os.path.join('docs', 'ir-candidate', 'metabolic.rst')
    # print('rendering', page_path)
    # with open(page_path, mode='w') as f:
    #     print(template.render(**data), file=f)
    #


if __name__ == '__main__':
    main()
