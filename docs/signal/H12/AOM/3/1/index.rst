:orphan:




H12/AOM/3/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **5,639,316** and
**5,819,316**.
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


The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP010530` (CLIPE4 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP010531` (fibrinogen-related protein 7),  :doc:`../../../../../gene/AGAP010534`,  :doc:`../../../../../gene/AGAP010535` (3-demethylubiquinone-9 3-methyltransferase 2),  :doc:`../../../../../gene/AGAP010536` (nucleolar complex protein 2).



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010519` (kinesin-like protein unc-104),  :doc:`../../../../../gene/AGAP010520` (krueppel-like factor, other),  :doc:`../../../../../gene/AGAP010537` (hexaprenyldihydroxybenzoate methyltransferase),  :doc:`../../../../../gene/AGAP010538` (M-phase phosphoprotein),  :doc:`../../../../../gene/AGAP010539` (coiled-coil and C2 domain-containing protein 1-like),  :doc:`../../../../../gene/AGAP010540`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 65
        # data points      = 485
        # variables        = 4
        chi-square         = 0.073
        reduced chi-square = 0.000
        Akaike info crit   = -4258.198
        Bayesian info crit = -4241.461
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.03522293 +/- 0.002730 (7.75%) (init= 0.5)
        decay:       1.35056217 +/- 0.188681 (13.97%) (init= 0.5)
        skew:       -0.99999999 +/- 0.011694 (1.17%) (init= 0)
        baseline:    0.02942177 +/- 0.000846 (2.88%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.580 
        C(amplitude, decay)          = -0.463 
        C(decay, skew)               = -0.287 
        C(amplitude, baseline)       = -0.112 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 484
        # variables        = 1
        chi-square         = 0.104
        reduced chi-square = 0.000
        Akaike info crit   = -4085.105
        Bayesian info crit = -4080.923
    [[Variables]]
        c:   0.03526716 +/- 0.000667 (1.89%) (init= 0.03)



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


