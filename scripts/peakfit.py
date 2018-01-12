# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division


from bisect import bisect_left, bisect_right
import collections
import numpy
import matplotlib.pyplot as plt
import lmfit
import scipy
import seaborn as sns
palette = sns.color_palette()


# workaround PyCharm issue with finding numpy functions
class ModuleWrapper(object):

    def __init__(self, mod):
        self.mod = mod

    def __getattr__(self, item):
        return getattr(self.mod, item)


np = ModuleWrapper(numpy)
sp = ModuleWrapper(scipy)


def extract_windowed_values(df, seqid, genome, spacing=0, values_col='value',
                            seqid_col='seqid', starts_col='start', ends_col='end'):
    """Extract windowed values from a dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        A dataframe with windowed data. Expect that start and end columns are
        GFF-style 1-based stop-inclusive physical coords.
    seqid : str
        Sequence identifier. May also be a tuple, e.g., ('2R', '2L'), in which
        case the data for each sequence will be concatenated.
    genome : dict-like [str -> array]
        Genome sequences.
    spacing : int, optional
        Amount of physical distance to insert when concatenating data from
        multiple sequences.
    values_col : str
        Name of column containing statistic values.
    seqid_col, starts_col, ends_col : str
        Column names for sequence identifier, start and end coordinates for each window.

    Returns
    -------
    starts
        Window physical start positions.
    ends
        Window physical end positions.
    gstarts
        Window genetic start positions.
    gends
        Window genetic end positions.
    values
        Statistic values.

    """

    # handle multiple sequences
    if isinstance(seqid, (tuple, list)):
        assert len(seqid) == 2, 'can only concatenate two sequences'
        ((starts1, ends1, values1, percentiles1),
         (starts2, ends2, values2, percentiles2)) = \
            [extract_windowed_values(df, values_col=values_col, seqid=c, genome=genome,
                                     seqid_col=seqid_col, starts_col=starts_col, ends_col=ends_col)
             for c in seqid]
        seq1_plen = len(genome[seqid[0]])
        starts = np.concatenate([starts1, starts2 + seq1_plen + spacing])
        ends = np.concatenate([ends1, ends2 + seq1_plen + spacing])
        values = np.concatenate([values1, values2])
        percentiles = np.concatenate([percentiles1, percentiles2])
        return starts, ends, values, percentiles

    # compute percentiles over whole dataframe, with nans removed
    df = df.iloc[~np.isnan(df[values_col].values)].copy()
    df['percentile'] = sp.stats.rankdata(df[values_col]) / len(df)

    # extract data for single sequence
    df = df.reset_index().set_index(seqid_col)
    df_seq = df.loc[seqid]

    # extract window starts and ends
    starts = np.asarray(df_seq[starts_col])
    ends = np.asarray(df_seq[ends_col])

    # extract the values column
    values = np.asarray(df_seq[values_col])
    percentiles = np.asarray(df_seq['percentile'])

    return starts, ends, values, percentiles


def plot_windowed_values(starts, ends, values, figsize=(8, 2), gmap=None, ax=None, dpi=None,
                         ylabel='Selection statistic'):
    """Convenience function to plot windowed values."""

    # determine x coord
    x = ((starts + ends) / 2).astype(int)
    if gmap is not None:
        x = gmap.take(x - 1)

    fig = None
    if ax is None:
        # noinspection PyTypeChecker
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi, facecolor='w')

    ax.plot(x, values, linestyle=' ', marker='o', mfc='none', markersize=2,
            color=palette[0], mew=.5)

    if gmap is None:
        ax.set_xlabel('Physical distance (Mbp)')
        ax.set_xlim(starts[0], ends[-1])
        ax.set_xticklabels(['{:.1f}'.format(x/1e6) for x in ax.get_xticks()])
    else:
        ax.set_xlabel('Genetic distance (cM)')
        ax.set_xlim(gmap[starts[0] - 1], gmap[ends[-1] - 1])
    ax.set_ylabel(ylabel)
    if fig is not None:
        fig.tight_layout()

    return ax


def exponential(x, amplitude, decay, baseline, floor, ceiling):
    """Exponential decay function.

    Parameters
    ----------
    x : ndarray
        Independent variable.
    amplitude : float
        Amplitude parameter.
    decay : float
        Decay parameter.
    baseline : float
        Baseline parameter.
    floor : float
        Minimum value that the result can take.
    ceiling : float
        Maximum value that the result can take.

    Returns
    -------
    y : ndarray

    """

    # compute exponential
    y = baseline + amplitude * np.exp(-x / decay)

    # apply limits
    y = y.clip(floor, ceiling)

    return y


def exponential_peak(x, center, amplitude, decay, baseline, floor, ceiling):
    """Symmetric exponential decay peak function.

    Parameters
    ----------
    x : ndarray
        Independent variable.
    center : int or float
        The center of the peak.
    amplitude : float
        Amplitude parameter.
    decay : float
        Decay parameter.
    baseline : float
        Baseline parameter.
    floor : float
        Minimum value that the result can take.
    ceiling : float
        Maximum value that the result can take.

    Returns
    -------
    y : ndarray

    """

    # locate the index at which to split data into left and right flanks
    ix_split = bisect_right(x, center)

    # compute left flank
    xl = center - x[:ix_split]
    yl = baseline + amplitude * np.exp(-xl / decay)

    # compute right flank
    xr = x[ix_split:] - center
    yr = baseline + amplitude * np.exp(-xr / decay)

    # prepare output
    y = np.concatenate([yl, yr])

    # apply limits
    y = y.clip(floor, ceiling)

    return y


