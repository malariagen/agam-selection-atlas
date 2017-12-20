:orphan:

Angola *An. coluzzii* | H12 | Chromosome X | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/AOM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X** between positions **4,300,001** and
**4,340,000**.




The following 3 genes overlap the focal region: :doc:`/gene/AGAP000228` (netrin 1),  :doc:`/gene/AGAP000230` (Or52 - odorant receptor 52),  :doc:`/gene/AGAP012975` (histamine-gated chloride channel subunit).




The following 5 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP013512`,  :doc:`/gene/AGAP000226` (Or41 - odorant receptor 41),  :doc:`/gene/AGAP000232` (regulator of G-protein signaling),  :doc:`/gene/AGAP000233`,  :doc:`/gene/AGAP000234`.


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
        # function evals   = 39
        # data points      = 201
        # variables        = 3
        chi-square         = 0.015
        reduced chi-square = 0.000
        Akaike info crit   = -1901.175
        Bayesian info crit = -1891.265
    [[Variables]]
        amplitude:   0.11382227 +/- 0.006435 (5.65%) (init= 0.5)
        decay:       0.20703501 +/- 0.018682 (9.02%) (init= 0.5)
        c:           0.02188869 +/- 0.000653 (2.98%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.611 
        C(decay, c)                  = -0.233 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 200
        # variables        = 3
        chi-square         = 0.027
        reduced chi-square = 0.000
        Akaike info crit   = -1773.764
        Bayesian info crit = -1763.869
    [[Variables]]
        amplitude:   0.27866577 +/- 0.015409 (5.53%) (init= 0.5)
        decay:       0.16045860 +/- 0.011253 (7.01%) (init= 0.5)
        c:           0.02766387 +/- 0.000868 (3.14%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.779 
        C(decay, c)                  = -0.205 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.045
        reduced chi-square = 0.000
        Akaike info crit   = -1679.856
        Bayesian info crit = -1676.558
    [[Variables]]
        c:   0.02463888 +/- 0.001058 (4.29%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 199
        # variables        = 1
        chi-square         = 0.106
        reduced chi-square = 0.001
        Akaike info crit   = -1497.815
        Bayesian info crit = -1494.522
    [[Variables]]
        c:   0.03162758 +/- 0.001640 (5.19%) (init= 0.03)


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
