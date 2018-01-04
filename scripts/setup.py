# -*- coding: utf-8 -*-
import sys
import os
from glob import glob
import numpy as np
import lmfit
import shutil
import jinja2
import yaml
import pandas as pd
import petl as etl
import allel
import bokeh.plotting as bplt
import bokeh.models as bmod
import bokeh.layouts as blay
import bokeh.embed as bemb
import matplotlib as mpl
import seaborn as sns
# print(os.path.abspath(__file__))
scripts_dir = os.path.dirname(__file__)
repo_dir = os.path.dirname(scripts_dir)
sys.path.insert(0, os.path.join(repo_dir, 'agam-report-base', 'src', 'python'))
import rockies
from ag1k import phase1_selection, phase1_ar3, phase1_ar31


# setup data sources
ag1k_dir = os.path.join(repo_dir, 'ngs.sanger.ac.uk', 'production', 'ag1000g', 'phase1')
phase1_ar3.init(os.path.join(ag1k_dir, 'AR3'))
phase1_ar31.init(os.path.join(ag1k_dir, 'AR3.1'))
phase1_selection.init(os.path.join(ag1k_dir, 'selection.1.RC2'))
genome = phase1_ar3.genome
seqids = '2R', '2L', '3R', '3L', 'X'


# setup styles
sns.set_context('paper', font_scale=0.9)
sns.set_style('darkgrid')


# load populations definitions
populations_file = os.path.join(repo_dir, 'docs', '_static', 'data', 'populations.yml')
with open(populations_file, mode='r') as f:
    populations = yaml.load(f)


def split_arms(chromosome, coord):
    assert chromosome is not None
    assert coord is not None
    if chromosome in '23':
        if coord > len(genome['{}R'.format(chromosome)]):
            seqid = '{}L'.format(chromosome)
            coord = coord - len(genome['{}R'.format(chromosome)])
        else:
            seqid = '{}R'.format(chromosome)
    else:
        seqid = chromosome
    return [seqid, coord]


# crude recombination rate lookup, keyed off chromatin state
# use units of cM / bp, assume 2 cM / Mbp == 2x10^-6 cM / bp
tbl_rr = (
    phase1_ar3.tbl_chromatin
    .rename('stop', 'end')  # go with GFF3 naming
    # extend heterochromatin on 2L
    .update('end', 2840000, where=lambda r: r.name == 'CH2L')
    .update('start', 2840001, where=lambda r: r.name == 'PEU2L')
    .addfield('rr', lambda r: .5e-6 if 'H' in r.name else 2e-6)
)
# per-base map of recombination rates
recmap = {chrom: np.full(len(genome[chrom]), fill_value=2e-6)
          for chrom in seqids}
for row in tbl_rr.records():
    recmap[row.chrom][row.start-1:row.end] = row.rr
