:orphan:

Guinea-Bissau | H12 | Chromosome 2 | Signal #3
================================================================================



This page describes a signal of selection found in the
:doc:`/population/GWA` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L between position 11,260,001 and
11,340,000**.




The following 3 genes overlap the focal region: :doc:`/gene/AGAP005169`,  :doc:`/gene/AGAP005170`,  :doc:`/gene/AGAP005171` (Tctex1 domain-containing protein 4).




The following 5 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP005165`,  :doc:`/gene/AGAP005172`,  :doc:`/gene/AGAP005173` (Px serine/threonine kinase),  :doc:`/gene/AGAP005174` (nucleoporin SEH1),  :doc:`/gene/AGAP005175` (acetyl-CoA carboxylase / biotin carboxylase).


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
        # data points      = 192
        # variables        = 3
        chi-square         = 0.135
        reduced chi-square = 0.001
        Akaike info crit   = -1387.250
        Bayesian info crit = -1377.478
    [[Variables]]
        amplitude:   0.19790682 +/- 0.018766 (9.48%) (init= 0.5)
        decay:       0.23707375 +/- 0.035692 (15.06%) (init= 0.5)
        c:           0.04952406 +/- 0.002064 (4.17%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.615 
        C(decay, c)                  = -0.257 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 198
        # variables        = 3
        chi-square         = 0.124
        reduced chi-square = 0.001
        Akaike info crit   = -1455.008
        Bayesian info crit = -1445.143
    [[Variables]]
        amplitude:   0.15959018 +/- 0.018625 (11.67%) (init= 0.5)
        decay:       0.36668196 +/- 0.060417 (16.48%) (init= 0.5)
        c:           0.05956215 +/- 0.001978 (3.32%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.713 
        C(decay, c)                  = -0.320 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 191
        # variables        = 1
        chi-square         = 0.223
        reduced chi-square = 0.001
        Akaike info crit   = -1288.221
        Bayesian info crit = -1284.969
    [[Variables]]
        c:   0.05510248 +/- 0.002476 (4.49%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 197
        # variables        = 1
        chi-square         = 0.192
        reduced chi-square = 0.001
        Akaike info crit   = -1363.770
        Bayesian info crit = -1360.486
    [[Variables]]
        c:   0.06573436 +/- 0.002230 (3.39%) (init= 0.03)


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
