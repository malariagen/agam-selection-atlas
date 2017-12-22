:orphan:

H12 / Guinea *An. gambiae* / Chromosome 3 / #4
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **18,980,001** and
**19,020,000**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>


No genes overlap the focal region.






The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008826`,  :doc:`../../../../../gene/AGAP028025`.


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/BFS/3/6/index`,"3R:18,600,001-19,100,000",82
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 139
        # variables        = 3
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1589.261
        Bayesian info crit = -1580.458
    [[Variables]]
        amplitude:   0.01452372 +/- 0.001608 (11.08%) (init= 0.5)
        decay:       1.09027754 +/- 0.195075 (17.89%) (init= 0.5)
        c:           0.01966788 +/- 0.000476 (2.42%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.706 
        C(amplitude, decay)          = -0.482 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 67
        # data points      = 149
        # variables        = 3
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1713.265
        Bayesian info crit = -1704.253
    [[Variables]]
        amplitude:   0.01504537 +/- 0.003528 (23.45%) (init= 0.5)
        decay:       0.19989030 +/- 0.062925 (31.48%) (init= 0.5)
        c:           0.02207603 +/- 0.000277 (1.25%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.760 
        C(decay, c)                  = -0.260 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 138
        # variables        = 1
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1531.888
        Bayesian info crit = -1528.961
    [[Variables]]
        c:   0.02150160 +/- 0.000329 (1.53%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1682.625
        Bayesian info crit = -1679.628
    [[Variables]]
        c:   0.02242877 +/- 0.000278 (1.24%) (init= 0.03)


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