def skewed_exponential_peak(x, center, amplitude, decay, skew, baseline, floor, ceiling):
    """Asymmetric exponential decay peak function.

    Parameters
    ----------
    x : ndarray
        Independent variable.
    center : int or float
        The center of the peak.
    amplitude : float
        Amplitude parameter.
    decay : float
        Decay parameter.
    skew : float
        Skew parameter.
    baseline : float
        Baseline parameter.
    floor : float
        Minimum value that the result can take.
    ceiling : float
        Maximum value that the result can take.

    Returns
    -------
    y : ndarray

    """

    decay_right = 2**(-skew) * decay
    decay_left = 2**skew * decay

    # locate the index at which to split data into left and right flanks
    ix_split = bisect_right(x, center)

    # compute left flank
    xl = center - x[:ix_split]
    yl = baseline + amplitude * np.exp(-xl / decay_left)

    # compute right flank
    xr = x[ix_split:] - center
    yr = baseline + amplitude * np.exp(-xr / decay_right)

    # prepare output
    y = np.concatenate([yl, yr])

    # apply limits
    y = y.clip(floor, ceiling)

    return y


def gaussian(x, center, amplitude, sigma, baseline, floor, ceiling):
    """Gaussian function.

    Parameters
    ----------
    x : ndarray
        Independent variable.
    center : int or float
        The center of the peak.
    amplitude : float
        Amplitude parameter.
    sigma : float
        Width parameter.
    baseline : float
        Baseline parameter.
    floor : float
        Minimum value that the result can take.
    ceiling : float
        Maximum value that the result can take.

    Returns
    -------
    y : ndarray

    """

    # y = (baseline +
    #      (amplitude / (np.sqrt(2 * np.pi) * sigma)) *
    #      np.exp(-(x - center)**2 / (2 * sigma**2)))
    y = (baseline +
         amplitude *
         np.exp(-(x - center)**2 / (2 * sigma**2)))

    # apply limits
    y = y.clip(floor, ceiling)

    return y


def skewed_gaussian(x, center, amplitude, sigma, skew, baseline, floor, ceiling):
    """Asymmetric Gaussian function.

    Parameters
    ----------
    x : ndarray
        Independent variable.
    center : int or float
        The center of the peak.
    amplitude : float
        Amplitude parameter.
    sigma : float
        Width parameter.
    skew : float
        Skew parameter.
    baseline : float
        Baseline parameter.
    floor : float
        Minimum value that the result can take.
    ceiling : float
        Maximum value that the result can take.

    Returns
    -------
    y : ndarray

    """

    sigma_right = 2**(-skew) * sigma
    sigma_left = 2**skew * sigma

    # locate the index at which to split data into left and right flanks
    ix_split = bisect_right(x, center)

    # compute left flank
    xl = center - x[:ix_split]
    yl = (baseline +
          amplitude *
          np.exp(-xl**2 / (2 * sigma_left**2)))

    # compute right flank
    xr = x[ix_split:] - center
    yr = (baseline +
          amplitude *
          np.exp(-xr**2 / (2 * sigma_right**2)))

    # prepare output
    y = np.concatenate([yl, yr])

    # apply limits
    y = y.clip(floor, ceiling)

    return y


PeakFitResult = collections.namedtuple(
    'PeakFitResult',
    'null_result peak_result null_result_left null_result_right peak_result_left '
    'peak_result_right xx yy loc best_fit peak residual peak_start_ix peak_end_ix '
    'peak_start_x peak_end_x baseline baseline_stderr delta_aic delta_aic_left '
    'delta_aic_right'
)


def find_peak_limits(best_fit, threshold):
    ix_peak_start = ix_peak_end = None

    # work forward to find peak start
    for i in range(best_fit.shape[0]):
        v = best_fit[i]
        if ix_peak_start is None:
            if v > threshold:
                ix_peak_start = i
                break

    # work backwards to find peak end
    for i in range(best_fit.shape[0] - 1, -1, -1):
        v = best_fit[i]
        if ix_peak_end is None:
            if v > threshold:
                ix_peak_end = i
                break

    return ix_peak_start, ix_peak_end


