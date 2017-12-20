:orphan:

Uganda *An. gambiae* | H12 | Chromosome 3 | Signal #4
================================================================================



This page describes a signal of selection found in the
:doc:`/population/UGS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **18,920,001** and
**18,980,000**.



Gene :doc:`/gene/AGAP008826` overlaps the focal region.




Gene :doc:`/gene/AGAP008825` is within 50 kbp of the focal region.



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
        # data points      = 189
        # variables        = 3
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -2106.554
        Bayesian info crit = -2096.828
    [[Variables]]
        amplitude:   0.01980271 +/- 0.003101 (15.66%) (init= 0.5)
        decay:       0.80982667 +/- 0.136257 (16.83%) (init= 0.5)
        c:           0.00807259 +/- 0.000348 (4.31%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.733 
        C(decay, c)                  = -0.482 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 199
        # variables        = 3
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -2246.553
        Bayesian info crit = -2236.673
    [[Variables]]
        amplitude:   0.03651451 +/- 0.003495 (9.57%) (init= 0.5)
        decay:       0.23481926 +/- 0.030387 (12.94%) (init= 0.5)
        c:           0.00890713 +/- 0.000264 (2.97%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.751 
        C(decay, c)                  = -0.243 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 188
        # variables        = 1
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -2047.317
        Bayesian info crit = -2044.081
    [[Variables]]
        c:   0.00921161 +/- 0.000314 (3.41%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.005
        reduced chi-square = 0.000
        Akaike info crit   = -2108.304
        Bayesian info crit = -2105.016
    [[Variables]]
        c:   0.00973420 +/- 0.000345 (3.55%) (init= 0.03)


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
