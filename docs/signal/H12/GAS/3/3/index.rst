:orphan:




H12/GAS/3/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **35,059,316** and
**35,139,316**.
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




The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP011917` (serine-type enodpeptidase),  :doc:`../../../../../gene/AGAP011918` (Serine-type enodpeptidase),  :doc:`../../../../../gene/AGAP011919` (eupolytin),  :doc:`../../../../../gene/AGAP011920` (eupolytin),  :doc:`../../../../../gene/AGAP011921`.




The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP011916` (COEB6582 - carboxylesterase),  :doc:`../../../../../gene/AGAP011922` (Lipase maturation factor),  :doc:`../../../../../gene/AGAP011923`,  :doc:`../../../../../gene/AGAP011924` (potassium channel subfamily K, invertebrate),  :doc:`../../../../../gene/AGAP011925` (Patatin-like phospholipase domain containing 5).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 51
        # data points      = 393
        # variables        = 4
        chi-square         = 0.071
        reduced chi-square = 0.000
        Akaike info crit   = -3378.137
        Bayesian info crit = -3362.241
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.08540069 +/- 0.010003 (11.71%) (init= 0.5)
        decay:       0.15000002 +/- 0.015678 (10.45%) (init= 0.5)
        skew:       -0.30762520 +/- 0.168761 (54.86%) (init= 0)
        baseline:    0.03082162 +/- 0.000711 (2.31%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.699 
        C(decay, baseline)           =  0.200 
        C(decay, skew)               = -0.148 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 392
        # variables        = 1
        chi-square         = 0.090
        reduced chi-square = 0.000
        Akaike info crit   = -3284.330
        Bayesian info crit = -3280.358
    [[Variables]]
        c:   0.03225381 +/- 0.000765 (2.37%) (init= 0.03)



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


