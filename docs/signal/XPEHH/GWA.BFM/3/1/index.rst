:orphan:




XPEHH/GWA.BFM/3/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/BFM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **6,100,000** and
**6,140,000**.
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


The following 8 genes overlap the focal region: :doc:`../../../../../gene/AGAP013769`,  :doc:`../../../../../gene/AGAP008139`,  :doc:`../../../../../gene/AGAP013729`,  :doc:`../../../../../gene/AGAP008140`,  :doc:`../../../../../gene/AGAP008141` (argininosuccinate lyase),  :doc:`../../../../../gene/AGAP008142`,  :doc:`../../../../../gene/AGAP008143`:sup:`1`,  :doc:`../../../../../gene/AGAP008144`.



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008136` (peptidyl-prolyl cis-trans isomerase-like 4),  :doc:`../../../../../gene/AGAP008137` (Niemann-Pick C1 protein),  :doc:`../../../../../gene/AGAP008138`,  :doc:`../../../../../gene/AGAP013752`,  :doc:`../../../../../gene/AGAP013711`,  :doc:`../../../../../gene/AGAP008146`,  :doc:`../../../../../gene/AGAP028548`,  :doc:`../../../../../gene/AGAP028549`,  :doc:`../../../../../gene/AGAP008147` (tRNA-splicing ligase RtcB homolog).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFM/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFM/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFM/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 75
        # data points      = 764
        # variables        = 4
        chi-square         = 191.593
        reduced chi-square = 0.252
        Akaike info crit   = -1048.761
        Bayesian info crit = -1030.207
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.78919282 +/- 0.123376 (6.90%) (init= 3)
        sigma:       0.24069686 +/- 0.023294 (9.68%) (init= 0.5)
        skew:       -0.99999615 +/- 0.119971 (12.00%) (init= 0)
        baseline:    1.43556409 +/- 0.019147 (1.33%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.520 
        C(amplitude, sigma)          = -0.466 
        C(sigma, baseline)           = -0.163 
        C(amplitude, baseline)       = -0.105 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 763
        # variables        = 1
        chi-square         = 237.806
        reduced chi-square = 0.312
        Akaike info crit   = -887.508
        Bayesian info crit = -882.871
    [[Variables]]
        c:   1.51199880 +/- 0.020224 (1.34%) (init= 1)



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