class PeakFitter(object):

    def __init__(self, null_model, null_params, peak_model, peak_params, half_peak_model,
                 peak_limit_frc=.2):
        self.null_model = null_model
        self.null_params = null_params
        self.peak_model = peak_model
        self.peak_params = peak_params
        self.half_peak_model = half_peak_model
        self.peak_limit_frc = peak_limit_frc

    def split_peak_params(self, peak_result):
        raise NotImplemented

    def get_baseline(self, peak_result):
        baseline = peak_result.params['baseline'].value
        baseline_stderr = peak_result.params['baseline'].stderr
        return baseline, baseline_stderr

    def fit(self, x, y, center, flank):

        # slice out the region of data to fit against
        ix_left = bisect_left(x, center - flank)
        ix_right = bisect_right(x, center + flank)
        loc = slice(ix_left, ix_right)
        xx = x[loc] - center  # make relative to center
        yy = y[loc]

        # split data into two flanks
        ix_cen = bisect_right(xx, 0)
        xx_left = -xx[:ix_cen]
        yy_left = yy[:ix_cen]
        xx_right = xx[ix_cen:]
        yy_right = yy[ix_cen:]

        # check number of data points on each flank
        if xx_left.shape[0] < 3 or xx_right.shape[0] < 3:
            # print('not enough data points', xx_left.shape, xx_right.shape)
            return None

        # fit the null model - exclude one outlier
        no_outlier = np.ones(yy.shape, dtype=bool)
        no_outlier[np.argmax(yy)] = False
        null_result = self.null_model.fit(yy[no_outlier], x=xx[no_outlier],
                                          params=self.null_params)

        # fit the peak model
        peak_result = self.peak_model.fit(yy, x=xx, params=self.peak_params)

        # obtain best fit for peak data for subtracting from values
        baseline, baseline_stderr = self.get_baseline(peak_result)
        best_fit = peak_result.best_fit
        peak = best_fit - baseline
        residual = yy - peak
        peak_height = np.max(peak)

        # figure out the width of the peak
        threshold = baseline + self.peak_limit_frc * peak_height
        # this doesn't work sometimes, because baseline stderr can be too small
        # threshold = baseline + 3 * baseline_stderr
        rix_peak_start, rix_peak_end = find_peak_limits(best_fit, threshold=threshold)
        if rix_peak_start is None or rix_peak_end is None or rix_peak_start == rix_peak_end:
            # print('could not find peak limits', rix_peak_start, rix_peak_end)
            # print(peak_result.fit_report())
            return None
        assert rix_peak_start < rix_peak_end
        peak_start_ix = ix_left + rix_peak_start
        peak_end_ix = ix_left + rix_peak_end
        peak_start_x = xx[rix_peak_start]
        peak_end_x = xx[rix_peak_end]

        # obtain fit for left and right flanks separately
        peak_params_left, peak_params_right = self.split_peak_params(peak_result)
        peak_result_left = self.half_peak_model.fit(yy_left, x=xx_left, params=peak_params_left)
        null_result_left = self.null_model.fit(yy_left, x=xx_left, params=self.null_params)
        peak_result_right = self.half_peak_model.fit(yy_right, x=xx_right, params=peak_params_right)
        null_result_right = self.null_model.fit(yy_right, x=xx_right, params=self.null_params)

        # obtain differences in AIC
        delta_aic = null_result.aic - peak_result.aic
        delta_aic_left = null_result_left.aic - peak_result_left.aic
        delta_aic_right = null_result_right.aic - peak_result_right.aic

        return PeakFitResult(null_result=null_result,
                             peak_result=peak_result,
                             null_result_left=null_result_left,
                             null_result_right=null_result_right,
                             peak_result_left=peak_result_left,
                             peak_result_right=peak_result_right,
                             xx=xx, yy=yy, loc=loc, best_fit=best_fit,
                             baseline=baseline, baseline_stderr=baseline_stderr,
                             peak=peak, peak_start_ix=peak_start_ix,
                             peak_end_ix=peak_end_ix, peak_start_x=peak_start_x,
                             peak_end_x=peak_end_x, residual=residual,
                             delta_aic=delta_aic, delta_aic_left=delta_aic_left,
                             delta_aic_right=delta_aic_right)


class ExponentialPeakFitter(PeakFitter):

    def __init__(self, amplitude, decay, baseline, floor, ceiling, null, peak_limit_frc=.2):

        # initialise null model
        null_model = lmfit.models.ConstantModel()
        null_params = lmfit.Parameters()
        null_params['c'] = null

        # initialise peak model
        peak_model = lmfit.Model(exponential_peak)
        peak_params = lmfit.Parameters()
        peak_params['center'] = lmfit.Parameter(value=0, vary=False)
        peak_params['amplitude'] = amplitude
        peak_params['decay'] = decay
        peak_params['baseline'] = baseline
        peak_params['ceiling'] = ceiling
        peak_params['floor'] = floor

        # initialise flank model
        half_peak_model = lmfit.Model(exponential)

        super(ExponentialPeakFitter, self).__init__(
            null_model=null_model, null_params=null_params, peak_model=peak_model,
            peak_params=peak_params, half_peak_model=half_peak_model, peak_limit_frc=peak_limit_frc
        )

    def split_peak_params(self, peak_result):
        amplitude = peak_result.params['amplitude'].value
        decay = peak_result.params['decay'].value
        baseline = peak_result.params['baseline'].value
        floor = peak_result.params['floor'].value
        ceiling = peak_result.params['ceiling'].value
        half_peak_params = lmfit.Parameters()
        half_peak_params['amplitude'] = lmfit.Parameter(value=amplitude, vary=False)
        half_peak_params['decay'] = lmfit.Parameter(value=decay, vary=False)
        half_peak_params['baseline'] = lmfit.Parameter(value=baseline, vary=False)
        half_peak_params['floor'] = lmfit.Parameter(value=floor, vary=False)
        half_peak_params['ceiling'] = lmfit.Parameter(value=ceiling, vary=False)
        return half_peak_params, half_peak_params


