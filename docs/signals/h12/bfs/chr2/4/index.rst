
Burkina Faso *An. gambiae* | H12 | Chromosome 2 | Signal #4
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2R from
position 3,400,001 to 3,480,000.




The following 6 genes overlap the focal region: :doc:`/genes/AGAP001350`,  :doc:`/genes/AGAP001351`,  :doc:`/genes/AGAP001352`,  :doc:`/genes/AGAP001353`,  :doc:`/genes/AGAP001354`,  :doc:`/genes/AGAP001355`.




The following 9 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP001344`,  :doc:`/genes/AGAP001345` (hexamerin),  :doc:`/genes/AGAP001346`,  :doc:`/genes/AGAP001347`,  :doc:`/genes/AGAP001348`,  :doc:`/genes/AGAP001349` (chronic lymphocytic leukemia deletion region gene 6 protein-like protein),  :doc:`/genes/AGAP001356` (ACE1 - Acetylcholinesterase),  :doc:`/genes/AGAP001357` (beta-catenin-like protein 1),  :doc:`/genes/AGAP001358`.


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
        # function evals   = 27
        # data points      = 148
        # variables        = 3
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -1590.501
        Bayesian info crit = -1581.510
    [[Variables]]
        amplitude:   0.05691908 +/- 0.002520 (4.43%) (init= 0.5)
        decay:       0.44727876 +/- 0.033086 (7.40%) (init= 0.5)
        c:           0.01265460 +/- 0.000449 (3.55%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.579 
        C(decay, c)                  = -0.422 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 83
        # data points      = 150
        # variables        = 3
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1571.773
        Bayesian info crit = -1562.741
    [[Variables]]
        amplitude:   0.03350768 +/- 0.002187 (6.53%) (init= 0.5)
        decay:       1.00065195 +/- 0.124227 (12.41%) (init= 0.5)
        c:           0.01081280 +/- 0.000719 (6.66%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.684 
        C(amplitude, decay)          = -0.531 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 147
        # variables        = 1
        chi-square         = 0.015
        reduced chi-square = 0.000
        Akaike info crit   = -1346.308
        Bayesian info crit = -1343.317
    [[Variables]]
        c:   0.01642202 +/- 0.000844 (5.14%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 149
        # variables        = 1
        chi-square         = 0.012
        reduced chi-square = 0.000
        Akaike info crit   = -1402.859
        Bayesian info crit = -1399.855
    [[Variables]]
        c:   0.01605582 +/- 0.000737 (4.59%) (init= 0.04)


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
