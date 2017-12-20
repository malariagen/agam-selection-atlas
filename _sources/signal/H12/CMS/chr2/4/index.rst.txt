:orphan:

Cameroon *An. gambiae* | H12 | Chromosome 2 | Signal #4
================================================================================



This page describes a signal of selection found in the
:doc:`/population/CMS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
2L between position 3,660,001 and
3,700,000.


No genes overlap the focal region.






The following 9 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP004795` (RNA polymerase II elongation factor ELL),  :doc:`/gene/AGAP004797`,  :doc:`/gene/AGAP004798` (Coatomer protein complex, subunit beta 2),  :doc:`/gene/AGAP004799`,  :doc:`/gene/AGAP004800`,  :doc:`/gene/AGAP004801` (Huntingtin interacting protein),  :doc:`/gene/AGAP004802` (4-hydroxyphenylpyruvate dioxygenase),  :doc:`/gene/AGAP004803`,  :doc:`/gene/AGAP004804`.


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
        # function evals   = 75
        # data points      = 375
        # variables        = 3
        chi-square         = 0.208
        reduced chi-square = 0.001
        Akaike info crit   = -2804.967
        Bayesian info crit = -2793.187
    [[Variables]]
        amplitude:   0.13379278 +/- 0.016357 (12.23%) (init= 0.5)
        decay:       0.24616735 +/- 0.046925 (19.06%) (init= 0.5)
        c:           0.05945103 +/- 0.001266 (2.13%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.632 
        C(decay, c)                  = -0.192 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 214
        # variables        = 3
        chi-square         = 0.066
        reduced chi-square = 0.000
        Akaike info crit   = -1722.601
        Bayesian info crit = -1712.503
    [[Variables]]
        amplitude:   0.04766016 +/- 0.005254 (11.02%) (init= 0.5)
        decay:       2.99999971 +/- 1.008659 (33.62%) (init= 0.5)
        c:           0.03909342 +/- 0.005542 (14.18%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.924 
        C(amplitude, c)              = -0.560 
        C(amplitude, decay)          =  0.281 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 374
        # variables        = 1
        chi-square         = 0.253
        reduced chi-square = 0.001
        Akaike info crit   = -2728.118
        Bayesian info crit = -2724.194
    [[Variables]]
        c:   0.06147935 +/- 0.001345 (2.19%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 213
        # variables        = 1
        chi-square         = 0.089
        reduced chi-square = 0.000
        Akaike info crit   = -1655.858
        Bayesian info crit = -1652.497
    [[Variables]]
        c:   0.05516291 +/- 0.001401 (2.54%) (init= 0.03)


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
