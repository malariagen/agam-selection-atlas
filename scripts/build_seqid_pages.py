# -*- coding: utf-8 -*-
from setup import *


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    # make the per-seqid pages
    seqid_template = env.get_template('seqid.rst')

    # load signals
    tbl_signals = etl.fromcsv('docs/_static/data/signals.csv')

    os.makedirs('docs/seqid', exist_ok=True)

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
