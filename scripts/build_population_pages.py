# -*- coding: utf-8 -*-
from setup import *


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    # load populations definitions
    with open('docs/_static/data/populations.yml', mode='r') as f:
        populations = yaml.load(f)

    # make the populations index page
    populations_template = env.get_template('populations.rst')
    data = dict(populations=populations)
    with open('docs/populations.rst', mode='w') as f:
        f.write(populations_template.render(populations=populations))

    # make the per-population pages
    population_template = env.get_template('population.rst')

    # load signals
    tbl_signals = etl.fromcsv('docs/_static/data/signals.csv')

    for pop_id, pop_label in populations.items():

        pop_signals = list(
            tbl_signals
            .eq('focal_population', pop_id)
            .dicts()
        )
        data = dict()
        data['population'] = {'id': pop_id, 'label': pop_label}
        data['signals'] = {
            '2R': [s for s in pop_signals if s['epicenter_seqid'] == '2R'],
            '2L': [s for s in pop_signals if s['epicenter_seqid'] == '2L'],
            '3R': [s for s in pop_signals if s['epicenter_seqid'] == '3R'],
            '3L': [s for s in pop_signals if s['epicenter_seqid'] == '3L'],
            'X': [s for s in pop_signals if s['epicenter_seqid'] == 'X'],
        }

        # render the report
        out_path = 'docs/population/{}.rst'.format(pop_id)
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(population_template.render(**data), file=f)
