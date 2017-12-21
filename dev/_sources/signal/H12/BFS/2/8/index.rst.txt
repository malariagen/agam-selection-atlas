:orphan:

H12 / Burkina Faso *An. gambiae* / Chromosome 2 / #8
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **42,300,001** and
**42,380,000**.
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



Gene :doc:`../../../../../gene/AGAP007086` (Sodium channel protein) overlaps the focal region.





The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007081`,  :doc:`../../../../../gene/AGAP007082` (NADH dehydrogenase (ubiquinone) Fe-S protein 4),  :doc:`../../../../../gene/AGAP007083`,  :doc:`../../../../../gene/AGAP007084`,  :doc:`../../../../../gene/AGAP007085`,  :doc:`../../../../../gene/AGAP007087` (RpL41 - 60s ribosomal protein L41),  :doc:`../../../../../gene/AGAP007088` (peptidyl-prolyl cis-trans isomerase B (cyclophilin B)),  :doc:`../../../../../gene/AGAP007089`.


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/8/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/8/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/8/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 150
        # variables        = 3
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1561.576
        Bayesian info crit = -1552.544
    [[Variables]]
        amplitude:   0.02565956 +/- 0.004404 (17.17%) (init= 0.5)
        decay:       0.15000022 +/- 0.042462 (28.31%) (init= 0.5)
        c:           0.01371870 +/- 0.000468 (3.41%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.581 
        C(decay, c)                  = -0.230 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 149
        # variables        = 3
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1748.198
        Bayesian info crit = -1739.186
    [[Variables]]
        amplitude:   0.03161851 +/- 0.002118 (6.70%) (init= 0.5)
        decay:       0.35489336 +/- 0.034119 (9.61%) (init= 0.5)
        c:           0.01113040 +/- 0.000263 (2.37%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.705 
        C(decay, c)                  = -0.368 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.005
        reduced chi-square = 0.000
        Akaike info crit   = -1532.440
        Bayesian info crit = -1529.436
    [[Variables]]
        c:   0.01425650 +/- 0.000477 (3.35%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1555.782
        Bayesian info crit = -1552.785
    [[Variables]]
        c:   0.01273623 +/- 0.000427 (3.36%) (init= 0.03)


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
