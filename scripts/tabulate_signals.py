# -*- coding: utf-8 -*-
from setup import *


if __name__ == '__main__':

    table = [[
        'uid',
        'pop_key',
        'focal_population',
        'focal_population_label',
        'reference_population',
        'reference_population_label',
        'statistic',
        'chromosome',
        'rank',
        'epicenter',
        'epicenter_seqid',
        'epicenter_coord',
        'focus_start',
        'focus_start_seqid',
        'focus_start_coord',
        'focus_end',
        'focus_end_seqid',
        'focus_end_coord',
        'peak_start',
        'peak_start_seqid',
        'peak_start_coord',
        'peak_end',
        'peak_end_seqid',
        'peak_end_coord',
        'delta_aic',
        'delta_aic_left',
        'delta_aic_right',
        'min_flank_delta_aic',
        'max_value',
        'max_percentile',
        'overlapping_genes',
    ]]

    features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    genes = features[features['type'] == 'gene']

    for path in sorted(glob('docs/_static/data/signal/*/*/*/*/report.yml')):
        print('reading', path)

        # load the basic signal report
        with open(path, mode='rb') as f:
            report = yaml.load(f)

        # obtain populations
        focal_pop = report['focal_population']['id']
        ref_pop = None
        if report['reference_population'] is not None:
            ref_pop = report['reference_population']['id']

        # obtain epicenter
        chromosome = report['chromosome']
        epicenter = report['epicenter']
        epicenter_seqid, epicenter_coord = split_arms(chromosome, epicenter)

        # obtain focus
        focus_start = report['focus_start']
        focus_start_seqid, focus_start_coord = split_arms(chromosome, focus_start)
        focus_end = report['focus_end']
        focus_end_seqid, focus_end_coord = split_arms(chromosome, focus_end)

        # obtain peak
        peak_start = report['peak_start']
        peak_start_seqid, peak_start_coord = split_arms(chromosome, peak_start)
        peak_end = report['peak_end']
        peak_end_seqid, peak_end_coord = split_arms(chromosome, peak_end)

        # crude way to deal with rare case where focus spans centromere
        if focus_start_seqid != epicenter_seqid:
            focus_start_coord = 1
        if focus_end_seqid != epicenter_seqid:
            focus_end_coord = len(genome[epicenter_seqid])

        # augment report with gene information
        # TODO deal with genes in whole chromosome coords
        overlapping_genes = genes[(
            (genes.seqid == epicenter_seqid) &
            (genes.start <= focus_end_coord) &
            (genes.end >= focus_start_coord)
        )]
        overlapping_genes = ' '.join(
            [g.ID for _, g in overlapping_genes.iterrows()]
        )

        row = [
            report['uid'],
            report['pop_key'],
            focal_pop,
            populations[focal_pop],
            ref_pop,
            populations[ref_pop] if ref_pop else None,
            report['statistic']['id'],
            chromosome,
            report['rank'],
            epicenter,
            epicenter_seqid,
            epicenter_coord,
            # focus may start and end on different arms, preserve this info
            focus_start,
            focus_start_seqid,
            focus_start_coord,
            focus_end,
            focus_end_seqid,
            focus_end_coord,
            # peak may start and end on different arms, preserve this info
            peak_start,
            peak_start_seqid,
            peak_start_coord,
            peak_end,
            peak_end_seqid,
            peak_end_coord,
            # other data
            report['delta_aic'],
            report['delta_aic_left'],
            report['delta_aic_right'],
            min(report['delta_aic_left'], report['delta_aic_right']),
            report['max_value'],
            report['max_percentile'],
            overlapping_genes,
        ]
        table += [row]

    table = etl.wrap(table).sort(key=('delta_aic', 'min_flank_delta_aic'), reverse=True)
    table.tocsv('docs/_static/data/signals.csv')
