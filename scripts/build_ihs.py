# -*- coding: utf-8 -*-
from setup import *


statistic_id = 'IHS'
statistic_label = 'IHS'


def build_dataframe(focal_pop, seqid, window_size):

    ihs_raw = phase1_selection.ihs_raw

    if seqid is None:
        df = pd.concat([build_dataframe(focal_pop, seqid=seqid, window_size=window_size)
                        for seqid in seqids])
        return df

    # extract raw values
    grp = ihs_raw[seqid][focal_pop]
    pos = grp['POS'][:]
    values = np.abs(grp['iHS_gw_std'][:])
    nomiss = ~np.isnan(values)
    pos_nomiss = pos[nomiss]
    values_nomiss = values[nomiss]

    # construct moving windows
    starts_col = allel.moving_statistic(pos_nomiss, statistic=lambda v: v[0], size=window_size)
    starts_col[0] = 1  # fix to start of sequence
    ends_col = np.append(starts_col[1:] - 1, [len(genome[seqid])])

    # summarise values in windows
    values_col = allel.moving_statistic(values_nomiss, statistic=np.max, size=window_size)

    # seqid column
    seqid_col = np.array([seqid] * len(starts_col))

    # build dataframe
    df = pd.DataFrame.from_items([
        ('seqid', seqid_col),
        ('start', starts_col),
        ('end', ends_col),
        ('value', values_col)
    ])
    return df


def main(focal_pop, chromosome, amplitude, min_amplitude, width, min_width,
         max_width, baseline, min_baseline, max_baseline, min_flank_delta_aic, min_peak_delta_aic,
         extend_focus_frc, peak_limit_frc, flank, ceiling, vary_ceiling, floor, vary_floor,
         max_skew, center_step, values_window_size):

    # obtain dataframe with selection stats
    df = build_dataframe(focal_pop=focal_pop, seqid=None, window_size=values_window_size)

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
    output_dir = ('docs/_static/data/signal/{}/{}/{}'
                  .format(statistic_id, focal_pop, chromosome))
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
        df, seqid=seqid, genome=genome, values_col='value', seqid_col='seqid',
        starts_col='start', ends_col='end'
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
        report = compile_signal_report(rank, peak, chromosome, focal_pop=focal_pop)
        signal_dir = os.path.join(output_dir, str(rank))
        os.makedirs(signal_dir, exist_ok=True)
        report_path = os.path.join(signal_dir, 'report.yml')
        with open(report_path, mode='w') as report_file:
            yaml.dump(report, report_file, default_flow_style=False)


def compile_signal_report(rank, peak, chromosome, focal_pop):
    # TODO refactor this to setup

    assert chromosome in '23X'

    epicenter_seqid, epicenter_coord = split_arms(chromosome, peak.epicenter)
    focus_start_seqid, focus_start_coord = split_arms(chromosome, peak.focus_start)
    focus_end_seqid, focus_end_coord = split_arms(chromosome, peak.focus_end)
    peak_start_seqid, peak_start_coord = split_arms(chromosome, peak.peak_start)
    peak_end_seqid, peak_end_coord = split_arms(chromosome, peak.peak_end)

    pop_key = focal_pop
    signal_uid = '{}/{}/{}/{}'.format(statistic_id, pop_key, chromosome, rank)
    report = {
        'uid': signal_uid,
        'chromosome': chromosome,
        'rank': rank,
        'pop_key': pop_key,
        'focal_population': {'id': focal_pop, 'label': populations[focal_pop]},
        'reference_population': None,
        'statistic': {
            'id': statistic_id,
            'label': statistic_label,
        },
        'epicenter': peak.epicenter,
        'epicenter_seqid': epicenter_seqid,
        'epicenter_coord': epicenter_coord,
        'focus_start': peak.focus_start,
        'focus_start_seqid': focus_start_seqid,
        'focus_start_coord': focus_start_coord,
        'focus_end': peak.focus_end,
        'focus_end_seqid': focus_end_seqid,
        'focus_end_coord': focus_end_coord,
        'peak_start': peak.peak_start,
        'peak_start_seqid': peak_start_seqid,
        'peak_start_coord': peak_start_coord,
        'peak_end': peak.peak_end,
        'peak_end_seqid': peak_end_seqid,
        'peak_end_coord': peak_end_coord,
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
    parser.add_argument('--focal-pop', required=True)
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
    parser.add_argument('--values-window-size', type=int, required=True)
    args = parser.parse_args()
    main(**vars(args))