class SkewedExponentialPeakFitter(PeakFitter):

    def __init__(self, amplitude, decay, skew, baseline, floor, ceiling, null, peak_limit_frc=.2):

        # initialise null model
        null_model = lmfit.models.ConstantModel()
        null_params = lmfit.Parameters()
        null_params['c'] = null

        # initialise peak model
        peak_model = lmfit.Model(skewed_exponential_peak)
        peak_params = lmfit.Parameters()
        peak_params['center'] = lmfit.Parameter(value=0, vary=False)
        peak_params['amplitude'] = amplitude
        peak_params['decay'] = decay
        peak_params['skew'] = skew
        peak_params['baseline'] = baseline
        peak_params['ceiling'] = ceiling
        peak_params['floor'] = floor

        # initialise flank model
        half_peak_model = lmfit.Model(exponential)

        super(SkewedExponentialPeakFitter, self).__init__(
            null_model=null_model, null_params=null_params, peak_model=peak_model,
            peak_params=peak_params, half_peak_model=half_peak_model, peak_limit_frc=peak_limit_frc
        )

    def split_peak_params(self, peak_result):

        amplitude = peak_result.params['amplitude'].value
        decay = peak_result.params['decay'].value
        skew = peak_result.params['skew'].value
        decay_right = 2**(-skew) * decay
        decay_left = 2**skew * decay
        baseline = peak_result.params['baseline'].value
        floor = peak_result.params['floor'].value
        ceiling = peak_result.params['ceiling'].value

        peak_params_left = lmfit.Parameters()
        peak_params_left['amplitude'] = lmfit.Parameter(value=amplitude, vary=False)
        peak_params_left['decay'] = lmfit.Parameter(value=decay_left, vary=False)
        peak_params_left['baseline'] = lmfit.Parameter(value=baseline, vary=False)
        peak_params_left['floor'] = lmfit.Parameter(value=floor, vary=False)
        peak_params_left['ceiling'] = lmfit.Parameter(value=ceiling, vary=False)

        peak_params_right = lmfit.Parameters()
        peak_params_right['amplitude'] = lmfit.Parameter(value=amplitude, vary=False)
        peak_params_right['decay'] = lmfit.Parameter(value=decay_right, vary=False)
        peak_params_right['baseline'] = lmfit.Parameter(value=baseline, vary=False)
        peak_params_right['floor'] = lmfit.Parameter(value=floor, vary=False)
        peak_params_right['ceiling'] = lmfit.Parameter(value=ceiling, vary=False)

        return peak_params_left, peak_params_right


class GaussianPeakFitter(PeakFitter):

    def __init__(self, amplitude, sigma, baseline, floor, ceiling, null, peak_limit_frc=.2):

        # initialise null model
        null_model = lmfit.models.ConstantModel()
        null_params = lmfit.Parameters()
        null_params['c'] = null

        # initialise peak model
        peak_model = lmfit.models.Model(gaussian)
        peak_params = lmfit.Parameters()
        peak_params['center'] = lmfit.Parameter(value=0, vary=False)
        peak_params['amplitude'] = amplitude
        peak_params['sigma'] = sigma
        peak_params['baseline'] = baseline
        peak_params['ceiling'] = ceiling
        peak_params['floor'] = floor

        # initialise flank model
        half_peak_model = lmfit.models.Model(gaussian)

        super(GaussianPeakFitter, self).__init__(
            null_model=null_model, null_params=null_params, peak_model=peak_model,
            peak_params=peak_params, half_peak_model=half_peak_model, peak_limit_frc=peak_limit_frc
        )

    def get_baseline(self, peak_result):
        baseline = peak_result.params['baseline'].value
        baseline_stderr = peak_result.params['baseline'].stderr
        return baseline, baseline_stderr

    def split_peak_params(self, peak_result):
        amplitude = peak_result.params['amplitude'].value
        sigma = peak_result.params['sigma'].value
        baseline = peak_result.params['baseline'].value
        floor = peak_result.params['floor'].value
        ceiling = peak_result.params['ceiling'].value
        half_peak_params = lmfit.Parameters()
        half_peak_params['amplitude'] = lmfit.Parameter(value=amplitude, vary=False)
        half_peak_params['sigma'] = lmfit.Parameter(value=sigma, vary=False)
        half_peak_params['baseline'] = lmfit.Parameter(value=baseline, vary=False)
        half_peak_params['center'] = lmfit.Parameter(value=0, vary=False)
        half_peak_params['floor'] = lmfit.Parameter(value=floor, vary=False)
        half_peak_params['ceiling'] = lmfit.Parameter(value=ceiling, vary=False)
        return half_peak_params, half_peak_params


