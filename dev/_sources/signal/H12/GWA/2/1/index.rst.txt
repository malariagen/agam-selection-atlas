:orphan:

H12 / Guinea-Bissau / Chromosome 2 / #1
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **47,760,001** and
**47,820,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

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




The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP004000` (myosin IX),  :doc:`../../../../../gene/AGAP004002` (60 kDa heat shock protein, mitochondrial precursor),  :doc:`../../../../../gene/AGAP013015` (p53 and DNA damage-regulated protein),  :doc:`../../../../../gene/AGAP004003`,  :doc:`../../../../../gene/AGAP004004`,  :doc:`../../../../../gene/AGAP004005`.




The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003997` (casein kinase 1, gamma),  :doc:`../../../../../gene/AGAP003999`,  :doc:`../../../../../gene/AGAP013019`,  :doc:`../../../../../gene/AGAP004006`,  :doc:`../../../../../gene/AGAP004007`,  :doc:`../../../../../gene/AGAP004008`,  :doc:`../../../../../gene/AGAP004011` (survival motor neuron protein),  :doc:`../../../../../gene/AGAP004012` (katanin p60 ATPase-containing subunit).


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 140
        # variables        = 3
        chi-square         = 0.043
        reduced chi-square = 0.000
        Akaike info crit   = -1125.133
        Bayesian info crit = -1116.309
    [[Variables]]
        amplitude:   0.23835243 +/- 0.013331 (5.59%) (init= 0.5)
        decay:       0.19467786 +/- 0.017671 (9.08%) (init= 0.5)
        c:           0.05057227 +/- 0.001621 (3.21%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.596 
        C(decay, c)                  = -0.274 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 144
        # variables        = 3
        chi-square         = 0.078
        reduced chi-square = 0.001
        Akaike info crit   = -1076.158
        Bayesian info crit = -1067.249
    [[Variables]]
        amplitude:   0.19138735 +/- 0.016433 (8.59%) (init= 0.5)
        decay:       0.40480750 +/- 0.051707 (12.77%) (init= 0.5)
        c:           0.05836369 +/- 0.002311 (3.96%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.681 
        C(decay, c)                  = -0.405 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 139
        # variables        = 1
        chi-square         = 0.155
        reduced chi-square = 0.001
        Akaike info crit   = -942.637
        Bayesian info crit = -939.703
    [[Variables]]
        c:   0.05822204 +/- 0.002846 (4.89%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 143
        # variables        = 1
        chi-square         = 0.182
        reduced chi-square = 0.001
        Akaike info crit   = -951.485
        Bayesian info crit = -948.522
    [[Variables]]
        c:   0.06931702 +/- 0.002992 (4.32%) (init= 0.03)


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
