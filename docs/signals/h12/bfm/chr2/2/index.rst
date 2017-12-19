
Burkina Faso *An. coluzzii* | H12 | Chromosome 2 | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfm` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2L from
position 25,400,001 to 25,520,000.




The following 9 genes overlap the focal region: :doc:`/genes/AGAP006028` (Rdl - GABA-gated chloride channel subunit),  :doc:`/genes/AGAP006029`,  :doc:`/genes/AGAP006030` (mfrn - mitoferrin),  :doc:`/genes/AGAP006031` (nuclear pore complex protein Nup54),  :doc:`/genes/AGAP006032`,  :doc:`/genes/AGAP006033`,  :doc:`/genes/AGAP006034`,  :doc:`/genes/AGAP006035` (Ras-related protein Rab-36),  :doc:`/genes/AGAP006036` (axonemal dynein intermediate chain inner arm i1).




The following 6 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP006037` (RpL24 - 60S ribosomal protein L24),  :doc:`/genes/AGAP006038` (serine/arginine repetitive matrix protein 2),  :doc:`/genes/AGAP006039`,  :doc:`/genes/AGAP006040` (peroxisomal membrane protein 2),  :doc:`/genes/AGAP006041` (E3 ubiquitin-protein ligase RNF5),  :doc:`/genes/AGAP006042`.


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

    :doc:`/signals/h12/bfs/chr2/5/index`,"2L:25380001-25420000",405
    :doc:`/signals/h12/aom/chr2/3/index`,"2L:25380001-25460000",339
    

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
        # function evals   = 19
        # data points      = 151
        # variables        = 3
        chi-square         = 0.041
        reduced chi-square = 0.000
        Akaike info crit   = -1235.742
        Bayesian info crit = -1226.690
    [[Variables]]
        amplitude:   0.32833370 +/- 0.007646 (2.33%) (init= 0.5)
        decay:       0.66634867 +/- 0.026671 (4.00%) (init= 0.5)
        c:           0.01406966 +/- 0.001799 (12.79%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.566 
        C(decay, c)                  = -0.531 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 150
        # variables        = 3
        chi-square         = 0.013
        reduced chi-square = 0.000
        Akaike info crit   = -1396.621
        Bayesian info crit = -1387.589
    [[Variables]]
        amplitude:   0.38089684 +/- 0.008128 (2.13%) (init= 0.5)
        decay:       0.28760863 +/- 0.008545 (2.97%) (init= 0.5)
        c:           0.01709531 +/- 0.000855 (5.00%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.724 
        C(decay, c)                  = -0.326 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 150
        # variables        = 1
        chi-square         = 0.672
        reduced chi-square = 0.005
        Akaike info crit   = -809.246
        Bayesian info crit = -806.235
    [[Variables]]
        c:   0.04916964 +/- 0.005482 (11.15%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 149
        # variables        = 1
        chi-square         = 0.341
        reduced chi-square = 0.002
        Akaike info crit   = -903.795
        Bayesian info crit = -900.791
    [[Variables]]
        c:   0.03221222 +/- 0.003933 (12.21%) (init= 0.04)


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
