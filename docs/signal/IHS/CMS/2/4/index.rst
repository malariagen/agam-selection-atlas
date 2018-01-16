:orphan:




IHS/CMS/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **19,100,000** and
**19,180,000**.
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


Gene :doc:`../../../../../gene/AGAP002310` (protocadherin-15) overlaps the focal region.



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002303`,  :doc:`../../../../../gene/AGAP002305` (pre-mRNA-splicing factor),  :doc:`../../../../../gene/AGAP002306` (RpL4 - 60S ribosomal protein L4),  :doc:`../../../../../gene/AGAP002307` (pre-mRNA-splicing factor 18),  :doc:`../../../../../gene/AGAP002308`:sup:`1` (Pyrroline-5-carboxylate reductase),  :doc:`../../../../../gene/AGAP002309` (WDY - WD repeat-containing protein on Y chromosome),  :doc:`../../../../../gene/AGAP002312`,  :doc:`../../../../../gene/AGAP002313`,  :doc:`../../../../../gene/AGAP002314`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 65
        # data points      = 682
        # variables        = 4
        chi-square         = 64.681
        reduced chi-square = 0.095
        Akaike info crit   = -1598.496
        Bayesian info crit = -1580.396
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.19554641 +/- 0.064869 (5.43%) (init= 3)
        decay:       0.73730147 +/- 0.078624 (10.66%) (init= 0.5)
        skew:       -0.99999996 +/- 0.351560 (35.16%) (init= 0)
        baseline:    1.53193266 +/- 0.016005 (1.04%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.488 
        C(decay, baseline)           = -0.484 
        C(decay, skew)               = -0.463 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 681
        # variables        = 1
        chi-square         = 106.922
        reduced chi-square = 0.157
        Akaike info crit   = -1258.844
        Bayesian info crit = -1254.320
    [[Variables]]
        c:   1.67099349 +/- 0.015195 (0.91%) (init= 1)



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


