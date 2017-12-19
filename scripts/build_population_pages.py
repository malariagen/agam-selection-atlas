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

    template = env.get_template('population.rst')

    # load populations definitions
    with open('docs/populations.yml', mode='r') as f:
        populations = yaml.load(f)

    # load signals
    tbl_signals = etl.fromcsv('docs/signals.csv')

    for population in populations:

        data = dict()
        data['population'] = population
        data['signals'] = list(
            tbl_signals
            .eq('population', population['id'])
            .dicts()
        )

        # render the report
        out_path = 'docs/populations/{}.rst'.format(population['id'])
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(template.render(**data), file=f)
