:orphan:

Angola *An. coluzzii* | H12 | Chromosome X | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/AOM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X between position 14,660,001 and
14,720,000**.



Gene :doc:`/gene/AGAP000801` (GLURIIb - ionotropic receptor GLURIIb) overlaps the focal region.





The following 4 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP000798` (GLURIIc - ionotropic receptor GLURIIc),  :doc:`/gene/AGAP000803` (GLURIIa - ionotropic receptor GLURIIa),  :doc:`/gene/AGAP000804` (GPXH2 - glutathione peroxidase 2),  :doc:`/gene/AGAP000805` (BTB/POZ domain-containing protein KCTD16).


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
        # data points      = 200
        # variables        = 3
        chi-square         = 0.017
        reduced chi-square = 0.000
        Akaike info crit   = -1866.759
        Bayesian info crit = -1856.864
    [[Variables]]
        amplitude:   0.05884861 +/- 0.003577 (6.08%) (init= 0.5)
        decay:       1.00738723 +/- 0.108062 (10.73%) (init= 0.5)
        c:           0.02546942 +/- 0.000934 (3.67%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.576 
        C(amplitude, decay)          = -0.553 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 191
        # variables        = 3
        chi-square         = 0.084
        reduced chi-square = 0.000
        Akaike info crit   = -1469.975
        Bayesian info crit = -1460.218
    [[Variables]]
        amplitude:   0.07606479 +/- 0.010894 (14.32%) (init= 0.5)
        decay:       0.68355152 +/- 0.159877 (23.39%) (init= 0.5)
        c:           0.05089292 +/- 0.001875 (3.68%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.627 
        C(decay, c)                  = -0.464 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 199
        # variables        = 1
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1661.964
        Bayesian info crit = -1658.671
    [[Variables]]
        c:   0.03268495 +/- 0.001086 (3.32%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 190
        # variables        = 1
        chi-square         = 0.111
        reduced chi-square = 0.001
        Akaike info crit   = -1411.949
        Bayesian info crit = -1408.702
    [[Variables]]
        c:   0.05619005 +/- 0.001761 (3.13%) (init= 0.03)


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
