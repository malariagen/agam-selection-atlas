:orphan:

H12 / Burkina Faso *An. gambiae* / Chromosome 3 / #4
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **31,760,001** and
**31,800,000**.
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




The following 16 genes overlap the focal region: :doc:`../../../../../gene/AGAP009359`,  :doc:`../../../../../gene/AGAP029068`,  :doc:`../../../../../gene/AGAP013734`,  :doc:`../../../../../gene/AGAP029063`,  :doc:`../../../../../gene/AGAP013756`,  :doc:`../../../../../gene/AGAP029094`,  :doc:`../../../../../gene/AGAP009360`,  :doc:`../../../../../gene/AGAP028158`,  :doc:`../../../../../gene/AGAP013714`,  :doc:`../../../../../gene/AGAP029089`,  :doc:`../../../../../gene/AGAP013731`,  :doc:`../../../../../gene/AGAP009361`,  :doc:`../../../../../gene/AGAP028039`,  :doc:`../../../../../gene/AGAP009362`,  :doc:`../../../../../gene/AGAP009363` (CYP9M1 - cytochrome P450),  :doc:`../../../../../gene/AGAP009364`.




The following 27 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP029071`,  :doc:`../../../../../gene/AGAP029072`,  :doc:`../../../../../gene/AGAP013718`,  :doc:`../../../../../gene/AGAP009352`,  :doc:`../../../../../gene/AGAP009353`,  :doc:`../../../../../gene/AGAP009354`,  :doc:`../../../../../gene/AGAP009355`,  :doc:`../../../../../gene/AGAP029090`,  :doc:`../../../../../gene/AGAP028222`,  :doc:`../../../../../gene/AGAP009356`,  :doc:`../../../../../gene/AGAP009357`,  :doc:`../../../../../gene/AGAP029081`,  :doc:`../../../../../gene/AGAP009358`,  :doc:`../../../../../gene/AGAP029076`,  :doc:`../../../../../gene/AGAP029075`,  :doc:`../../../../../gene/AGAP013776`,  :doc:`../../../../../gene/AGAP009365` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP009366`,  :doc:`../../../../../gene/AGAP009367`,  :doc:`../../../../../gene/AGAP009368` (plugin - plugin),  :doc:`../../../../../gene/AGAP009369`,  :doc:`../../../../../gene/AGAP009370` (Acp34A-2),  :doc:`../../../../../gene/AGAP009371`,  :doc:`../../../../../gene/AGAP009372`,  :doc:`../../../../../gene/AGAP009373`,  :doc:`../../../../../gene/AGAP009374` (CYP9M1 - cytochrome P450),  :doc:`../../../../../gene/AGAP009375` (CYP9M2 - cytochrome P450).


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 129
        # variables        = 3
        chi-square         = 0.010
        reduced chi-square = 0.000
        Akaike info crit   = -1214.417
        Bayesian info crit = -1205.837
    [[Variables]]
        amplitude:   0.02677610 +/- 0.005288 (19.75%) (init= 0.5)
        decay:       0.37359485 +/- 0.121136 (32.42%) (init= 0.5)
        c:           0.02130454 +/- 0.000928 (4.35%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.598 
        C(decay, c)                  = -0.403 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 128
        # variables        = 3
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1310.393
        Bayesian info crit = -1301.837
    [[Variables]]
        amplitude:   0.02883969 +/- 0.003178 (11.02%) (init= 0.5)
        decay:       0.72766011 +/- 0.141689 (19.47%) (init= 0.5)
        c:           0.01668192 +/- 0.000686 (4.11%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.657 
        C(decay, c)                  = -0.505 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 128
        # variables        = 1
        chi-square         = 0.012
        reduced chi-square = 0.000
        Akaike info crit   = -1187.001
        Bayesian info crit = -1184.149
    [[Variables]]
        c:   0.02304012 +/- 0.000853 (3.70%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 127
        # variables        = 1
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1242.313
        Bayesian info crit = -1239.469
    [[Variables]]
        c:   0.01964063 +/- 0.000664 (3.38%) (init= 0.03)


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
