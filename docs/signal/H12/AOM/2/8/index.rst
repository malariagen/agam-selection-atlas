:orphan:




H12/AOM/2/8
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **48,120,000** and
**48,160,000**.
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



Gene :doc:`../../../../../gene/AGAP004033` overlaps the focal region.




Gene :doc:`../../../../../gene/AGAP004034` (GPRNNA4 - putative GPCR class a orphan receptor 4) is within 50 kbp of the focal region.



Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/8/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/8/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/8/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 65
        # data points      = 385
        # variables        = 4
        chi-square         = 0.184
        reduced chi-square = 0.000
        Akaike info crit   = -2936.498
        Bayesian info crit = -2920.685
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.08865044 +/- 0.008961 (10.11%) (init= 0.5)
        decay:       0.38878674 +/- 0.068588 (17.64%) (init= 0.5)
        skew:       -0.99999994 +/- 0.081208 (8.12%) (init= 0)
        baseline:    0.04958978 +/- 0.001287 (2.60%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.586 
        C(decay, skew)               = -0.475 
        C(decay, baseline)           = -0.331 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 384
        # variables        = 1
        chi-square         = 0.252
        reduced chi-square = 0.001
        Akaike info crit   = -2811.897
        Bayesian info crit = -2807.946
    [[Variables]]
        c:   0.05480143 +/- 0.001309 (2.39%) (init= 0.03)



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


