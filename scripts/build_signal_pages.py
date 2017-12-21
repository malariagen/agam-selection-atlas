# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
import yaml
from glob import glob
import os
import allel
import pandas as pd
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


def plot_signal_location(report, plot_width=900, plot_height=200):
    fig = bplt.figure(title='Signal location', plot_width=plot_width,
                      plot_height=plot_height,
                      tools='xpan,xzoom_in,xzoom_out,xwheel_zoom,reset',
                      toolbar_location='above', active_drag='xpan',
                      active_scroll='xwheel_zoom')
    x = np.array(report['fit_data']['xx_ppos']) / 1e6
    y_data = np.array(report['fit_data']['yy_signal'])
    y_fit = np.array(report['fit_data']['yy_best_fit'])
    peak_span = bmod.BoxAnnotation(left=report['peak_start']/1e6,
                                   right=report['peak_stop']/1e6,
                                   level='underlay',
                                   fill_color='blue', fill_alpha=.1)
    focus_span = bmod.BoxAnnotation(left=report['focus_start']/1e6,
                                    right=report['focus_stop']/1e6,
                                    level='underlay',
                                    fill_color='red', fill_alpha=.3)
    epicenter_span = bmod.BoxAnnotation(left=report['epicenter_start']/1e6,
                                        right=report['epicenter_stop']/1e6,
                                        level='underlay', fill_color='red',
                                        fill_alpha=.3)
    fig.add_layout(peak_span)
    fig.add_layout(focus_span)
    fig.add_layout(epicenter_span)
    fig.line(x, y_fit, line_color='black', line_dash='dashed')
    fig.circle(x, y_data, alpha=1)
    # bound the range to prevent zooming out too far
    fig.x_range = bmod.Range1d(x[0], x[-1], bounds=(x[0], x[-1]))
    fig.xaxis.axis_label = \
        'Chromosome {} position (Mbp)'.format(report['chromosome'])
    fig.yaxis.axis_label = 'Selection statistic'
    return fig


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
        url = '../../../../../gene/@id'
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


def fig_signal_location(report, genes):
    fig1 = plot_signal_location(report)
    chrom = report['chromosome']
    start = report['fit_data']['xx_ppos'][0]
    stop = report['fit_data']['xx_ppos'][-1]
    fig1.xaxis.visible = False
    fig2 = plot_genes(genes, chrom, start, stop, x_range=fig1.x_range)
    gfig = blay.gridplot([[fig1], [fig2]], toolbar_location='right')
    return gfig


def build_signal_outputs(path, template, genes, signals):

    # load the basic signal report
    with open(path, mode='rb') as f:
        report = yaml.load(f)

    # figure out what chromosome arm
    epicenter = report['epicenter']
    # check epicenter does not span centromere - not sure how to handle that
    # case
    assert epicenter['start'][0] == epicenter['stop'][0]
    epicenter_arm = epicenter['start'][0]

    # obtain focus
    focus = report['focus']
    focus_start_arm = focus['start'][0]
    focus_stop_arm = focus['stop'][0]
    focus_start = focus['start'][1]
    focus_stop = focus['stop'][1]

    # crude way to deal with rare case where focus spans centromere
    if focus_start_arm != epicenter_arm:
        focus_start = 1
    if focus_stop_arm != epicenter_arm:
        focus_stop = len(genome[epicenter_arm])

    # augment report with gene information
    overlapping_genes = genes[(
        (genes.seqid == epicenter_arm) &
        (genes.start <= focus_stop) &
        (genes.end >= focus_start)
    )]
    report['overlapping_genes'] = [
        {'id': gene.ID,
         'name': gene.Name,
         'description': gene.description.split('[Source:')[0].strip()}
        for _, gene in overlapping_genes.iterrows()
    ]

    adjacent_genes = genes[(
            (genes.seqid == epicenter_arm) &
            ((genes.end < focus_start) | (genes.start > focus_stop)) &
            (genes.start <= (focus_stop + 50000)) &
            (genes.end >= (focus_start - 50000))

    )]
    report['adjacent_genes'] = [
        {'id': gene.ID,
         'name': gene.Name,
         'description': gene.description.split('[Source:')[0].strip()}
        for _, gene in adjacent_genes.iterrows()
    ]

    # augment report with related signals information
    # TODO this doesn't properly handle overlapping signals spanning a
    # centromere
    overlapping_signals = signals[(
            (signals.epicenter_arm == epicenter_arm) &
            (signals.focus_start <= focus_stop) &
            (signals.focus_stop >= focus_start) &
            # don't include self
            ((signals.population != report['population']['id']) |
             (signals.statistic != report['statistic']['id']))
    )]
    report['overlapping_signals'] = overlapping_signals.to_dict(
        orient='records')

    # render the report
    out_dir = os.path.join(
        'docs',
        os.path.dirname(path)[len('docs/_static/data/'):]
    )
    os.makedirs(out_dir, exist_ok=True)
    page_path = os.path.join(out_dir, 'index.rst')
    print('rendering', page_path)
    with open(page_path, mode='w') as f:
        print(template.render(**report), file=f)

    # render a bokeh signal plot
    fig = fig_signal_location(report, genes)
    script, div = bemb.components(fig)
    plot_path = os.path.join(out_dir, 'peak_location.html')
    print('rendering', plot_path)
    with open(plot_path, mode='w') as f:
        print('<div class="bokeh-figure peak-location">', file=f)
        print(script, file=f)
        print(div, file=f)
        print('</div>', file=f)


def main():

    # setup jinja
    loader = jinja2.FileSystemLoader('templates')
    env = jinja2.Environment(loader=loader)
    template = env.get_template('signal.rst')

    # setup genes
    features = allel.gff3_to_dataframe(
        'vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz',
        attributes=['ID', 'Name', 'description'], attributes_fill='',
    )
    genes = features[features['type'] == 'gene']

    # setup signals
    signals = pd.read_csv('docs/_static/data/signals.csv')

    # iterate over signal reports
    for path in sorted(glob('docs/_static/data/signal/*/*/*/*/report.yml')):
        build_signal_outputs(path, template, genes, signals)


if __name__ == '__main__':
    main()

