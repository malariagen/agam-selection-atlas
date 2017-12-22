# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
import petl as etl
seqids = '2R', '2L', '3R', '3L', 'X'


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    # make the per-seqid pages
    seqid_template = env.get_template('seqid.rst')

    # load signals
    tbl_signals = etl.fromcsv('docs/_static/data/signals.csv')

    for seqid in seqids:

        seq_signals = list(
            tbl_signals
            .eq('epicenter_seqid', seqid)
            .dicts()
        )
        data = dict()
        data['seqid'] = seqid
        data['signals'] = seq_signals

        # render the report
        out_path = 'docs/seqid/{}.rst'.format(seqid)
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(seqid_template.render(**data), file=f)
