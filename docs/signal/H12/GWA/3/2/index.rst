:orphan:




H12/GWA/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **25,059,316** and
**25,179,316**.
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




The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP011479` (hyaluronoglucosaminidase),  :doc:`../../../../../gene/AGAP011480`:sup:`4`,  :doc:`../../../../../gene/AGAP011481` (GPR5HT1B - putative serotonin 5HT-1b receptor).




The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP028522`,  :doc:`../../../../../gene/AGAP011475` (Envelysin),  :doc:`../../../../../gene/AGAP011476`,  :doc:`../../../../../gene/AGAP011477` (eupolytin),  :doc:`../../../../../gene/AGAP011478`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 391
        # variables        = 4
        chi-square         = 0.030
        reduced chi-square = 0.000
        Akaike info crit   = -3697.383
        Bayesian info crit = -3681.508
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.04030958 +/- 0.004581 (11.37%) (init= 0.5)
        decay:       0.28584656 +/- 0.049065 (17.17%) (init= 0.5)
        skew:        0.44867621 +/- 0.171131 (38.14%) (init= 0)
        baseline:    0.02509793 +/- 0.000483 (1.92%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.668 
        C(decay, baseline)           = -0.277 
        C(decay, skew)               = -0.207 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 390
        # variables        = 1
        chi-square         = 0.038
        reduced chi-square = 0.000
        Akaike info crit   = -3600.542
        Bayesian info crit = -3596.576
    [[Variables]]
        c:   0.02648986 +/- 0.000500 (1.89%) (init= 0.03)



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


