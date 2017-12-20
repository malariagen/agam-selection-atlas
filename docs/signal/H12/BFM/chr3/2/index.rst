:orphan:

Burkina Faso *An. coluzzii* | H12 | Chromosome 3 | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3L between position 11,200,001 and
11,240,000**.




The following 2 genes overlap the focal region: :doc:`/gene/AGAP010815` (TEP1 - thioester-containing protein 1),  :doc:`/gene/AGAP010816` (TEP3 - thioester-containing protein 3).




The following 4 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP010813` (TEP18 - thioester-containing protein 18),  :doc:`/gene/AGAP010814` (TEP6 - thioester-containing protein 6),  :doc:`/gene/AGAP010817`,  :doc:`/gene/AGAP010818` (TEP11 - thioester-containing protein 11).


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
        # function evals   = 45
        # data points      = 192
        # variables        = 3
        chi-square         = 0.135
        reduced chi-square = 0.001
        Akaike info crit   = -1387.592
        Bayesian info crit = -1377.820
    [[Variables]]
        amplitude:   0.80003949 +/- 0.021678 (2.71%) (init= 0.5)
        decay:       0.15000000 +/- 0.019310 (12.87%) (init= 0.5)
        c:           0.02821290 +/- 0.002011 (7.13%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.587 
        C(decay, c)                  =  0.202 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 197
        # variables        = 3
        chi-square         = 1.385
        reduced chi-square = 0.007
        Akaike info crit   = -970.670
        Bayesian info crit = -960.821
    [[Variables]]
        amplitude:   0.34589027 +/- 0.037652 (10.89%) (init= 0.5)
        decay:       0.88502710 +/- 0.158717 (17.93%) (init= 0.5)
        c:           0.01191628 +/- 0.008037 (67.45%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.610 
        C(decay, c)                  = -0.535 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 191
        # variables        = 1
        chi-square         = 1.077
        reduced chi-square = 0.006
        Akaike info crit   = -986.939
        Bayesian info crit = -983.687
    [[Variables]]
        c:   0.04215808 +/- 0.005448 (12.92%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 1.838
        reduced chi-square = 0.009
        Akaike info crit   = -913.172
        Bayesian info crit = -909.894
    [[Variables]]
        c:   0.04477600 +/- 0.006935 (15.49%) (init= 0.03)


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
