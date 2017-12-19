# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
import jinja2
import yaml
from glob import glob
import os


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    template = env.get_template('signal_report.rst')

    for path in sorted(glob('docs/signals/*/*/*/*/signal_report.yml')):

        with open(path, mode='rb') as f:
            signal_report = yaml.load(f)

        out_path = os.path.join(os.path.dirname(path), 'index.rst')
        print('rendering', out_path)
        with open(out_path, mode='w') as f:
            print(template.render(**signal_report), file=f)
