:orphan:




IHS/BFM/3/5
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3L** between positions **23,159,316** and
**23,219,316**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).





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


Gene :doc:`../../../../../gene/AGAP011384` overlaps the focal region.



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP029132`,  :doc:`../../../../../gene/AGAP011387` (ribosome assembly protein SQT1),  :doc:`../../../../../gene/AGAP029131`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 586
        # variables        = 4
        chi-square         = 88.485
        reduced chi-square = 0.152
        Akaike info crit   = -1099.823
        Bayesian info crit = -1082.330
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.40308549 +/- 0.107712 (7.68%) (init= 3)
        sigma:       0.31653886 +/- 0.028811 (9.10%) (init= 0.5)
        skew:       -0.93147233 +/- 0.111302 (11.95%) (init= 0)
        baseline:    2.04409771 +/- 0.017161 (0.84%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.552 
        C(amplitude, sigma)          = -0.472 
        C(sigma, baseline)           = -0.189 
        C(amplitude, baseline)       = -0.118 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 585
        # variables        = 1
        chi-square         = 120.629
        reduced chi-square = 0.207
        Akaike info crit   = -921.652
        Bayesian info crit = -917.280
    [[Variables]]
        c:   2.11071124 +/- 0.018790 (0.89%) (init= 1)



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