class SkewedGaussianPeakFitter(PeakFitter):

    def __init__(self, amplitude, sigma, skew, baseline, floor, ceiling, null, peak_limit_frc=.2):

        # initialise null model
        null_model = lmfit.models.ConstantModel()
        null_params = lmfit.Parameters()
        null_params['c'] = null

        # initialise peak model
        peak_model = lmfit.Model(skewed_gaussian)
        peak_params = lmfit.Parameters()
        peak_params['center'] = lmfit.Parameter(value=0, vary=False)
        peak_params['amplitude'] = amplitude
        peak_params['sigma'] = sigma
        peak_params['skew'] = skew
        peak_params['baseline'] = baseline
        peak_params['ceiling'] = ceiling
        peak_params['floor'] = floor

        # initialise flank model
        half_peak_model = lmfit.Model(gaussian)

        super(SkewedGaussianPeakFitter, self).__init__(
            null_model=null_model, null_params=null_params, peak_model=peak_model,
            peak_params=peak_params, half_peak_model=half_peak_model, peak_limit_frc=peak_limit_frc
        )

    def split_peak_params(self, peak_result):

        amplitude = peak_result.params['amplitude'].value
        sigma = peak_result.params['sigma'].value
        skew = peak_result.params['skew'].value
        sigma_right = 2**(-skew) * sigma
        sigma_left = 2**skew * sigma
        baseline = peak_result.params['baseline'].value
        floor = peak_result.params['floor'].value
        ceiling = peak_result.params['ceiling'].value

        peak_params_left = lmfit.Parameters()
        peak_params_left['center'] = lmfit.Parameter(value=0, vary=False)
        peak_params_left['amplitude'] = lmfit.Parameter(value=amplitude, vary=False)
        peak_params_left['sigma'] = lmfit.Parameter(value=sigma_left, vary=False)
        peak_params_left['baseline'] = lmfit.Parameter(value=baseline, vary=False)
        peak_params_left['floor'] = lmfit.Parameter(value=floor, vary=False)
        peak_params_left['ceiling'] = lmfit.Parameter(value=ceiling, vary=False)

        peak_params_right = lmfit.Parameters()
        peak_params_right['center'] = lmfit.Parameter(value=0, vary=False)
        peak_params_right['amplitude'] = lmfit.Parameter(value=amplitude, vary=False)
        peak_params_right['sigma'] = lmfit.Parameter(value=sigma_right, vary=False)
        peak_params_right['baseline'] = lmfit.Parameter(value=baseline, vary=False)
        peak_params_right['floor'] = lmfit.Parameter(value=floor, vary=False)
        peak_params_right['ceiling'] = lmfit.Parameter(value=ceiling, vary=False)

        return peak_params_left, peak_params_right


import os


def setup_logging(log_file, output_dir, verbose):

    # determine path to log file
    log_path = None
    if log_file:
        if output_dir:
            log_path = os.path.join(output_dir, log_file)
        else:
            log_path = log_file
        if os.path.exists(log_path):
            os.remove(log_path)

    # define logging function
    def log(*args):
        if verbose:
            if log_path:
                with open(log_path, mode='a') as f:
                    kwargs = dict(file=f)
                    print(*args, **kwargs)
            else:
                print(*args)

    return log


Peak = collections.namedtuple(
    'Peak',
    'peak_fit delta_aic delta_aic_left delta_aic_right peak_center_ix epicenter '
    'focus_start focus_end peak_start peak_end pos gpos values max_value max_percentile'
)


