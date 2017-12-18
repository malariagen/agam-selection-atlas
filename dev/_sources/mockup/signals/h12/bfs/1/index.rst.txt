
Burkina Faso *An. gambiae* H12 #1
=================================

This page describes a signal of selection found in the
:doc:`/mockup/populations/bfs` population using the :doc:`/mockup/methods/h12`
statistic.

The inferred focus of this signal is on chromosome arm 2L from position
2,420,000 to 2,460,000. The following 3 genes overlap the focal region:
:doc:`/mockup/genes/AGAP001234`, :doc:`/mockup/genes/AGAP001234`,
:doc:`/mockup/genes/AGAP001234`. The following 5 genes
are in windows immediately adjacent to the focal region:
:doc:`/mockup/genes/AGAP001234`, :doc:`/mockup/genes/AGAP001234`,
:doc:`/mockup/genes/AGAP001234`, :doc:`/mockup/genes/AGAP001234`,
:doc:`/mockup/genes/AGAP001234`.

.. figure:: signal_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Related signals
---------------

Overlapping signals
~~~~~~~~~~~~~~~~~~~

The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Adjacent signals
~~~~~~~~~~~~~~~~

The following selection signals have an inferred focus that is immediately
adjacent to the focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Nearby signals
~~~~~~~~~~~~~~

The following signals affect a genome region that overlaps with the genome region
affected by this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/mockup/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Fit report
----------

The information below provides some diagnostics from the
:doc:`/mockup/methods/peak_modelling` procedure.

.. figure:: signal_fit.png

    **Figure 2**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Left flank, peak model
~~~~~~~~~~~~~~~~~~~~~~

::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 150
        # variables        = 3
        chi-square         = 0.038
        reduced chi-square = 0.000
        Akaike info crit   = -1235.725
        Bayesian info crit = -1226.693
    [[Variables]]
        amplitude:   0.39058926 +/- 0.010529 (2.70%) (init= 0.5)
        decay:       0.28708964 +/- 0.012383 (4.31%) (init= 0.2)
        c:           0.01937928 +/- 0.001462 (7.54%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.609
        C(decay, c)                  = -0.326

Right flank, peak model
~~~~~~~~~~~~~~~~~~~~~~~

::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 149
        # variables        = 3
        chi-square         = 0.027
        reduced chi-square = 0.000
        Akaike info crit   = -1275.307
        Bayesian info crit = -1266.295
    [[Variables]]
        amplitude:   0.30093218 +/- 0.010142 (3.37%) (init= 0.5)
        decay:       0.36692247 +/- 0.017836 (4.86%) (init= 0.2)
        c:           0.02440119 +/- 0.001293 (5.30%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.702
        C(decay, c)                  = -0.375

Left flank, null model
~~~~~~~~~~~~~~~~~~~~~~

::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 149
        # variables        = 1
        chi-square         = 0.455
        reduced chi-square = 0.003
        Akaike info crit   = -860.847
        Bayesian info crit = -857.843
    [[Variables]]
        c:   0.03680943 +/- 0.004543 (12.34%) (init= 0.04)

Right flank, null model
~~~~~~~~~~~~~~~~~~~~~~~

::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.272
        reduced chi-square = 0.002
        Akaike info crit   = -930.360
        Bayesian info crit = -927.363
    [[Variables]]
        c:   0.04001378 +/- 0.003534 (8.83%) (init= 0.04)
