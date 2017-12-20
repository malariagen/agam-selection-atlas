:orphan:

Uganda *An. gambiae* | H12 | Chromosome 3 | Signal #5
================================================================================



This page describes a signal of selection found in the
:doc:`/population/UGS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **37,080,001** and
**37,260,000**.




The following 7 genes overlap the focal region: :doc:`/gene/AGAP009621` (alpha-N-acetylgalactosaminidase),  :doc:`/gene/AGAP009622` (6-phosphofructo-2-kinase / fructose-2,6-bisphosphatase),  :doc:`/gene/AGAP009623` (GAPDH - glyceraldehyde 3-phosphate dehydrogenase),  :doc:`/gene/AGAP009624` (CTPsyn - CTP synthase),  :doc:`/gene/AGAP009625`,  :doc:`/gene/AGAP009626` (Kv channel-interacting protein 4 isoform 2),  :doc:`/gene/AGAP009627`.




The following 6 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP009616`,  :doc:`/gene/AGAP009617` (fatty-acid amide hydrolase 2),  :doc:`/gene/AGAP009618`,  :doc:`/gene/AGAP009619` (S-adenosylmethionine decarboxylase proenzyme),  :doc:`/gene/AGAP009620` (reduction in cnn dots 4),  :doc:`/gene/AGAP009628` (phosphatidylinositol-3,4,5-trisphosphate 3-phosphatase and dual-specificity).


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
        # function evals   = 40
        # data points      = 198
        # variables        = 3
        chi-square         = 0.043
        reduced chi-square = 0.000
        Akaike info crit   = -1666.064
        Bayesian info crit = -1656.200
    [[Variables]]
        amplitude:   0.04493381 +/- 0.004360 (9.70%) (init= 0.5)
        decay:       3          +/- 3.42e-06 (0.00%) (init= 0.5)
        c:           0.01650384 +/- 0.004736 (28.70%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.926 
        C(amplitude, c)              = -0.608 
        C(amplitude, decay)          = -0.347 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 288
        # variables        = 3
        chi-square         = 0.073
        reduced chi-square = 0.000
        Akaike info crit   = -2379.470
        Bayesian info crit = -2368.481
    [[Variables]]
        amplitude:   0.08082439 +/- 0.015686 (19.41%) (init= 0.5)
        decay:       0.23714943 +/- 0.061001 (25.72%) (init= 0.5)
        c:           0.04426850 +/- 0.000983 (2.22%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.752 
        C(decay, c)                  = -0.208 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 197
        # variables        = 1
        chi-square         = 0.059
        reduced chi-square = 0.000
        Akaike info crit   = -1597.614
        Bayesian info crit = -1594.331
    [[Variables]]
        c:   0.03186261 +/- 0.001232 (3.87%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 287
        # variables        = 1
        chi-square         = 0.083
        reduced chi-square = 0.000
        Akaike info crit   = -2336.569
        Bayesian info crit = -2332.910
    [[Variables]]
        c:   0.04554007 +/- 0.001005 (2.21%) (init= 0.03)


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
