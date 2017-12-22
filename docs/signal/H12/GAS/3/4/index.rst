:orphan:

H12 / Gabon *An. gambiae* / Chromosome 3 / #4
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **50,640,001** and
**50,720,000**.
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




The following 8 genes overlap the focal region: :doc:`../../../../../gene/AGAP010201`,  :doc:`../../../../../gene/AGAP010202`,  :doc:`../../../../../gene/AGAP010203` (TPR repeat-containing protein LOC90826-like protein),  :doc:`../../../../../gene/AGAP028722`,  :doc:`../../../../../gene/AGAP010204`,  :doc:`../../../../../gene/AGAP010205`,  :doc:`../../../../../gene/AGAP010206` (Protein bicaudal D homolog 2),  :doc:`../../../../../gene/AGAP010207`.




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010200`,  :doc:`../../../../../gene/AGAP013755`,  :doc:`../../../../../gene/AGAP010208`.


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 147
        # variables        = 3
        chi-square         = 0.014
        reduced chi-square = 0.000
        Akaike info crit   = -1356.775
        Bayesian info crit = -1347.804
    [[Variables]]
        amplitude:   0.03519315 +/- 0.005582 (15.86%) (init= 0.5)
        decay:       0.40861415 +/- 0.105013 (25.70%) (init= 0.5)
        c:           0.03121324 +/- 0.000952 (3.05%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.603 
        C(decay, c)                  = -0.402 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 55
        # data points      = 207
        # variables        = 3
        chi-square         = 0.039
        reduced chi-square = 0.000
        Akaike info crit   = -1768.656
        Bayesian info crit = -1758.658
    [[Variables]]
        amplitude:   0.03038872 +/- 0.004561 (15.01%) (init= 0.5)
        decay:       1.45637035 +/- 0.550392 (37.79%) (init= 0.5)
        c:           0.02686479 +/- 0.002530 (9.42%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.865 
        C(amplitude, decay)          = -0.338 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 146
        # variables        = 1
        chi-square         = 0.019
        reduced chi-square = 0.000
        Akaike info crit   = -1304.126
        Bayesian info crit = -1301.143
    [[Variables]]
        c:   0.03358479 +/- 0.000948 (2.82%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 206
        # variables        = 1
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1728.912
        Bayesian info crit = -1725.584
    [[Variables]]
        c:   0.03248758 +/- 0.001046 (3.22%) (init= 0.03)


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
