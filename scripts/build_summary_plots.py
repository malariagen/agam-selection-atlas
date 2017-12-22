# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
import yaml
from glob import glob
import os
import allel
import pandas as pd
import matplotlib as mpl
import sys
import numpy as np
import bokeh.plotting as bplt
import bokeh.models as bmod
import bokeh.layouts as blay
import bokeh.embed as bemb
import itertools
sys.path.insert(0, 'agam-report-base/src/python')
from ag1k import phase1_ar3
# setup data sources
ag1k_dir = 'ngs.sanger.ac.uk/production/ag1000g/phase1'
phase1_ar3.init(os.path.join(ag1k_dir, 'AR3'))
genome = phase1_ar3.genome
import seaborn as sns
palette = [mpl.colors.rgb2hex(c) for c in sns.color_palette()]


def plot_genes(genes, chrom, start, stop, fig=None, offset=0, x_range=None,
               plot_width=900, plot_height=100):

    # setup figure
    if fig is None:
        hover = bmod.HoverTool(
            tooltips="<p>@label<br/>@seqid:@start{,}-@end{,}</p>")
        fig = bplt.figure(title='Genes', plot_width=plot_width,
                          plot_height=plot_height, x_range=x_range,
                          tools='xpan,xzoom_in,xzoom_out,xwheel_zoom,'
                                'reset,tap'.split() + [hover],
                          toolbar_location='above', active_drag='xpan',
                          active_scroll='xwheel_zoom')
        fig.xaxis.axis_label = 'Chromosome {} position (Mbp)'.format(chrom)
        url = '../gene/@id'
        taptool = fig.select(type=bmod.TapTool)
        taptool.callback = bmod.OpenURL(url=url)

    # handle joined chromosomes
    if chrom in '23':
        # plot R arm (on the left)
        rarm = '{}R'.format(chrom)
        rarm_len = len(genome[rarm])
        if start < rarm_len:
            rarm_start = start
            rarm_stop = min(rarm_len, stop)
            plot_genes(genes, rarm, rarm_start, rarm_stop, fig=fig)
        # plot L arm (on the right)
        larm = '{}L'.format(chrom)
        if stop > rarm_len:
            larm_start = max(0, start - rarm_len)
            larm_stop = stop - rarm_len
            plot_genes(genes, larm, larm_start, larm_stop, fig=fig,
                       offset=rarm_len)
        return fig

    # from here assume single arm
    arm = chrom
    df = genes[(genes.seqid == arm) &
               (genes.end >= start) &
               (genes.start <= stop)]
    labels = [('{}'.format(gene.ID) +
               (' ({})'.format(gene.Name) if gene.Name else '') +
               (' - {}'.format(gene.description.split('[Source:')[0])
                if gene.description else ''))
              for _, gene in df.iterrows()]
#     hover = bmod.HoverTool(tooltips=[
#         ("ID", '@id'),
#         ("Name", '@name'),
#         ("Description", '@description'),
#         ("Location", "@seqid:@start-@end"),
#     ])
    bottom = np.zeros(len(df))
    bottom[df.strand == '+'] = 1
    source = bmod.ColumnDataSource(data={
        'seqid': df.seqid,
        'start': df.start,
        'end': df.end,
        'left': (df.start + offset) / 1e6,
        'right': (df.end + offset) / 1e6,
        'bottom': bottom,
        'top': bottom + .8,
        'id': df.ID,
        'name': df.Name,
        'description': df.description,
        'label': labels,
    })
    fig.quad(bottom='bottom', top='top', left='left', right='right',
             source=source, line_width=0)
    fig.y_range = bmod.Range1d(-.5, 2.3)
    yticks = [0.4, 1.4]
    yticklabels = ['reverse', 'forward']
    fig.yaxis.ticker = yticks
    fig.yaxis.major_label_overrides = {k: v for k, v in zip(yticks, yticklabels)}
    fig.ygrid.visible = False

    return fig


def stack_overlaps(df, start_col, stop_col, tolerance=10000):
    occupants = [None]
    out = []
    for _, cur in df.iterrows():

        level = 0
        prv = occupants[level]
        # search upwards to find the first vacant level
        while prv is not None and cur[start_col] <= (prv[stop_col] + tolerance):
            level += 1
            if level == len(occupants):
                occupants.append(None)
            prv = occupants[level]
        occupants[level] = cur
        out.append(level)
    return np.asarray(out)


