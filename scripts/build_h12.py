# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import sys
import os
import numpy as np
import lmfit
import shutil
import yaml
import seaborn as sns
sns.set_context('paper')
sns.set_style('darkgrid')
sys.path.insert(0, 'agam-report-base/src/python')
import rockies
from ag1k import phase1_selection, phase1_ar3, phase1_ar31
# setup data sources
ag1k_dir = 'ngs.sanger.ac.uk/production/ag1000g/phase1'
phase1_ar3.init(os.path.join(ag1k_dir, 'AR3'))
phase1_ar31.init(os.path.join(ag1k_dir, 'AR3.1'))
phase1_selection.init(os.path.join(ag1k_dir, 'selection.1.RC2'))
genome = phase1_ar3.genome
chromosomes = '2R', '2L', '3R', '3L', 'X'


# setup population labels
pop_labels = {
    'AOM': 'Angola *An. coluzzii*',
    'BFM': 'Burkina Faso *An. coluzzii*',
    'BFS': 'Burkina Faso *An. gambiae*',
    'CMS': 'Cameroon *An. gambiae*',
    'GAS': 'Gabon *An. gambiae*',
    'GNS': 'Guinea *An. gambiae*',
    'GWA': 'Guinea-Bissau',
    'KES': 'Kenya',
    'UGS': 'Uganda *An. gambiae*',
}


def split_coords(chromosome, start, stop):
    if chromosome == '2':
        if start > len(genome['2R']):
            arm = '2L'
            start = start - len(genome['2R'])
            stop = stop - len(genome['2R'])
        else:
            arm = '2R'
    elif chromosome == '3':
        if start > len(genome['3R']):
            arm = '3L'
            start = start - len(genome['3R'])
            stop = stop - len(genome['3R'])
        else:
            arm = '3R'
    else:
        arm = chromosome
    return arm, start, stop


def compile_signal_report(rank, peak, chromosome, population):

    report = dict()
    report['chromosome'] = chromosome
    report['rank'] = rank
    report['population'] = {'id': population,
                            'label': pop_labels[population]}
    report['statistic'] = {'id': 'H12',
                           'label': 'H12'}

    epicenter_arm, epicenter_start, epicenter_stop = split_coords(
        chromosome, peak.epicenter_start, peak.epicenter_stop
    )
    report['epicenter'] = {'arm': epicenter_arm,
                           'start': epicenter_start,
                           'stop': epicenter_stop}

    focus_arm, focus_start, focus_stop = split_coords(
        chromosome, peak.focus_start, peak.focus_stop
    )
    report['focus'] = {'arm': focus_arm,
                       'start': focus_start,
                       'stop': focus_stop}

    if peak.peak_start is not None and peak.peak_stop is not None:
        peak_arm, peak_start, peak_stop = split_coords(
            chromosome, peak.peak_start, peak.peak_stop
        )
    else:
        peak_arm = peak_start = peak_stop = None
    report['peak'] = {'arm': peak_arm,
                      'start': peak_start,
                      'stop': peak_stop}

    report['fit_reports'] = {
        'left_peak': peak.best_fit.peak_result[0].fit_report(),
        'right_peak': peak.best_fit.peak_result[1].fit_report(),
        'left_null': peak.best_fit.null_result[0].fit_report(),
        'right_null': peak.best_fit.null_result[1].fit_report(),
    }

    report['minor_delta_aic'] = peak.minor_delta_aic
    report['sum_delta_aic'] = peak.sum_delta_aic

    return report


def main(population, chromosome, amplitude=0.5, min_amplitude=0, decay=0.5,
         min_decay=0.15, baseline=0.04, min_baseline=0, min_minor_di=40, min_total_di=80,
         extend_di_frc=0.05, flank=6, cap=1, vary_cap=False):

    # crude recombination rate lookup, keyed off chromatin state
    # use units of cM / bp, assume 2 cM / Mbp == 2x10^-6 cM / bp
    tbl_rr = (
        phase1_ar3.tbl_chromatin
        # extend heterochromatin on 2L
        .update('stop', 2840000, where=lambda r: r.name == 'CH2L')
        .update('start', 2840001, where=lambda r: r.name == 'PEU2L')
        .addfield('rr', lambda r: .5e-6 if 'H' in r.name else 2e-6)
    )
    # per-base map of recombination rates
    recmap = {chrom: np.full(len(genome[chrom]), fill_value=2e-6)
              for chrom in chromosomes}
    for row in tbl_rr.records():
        recmap[row.chrom][row.start-1:row.stop] = row.rr

    # obtain dataframe with selection stats
    df_h12 = phase1_selection.hstats_windowed

    # setup peak fitter
    peak_fitter = rockies.PairExponentialPeakFitter(
        amplitude=lmfit.Parameter(value=amplitude, vary=True, min=min_amplitude),
        decay=lmfit.Parameter(value=decay, vary=True, min=min_decay),
        c=lmfit.Parameter(value=baseline, vary=True, min=min_baseline),
        cap=lmfit.Parameter(value=cap, vary=vary_cap)
    )

    # setup output directory
    output_dir = 'docs/signal/H12/{}/chr{}'.format(population, chromosome)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # obtain signal
    chrom = chromosome
    if chrom == '2':
        chrom = '2R', '2L'
    if chrom == '3':
        chrom = '3R', '3L'
    starts, stops, gpos, signal = rockies.extract_signal(
        df_h12, col=population, chrom=chrom, recmap=recmap
    )

    # find peaks
    peaks = rockies.find_peaks(starts, stops, gpos, signal,
                               flank=flank, fitter=peak_fitter,
                               min_minor_delta_aic=min_minor_di,
                               min_total_delta_aic=min_total_di,
                               extend_delta_aic_frc=extend_di_frc,
                               verbose=True, output_dir=output_dir)

    # build peak reports
    for i, peak in enumerate(peaks):
        rank = i + 1

        report = compile_signal_report(rank, peak, chromosome, population)

        report_path = os.path.join(output_dir, str(rank), 'report.yml')
        with open(report_path, mode='w') as f:
            yaml.dump(report, f, default_flow_style=False)


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--population', required=True)
    parser.add_argument('--chromosome', required=True)
    parser.add_argument('--amplitude', type=float, default=0.5)
    parser.add_argument('--min-amplitude', type=float, default=0)
    parser.add_argument('--decay', type=float, default=0.5)
    parser.add_argument('--min-decay', type=float, default=0.15)
    parser.add_argument('--baseline', type=float, default=0.04)
    parser.add_argument('--min-baseline', type=float, default=0)
    parser.add_argument('--min-minor-di', type=float, default=40)
    parser.add_argument('--min-total-di', type=float, default=80)
    parser.add_argument('--extend-di-frc', type=float, default=0.05)
    parser.add_argument('--flank', type=float, default=6)
    parser.add_argument('--cap', type=float, default=1)
    parser.add_argument('--vary-cap', action='store_true', default=False)
    args = parser.parse_args()
    main(**vars(args))