def find_peaks(starts, ends, values, percentiles, centers, gflank, gmap, fitters,
               min_flank_delta_aic=20, min_peak_delta_aic=80, max_iter=100,
               extend_focus_frc=0.05, verbose=True, output_dir=None, log_file='log.txt',
               dpi=None, statistic_label='Selection statistic', show_plots=False):
    """Iterative algorithm to find peaks.

    Parameters
    ----------
    starts : ndarray
        Array of window start positions (physical distance).
    ends : ndarray
        Array of window end positions (physical distance).
    values : ndarray
        Selection statistic windowed values.
    percentiles : ndarray
        Selection statistic windowed percentiles.
    centers : ndarray
        Positions at which to fit peak models (physical distance).
    gflank : float
        Size of flank to use when fitting (genetic distance).
    gmap : ndarray
        Genetic map.
    fitters : sequence of PeakFitters
        Peak fitters.
    min_flank_delta_aic : float, optional
        If either flank falls below this value, peak will be skipped.
    min_peak_delta_aic : float, optional
        Do not report peaks below this value.
    max_iter : int, optional
        Limit number of iterations (mostly useful for debugging).
    extend_focus_frc : float, optional
        Extend the peak focus as long as the delta AIC difference with the peak value
        remains within this fraction of the peak value.
    verbose : bool, optional
        Log more.
    output_dir : str, optional
        Path to output directory.
    log_file : str, optional
        Name of log file.
    dpi : int, optional
        Plotting resolution.
    statistic_label : str, optional
        Name of selection statistic.
    show_plots : bool, optional
        Set True to have plots shown after each iteration.

    """

    # setup logging
    log = setup_logging(log_file, output_dir, verbose)

    # check input data
    starts = np.asarray(starts)
    ends = np.asarray(ends)
    pos = ((starts + ends) / 2).astype(int)
    original_values = np.asarray(values)
    values = original_values.copy()
    # check no missing data
    assert ~np.any(np.isnan(values))
    percentiles = np.asarray(percentiles)
    assert (starts.shape == ends.shape == values.shape == percentiles.shape)

    # prepare centers and positions in genetic distance
    centers = np.asarray(centers, dtype=int)
    gcenters = gmap.take(centers - 1)
    n_centers = centers.shape[0]
    gpos = gmap.take(pos - 1)
    gstarts = gmap.take(starts - 1)
    gends = gmap.take(ends - 1)

    # setup working data structures
    delta_aics = np.zeros(n_centers, dtype='f4')
    flank_delta_aics = np.zeros((n_centers, 2), dtype='f4')
    fits = np.empty(n_centers, dtype=object)
    in_peak = np.zeros(n_centers, dtype=bool)

    # first pass model fits
    scan_fit(gpos, values, gcenters=gcenters, gflank=gflank, fitters=fitters, delta_aics=delta_aics,
             flank_delta_aics=flank_delta_aics, fits=fits, log=log, gstart=None,
             gend=None)

    # keep track of which iteration we're on, starting from 1 (be human friendly)
    iteration = 1

    # find the first peak
    peak_cix = np.argmax(delta_aics)
    peak_delta_aic = delta_aics[peak_cix]
    peak_fit = fits[peak_cix]
    log('first peak:', peak_cix, peak_delta_aic)

    # iterate
    while peak_delta_aic > min_peak_delta_aic and iteration < max_iter:

        log('=' * 80)
        log('Iteration', iteration)
        log('Peak center (index, location): {}, {:.1f}'
            .format(peak_cix, centers[peak_cix]))
        log('Delta AIC: {:.1f}'.format(peak_delta_aic))
        log('Flank delta AICs: {:.1f}, {:.1f}'.format(*flank_delta_aics[peak_cix]))

        log('find limits of peak')
        # N.B., physical coords
        peak_start = int(starts[peak_fit.peak_start_ix])
        peak_end = int(ends[peak_fit.peak_end_ix])
        peak_gstart = float(gstarts[peak_fit.peak_start_ix])
        peak_gend = float(gends[peak_fit.peak_end_ix])
        peak_start_cix = min(peak_cix, bisect_left(centers, peak_start))
        peak_end_cix = max(peak_cix, bisect_right(centers, peak_end)) + 1
        log('peak limits:', peak_start, peak_end, peak_start_cix, peak_end_cix)

        log('check flank fits')
        peak_delta_aic_left, peak_delta_aic_right = flank_delta_aics[peak_cix]
        minor_flank_delta_aic = min(peak_delta_aic_left, peak_delta_aic_right)

        if minor_flank_delta_aic < min_flank_delta_aic:
            log('POOR FLANK: SKIPPING PEAK')

            log('plot some diagnostics for the peak fit')
            plot_peak_fit(peak_fit, ylabel=statistic_label, dpi=dpi)
            log(peak_fit.peak_result.fit_report())
            log(peak_fit.null_result.fit_report())

            # scrub delta aics in the peak region, so we don't find the same peak twice
            in_peak[peak_start_cix:peak_end_cix] = True
            delta_aics[in_peak] = 0
            flank_delta_aics[in_peak, :] = 0
            fits[in_peak] = None

        else:
            log('FLANK OK: PROCESSING PEAK')
            log(peak_fit.peak_result.fit_report())
            log(peak_fit.null_result.fit_report())

            log('setup output directory for this peak')
            if output_dir:
                peak_dir = os.path.join(output_dir, str(iteration))
                os.makedirs(peak_dir, exist_ok=True)
            else:
                peak_dir = None

            log('plot some diagnostics about the peak finding algorithm')
            plot_peak_finding(pos, values, original_values, centers=centers,
                              delta_aics=delta_aics, peak_center_ix=peak_cix,
                              iteration=iteration, ylabel=statistic_label,
                              peak_dir=peak_dir, dpi=dpi)

            log('plot some diagnostics for the peak fit')
            plot_peak_fit(peak_fit, ylabel=statistic_label, peak_dir=peak_dir, dpi=dpi)

            log('find focus of selection')
            epicenter = int(centers[peak_cix])
            log('epicenter:', epicenter)
            # TODO review this logic for deciding boundaries
            focus_start = int(centers[peak_cix - 1])
            focus_end = int(centers[peak_cix + 1])
            # search left
            i = peak_cix - 2
            while peak_start_cix <= i <= peak_end_cix:
                if (fits[i] is not None and
                        (peak_delta_aic - fits[i].delta_aic) <
                        (extend_focus_frc * peak_delta_aic)):
                    focus_start = int(centers[i])
                    log('extend focus left', focus_start)
                    i -= 1
                else:
                    break
            # search right
            i = peak_cix + 2
            while peak_start_cix <= i <= peak_end_cix:
                if (fits[i] is not None and
                        (peak_delta_aic - fits[i].delta_aic) <
                        (extend_focus_frc * peak_delta_aic)):
                    focus_end = int(centers[i])
                    log('extend focus right', focus_end)
                    i += 1
                else:
                    break
            log('found focus:', focus_start, focus_end)

            # plot peak focus
            plot_peak_focus(pos, original_values, peak_fit=peak_fit, epicenter=epicenter,
                            focus_start=focus_start, focus_end=focus_end,
                            peak_start=peak_start, peak_end=peak_end, ylabel=statistic_label,
                            dpi=dpi, peak_dir=peak_dir)

            # plot peak targetting diagnostics
            plot_peak_targetting(epicenter, focus_start, focus_end, peak_start, peak_end,
                                 centers=centers, delta_aics=delta_aics,
                                 flank_delta_aics=flank_delta_aics, dpi=dpi,
                                 peak_dir=peak_dir)

            log('find max peak value')
            peak_start_pix = bisect_left(pos, peak_start)
            peak_end_pix = bisect_right(pos, peak_end)
            peak_values = values[peak_start_pix:peak_end_pix]
            peak_max_value_ix = peak_start_pix + np.argmax(peak_values)
            peak_max_value = values[peak_max_value_ix]
            peak_max_percentile = percentiles[peak_max_value_ix]

            log('yield peak')
            yield Peak(peak_fit=peak_fit, delta_aic=peak_delta_aic,
                       delta_aic_left=peak_delta_aic_left, delta_aic_right=peak_delta_aic_right,
                       peak_center_ix=peak_cix, epicenter=epicenter, focus_start=focus_start,
                       focus_end=focus_end, peak_start=peak_start, peak_end=peak_end,
                       pos=pos[peak_fit.loc], gpos=gpos[peak_fit.loc],
                       values=original_values[peak_fit.loc], max_value=peak_max_value,
                       max_percentile=peak_max_percentile)
            iteration += 1

            log('subtract peak from values')
            # TODO clip might not always be appropriate here
            values[peak_fit.loc] = (values[peak_fit.loc] - peak_fit.peak).clip(0, None)

            log('rescan region around the peak')
            scan_fit(gpos, values, gcenters=gcenters, gflank=gflank, fitters=fitters,
                     delta_aics=delta_aics, flank_delta_aics=flank_delta_aics, fits=fits,
                     log=log, gstart=gcenters[peak_cix] - (gflank * 2), gend=peak_gstart)
            scan_fit(gpos, values, gcenters=gcenters, gflank=gflank, fitters=fitters,
                     delta_aics=delta_aics, flank_delta_aics=flank_delta_aics, fits=fits,
                     log=log, gstart=peak_gend, gend=gcenters[peak_cix] + (gflank * 2))

            # scrub delta aics in the peak region, to guarantee no signal from residuals
            in_peak[peak_start_cix:peak_end_cix] = True
            delta_aics[in_peak] = 0
            flank_delta_aics[in_peak, :] = 0
            fits[in_peak] = None

        if show_plots:
            plt.show()
        plt.close()

        log('find the next peak')
        # find the next peak
        peak_cix = np.argmax(delta_aics)
        peak_delta_aic = delta_aics[peak_cix]
        peak_fit = fits[peak_cix]
        log('next peak:', peak_cix, peak_delta_aic)

    log('all done')


