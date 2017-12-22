:orphan:

H12 / Gabon *An. gambiae* / Chromosome 3 / #1
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3L** between positions **9,760,001** and
**9,960,000**.
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




The following 15 genes overlap the focal region: :doc:`../../../../../gene/AGAP010748`,  :doc:`../../../../../gene/AGAP010750` (ryanodine receptor 2),  :doc:`../../../../../gene/AGAP010751`,  :doc:`../../../../../gene/AGAP010752`,  :doc:`../../../../../gene/AGAP010753`,  :doc:`../../../../../gene/AGAP010754`,  :doc:`../../../../../gene/AGAP010755` (protein mago nashi),  :doc:`../../../../../gene/AGAP010756`,  :doc:`../../../../../gene/AGAP010757`,  :doc:`../../../../../gene/AGAP010758` (Metalloendopeptidase (Fragment)),  :doc:`../../../../../gene/AGAP010759`,  :doc:`../../../../../gene/AGAP010760`,  :doc:`../../../../../gene/AGAP010761`,  :doc:`../../../../../gene/AGAP010762`,  :doc:`../../../../../gene/AGAP010763`.



Gene :doc:`../../../../../gene/AGAP010746` is within 50 kbp of the focal region.



Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 146
        # variables        = 3
        chi-square         = 0.016
        reduced chi-square = 0.000
        Akaike info crit   = -1329.912
        Bayesian info crit = -1320.961
    [[Variables]]
        amplitude:   0.05315150 +/- 0.003445 (6.48%) (init= 0.5)
        decay:       1.44490523 +/- 0.232282 (16.08%) (init= 0.5)
        c:           0.02586593 +/- 0.002067 (7.99%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.818 
        C(amplitude, decay)          = -0.251 
        C(amplitude, c)              = -0.177 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 55
        # data points      = 144
        # variables        = 3
        chi-square         = 0.028
        reduced chi-square = 0.000
        Akaike info crit   = -1224.449
        Bayesian info crit = -1215.540
    [[Variables]]
        amplitude:   0.04563237 +/- 0.007133 (15.63%) (init= 0.5)
        decay:       0.84438555 +/- 0.211870 (25.09%) (init= 0.5)
        c:           0.03719814 +/- 0.001741 (4.68%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.613 
        C(amplitude, decay)          = -0.581 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 145
        # variables        = 1
        chi-square         = 0.040
        reduced chi-square = 0.000
        Akaike info crit   = -1185.433
        Bayesian info crit = -1182.457
    [[Variables]]
        c:   0.03854899 +/- 0.001388 (3.60%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 143
        # variables        = 1
        chi-square         = 0.038
        reduced chi-square = 0.000
        Akaike info crit   = -1175.679
        Bayesian info crit = -1172.716
    [[Variables]]
        c:   0.04248541 +/- 0.001366 (3.22%) (init= 0.03)


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
