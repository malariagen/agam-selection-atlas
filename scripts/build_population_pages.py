# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
import yaml
from glob import glob
import os
import allel
import petl as etl


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

    for population in populations:

        pop_signals = list(
            tbl_signals
            .eq('population', population['id'])
            .dicts()
        )
        data = dict()
        data['population'] = population
        data['signals'] = {
            '2': [s for s in pop_signals if s['chromosome'] == '2'],
            '3': [s for s in pop_signals if s['chromosome'] == '3'],
            'X': [s for s in pop_signals if s['chromosome'] == 'X'],
        }

        # render the report
        out_path = 'docs/population/{}.rst'.format(population['id'])
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(population_template.render(**data), file=f)