def scan_fit(gpos, values, gcenters, gflank, fitters, delta_aics, flank_delta_aics, fits, log,
             gstart, gend):

    # determine region to scan
    n = gcenters.shape[0]
    if gstart is None:
        start_index = 0
    else:
        start_index = bisect_left(gcenters, gstart)
    if gend is None:
        end_index = n
    else:
        end_index = bisect_right(gcenters, gend)
    assert 0 <= start_index < end_index <= n

    # iterate and fit
    for i in range(start_index, end_index):
        if i % 100 == 0:
            log('scan progress', i, gcenters[i])

        # central position to fit peak at
        gcenter = gcenters[i]

        # fit the peak
        results = [fitter.fit(x=gpos, y=values, center=gcenter, flank=gflank)
                   for fitter in fitters]
        results = [fit for fit in results if fit is not None]
        fit = None
        if results:
            # take the best fit
            results = sorted(results, key=lambda o: o.delta_aic, reverse=True)
            fit = results[0]

        # store the results
        if fit is not None:
            fits[i] = fit
            delta_aics[i] = fit.delta_aic
            flank_delta_aics[i, 0] = fit.delta_aic_left
            flank_delta_aics[i, 1] = fit.delta_aic_right


def plot_peak_fit(fit, figsize=(8, 2.5), dpi=None, xlabel='Genetic distance (cM)',
                  ylabel='Selection statistic', peak_dir=None):

    # noinspection PyTypeChecker
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=figsize, facecolor='w', dpi=dpi)
    plot_opts = dict(marker='o', linestyle=' ', markersize=2, mfc='none',
                     color=palette[0], mew=.5)

    ax = axs[0]
    # plot width of the peak
    ax.axvspan(fit.peak_start_x, fit.peak_end_x, facecolor=palette[0], alpha=.2)
    # plot the best fit line
    ax.plot(fit.xx, fit.best_fit, lw=.5, linestyle='--', color='k')
    # # plot the baseline
    # if fit.baseline is not None:
    #     ax.axhline(fit.baseline, lw=1, linestyle='--', color='k')
    # plot the data
    ax.plot(fit.xx, fit.yy, **plot_opts)
    ax.text(.02, .98, r'$\Delta_{i}$ : %.1f' % fit.delta_aic_left,
            transform=ax.transAxes, ha='left', va='top')
    ax.text(.98, .98, r'$\Delta_{i}$ : %.1f' % fit.delta_aic_right,
            transform=ax.transAxes, ha='right', va='top')
    ax.text(.5, 1.02, r'$\Delta_{i}$ : %.1f' % fit.delta_aic,
            transform=ax.transAxes, ha='center', va='bottom')
    ax.set_title('Peak fit', loc='left')
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_ylim(bottom=0)

    ax = axs[1]
    ax.axhline(fit.baseline, lw=.5, linestyle='--', color='k')
    ax.plot(fit.xx, fit.residual, **plot_opts)
    ax.set_ylim(axs[0].get_ylim())
    ax.set_title('Residual', loc='left')
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_ylim(bottom=0)

    ax = axs[2]
    ax.hist(fit.residual, bins=30)
    ax.axvline(fit.baseline, lw=.5, linestyle='--', color='k')
    ax.set_xlabel(ylabel)
    ax.set_ylabel('Frequency')
    ax.set_title('Residual', loc='left')

    fig.tight_layout()
    if peak_dir:
        fig.savefig(os.path.join(peak_dir, 'peak_fit.png'), bbox_inches='tight', dpi=dpi,
                    facecolor='w')

    return fig


