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
seqids = '2R', '2L', '3R', '3L', 'X'


def plot_genes(genes, chrom, start=None, end=None, fig=None, offset=0, x_range=None,
               plot_width=900, plot_height=100, root_path='../'):

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
        url = root_path + 'gene/@id.html'
        taptool = fig.select(type=bmod.TapTool)
        taptool.callback = bmod.OpenURL(url=url)

    # handle joined chromosomes
    if chrom in '23':
        # plot R arm (on the left)
        rarm = '{}R'.format(chrom)
        rarm_len = len(genome[rarm])
        if start < rarm_len:
            rarm_start = start
            rarm_end = min(rarm_len, end)
            plot_genes(genes, rarm, rarm_start, rarm_end, fig=fig)
        # plot L arm (on the right)
        larm = '{}L'.format(chrom)
        if end > rarm_len:
            larm_start = max(0, start - rarm_len)
            larm_end = end - rarm_len
            plot_genes(genes, larm, larm_start, larm_end, fig=fig,
                       offset=rarm_len)
        return fig

    # from here assume single sequence
    seqid = chrom
    loc = (genes.seqid == seqid)
    if start is not None:
        loc = loc & (genes.end >= start)
    if end is not None:
        loc = loc & (genes.start <= end)
    df = genes[loc]
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


def stack_overlaps(df, start_col, end_col, tolerance=10000):
    occupants = [None]
    out = []
    for _, cur in df.iterrows():

        level = 0
        prv = occupants[level]
        # search upwards to find the first vacant level
        while prv is not None and cur[start_col] <= (prv[end_col] + tolerance):
            level += 1
            if level == len(occupants):
                occupants.append(None)
            prv = occupants[level]
        occupants[level] = cur
        out.append(level)
    return np.asarray(out)


def plot_signals(df_signals, seqid, pop_labels, root_path='../',
                 title='Selection signals'):

    # setup
    if len(seqid) > 1:
        arm = seqid[1]
    else:
        arm = None
    seq_len = len(genome[seqid])

    # find overlapping peaks
    loc = ((df_signals.peak_start_seqid == seqid) | (df_signals.peak_end_seqid == seqid))
    df = df_signals[loc].copy()

    # check there are signals
    if len(df) == 0:
        raise ValueError('no signals')

    # fix coordinates where peaks span two arms
    peak_start_seqid = df.peak_start_seqid
    peak_end_seqid = df.peak_end_seqid
    peak_start = df.peak_start.copy()
    peak_end = df.peak_end.copy()
    if arm == 'R':
        peak_end[peak_end_seqid != seqid] = seq_len
    elif arm == 'L':
        peak_start[peak_start_seqid != seqid] = 1
    df['peak_start_fixed'] = peak_start
    df['peak_end_fixed'] = peak_end
    focus_start_seqid = df.focus_start_seqid
    focus_end_seqid = df.focus_end_seqid
    focus_start = df.focus_start.copy()
    focus_end = df.focus_end.copy()
    if arm == 'R':
        focus_start[focus_start_seqid != seqid] = seq_len
        focus_end[focus_end_seqid != seqid] = seq_len
    elif arm == 'L':
        focus_start[focus_start_seqid != seqid] = 1
        focus_end[focus_end_seqid != seqid] = 1
    df['focus_start_fixed'] = focus_start
    df['focus_end_fixed'] = focus_end

    # sort by peak start
    df.sort_values(by='peak_start_fixed', inplace=True)

    # stack up signals to avoid overlaps
    df['level'] = stack_overlaps(df, 'peak_start_fixed', 'peak_end_fixed')

    # setup plotting data source
    source = bmod.ColumnDataSource(data={
        'population': df.population,
        'pop_label': [pop_labels[p].replace('*', '') for p in df.population],
        'statistic': df.statistic,
        'chromosome': df.chromosome,
        'rank': df['rank'],
        'score': df.sum_delta_aic.astype(int),
        'score_left': df.delta_aic_left.astype(int),
        'score_right': df.delta_aic_right.astype(int),
        'peak_start_coord': df.peak_start_fixed / 1e6,
        'peak_end_coord': df.peak_end_fixed / 1e6,
        'focus_start_seqid': df.focus_start_seqid,
        'focus_end_seqid': df.focus_end_seqid,
        'focus_start': df.focus_start,
        'focus_end': df.focus_end,
        'focus_start_coord': df.focus_start_fixed / 1e6,
        'focus_end_coord': df.focus_end_fixed / 1e6,
        'bottom': df.level,
        'top': df.level + .8,
    })

    # hover = bmod.HoverTool(tooltips=[
    #     ('Population', '@pop_label'),
    #     ('Statistic', '@statistic'),
    #     ('Score', '@score (@score_left | @score_right)'),
    #     ('Focus',
    #      '@focus_start_seqid:@focus_start{,} - @focus_end_seqid:@focus_end{,}'),
    # ])
    img_src = (
        '{}_static/data/signal/@statistic/@population/@chromosome/@rank/peak_location.png'
        .format(root_path)
    )
    hover = bmod.HoverTool(tooltips="""
        <div class='signal-summary'>
        <img src='{}'/>
        <table>
            <tr><th>Population: </th><td>@pop_label</td></tr>
            <tr><th>Statistic: </th><td>@statistic</td></tr>
            <tr><th>Score: </th><td>@score (@score_left | @score_right)</td></tr>
            <tr><th>Focus: </th><td>@focus_start_seqid:@focus_start{{,}} - 
            @focus_end_seqid:@focus_end{{,}}</td></tr>
        </table>
        </div>
    """.format(img_src))

    tools = 'tap,xpan,xzoom_in,xzoom_out,xwheel_zoom,reset'.split() + [hover]
    fig = bplt.figure(title=title,
                      plot_width=900, plot_height=90 + (10 * max(df.level)),
                      tools=tools, toolbar_location='above',
                      active_drag='xpan', active_scroll='xwheel_zoom')
    fig.quad(bottom='bottom', top='top', left='peak_start_coord',
             right='focus_start_coord', source=source, color=palette[0],
             alpha=.5, line_width=0)
    fig.quad(bottom='bottom', top='top', left='focus_start_coord',
             right='focus_end_coord', source=source, color=palette[3],
             alpha=.7, line_width=0)
    fig.quad(bottom='bottom', top='top', left='focus_end_coord',
             right='peak_end_coord', source=source, color=palette[0],
             alpha=.5, line_width=0)
    fig.x_range = bmod.Range1d(0, seq_len / 1e6, bounds=(1, seq_len / 1e6))
    fig.y_range = bmod.Range1d(-0.5, max(df.level) + 1.3)
    fig.yaxis.visible = False
    fig.ygrid.visible = False
    fig.xaxis.axis_label = (
        'Chromosome {}{} position (Mbp)'
        .format('arm ' if arm else '', seqid)
    )
    url = root_path + 'signal/@statistic/@population/@chromosome/@rank/'
    taptool = fig.select(type=bmod.TapTool)
    taptool.callback = bmod.OpenURL(url=url)
    return fig


