:orphan:

Gabon *An. gambiae* | H12 | Chromosome X | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/GAS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X** between positions **9,160,001** and
**9,200,000**.


No genes overlap the focal region.






The following 3 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP000515` (enhancer of rudimentary protein),  :doc:`/gene/AGAP000516` (enhancer of rudimentary protein),  :doc:`/gene/AGAP000519` (diacylglycerol kinase (ATP dependent)).


.. figure:: peak_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`/signal/H12/BFS/chrX/2/index`,"X:9,180,001-9,260,000",504
    



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
        # function evals   = 44
        # data points      = 201
        # variables        = 3
        chi-square         = 0.195
        reduced chi-square = 0.001
        Akaike info crit   = -1388.094
        Bayesian info crit = -1378.184
    [[Variables]]
        amplitude:   0.07732815 +/- 0.009178 (11.87%) (init= 0.5)
        decay:       3          +/- 0.000289 (0.01%) (init= 0.5)
        c:           0.02869854 +/- 0.009927 (34.59%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.926 
        C(amplitude, c)              = -0.599 
        C(amplitude, decay)          = -0.337 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 45
        # data points      = 199
        # variables        = 3
        chi-square         = 0.492
        reduced chi-square = 0.003
        Akaike info crit   = -1188.403
        Bayesian info crit = -1178.523
    [[Variables]]
        amplitude:   0.31119670 +/- 0.053439 (17.17%) (init= 0.5)
        decay:       0.21086195 +/- 0.047770 (22.65%) (init= 0.5)
        c:           0.05999998 +/- 0.003761 (6.27%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.756 
        C(decay, c)                  = -0.237 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.254
        reduced chi-square = 0.001
        Akaike info crit   = -1332.140
        Bayesian info crit = -1328.842
    [[Variables]]
        c:   0.05503109 +/- 0.002523 (4.59%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.603
        reduced chi-square = 0.003
        Akaike info crit   = -1145.276
        Bayesian info crit = -1141.988
    [[Variables]]
        c:   0.07229844 +/- 0.003931 (5.44%) (init= 0.03)


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
