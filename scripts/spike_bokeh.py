# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division
from bokeh.plotting import figure
from bokeh.embed import components
import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = 'example.html'

x = [1, 2, 3, 4, 5, 12, 2, 2, 3]
y = [6, 7, 6, 4, 5, 15, 23, 45, 4]

p = figure(title="example", plot_width=300, plot_height=300)
p.line(x, y, line_width=2)
p.circle(x, y, size=10, fill_color="white")

script, div = components(p)
with open(fn, mode='w') as f:
    print(script, file=f)
    print(div, file=f)

