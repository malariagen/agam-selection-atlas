:orphan:

Burkina Faso *An. gambiae* | H12 | Chromosome 2 | Signal #10
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
2R between position 27,480,001 and
27,520,000.


No genes overlap the focal region.





Gene :doc:`/gene/AGAP002793` (slit homolog 1 protein precursor) is within 50 kbp of the focal region.



.. figure:: peak_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Overlapping signals
-------------------


No overlapping signals.


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
        # function evals   = 39
        # data points      = 201
        # variables        = 3
        chi-square         = 0.005
        reduced chi-square = 0.000
        Akaike info crit   = -2108.881
        Bayesian info crit = -2098.971
    [[Variables]]
        amplitude:   0.02033807 +/- 0.002326 (11.44%) (init= 0.5)
        decay:       0.72568643 +/- 0.136641 (18.83%) (init= 0.5)
        c:           0.01038774 +/- 0.000462 (4.44%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.597 
        C(decay, c)                  = -0.469 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 199
        # variables        = 3
        chi-square         = 0.019
        reduced chi-square = 0.000
        Akaike info crit   = -1839.214
        Bayesian info crit = -1829.334
    [[Variables]]
        amplitude:   0.08382861 +/- 0.013494 (16.10%) (init= 0.5)
        decay:       0.15000000 +/- 0.013249 (8.83%) (init= 0.5)
        c:           0.01568207 +/- 0.000720 (4.59%) (init= 0.03)
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
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -2039.954
        Bayesian info crit = -2036.656
    [[Variables]]
        c:   0.01209457 +/- 0.000430 (3.56%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.024
        reduced chi-square = 0.000
        Akaike info crit   = -1780.788
        Bayesian info crit = -1777.499
    [[Variables]]
        c:   0.01674350 +/- 0.000789 (4.72%) (init= 0.03)


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
