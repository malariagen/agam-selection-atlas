:orphan:




H12/AOM/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **22,359,316** and
**22,539,316**.
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




The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP011374` (AP-1 complex subunit mu),  :doc:`../../../../../gene/AGAP011375` (Selenophosphate synthetase 2),  :doc:`../../../../../gene/AGAP011376`,  :doc:`../../../../../gene/AGAP011377`.



Gene :doc:`../../../../../gene/AGAP011373` is within 50 kbp of the focal region.



Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 387
        # variables        = 4
        chi-square         = 0.020
        reduced chi-square = 0.000
        Akaike info crit   = -3805.474
        Bayesian info crit = -3789.641
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.02636686 +/- 0.002050 (7.78%) (init= 0.5)
        sigma:       0.42501744 +/- 0.039503 (9.29%) (init= 0.5)
        skew:       -0.33118647 +/- 0.107502 (32.46%) (init= 0)
        baseline:    0.02238142 +/- 0.000401 (1.79%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.515 
        C(sigma, baseline)           = -0.227 
        C(sigma, skew)               =  0.181 
        C(amplitude, baseline)       = -0.141 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 386
        # variables        = 1
        chi-square         = 0.031
        reduced chi-square = 0.000
        Akaike info crit   = -3636.086
        Bayesian info crit = -3632.130
    [[Variables]]
        c:   0.02414939 +/- 0.000458 (1.90%) (init= 0.03)



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


