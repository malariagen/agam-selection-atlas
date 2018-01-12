:orphan:




H12 / Burkina Faso *An. gambiae* / Chromosome X / #3
====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **9760000** and
**9800000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area shows the focus of the
    selection signal. The shaded blue area shows the genomic region in linkage with the
    selection event. Use the mouse wheel or the controls at the top right of the plot to zoom
    in, and hover over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP013055`,  :doc:`../../../../../gene/AGAP000543` (vitamin-K-epoxide reductase (warfarin-sensitive)).




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000544` (solute carrier family 35, member E1),  :doc:`../../../../../gene/AGAP000545`,  :doc:`../../../../../gene/AGAP000546` (acyl-CoA-binding protein),  :doc:`../../../../../gene/AGAP000547` (rabenosyn-5),  :doc:`../../../../../gene/AGAP000548` (SG1b - salivary gland protein 1-like 2),  :doc:`../../../../../gene/AGAP000549` (2-oxoisovalerate dehydrogenase E2 component (dihydrolipoyl transacylase)),  :doc:`../../../../../gene/AGAP000550`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

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

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 299
        # variables        = 4
        chi-square         = 0.028
        reduced chi-square = 0.000
        Akaike info crit   = -2766.207
        Bayesian info crit = -2751.406
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.06348752 +/- 0.004354 (6.86%) (init= 0.5)
        decay:       0.37934155 +/- 0.041060 (10.82%) (init= 0.5)
        skew:        0.50146343 +/- 0.104585 (20.86%) (init= 0)
        baseline:    0.01808591 +/- 0.000658 (3.64%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.636 
        C(decay, baseline)           = -0.385 
        C(decay, skew)               = -0.225 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 298
        # variables        = 1
        chi-square         = 0.059
        reduced chi-square = 0.000
        Akaike info crit   = -2541.150
        Bayesian info crit = -2537.453
    [[Variables]]
        c:   0.02213574 +/- 0.000814 (3.68%) (init= 0.03)



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


