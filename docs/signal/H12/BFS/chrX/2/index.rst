:orphan:

Burkina Faso *An. gambiae* | H12 | Chromosome X | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X between position 9,180,001 and
9,260,000**.



Gene :doc:`/gene/AGAP000519` (diacylglycerol kinase (ATP dependent)) overlaps the focal region.





The following 2 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP000520`,  :doc:`/gene/AGAP000521`.


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

    :doc:`/signal/H12/BFM/chrX/2/index`,":9200001-9240000",170
    :doc:`/signal/H12/GAS/chrX/2/index`,":9160001-9200000",99
    



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
        # data points      = 201
        # variables        = 3
        chi-square         = 0.031
        reduced chi-square = 0.000
        Akaike info crit   = -1758.262
        Bayesian info crit = -1748.352
    [[Variables]]
        amplitude:   0.25479899 +/- 0.009911 (3.89%) (init= 0.5)
        decay:       0.16228390 +/- 0.010250 (6.32%) (init= 0.5)
        c:           0.01711468 +/- 0.000921 (5.38%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.595 
        C(decay, c)                  = -0.206 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 55
        # data points      = 199
        # variables        = 3
        chi-square         = 0.051
        reduced chi-square = 0.000
        Akaike info crit   = -1641.280
        Bayesian info crit = -1631.400
    [[Variables]]
        amplitude:   0.34146092 +/- 0.022227 (6.51%) (init= 0.5)
        decay:       0.15000024 +/- 0.011666 (7.78%) (init= 0.5)
        c:           0.02283849 +/- 0.001184 (5.19%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.786 
        C(decay, c)                  = -0.198 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.120
        reduced chi-square = 0.001
        Akaike info crit   = -1480.987
        Bayesian info crit = -1477.689
    [[Variables]]
        c:   0.02159231 +/- 0.001739 (8.06%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.155
        reduced chi-square = 0.001
        Akaike info crit   = -1414.456
        Bayesian info crit = -1411.168
    [[Variables]]
        c:   0.02727218 +/- 0.001992 (7.30%) (init= 0.03)


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
