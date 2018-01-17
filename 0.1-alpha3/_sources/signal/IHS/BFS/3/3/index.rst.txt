:orphan:




IHS/BFS/3/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **32,440,000** and
**32,880,000**.
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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP009416`,  :doc:`../../../../../gene/AGAP009417`,  :doc:`../../../../../gene/AGAP009418`,  :doc:`../../../../../gene/AGAP009419`,  :doc:`../../../../../gene/AGAP009420`,  :doc:`../../../../../gene/AGAP009424`.



No genes are within 50 kbp of the focal region.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 84
        # data points      = 546
        # variables        = 4
        chi-square         = 132.256
        reduced chi-square = 0.244
        Akaike info crit   = -766.162
        Bayesian info crit = -748.952
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.49770129 +/- 0.097248 (6.49%) (init= 3)
        sigma:       0.99077048 +/- 0.073263 (7.39%) (init= 0.5)
        skew:        0.62135468 +/- 0.077403 (12.46%) (init= 0)
        baseline:    1.86089905 +/- 0.025938 (1.39%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.513 
        C(sigma, baseline)           = -0.394 
        C(sigma, skew)               = -0.332 
        C(amplitude, baseline)       = -0.131 
        C(amplitude, skew)           =  0.106 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 545
        # variables        = 1
        chi-square         = 205.022
        reduced chi-square = 0.377
        Akaike info crit   = -530.830
        Bayesian info crit = -526.530
    [[Variables]]
        c:   2.04310203 +/- 0.026296 (1.29%) (init= 1)



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


