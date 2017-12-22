:orphan:




H12 / Burkina Faso *An. gambiae* / Chromosome 3 / #5
====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **43,640,001** and
**43,680,000**.
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
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 7 genes overlap the focal region: :doc:`../../../../../gene/AGAP009799` (ABCC13 - ATP-binding cassette transporter (ABC transporter) family C member 13),  :doc:`../../../../../gene/AGAP009800`,  :doc:`../../../../../gene/AGAP009801`,  :doc:`../../../../../gene/AGAP009802`:sup:`3` (Gr12 - gustatory receptor 12),  :doc:`../../../../../gene/AGAP009803`:sup:`3` (Gr11 - gustatory receptor 11),  :doc:`../../../../../gene/AGAP009804`:sup:`3` (Gr10 - gustatory receptor 10),  :doc:`../../../../../gene/AGAP009805`:sup:`3` (Gr9 - gustatory receptor 9).




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009806` (MAX-like protein X),  :doc:`../../../../../gene/AGAP009807` (E2F transcription factor 4/5),  :doc:`../../../../../gene/AGAP009808` (ATP-dependent RNA helicase DDX47/RRP3),  :doc:`../../../../../gene/AGAP009809`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/5/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 44
        # data points      = 239
        # variables        = 3
        chi-square         = 0.144
        reduced chi-square = 0.001
        Akaike info crit   = -1766.714
        Bayesian info crit = -1756.285
    [[Variables]]
        amplitude:   0.06203460 +/- 0.007215 (11.63%) (init= 0.5)
        decay:       1.99999908 +/- 0.748801 (37.44%) (init= 0.5)
        c:           0.03239854 +/- 0.006633 (20.48%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.936 
        C(amplitude, c)              = -0.348 
        C(amplitude, decay)          =  0.101 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 37
        # data points      = 148
        # variables        = 3
        chi-square         = 0.057
        reduced chi-square = 0.000
        Akaike info crit   = -1157.863
        Bayesian info crit = -1148.871
    [[Variables]]
        amplitude:   0.15957289 +/- 0.027369 (17.15%) (init= 0.5)
        decay:       0.15000000 +/- 0.001981 (1.32%) (init= 0.5)
        c:           0.04751270 +/- 0.001718 (3.62%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.782 
        C(decay, c)                  =  0.232 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 238
        # variables        = 1
        chi-square         = 0.173
        reduced chi-square = 0.001
        Akaike info crit   = -1718.313
        Bayesian info crit = -1714.841
    [[Variables]]
        c:   0.04649386 +/- 0.001750 (3.76%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.070
        reduced chi-square = 0.000
        Akaike info crit   = -1121.802
        Bayesian info crit = -1118.812
    [[Variables]]
        c:   0.05006184 +/- 0.001810 (3.62%) (init= 0.03)


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
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments.</a></noscript>


