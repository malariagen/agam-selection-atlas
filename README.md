# Ag1000G selection atlas

This repository contains code for building the [Ag1000G selection atlas](https://malariagen.github.io/agam-selection-atlas/).

## Information for developers

Here's how to set up a local development environment to build the site.

### Cloning the repo

The site is deployed via GitHub pages. To get your local system set up in a way that 
is compatible with the live deployment of the site requires cloning the repo in a 
particular way.

Clone the GitHub repo for source code development:

```
$ git clone --recursive git@github.com:malariagen/agam-selection-atlas.git
```

Make a directory representing the "malariagen.github.io" site:

```
$ mkdir malariagen.github.io
$ cd malariagen.github.io
```

Clone the GitHub repo again for deployment of the built site (via the gh-pages branch):

```
$ git clone git@github.com:malariagen/agam-selection-atlas.git
$ cd agam-selection-atlas
$ git checkout gh-pages
```

Local directory structure should now look something like:

```
$ cd ../..
$ tree -L 2
.
├── agam-selection-atlas
│   ├── agam-report-base
│   ├── annotation
│   ├── build
│   ├── deps
│   ├── docs
│   ├── env.sh
│   ├── LICENSE
│   ├── notebooks
│   ├── README.md
│   ├── scripts
│   ├── snakemake
│   └── templates
└── malariagen.github.io
    └── agam-selection-atlas
```

So the repo has been cloned twice, into two different locations, one of which will be used 
for site development, the other for site deployment (checked out to gh-pages branch). 

### Setting up external data resources

To build the signals, some external data resources are needed in the agam-selection-atlas 
development directory.

Data from Ag1000G are required. Primarily this is the phase 1 selection release, although 
this is not public yet. I have the data setup as follows, assuming data from public data 
releases are copied locally in a similar way to the directory structure on the Oxford 
cluster:

```
$ cd agam-selection-atlas
$ ll ngs.sanger.ac.uk/production/ag1000g/phase1/*
lrwxrwxrwx 1 aliman aliman 40 Dec 15 12:47 ngs.sanger.ac.uk/production/ag1000g/phase1/AR3 -> /kwiat/vector/ag1000g/release/phase1.AR3/
lrwxrwxrwx 1 aliman aliman 42 Dec 15 12:47 ngs.sanger.ac.uk/production/ag1000g/phase1/AR3.1 -> /kwiat/vector/ag1000g/release/phase1.AR3.1/
lrwxrwxrwx 1 aliman aliman 52 Dec 15 12:48 ngs.sanger.ac.uk/production/ag1000g/phase1/selection.1.RC2 -> /kwiat/vector/ag1000g/release/phase1.selection.1.RC2/
```

The following files are also needed from VectorBase:

```
$ ll vectorbase.org/*
-rw-r--r-- 1 aliman aliman 2648817 Dec 18 23:07 vectorbase.org/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.8.gff3.gz
```

### Setting up the development environment

To set up a local development environment, do:

```
$ agam-report-base/install/install.sh
```

This should install conda and latex into the "deps" directory. To activate the environment
do:

```
$ source env.sh
```

### Building the signals

Building of the selection signals data is controlled via the ``snakemake/data.yml`` rules 
file. Building the signals data can take a bit of time, so only rebuild if necessary. 
E.g., to build all H12 signals:

```
$ snakemake -s snakemake/data.yml all_h12
```

### Building the site

Building of the static web site is controlled via the ``snakemake/site.yml`` rules file.
To completely rebuild the site, do:

```
$ snakemake -s snakemake/site.yml all
```

First time round this will take some time, as many pages (especially for genes) need to be
built, although any subsequent incremental builds will be faster, especially if they don't 
require rebuilding the gene pages.

### Previewing the site

The final step in the site build copies all built files across to the 
``malariagen.gitub.io/agam-selection-atlas`` folder where the gh-pages branch is checked 
out. To preview the site, do:

```
$ cd ../malariagen.github.io
$ python -m http.server
```

...then browse to [http://0.0.0.0:8000/agam-selection-atlas/dev/](http://0.0.0.0:8000/agam-selection-atlas/dev/).

Note that some changes make need an empty cache and hard reload in the browser.
