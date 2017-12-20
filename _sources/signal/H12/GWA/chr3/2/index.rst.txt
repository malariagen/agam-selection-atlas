:orphan:

Guinea-Bissau | H12 | Chromosome 3 | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/GWA` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3L** between positions **25,080,001** and
**25,120,000**.



Gene :doc:`/gene/AGAP011480` overlaps the focal region.





The following 4 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP011475` (Envelysin),  :doc:`/gene/AGAP011477` (eupolytin),  :doc:`/gene/AGAP011478`,  :doc:`/gene/AGAP011479` (hyaluronoglucosaminidase).


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
        # function evals   = 41
        # data points      = 193
        # variables        = 3
        chi-square         = 0.013
        reduced chi-square = 0.000
        Akaike info crit   = -1846.007
        Bayesian info crit = -1836.219
    [[Variables]]
        amplitude:   0.02804010 +/- 0.004755 (16.96%) (init= 0.5)
        decay:       0.40568813 +/- 0.109117 (26.90%) (init= 0.5)
        c:           0.02652964 +/- 0.000671 (2.53%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.624 
        C(decay, c)                  = -0.337 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 199
        # variables        = 3
        chi-square         = 0.016
        reduced chi-square = 0.000
        Akaike info crit   = -1872.275
        Bayesian info crit = -1862.395
    [[Variables]]
        amplitude:   0.06214354 +/- 0.009936 (15.99%) (init= 0.5)
        decay:       0.20073610 +/- 0.042060 (20.95%) (init= 0.5)
        c:           0.02382495 +/- 0.000671 (2.82%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.760 
        C(decay, c)                  = -0.227 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 192
        # variables        = 1
        chi-square         = 0.016
        reduced chi-square = 0.000
        Akaike info crit   = -1799.256
        Bayesian info crit = -1795.998
    [[Variables]]
        c:   0.02791356 +/- 0.000664 (2.38%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.020
        reduced chi-square = 0.000
        Akaike info crit   = -1820.103
        Bayesian info crit = -1816.815
    [[Variables]]
        c:   0.02494462 +/- 0.000715 (2.87%) (init= 0.03)


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