def plot_signals(df_signals, seqid, populations):

    # setup
    if len(seqid) > 1:
        arm = seqid[1]
    else:
        arm = None
    seq_len = len(genome[seqid])

    # find overlapping peaks
    df = df_signals[(df_signals.peak_start_arm == seqid) |
                    (df_signals.peak_stop_arm == seqid)].copy()

    # fix coordinates where peaks span two arms
    peak_start_arm = df.peak_start_arm
    peak_stop_arm = df.peak_stop_arm
    peak_start = df.peak_start.copy()
    peak_stop = df.peak_stop.copy()
    if arm == 'R':
        peak_stop[peak_stop_arm != seqid] = seq_len
    elif arm == 'L':
        peak_start[peak_start_arm != seqid] = 1
    df['peak_start_fixed'] = peak_start
    df['peak_stop_fixed'] = peak_stop
    focus_start_arm = df.focus_start_arm
    focus_stop_arm = df.focus_stop_arm
    focus_start = df.focus_start.copy()
    focus_stop = df.focus_stop.copy()
    if arm == 'R':
        focus_start[focus_start_arm != seqid] = seq_len
        focus_stop[focus_stop_arm != seqid] = seq_len
    elif arm == 'L':
        focus_start[focus_start_arm != seqid] = 1
        focus_stop[focus_stop_arm != seqid] = 1
    df['focus_start_fixed'] = focus_start
    df['focus_stop_fixed'] = focus_stop

    # sort by peak start
    df.sort_values(by='peak_start_fixed', inplace=True)

    # stack up signals to avoid overlaps
    df['level'] = stack_overlaps(df, 'peak_start_fixed', 'peak_stop_fixed')

    # setup plotting data source
    source = bmod.ColumnDataSource(data={
        'population': df.population,
        'pop_label': [pop_labels[p] for p in df.population],
        'statistic': df.statistic,
        'chromosome': df.chromosome,
        'rank': df['rank'],
        'score': df.sum_delta_aic.astype(int),
        'peak_start_coord': df.peak_start_fixed / 1e6,
        'peak_stop_coord': df.peak_stop_fixed / 1e6,
        'focus_start_arm': df.focus_start_arm,
        'focus_stop_arm': df.focus_stop_arm,
        'focus_start': df.focus_start,
        'focus_stop': df.focus_stop,
        'focus_start_coord': df.focus_start_fixed / 1e6,
        'focus_stop_coord': df.focus_stop_fixed / 1e6,
        'bottom': df.level,
        'top': df.level + .8,
    })

    hover = bmod.HoverTool(tooltips=[
        ('Population', '@pop_label'),
        ('Statistic', '@statistic'),
        ('Score', '@score'),
        ('Focus',
         '@focus_start_arm:@focus_start{,} - @focus_stop_arm:@focus_stop{,}'),
    ])

    tools = 'tap,xpan,xzoom_in,xzoom_out,xwheel_zoom,reset'.split() + [hover]
    fig = bplt.figure(title='Selection signals',
                      plot_width=900, plot_height=90 + (10 * max(df.level)),
                      tools=tools, toolbar_location='above',
                      active_drag='xpan', active_scroll='xwheel_zoom')
    fig.quad(bottom='bottom', top='top', left='peak_start_coord',
             right='focus_start_coord', source=source, color=palette[0],
             alpha=.5, line_width=0)
    fig.quad(bottom='bottom', top='top', left='focus_start_coord',
             right='focus_stop_coord', source=source, color=palette[3],
             alpha=.7, line_width=0)
    fig.quad(bottom='bottom', top='top', left='focus_stop_coord',
             right='peak_stop_coord', source=source, color=palette[0],
             alpha=.5, line_width=0)
    fig.x_range = bmod.Range1d(0, seq_len / 1e6, bounds=(1, seq_len / 1e6))
    fig.y_range = bmod.Range1d(-0.5, max(df.level) + 1.3)
    fig.yaxis.visible = False
    fig.ygrid.visible = False
    fig.xaxis.axis_label = (
        'Chromosome {}{} position (Mbp)'
        .format('arm ' if arm else '', seqid)
    )
    url = '../signal/@statistic/@population/@chromosome/@rank/'
    taptool = fig.select(type=bmod.TapTool)
    taptool.callback = bmod.OpenURL(url=url)
    return fig
