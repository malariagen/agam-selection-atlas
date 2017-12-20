:orphan:

Angola *An. coluzzii* | H12 | Chromosome 2 | Signal #7
================================================================================



This page describes a signal of selection found in the
:doc:`/population/AOM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **48,140,001** and
**48,280,000**.




The following 6 genes overlap the focal region: :doc:`/gene/AGAP004033`,  :doc:`/gene/AGAP004034` (GPRNNA4 - putative GPCR class a orphan receptor 4),  :doc:`/gene/AGAP013324` (putative G-protein coupled receptor GPCR),  :doc:`/gene/AGAP004035` (GPRFSH - putative glyco-protein hormone fsh-like receptor),  :doc:`/gene/AGAP004036` (HPX7 - heme peroxidase 7),  :doc:`/gene/AGAP004038` (HPX8 - heme peroxidase 8).



Gene :doc:`/gene/AGAP004039` (afadin) is within 50 kbp of the focal region.



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
        chi-square         = 0.071
        reduced chi-square = 0.000
        Akaike info crit   = -1485.231
        Bayesian info crit = -1475.505
    [[Variables]]
        amplitude:   0.10908514 +/- 0.014131 (12.95%) (init= 0.5)
        decay:       0.21792152 +/- 0.046453 (21.32%) (init= 0.5)
        c:           0.04570022 +/- 0.001504 (3.29%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.611 
        C(decay, c)                  = -0.243 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 195
        # variables        = 3
        chi-square         = 0.107
        reduced chi-square = 0.001
        Akaike info crit   = -1457.473
        Bayesian info crit = -1447.654
    [[Variables]]
        amplitude:   0.08046150 +/- 0.013203 (16.41%) (init= 0.5)
        decay:       0.59018925 +/- 0.145536 (24.66%) (init= 0.5)
        c:           0.05573531 +/- 0.002020 (3.63%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.672 
        C(decay, c)                  = -0.416 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 188
        # variables        = 1
        chi-square         = 0.096
        reduced chi-square = 0.001
        Akaike info crit   = -1422.121
        Bayesian info crit = -1418.884
    [[Variables]]
        c:   0.04848773 +/- 0.001656 (3.42%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 194
        # variables        = 1
        chi-square         = 0.132
        reduced chi-square = 0.001
        Akaike info crit   = -1412.610
        Bayesian info crit = -1409.342
    [[Variables]]
        c:   0.06102162 +/- 0.001878 (3.08%) (init= 0.03)


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
