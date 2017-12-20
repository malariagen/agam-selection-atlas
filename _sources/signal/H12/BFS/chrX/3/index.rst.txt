:orphan:

Burkina Faso *An. gambiae* | H12 | Chromosome X | Signal #3
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X** between positions **9,620,001** and
**9,740,000**.




The following 7 genes overlap the focal region: :doc:`/gene/AGAP000536` (PGRPS1 - peptidoglycan recognition protein (short)),  :doc:`/gene/AGAP000537` (TWDL8 - cuticular protein TWDL family (TWDL8)),  :doc:`/gene/AGAP000538` (TWDL9 - cuticular protein TWDL family (TWDL9)),  :doc:`/gene/AGAP000539`,  :doc:`/gene/AGAP000540` (proton-coupled amino acid transporter),  :doc:`/gene/AGAP000541` (RpS15a-1 - 40S ribosomal protein S15a),  :doc:`/gene/AGAP013055`.




The following 5 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP013287`,  :doc:`/gene/AGAP000535`,  :doc:`/gene/AGAP028592`,  :doc:`/gene/AGAP012976`,  :doc:`/gene/AGAP013521`.


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
        # function evals   = 35
        # data points      = 201
        # variables        = 3
        chi-square         = 0.034
        reduced chi-square = 0.000
        Akaike info crit   = -1739.051
        Bayesian info crit = -1729.141
    [[Variables]]
        amplitude:   0.06969484 +/- 0.009657 (13.86%) (init= 0.5)
        decay:       0.20544312 +/- 0.045457 (22.13%) (init= 0.5)
        c:           0.01824651 +/- 0.000977 (5.35%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.610 
        C(decay, c)                  = -0.232 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 199
        # variables        = 3
        chi-square         = 0.008
        reduced chi-square = 0.000
        Akaike info crit   = -1998.741
        Bayesian info crit = -1988.861
    [[Variables]]
        amplitude:   0.07702811 +/- 0.004743 (6.16%) (init= 0.5)
        decay:       0.37899841 +/- 0.033057 (8.72%) (init= 0.5)
        c:           0.01731812 +/- 0.000515 (2.98%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.711 
        C(decay, c)                  = -0.324 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.043
        reduced chi-square = 0.000
        Akaike info crit   = -1687.763
        Bayesian info crit = -1684.465
    [[Variables]]
        c:   0.01983468 +/- 0.001037 (5.23%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.027
        reduced chi-square = 0.000
        Akaike info crit   = -1758.374
        Bayesian info crit = -1755.086
    [[Variables]]
        c:   0.02047783 +/- 0.000836 (4.08%) (init= 0.03)


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
