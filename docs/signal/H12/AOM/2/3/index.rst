:orphan:




H12/AOM/2/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **25,214,895** and
**25,334,895**.
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



Gene :doc:`../../../../../gene/AGAP006027`:sup:`2` (glutamate receptor, ionotropic , AMPA) overlaps the focal region.





The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006025` (Ras-like protein family member),  :doc:`../../../../../gene/AGAP006026`:sup:`2`,  :doc:`../../../../../gene/AGAP006028`:sup:`2` (Rdl - GABA-gated chloride channel subunit).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 400
        # variables        = 4
        chi-square         = 0.056
        reduced chi-square = 0.000
        Akaike info crit   = -3539.947
        Bayesian info crit = -3523.981
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.07523390 +/- 0.003447 (4.58%) (init= 0.5)
        decay:       0.76594228 +/- 0.064472 (8.42%) (init= 0.5)
        skew:       -0.99999999 +/- 0.036743 (3.67%) (init= 0)
        baseline:    0.02414295 +/- 0.000807 (3.34%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.535 
        C(decay, baseline)           = -0.491 
        C(decay, skew)               =  0.413 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 399
        # variables        = 1
        chi-square         = 0.151
        reduced chi-square = 0.000
        Akaike info crit   = -3140.971
        Bayesian info crit = -3136.982
    [[Variables]]
        c:   0.03288150 +/- 0.000976 (2.97%) (init= 0.03)



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


