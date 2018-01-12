# -*- coding: utf-8 -*-
from setup import *


statistic_id = 'H12'
statistic_label = 'H12'


def main(population, chromosome, amplitude, min_amplitude, width, min_width, max_width,
         baseline, min_baseline, max_baseline, min_flank_delta_aic, min_peak_delta_aic,
         extend_focus_frc, peak_limit_frc, flank, ceiling, vary_ceiling, floor, vary_floor,
         max_skew, center_step):

    # obtain dataframe with selection stats
    df_h12 = phase1_selection.hstats_windowed

    # setup parameters
    amplitude_param = lmfit.Parameter(value=amplitude, vary=True, min=min_amplitude)
    decay_param = lmfit.Parameter(value=width, vary=True, min=min_width, max=max_width)
    sigma_param = lmfit.Parameter(value=width, vary=True, min=min_width, max=max_width)
    skew_param = lmfit.Parameter(value=0, vary=True, min=-max_skew, max=max_skew)
    baseline_param = lmfit.Parameter(value=baseline, vary=True, min=min_baseline, max=max_baseline)
    ceiling_param = lmfit.Parameter(value=ceiling, vary=vary_ceiling)
    floor_param = lmfit.Parameter(value=floor, vary=vary_floor)
    null_param = lmfit.Parameter(value=baseline, vary=True, min=min_baseline, max=max_baseline)

    # setup peak fitters
    skewed_exp_fitter = peakfit.SkewedExponentialPeakFitter(
        amplitude=amplitude_param,
        decay=decay_param,
        skew=skew_param,
        baseline=baseline_param,
        ceiling=ceiling_param,
        floor=floor_param,
        null=null_param,
        peak_limit_frc=peak_limit_frc,
    )
    skewed_gauss_fitter = peakfit.SkewedGaussianPeakFitter(
        amplitude=amplitude_param,
        sigma=sigma_param,
        skew=skew_param,
        baseline=baseline_param,
        ceiling=ceiling_param,
        floor=floor_param,
        null=null_param,
        peak_limit_frc=peak_limit_frc,
    )
    peak_fitters = [skewed_exp_fitter, skewed_gauss_fitter]

    # setup output directory
    output_dir = 'docs/_static/data/signal/H12/{}/{}'.format(population, chromosome)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # setup seqid
    if chromosome == '2':
        seqid = '2R', '2L'
    elif chromosome == '3':
        seqid = '3R', '3L'
    else:
        seqid = chromosome

    # extract data
    starts, ends, values, percentiles = peakfit.extract_windowed_values(
        df_h12, seqid=seqid, genome=genome, values_col=population, seqid_col='chrom',
        starts_col='start', ends_col='stop'
    )

    # setup centers
    centers = np.arange(center_step, ends[-1] - center_step, center_step)

    # find peaks
    peaks = peakfit.find_peaks(starts=starts, ends=ends, values=values, percentiles=percentiles,
                               centers=centers, gflank=flank, gmap=gmap[chromosome],
                               fitters=peak_fitters, show_plots=False,
                               statistic_label=statistic_label,
                               verbose=True, output_dir=output_dir,
                               min_flank_delta_aic=min_flank_delta_aic,
                               min_peak_delta_aic=min_peak_delta_aic,
                               extend_focus_frc=extend_focus_frc)

    # build peak reports
    for i, peak in enumerate(peaks):
        rank = i + 1
        report = compile_signal_report(rank, peak, chromosome, population)
        signal_dir = os.path.join(output_dir, str(rank))
        os.makedirs(signal_dir, exist_ok=True)
        report_path = os.path.join(signal_dir, 'report.yml')
        with open(report_path, mode='w') as report_file:
            yaml.dump(report, report_file, default_flow_style=False)


def compile_signal_report(rank, peak, chromosome, pop_id):
    assert chromosome in '23X'

    report = {
        'chromosome': chromosome,
        'rank': rank,
        'population': {'id': pop_id, 'label': populations[pop_id]},
        'statistic': {'id': statistic_id, 'label': statistic_label},
        'epicenter': split_arms(chromosome, peak.epicenter),
        'focus_start': split_arms(chromosome, peak.focus_start),
        'focus_end': split_arms(chromosome, peak.focus_end),
        'peak_start': split_arms(chromosome, peak.peak_start),
        'peak_end': split_arms(chromosome, peak.peak_end),
        'fit_reports': {
            'peak': peak.peak_fit.peak_result.fit_report(),
            'null': peak.peak_fit.null_result.fit_report(),
        },
        'delta_aic': float(peak.delta_aic),
        'delta_aic_left': float(peak.delta_aic_left),
        'delta_aic_right': float(peak.delta_aic_right),
        'pos': peak.pos.tolist(),
        'gpos': peak.gpos.tolist(),
        'values': peak.values.tolist(),
        'best_fit': peak.peak_fit.best_fit.tolist(),
        'max_value': float(peak.max_value),
        'max_percentile': float(peak.max_percentile),
    }

    return report


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--population', required=True)
    parser.add_argument('--chromosome', required=True)
    parser.add_argument('--amplitude', type=float, required=True)
    parser.add_argument('--min-amplitude', type=float, required=True)
    parser.add_argument('--width', type=float, required=True)
    parser.add_argument('--min-width', type=float, required=True)
    parser.add_argument('--max-width', type=float, required=True)
    parser.add_argument('--baseline', type=float, required=True)
    parser.add_argument('--min-baseline', type=float, required=True)
    parser.add_argument('--max-baseline', type=float, required=True)
    parser.add_argument('--min-flank-delta-aic', type=float, required=True)
    parser.add_argument('--min-peak-delta-aic', type=float, required=True)
    parser.add_argument('--extend-focus-frc', type=float, required=True)
    parser.add_argument('--peak-limit-frc', type=float, required=True)
    parser.add_argument('--flank', type=float, required=True)
    parser.add_argument('--ceiling', type=float, required=True)
    parser.add_argument('--vary-ceiling', action='store_true', default=False)
    parser.add_argument('--floor', type=float, required=True)
    parser.add_argument('--vary-floor', action='store_true', default=False)
    parser.add_argument('--max-skew', type=float, required=True)
    parser.add_argument('--center-step', type=int, required=True)
    args = parser.parse_args()
    main(**vars(args))
