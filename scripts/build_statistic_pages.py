# -*- coding: utf-8 -*-
from setup import *


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    # make the per-seqid pages
    page_template = env.get_template('statistic.rst')

    # load signals
    tbl_signals = etl.fromcsv('docs/_static/data/signals.csv')

    for statistic in ['H12', 'IHS', 'XPEHH']:

        seq_signals = list(
            tbl_signals
            .eq('statistic', statistic)
            .dicts()
        )
        data = dict()
        data['statistic'] = statistic
        data['signals'] = seq_signals

        # render the report
        out_path = 'docs/statistic/{}.rst'.format(statistic)
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(page_template.render(**data), file=f)
