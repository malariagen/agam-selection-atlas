:orphan:

Angola *An. coluzzii* | H12 | Chromosome 3 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/AOM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3L** between positions **5,980,001** and
**6,040,000**.




The following 2 genes overlap the focal region: :doc:`/gene/AGAP010543` (Yellow-x),  :doc:`/gene/AGAP010544` (cell cycle arrest protein BUB3).




The following 3 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP010542`,  :doc:`/gene/AGAP010545`,  :doc:`/gene/AGAP028728` (CLIPE5 - CLIP-domain serine protease).


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
        # function evals   = 27
        # data points      = 270
        # variables        = 3
        chi-square         = 0.039
        reduced chi-square = 0.000
        Akaike info crit   = -2383.245
        Bayesian info crit = -2372.450
    [[Variables]]
        amplitude:   0.06179891 +/- 0.005499 (8.90%) (init= 0.5)
        decay:       0.65760624 +/- 0.091506 (13.92%) (init= 0.5)
        c:           0.03149532 +/- 0.000884 (2.81%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.606 
        C(decay, c)                  = -0.452 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 45
        # data points      = 191
        # variables        = 3
        chi-square         = 0.023
        reduced chi-square = 0.000
        Akaike info crit   = -1721.152
        Bayesian info crit = -1711.396
    [[Variables]]
        amplitude:   0.02195347 +/- 0.003312 (15.09%) (init= 0.5)
        decay:       3          +/- 8.02e-05 (0.00%) (init= 0.5)
        c:           0.03024521 +/- 0.003690 (12.20%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.931 
        C(amplitude, c)              = -0.602 
        C(amplitude, decay)          =  0.349 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 269
        # variables        = 1
        chi-square         = 0.064
        reduced chi-square = 0.000
        Akaike info crit   = -2244.185
        Bayesian info crit = -2240.590
    [[Variables]]
        c:   0.03535367 +/- 0.000939 (2.66%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 190
        # variables        = 1
        chi-square         = 0.028
        reduced chi-square = 0.000
        Akaike info crit   = -1677.399
        Bayesian info crit = -1674.152
    [[Variables]]
        c:   0.03780336 +/- 0.000876 (2.32%) (init= 0.03)


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
