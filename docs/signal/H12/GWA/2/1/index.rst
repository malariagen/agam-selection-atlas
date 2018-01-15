:orphan:




H12/GWA/2/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **31,954,895** and
**31,994,895**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP006439` (fringe),  :doc:`../../../../../gene/AGAP006440` (IR136 - ionotropic receptor IR136).



Gene :doc:`../../../../../gene/AGAP006441` (GTP cyclohydrolase I) is within 50 kbp of the focal region.



Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/1/peak_finding.png"/>
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

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 393
        # variables        = 4
        chi-square         = 0.112
        reduced chi-square = 0.000
        Akaike info crit   = -3200.490
        Bayesian info crit = -3184.595
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.25298218 +/- 0.012112 (4.79%) (init= 0.5)
        decay:       0.15484055 +/- 0.010777 (6.96%) (init= 0.5)
        skew:        0.28590988 +/- 0.070170 (24.54%) (init= 0)
        baseline:    0.04377143 +/- 0.000892 (2.04%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.687 
        C(decay, baseline)           = -0.203 
        C(decay, skew)               = -0.134 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 392
        # variables        = 1
        chi-square         = 0.294
        reduced chi-square = 0.001
        Akaike info crit   = -2818.473
        Bayesian info crit = -2814.502
    [[Variables]]
        c:   0.04822766 +/- 0.001385 (2.87%) (init= 0.03)



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


