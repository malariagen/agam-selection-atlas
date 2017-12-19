
Burkina Faso *An. gambiae* | H12 | Chromosome 2 | Signal #3
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2R from
position 28,440,001 to 28,520,000.




The following 12 genes overlap the focal region: :doc:`/genes/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`/genes/AGAP002862` (CYP6AA1 - cytochrome P450),  :doc:`/genes/AGAP013128` (CYP6AA2 - cytochrome P450),  :doc:`/genes/AGAP002863` (COEAE6O - carboxylesterase alpha esterase),  :doc:`/genes/AGAP002864` (CYP6P15P - cytochrome P450),  :doc:`/genes/AGAP002865` (CYP6P3 - cytochrome P450),  :doc:`/genes/AGAP002866` (CYP6P5 - cytochrome P450),  :doc:`/genes/AGAP002867` (CYP6P4 - cytochrome P450),  :doc:`/genes/AGAP002868` (CYP6P1 - cytochrome P450),  :doc:`/genes/AGAP002869` (CYP6P2 - cytochrome P450),  :doc:`/genes/AGAP002870` (CYP6AD1 - cytochrome P450),  :doc:`/genes/AGAP013202`.




The following 5 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP000586`,  :doc:`/genes/AGAP002872` (lipase),  :doc:`/genes/AGAP002873`,  :doc:`/genes/AGAP013069`,  :doc:`/genes/AGAP002874`.


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
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`/signals/h12/ugs/chr2/1/index`,"2R:28420001-28520000",1230
    :doc:`/signals/h12/bfm/chr2/3/index`,"2R:28420001-28560000",557
    

Adjacent signals
~~~~~~~~~~~~~~~~

The following selection signals have an inferred focus that is immediately
adjacent to the focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Nearby signals
~~~~~~~~~~~~~~

The following signals affect a genome region that overlaps with the genome region
affected by this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/methods/peak_modelling` procedure.

.. figure:: signal_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: signal_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: signal_fit.png

    **Figure 4**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 151
        # variables        = 3
        chi-square         = 0.031
        reduced chi-square = 0.000
        Akaike info crit   = -1274.992
        Bayesian info crit = -1265.940
    [[Variables]]
        amplitude:   0.38063677 +/- 0.010058 (2.64%) (init= 0.5)
        decay:       0.24559229 +/- 0.010400 (4.23%) (init= 0.5)
        c:           0.02019624 +/- 0.001292 (6.40%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.607 
        C(decay, c)                  = -0.298 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 149
        # variables        = 3
        chi-square         = 0.028
        reduced chi-square = 0.000
        Akaike info crit   = -1273.906
        Bayesian info crit = -1264.894
    [[Variables]]
        amplitude:   0.34898931 +/- 0.010487 (3.01%) (init= 0.5)
        decay:       0.35025803 +/- 0.015079 (4.31%) (init= 0.5)
        c:           0.02480875 +/- 0.001290 (5.20%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.706 
        C(decay, c)                  = -0.365 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 150
        # variables        = 1
        chi-square         = 0.358
        reduced chi-square = 0.002
        Akaike info crit   = -903.690
        Bayesian info crit = -900.679
    [[Variables]]
        c:   0.03437788 +/- 0.004002 (11.64%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 8
        # data points      = 148
        # variables        = 1
        chi-square         = 0.353
        reduced chi-square = 0.002
        Akaike info crit   = -891.818
        Bayesian info crit = -888.821
    [[Variables]]
        c:   0.04210692 +/- 0.004026 (9.56%) (init= 0.04)


Comments
--------

.. raw:: html

    <div id="disqus_thread"></div>
    <script>
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://agam-selection-atlas.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
