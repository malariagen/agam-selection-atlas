:orphan:




H12/AOM/X/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **19,300,000** and
**19,520,000**.
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


The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP001011`,  :doc:`../../../../../gene/AGAP001012`:sup:`3` (Or36 - odorant receptor 36),  :doc:`../../../../../gene/AGAP001013`,  :doc:`../../../../../gene/AGAP001014`,  :doc:`../../../../../gene/AGAP001015` (notch gene homolog 1).



Gene :doc:`../../../../../gene/AGAP001010` (chondroitin sulfate synthase) is within 50 kbp of the focal region.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 406
        # variables        = 4
        chi-square         = 0.143
        reduced chi-square = 0.000
        Akaike info crit   = -3221.300
        Bayesian info crit = -3205.275
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.04797921 +/- 0.003015 (6.28%) (init= 0.5)
        sigma:       1.81157458 +/- 0.156931 (8.66%) (init= 0.5)
        skew:        0.45020990 +/- 0.057244 (12.72%) (init= 0)
        baseline:    0.01808896 +/- 0.002513 (13.90%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.816 
        C(amplitude, baseline)       = -0.576 
        C(sigma, skew)               =  0.211 
        C(amplitude, sigma)          =  0.178 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 405
        # variables        = 1
        chi-square         = 0.223
        reduced chi-square = 0.001
        Akaike info crit   = -3037.510
        Bayesian info crit = -3033.507
    [[Variables]]
        c:   0.03541135 +/- 0.001167 (3.30%) (init= 0.03)



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


