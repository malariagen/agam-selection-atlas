:orphan:

Burkina Faso *An. coluzzii* | H12 | Chromosome X | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X between position 9,200,001 and
9,240,000**.



Gene :doc:`/gene/AGAP000519` (diacylglycerol kinase (ATP dependent)) overlaps the focal region.




No genes are within 50 kbp of the focal region.




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

    :doc:`/signal/H12/BFS/chrX/2/index`,":9180001-9260000",504
    



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
        # function evals   = 43
        # data points      = 201
        # variables        = 3
        chi-square         = 0.032
        reduced chi-square = 0.000
        Akaike info crit   = -1749.539
        Bayesian info crit = -1739.629
    [[Variables]]
        amplitude:   0.10367694 +/- 0.010360 (9.99%) (init= 0.5)
        decay:       0.15000002 +/- 0.024549 (16.37%) (init= 0.5)
        c:           0.01850778 +/- 0.000938 (5.07%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.588 
        C(decay, c)                  = -0.197 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 44
        # data points      = 199
        # variables        = 3
        chi-square         = 0.027
        reduced chi-square = 0.000
        Akaike info crit   = -1768.249
        Bayesian info crit = -1758.369
    [[Variables]]
        amplitude:   0.17284754 +/- 0.016128 (9.33%) (init= 0.5)
        decay:       0.15000000 +/- 5.44e-06 (0.00%) (init= 0.5)
        c:           0.02278816 +/- 0.000861 (3.78%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.785 
        C(decay, c)                  =  0.199 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.042
        reduced chi-square = 0.000
        Akaike info crit   = -1690.521
        Bayesian info crit = -1687.223
    [[Variables]]
        c:   0.02009756 +/- 0.001030 (5.13%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1656.682
        Bayesian info crit = -1653.393
    [[Variables]]
        c:   0.02488382 +/- 0.001080 (4.34%) (init= 0.03)


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
