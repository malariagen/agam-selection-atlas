:orphan:

H12 / Burkina Faso *An. gambiae* / Chromosome X / #3
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X** between positions **9,640,001** and
**9,720,000**.
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




The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP000539`,  :doc:`../../../../../gene/AGAP000540` (proton-coupled amino acid transporter),  :doc:`../../../../../gene/AGAP000541` (RpS15a-1 - 40S ribosomal protein S15a),  :doc:`../../../../../gene/AGAP013055`.




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000535`,  :doc:`../../../../../gene/AGAP028592`,  :doc:`../../../../../gene/AGAP012976`,  :doc:`../../../../../gene/AGAP013521`,  :doc:`../../../../../gene/AGAP000536` (PGRPS1 - peptidoglycan recognition protein (short)),  :doc:`../../../../../gene/AGAP000537` (TWDL8 - cuticular protein TWDL family (TWDL8)),  :doc:`../../../../../gene/AGAP000538` (TWDL9 - cuticular protein TWDL family (TWDL9)).


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 151
        # variables        = 3
        chi-square         = 0.032
        reduced chi-square = 0.000
        Akaike info crit   = -1272.262
        Bayesian info crit = -1263.210
    [[Variables]]
        amplitude:   0.06460198 +/- 0.011786 (18.25%) (init= 0.5)
        decay:       0.15435250 +/- 0.045938 (29.76%) (init= 0.5)
        c:           0.02036912 +/- 0.001259 (6.18%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.584 
        C(decay, c)                  = -0.233 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 149
        # variables        = 3
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -1595.473
        Bayesian info crit = -1586.461
    [[Variables]]
        amplitude:   0.07966178 +/- 0.003243 (4.07%) (init= 0.5)
        decay:       0.40856456 +/- 0.024394 (5.97%) (init= 0.5)
        c:           0.01702704 +/- 0.000450 (2.64%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.691 
        C(decay, c)                  = -0.399 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.036
        reduced chi-square = 0.000
        Akaike info crit   = -1247.831
        Bayesian info crit = -1244.821
    [[Variables]]
        c:   0.02175038 +/- 0.001270 (5.84%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.025
        reduced chi-square = 0.000
        Akaike info crit   = -1285.253
        Bayesian info crit = -1282.256
    [[Variables]]
        c:   0.02180952 +/- 0.001065 (4.89%) (init= 0.03)


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
