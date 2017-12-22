:orphan:

H12 / Guinea *An. gambiae* / Chromosome 2 / #6
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **56,440,001** and
**56,520,000**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP013508`,  :doc:`../../../../../gene/AGAP004453` (GPRDOP3 - GPCR Dopamine Family 3).



Gene :doc:`../../../../../gene/AGAP004452` is within 50 kbp of the focal region.



Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/6/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 601
        # data points      = 143
        # variables        = 3
        chi-square         = 0.068
        reduced chi-square = 0.000
        Akaike info crit   = -1087.617
        Bayesian info crit = -1078.728
    [[Variables]]
        amplitude:   0.06071392 +/- 0.007143 (11.77%) (init= 0.5)
        decay:       1.99998163 +/- 0.711613 (35.58%) (init= 0.5)
        c:           0.05999999 +/- 0.000426 (0.71%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.904 
        C(amplitude, c)              = -0.478 
        C(amplitude, decay)          =  0.166 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 49
        # data points      = 213
        # variables        = 3
        chi-square         = 0.308
        reduced chi-square = 0.001
        Akaike info crit   = -1386.999
        Bayesian info crit = -1376.916
    [[Variables]]
        amplitude:   0.11609596 +/- 0.011008 (9.48%) (init= 0.5)
        decay:       1.99999998 +/- 2.170142 (108.51%) (init= 0.5)
        c:           0.04684975 +/- 0.008301 (17.72%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.896 
        C(amplitude, decay)          =  0.178 
        C(amplitude, c)              = -0.148 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 142
        # variables        = 1
        chi-square         = 0.084
        reduced chi-square = 0.001
        Akaike info crit   = -1052.993
        Bayesian info crit = -1050.037
    [[Variables]]
        c:   0.08082103 +/- 0.002051 (2.54%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 212
        # variables        = 1
        chi-square         = 0.460
        reduced chi-square = 0.002
        Akaike info crit   = -1298.176
        Bayesian info crit = -1294.820
    [[Variables]]
        c:   0.07401708 +/- 0.003207 (4.33%) (init= 0.03)


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
