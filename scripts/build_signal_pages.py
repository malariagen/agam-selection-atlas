# -*- coding: utf-8 -*-
from setup import *


def plot_signal_location(report, plot_width=900, plot_height=200):
    fig = bplt.figure(title='Signal location', plot_width=plot_width,
                      plot_height=plot_height,
                      tools='xpan,xzoom_in,xzoom_out,xwheel_zoom,reset',
                      toolbar_location='above', active_drag='xpan',
                      active_scroll='xwheel_zoom')
    x = np.array(report['pos']) / 1e6
    y_data = np.array(report['values'])
    y_fit = np.array(report['best_fit'])
    peak_span = bmod.BoxAnnotation(left=report['peak_start']/1e6,
                                   right=report['peak_end']/1e6,
                                   level='underlay',
                                   fill_color='blue', fill_alpha=.1)
    focus_span = bmod.BoxAnnotation(left=report['focus_start']/1e6,
                                    right=report['focus_end']/1e6,
                                    level='underlay',
                                    fill_color='red', fill_alpha=.3)
    epicenter_span = bmod.BoxAnnotation(left=(report['epicenter'] - 10000)/1e6,
                                        right=(report['epicenter'] + 10000)/1e6,
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
    fig.yaxis.axis_label = report['statistic']['id']
    return fig


def plot_genes(genes, chrom, start, end, fig=None, offset=0, x_range=None,
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
        url = '../../../../../gene/@id.html'
        taptool = fig.select(type=bmod.TapTool)
        taptool.callback = bmod.OpenURL(url=url)

    # handle joined chromosomes
    # TODO (thumps desk) there must be a better way!
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

    # from here assume single arm
    seqid = chrom
    df = genes[(genes.seqid == seqid) &
               (genes.end >= start) &
               (genes.start <= end)]
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
    start = report['pos'][0]
    end = report['pos'][-1]
    fig1.xaxis.visible = False
    fig2 = plot_genes(genes, chrom, start, end, x_range=fig1.x_range)
    gfig = blay.gridplot([[fig1], [fig2]], toolbar_location='above')
    return gfig


def build_signal_outputs(path, template, genes, signals, ir_candidates):

    # load the basic signal report
    with open(path, mode='rb') as plot_file:
        report = yaml.load(plot_file)

    # figure out what chromosome arm
    chromosome = report['chromosome']
    epicenter = report['epicenter']
    epicenter_seqid, epicenter_coord = split_arms(chromosome, epicenter)

    # obtain focus
    focus_start = report['focus_start']
    focus_start_seqid, focus_start_coord = split_arms(chromosome, focus_start)
    focus_end = report['focus_end']
    focus_end_seqid, focus_end_coord = split_arms(chromosome, focus_end)

    # crude way to deal with rare case where focus spans centromere
    # TODO handle whole chromosomes
    if focus_start_seqid != epicenter_seqid:
        focus_start_coord = 1
    if focus_end_seqid != epicenter_seqid:
        focus_end_coord = len(genome[epicenter_seqid])

    report['min_flank_delta_aic'] = min(report['delta_aic_left'], report['delta_aic_right'])

    # augment report with gene information
    overlapping_genes = genes[(
        (genes.seqid == epicenter_seqid) &
        (genes.start <= focus_end_coord) &
        (genes.end >= focus_start_coord)
    )]
    report['overlapping_genes'] = [
        {'id': gene.ID,
         'name': gene.Name,
         'description': gene.description.split('[Source:')[0].strip()}
        for _, gene in overlapping_genes.iterrows()
    ]

    adjacent_genes = genes[(
            (genes.seqid == epicenter_seqid) &
            ((genes.end < focus_start_coord) | (genes.start > focus_end_coord)) &
            (genes.start <= (focus_end_coord + 50000)) &
            (genes.end >= (focus_start_coord - 50000))

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
            (signals.epicenter_seqid == epicenter_seqid) &
            (signals.focus_start_coord <= focus_end_coord) &
            (signals.focus_end_coord >= focus_start_coord) &
            # don't include self
            ((signals.pop_key != report['pop_key']) |
             (signals.statistic != report['statistic']['id']))
    )]
    report['overlapping_signals'] = overlapping_signals.to_dict(orient='records')

    report['ir_candidates'] = ir_candidates

    # render the report
    out_dir = os.path.join(
        'docs',
        os.path.dirname(path)[len('docs/_static/data/'):]
    )
    os.makedirs(out_dir, exist_ok=True)
    page_path = os.path.join(out_dir, 'index.rst')
    print('rendering', page_path)
    with open(page_path, mode='w') as page_file:
        print(template.render(**report), file=page_file)

    # render a bokeh signal plot
    fig = fig_signal_location(report, genes)
    script, div = bemb.components(fig)
    plot_path = os.path.join(out_dir, 'peak_location.html')
    print('rendering', plot_path)
    with open(plot_path, mode='w') as plot_file:
        print('<div class="bokeh-figure peak-location">', file=plot_file)
        print(script, file=plot_file)
        print(div, file=plot_file)
        print('</div>', file=plot_file)


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

    # setup IR candidates
    ir_candidates = {
        slug: (
            etl
            .fromtsv('docs/_static/data/ir-candidate-genes/{}.csv'.format(slug))
            .values(0).set()
        )
        for slug in ['metabolic', 'target_site', 'behavioural', 'cuticular']
    }

    # iterate over signal reports
    for path in sorted(glob('docs/_static/data/signal/*/*/*/*/report.yml')):
        build_signal_outputs(path, template, genes, signals, ir_candidates)


if __name__ == '__main__':
    main()

