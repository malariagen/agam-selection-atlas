
Guinea-Bissau | H12 | Chromosome 2 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/gwa` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2R from
position 47,760,001 to 47,820,000.




The following 6 genes overlap the focal region: :doc:`/genes/AGAP004000` (myosin IX),  :doc:`/genes/AGAP004002` (60 kDa heat shock protein, mitochondrial precursor),  :doc:`/genes/AGAP013015` (p53 and DNA damage-regulated protein),  :doc:`/genes/AGAP004003`,  :doc:`/genes/AGAP004004`,  :doc:`/genes/AGAP004005`.




The following 6 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP003997` (casein kinase 1, gamma),  :doc:`/genes/AGAP003999`,  :doc:`/genes/AGAP013019`,  :doc:`/genes/AGAP004006`,  :doc:`/genes/AGAP004007`,  :doc:`/genes/AGAP004008`.


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
        # function evals   = 23
        # data points      = 140
        # variables        = 3
        chi-square         = 0.043
        reduced chi-square = 0.000
        Akaike info crit   = -1125.133
        Bayesian info crit = -1116.309
    [[Variables]]
        amplitude:   0.23835259 +/- 0.013331 (5.59%) (init= 0.5)
        decay:       0.19467749 +/- 0.017670 (9.08%) (init= 0.5)
        c:           0.05057228 +/- 0.001621 (3.21%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.596 
        C(decay, c)                  = -0.274 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 144
        # variables        = 3
        chi-square         = 0.078
        reduced chi-square = 0.001
        Akaike info crit   = -1076.158
        Bayesian info crit = -1067.249
    [[Variables]]
        amplitude:   0.19138704 +/- 0.016433 (8.59%) (init= 0.5)
        decay:       0.40480895 +/- 0.051706 (12.77%) (init= 0.5)
        c:           0.05836366 +/- 0.002309 (3.96%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.681 
        C(decay, c)                  = -0.405 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 10
        # data points      = 139
        # variables        = 1
        chi-square         = 0.155
        reduced chi-square = 0.001
        Akaike info crit   = -942.637
        Bayesian info crit = -939.703
    [[Variables]]
        c:   0.05822204 +/- 0.002846 (4.89%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 143
        # variables        = 1
        chi-square         = 0.182
        reduced chi-square = 0.001
        Akaike info crit   = -951.485
        Bayesian info crit = -948.522
    [[Variables]]
        c:   0.06931702 +/- 0.002992 (4.32%) (init= 0.04)


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