def fig_signals(df_signals, df_genes, seqid, pop_labels, root_path='../'):
    layout = []
    empty = True
    for statistic in ['H12']:
        df = df_signals[df_signals.statistic == statistic]
        try:
            fig = plot_signals(df, seqid=seqid, pop_labels=pop_labels,
                               root_path=root_path,
                               title='Selection signals ({})'.format(statistic))
        except ValueError:
            pass
        else:
            x_range = fig.x_range
            fig.xaxis.visible = False
            layout.append([fig])
            empty = False
    if empty:
        raise ValueError('no signals')
    else:
        fig = plot_genes(df_genes, seqid, x_range=x_range)
        layout.append([fig])
        gfig = blay.gridplot(layout, toolbar_location='above')
        return gfig


def build_population_plots(df_signals, df_genes):

    # load populations definitions
    with open('docs/_static/data/populations.yml', mode='r') as f:
        populations = yaml.load(f)

    print('rendering population plots')
    for pop in populations:
        df_pop = df_signals[df_signals.population == pop]
        for seqid in seqids:
            plot_path = 'docs/population/{}.{}.signals.html'.format(pop, seqid)
            try:
                fig = fig_signals(df_pop, df_genes, seqid=seqid, pop_labels=populations,
                                  root_path='../')
            except ValueError:
                print('no signals, skipping', plot_path)
            else:
                script, div = bemb.components(fig)
                print('rendering', plot_path)
                with open(plot_path, mode='w') as f:
                    print('<div class="bokeh-figure peak-location">', file=f)
                    print(script, file=f)
                    print(div, file=f)
                    print('</div>', file=f)

    print('rendering seqid plots')
    for seqid in seqids:
        plot_path = 'docs/seqid/{}.signals.html'.format(seqid)
        try:
            fig = fig_signals(df_signals, df_genes, seqid=seqid, pop_labels=populations,
                              root_path='../')
        except ValueError:
            print('no signals, skipping', plot_path)
        else:
            script, div = bemb.components(fig)
            print('rendering', plot_path)
            with open(plot_path, mode='w') as f:
                print('<div class="bokeh-figure peak-location">', file=f)
                print(script, file=f)
                print(div, file=f)
                print('</div>', file=f)


def main():

    # setup signals
    df_signals = pd.read_csv('docs/_static/data/signals.csv')

    # setup genes
    df_features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    df_genes = df_features[df_features['type'] == 'gene']

    build_population_plots(df_signals, df_genes)


if __name__ == '__main__':
    main()