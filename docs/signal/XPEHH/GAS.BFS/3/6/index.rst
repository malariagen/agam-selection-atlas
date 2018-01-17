:orphan:




XPEHH/GAS.BFS/3/6
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3L** between positions **15,059,316** and
**15,199,316**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).





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


No genes overlap the focal region.



No genes are within 50 kbp of the focal region.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/6/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 126
        # data points      = 409
        # variables        = 4
        chi-square         = 110.181
        reduced chi-square = 0.272
        Akaike info crit   = -528.441
        Bayesian info crit = -512.386
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.92437110 +/- 0.083605 (9.04%) (init= 3)
        sigma:       2.78301218 +/- 0.364061 (13.08%) (init= 0.5)
        skew:       -0.99999948 +/- 0.348633 (34.86%) (init= 0)
        baseline:    1.47491000 +/- 0.070985 (4.81%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.801 
        C(sigma, skew)               = -0.533 
        C(sigma, baseline)           = -0.471 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 408
        # variables        = 1
        chi-square         = 140.316
        reduced chi-square = 0.345
        Akaike info crit   = -433.486
        Bayesian info crit = -429.475
    [[Variables]]
        c:   2.07171478 +/- 0.029068 (1.40%) (init= 1)



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


