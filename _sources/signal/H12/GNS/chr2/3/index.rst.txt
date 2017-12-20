:orphan:

Guinea *An. gambiae* | H12 | Chromosome 2 | Signal #3
================================================================================



This page describes a signal of selection found in the
:doc:`/population/GNS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **28,740,001** and
**28,840,000**.




The following 9 genes overlap the focal region: :doc:`/gene/AGAP006260` (Z band alternatively spliced PDZ-motif protein 66),  :doc:`/gene/AGAP006261` (CPR135 - cuticular protein RR-2 family 135),  :doc:`/gene/AGAP006262`,  :doc:`/gene/AGAP006263` (ARR2 - arrestin Arr2-like),  :doc:`/gene/AGAP006264` (Peroxisomal targeting signal 2 receptor),  :doc:`/gene/AGAP006265`,  :doc:`/gene/AGAP006266` (HIV Tat-specific factor 1),  :doc:`/gene/AGAP006267` (CTL6 - C-type lectin (CTL)),  :doc:`/gene/AGAP006268`.




The following 2 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP006258` (PPO2 - prophenoloxidase 2),  :doc:`/gene/AGAP006259`.


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
        # function evals   = 1512
        # data points      = 201
        # variables        = 3
        chi-square         = 0.791
        reduced chi-square = 0.004
        Akaike info crit   = -1107.013
        Bayesian info crit = -1097.104
    [[Variables]]
        amplitude:   0.18223429 +/- 0.018449 (10.12%) (init= 0.5)
        decay:       2.99604893 +/- 0.957667 (31.96%) (init= 0.5)
        c:           0.05999999 +/- 0.035856 (59.76%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.926 
        C(amplitude, c)              =  0.597 
        C(amplitude, decay)          =  0.335 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 193
        # variables        = 3
        chi-square         = 0.076
        reduced chi-square = 0.000
        Akaike info crit   = -1506.904
        Bayesian info crit = -1497.116
    [[Variables]]
        amplitude:   0.28110957 +/- 0.013619 (4.84%) (init= 0.5)
        decay:       0.42053900 +/- 0.029240 (6.95%) (init= 0.5)
        c:           0.03620272 +/- 0.001624 (4.49%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.702 
        C(decay, c)                  = -0.344 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.961
        reduced chi-square = 0.005
        Akaike info crit   = -1065.633
        Bayesian info crit = -1062.335
    [[Variables]]
        c:   0.13081946 +/- 0.004913 (3.76%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 192
        # variables        = 1
        chi-square         = 0.374
        reduced chi-square = 0.002
        Akaike info crit   = -1196.027
        Bayesian info crit = -1192.769
    [[Variables]]
        c:   0.04976641 +/- 0.003195 (6.42%) (init= 0.03)


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
