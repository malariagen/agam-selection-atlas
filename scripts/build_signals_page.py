# -*- coding: utf-8 -*-
from setup import *


if __name__ == '__main__':

    loader = jinja2.FileSystemLoader('templates')

    env = jinja2.Environment(loader=loader)

    template = env.get_template('signals.rst')

    data = dict()
    data['signals'] = list(etl.fromcsv('docs/_static/data/signals.csv').dicts())

    # render the report
    out_path = 'docs/signals.rst'
    print('rendering', out_path)
    with open(out_path, mode='w') as f:
        print(template.render(**data), file=f)
