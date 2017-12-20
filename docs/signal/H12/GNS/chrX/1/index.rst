:orphan:

Guinea *An. gambiae* | H12 | Chromosome X | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/GNS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X between position 15,100,001 and
15,220,000**.



Gene :doc:`/gene/AGAP012997` overlaps the focal region.





The following 4 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP013173`,  :doc:`/gene/AGAP013424`,  :doc:`/gene/AGAP000818` (CYP9K1 - cytochrome P450),  :doc:`/gene/AGAP000819` (nuclear receptor subfamily 2 group E member (Tailless)).


.. figure:: peak_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`/signal/H12/BFM/chrX/1/index`,":15100001-15380000",1272
    :doc:`/signal/H12/BFS/chrX/1/index`,":15120001-15260000",1073
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. figure:: peak_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: peak_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: peak_fit.png

    **Figure 4**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 195
        # variables        = 3
        chi-square         = 0.036
        reduced chi-square = 0.000
        Akaike info crit   = -1668.583
        Bayesian info crit = -1658.764
    [[Variables]]
        amplitude:   0.26724281 +/- 0.007476 (2.80%) (init= 0.5)
        decay:       0.62566433 +/- 0.025020 (4.00%) (init= 0.5)
        c:           0.02652541 +/- 0.001174 (4.43%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.584 
        C(decay, c)                  = -0.427 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 196
        # variables        = 3
        chi-square         = 0.196
        reduced chi-square = 0.001
        Akaike info crit   = -1347.923
        Bayesian info crit = -1338.089
    [[Variables]]
        amplitude:   0.23332141 +/- 0.019341 (8.29%) (init= 0.5)
        decay:       0.55726151 +/- 0.066225 (11.88%) (init= 0.5)
        c:           0.05999999 +/- 0.003920 (6.53%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.683 
        C(decay, c)                  =  0.404 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 194
        # variables        = 1
        chi-square         = 0.356
        reduced chi-square = 0.002
        Akaike info crit   = -1220.526
        Bayesian info crit = -1217.258
    [[Variables]]
        c:   0.04284089 +/- 0.003081 (7.19%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 195
        # variables        = 1
        chi-square         = 0.409
        reduced chi-square = 0.002
        Akaike info crit   = -1200.544
        Bayesian info crit = -1197.271
    [[Variables]]
        c:   0.07944182 +/- 0.003288 (4.14%) (init= 0.03)


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