def plot_peak_finding(pos, values, original_values, centers, delta_aics, peak_center_ix,
                      iteration, ylabel='Selection statistic', figsize=(8, 5), peak_dir=None,
                      dpi=None):
    # noinspection PyTypeChecker
    fig, axs = plt.subplots(nrows=3, figsize=figsize, sharex=True, dpi=dpi, facecolor='w')
    vline_opts = dict(linestyle='--', lw=.5, color='k')
    plot_opts = dict(marker='o', linestyle=' ', markersize=2, mfc='none', mew=.5)

    # plot original values over the genome
    ax = axs[0]
    ax.axvline(centers[peak_center_ix], **vline_opts)
    ax.plot(pos, original_values, **plot_opts)
    ax.set_ylim(bottom=0)
    ax.set_ylabel(ylabel)
    ax.set_title('Original values')

    # plot remaining values over the genome
    ax = axs[1]
    ax.axvline(centers[peak_center_ix], **vline_opts)
    ax.plot(pos, values, **plot_opts)
    ax.set_ylim(axs[0].get_ylim())
    ax.set_ylabel(ylabel)
    ax.set_title('Remaining values at iteration {}'.format(iteration))

    # plot delta AICs over the genome
    ax = axs[2]
    ax.plot(centers, delta_aics, lw=.5)
    ax.text(centers[peak_center_ix], delta_aics[peak_center_ix], 'v', va='bottom', ha='center')
    ax.set_ylim(bottom=0)
    ax.set_ylabel(r'$\Delta_{i}$')
    ax.set_xticklabels(['{:.1f}'.format(x/1e6) for x in ax.get_xticks()])
    ax.set_xlabel('Position (Mbp)')
    ax.set_title('Peak model fits at iteration {}'.format(iteration))

    fig.tight_layout()
    if peak_dir:
        fig.savefig(os.path.join(peak_dir, 'peak_finding.png'), bbox_inches='tight', dpi=dpi,
                    facecolor='w')

    return fig


def plot_peak_focus(pos, values, peak_fit, epicenter, focus_start, focus_end, peak_start, peak_end,
                    figsize=(6, 3), ylabel='Selection statistic', peak_dir=None, dpi=None):

    # noinspection PyTypeChecker
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi, facecolor='w')
    plot_opts = dict(marker='o', linestyle=' ', color=palette[0], mew=.5, mfc='none', markersize=2)

    # plot linked regions
    ax.axvspan(peak_start, focus_start, color=palette[0], alpha=.2)
    ax.axvspan(focus_end, peak_end, color=palette[0], alpha=.2)

    # plot focus
    ax.axvspan(focus_start, focus_end, color=palette[3], alpha=.3)

    # plot epicenter
    ax.axvline(epicenter, color=palette[3], alpha=1, lw=1)

    # plot fit
    ax.plot(pos[peak_fit.loc], peak_fit.best_fit, linestyle='--', color='k', lw=.5)

    # plot values
    ax.plot(pos[peak_fit.loc], values[peak_fit.loc], **plot_opts)

    # tidy up
    ax.set_xticklabels(['{:.1f}'.format(x/1e6) for x in ax.get_xticks()])
    ax.set_xlabel('Position (Mbp)')
    ax.set_ylabel(ylabel)
    ax.set_ylim(bottom=0)
    fig.tight_layout()

    # output
    if peak_dir:
        fig.savefig(os.path.join(peak_dir, 'peak_focus.png'), bbox_inches='tight', dpi=dpi,
                    facecolor='w')

    return fig


def plot_peak_targetting(epicenter, focus_start, focus_end, peak_start, peak_end,
                         centers, delta_aics, flank_delta_aics, figsize=(6, 3), dpi=None,
                         peak_dir=None):

    # noinspection PyTypeChecker
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi, facecolor='w')

    # plot focus and epicenter
    ax.axvspan(focus_start, focus_end, color=palette[3], alpha=.3)
    ax.axvline(epicenter, color=palette[3], alpha=1, lw=2)

    # plot AICs
    loc = slice(bisect_left(centers, peak_start), bisect_right(centers, peak_end))
    x = centers[loc]
    y1 = delta_aics[loc]
    y2 = flank_delta_aics[loc, 0]
    y3 = flank_delta_aics[loc, 1]
    ax.plot(x, y1, lw=2, label='peak')
    ax.plot(x, y2, lw=2, label='left flank')
    ax.plot(x, y3, lw=2, label='right flank')

    # tidy
    ax.set_xticklabels(['{:.2f}'.format(x/1e6) for x in ax.get_xticks()])
    ax.set_xlabel('Position (Mbp)')
    ax.set_ylabel(r'Model fit ($\Delta_{i}$)')
    ax.set_ylim(bottom=0)
    ax.set_title('Peak targetting')
    ax.legend(loc='upper right', title='Model')
    fig.tight_layout()

    # output
    if peak_dir:
        fig.savefig(os.path.join(peak_dir, 'peak_targetting.png'), bbox_inches='tight', dpi=dpi,
                    facecolor='w')

    return fig
