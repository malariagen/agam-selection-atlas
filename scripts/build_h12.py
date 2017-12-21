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


def split_arms(chromosome, coord):
    assert chromosome is not None
    assert coord is not None
    if chromosome == '2':
        if coord > len(genome['2R']):
            arm = '2L'
            coord = coord - len(genome['2R'])
        else:
            arm = '2R'
    elif chromosome == '3':
        if coord > len(genome['3R']):
            arm = '3L'
            coord = coord - len(genome['3R'])
        else:
            arm = '3R'
    else:
        arm = chromosome
    return [arm, coord]


def compile_signal_report(rank, peak, chromosome, population):

    report = dict()
    report['chromosome'] = chromosome
    report['rank'] = rank
    report['population'] = {'id': population,
                            'label': pop_labels[population]}
    report['statistic'] = {'id': 'H12',
                           'label': 'H12'}

    report['epicenter_start'] = peak.epicenter_start
    report['epicenter_stop'] = peak.epicenter_stop
    epicenter_start = split_arms(chromosome, peak.epicenter_start)
    epicenter_stop = split_arms(chromosome, peak.epicenter_stop)
    report['epicenter'] = {'start': epicenter_start, 'stop': epicenter_stop}

    report['focus_start'] = peak.focus_start
    report['focus_stop'] = peak.focus_stop
    focus_start = split_arms(chromosome, peak.focus_start)
    focus_stop = split_arms(chromosome, peak.focus_stop)
    report['focus'] = {'start': focus_start, 'stop': focus_stop}

    report['peak_start'] = peak.peak_start
    report['peak_stop'] = peak.peak_stop
    peak_start = split_arms(chromosome, peak.peak_start)
    peak_stop = split_arms(chromosome, peak.peak_stop)
    report['peak'] = {'start': peak_start, 'stop': peak_stop}

    report['fit_reports'] = {
        'left_peak': peak.best_fit.peak_result[0].fit_report(),
        'right_peak': peak.best_fit.peak_result[1].fit_report(),
        'left_null': peak.best_fit.null_result[0].fit_report(),
        'right_null': peak.best_fit.null_result[1].fit_report(),
    }

    report['minor_delta_aic'] = peak.minor_delta_aic
    report['sum_delta_aic'] = peak.sum_delta_aic
    report['delta_aic'] = peak.delta_aic.tolist()

    report['fit_data'] = {
        'xx_gpos': peak.best_fit.xx.tolist(),
        'xx_ppos': peak.ppos.tolist(),
        'yy_signal': peak.signal.tolist(),
        'yy_signal_fitted': peak.best_fit.yy.tolist(),
        'yy_best_fit': peak.best_fit.best_fit.tolist(),
    }

    return report


def main(population, chromosome, amplitude, min_amplitude, decay,
         min_decay, max_decay, baseline, min_baseline,
         max_baseline, min_minor_di, min_total_di,
         extend_di_frc, flank, cap, vary_cap):

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
        amplitude=lmfit.Parameter(value=amplitude, vary=True,
                                  min=min_amplitude),
        decay=lmfit.Parameter(value=decay, vary=True, min=min_decay,
                              max=max_decay),
        c=lmfit.Parameter(value=baseline, vary=True, min=min_baseline,
                          max=max_baseline),
        cap=lmfit.Parameter(value=cap, vary=vary_cap)
    )

    # setup output directory
    output_dir = 'docs/_static/data/signal/H12/{}/{}'.format(population, chromosome)
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
    parser.add_argument('--max-decay', type=float, default=3.0)
    parser.add_argument('--baseline', type=float, default=0.03)
    parser.add_argument('--min-baseline', type=float, default=0)
    parser.add_argument('--max-baseline', type=float, default=0.06)
    parser.add_argument('--min-minor-di', type=float, default=40)
    parser.add_argument('--min-total-di', type=float, default=80)
    parser.add_argument('--extend-di-frc', type=float, default=0.05)
    parser.add_argument('--flank', type=float, default=6)
    parser.add_argument('--cap', type=float, default=1)
    parser.add_argument('--vary-cap', action='store_true', default=False)
    args = parser.parse_args()
    main(**vars(args))
