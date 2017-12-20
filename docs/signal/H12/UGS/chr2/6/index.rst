:orphan:

Uganda *An. gambiae* | H12 | Chromosome 2 | Signal #6
================================================================================



This page describes a signal of selection found in the
:doc:`/population/UGS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
2L between position 42,760,001 and
42,800,000.




The following 3 genes overlap the focal region: :doc:`/gene/AGAP007103` (calsyntenin-1),  :doc:`/gene/AGAP007104` (farnesyl diphosphate synthase),  :doc:`/gene/AGAP007105`.




The following 3 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP007106` (ubiquitin carboxyl-terminal hydrolase 47),  :doc:`/gene/AGAP007107` (DnaJ homolog subfamily B member 4),  :doc:`/gene/AGAP007108` (multiple PDZ domain protein).


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
        # function evals   = 31
        # data points      = 200
        # variables        = 3
        chi-square         = 0.017
        reduced chi-square = 0.000
        Akaike info crit   = -1866.568
        Bayesian info crit = -1856.673
    [[Variables]]
        amplitude:   0.03236057 +/- 0.003616 (11.18%) (init= 0.5)
        decay:       0.98432756 +/- 0.193031 (19.61%) (init= 0.5)
        c:           0.01570219 +/- 0.000924 (5.89%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.569 
        C(amplitude, decay)          = -0.557 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 44
        # data points      = 199
        # variables        = 3
        chi-square         = 0.033
        reduced chi-square = 0.000
        Akaike info crit   = -1728.740
        Bayesian info crit = -1718.860
    [[Variables]]
        amplitude:   0.12763044 +/- 0.017811 (13.96%) (init= 0.5)
        decay:       0.15000002 +/- 0.026269 (17.51%) (init= 0.5)
        c:           0.01711704 +/- 0.000951 (5.55%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.785 
        C(decay, c)                  = -0.199 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 199
        # variables        = 1
        chi-square         = 0.023
        reduced chi-square = 0.000
        Akaike info crit   = -1801.934
        Bayesian info crit = -1798.641
    [[Variables]]
        c:   0.01943642 +/- 0.000764 (3.93%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.040
        reduced chi-square = 0.000
        Akaike info crit   = -1681.923
        Bayesian info crit = -1678.635
    [[Variables]]
        c:   0.01860436 +/- 0.001013 (5.45%) (init= 0.03)


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
