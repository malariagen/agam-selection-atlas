:orphan:




XPEHH/GWA.UGS/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/UGS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **48,934,895** and
**49,014,895**.
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


The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP007675` (dynein, axonemal heavy chain),  :doc:`../../../../../gene/AGAP007676`,  :doc:`../../../../../gene/AGAP007677`,  :doc:`../../../../../gene/AGAP007678`,  :doc:`../../../../../gene/AGAP007679`,  :doc:`../../../../../gene/AGAP007680`,  :doc:`../../../../../gene/AGAP013037`,  :doc:`../../../../../gene/AGAP007681` (Rad and Gem related GTP binding protein 1),  :doc:`../../../../../gene/AGAP007682`,  :doc:`../../../../../gene/AGAP007683` (Vacuolar protein sorting-associated protein 35),  :doc:`../../../../../gene/AGAP007684` (Tubulointerstitial nephritis antigen).



The following 11 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007667` (sugar transporter ERD6-like 4),  :doc:`../../../../../gene/AGAP007668` (eIF3g - Eukaryotic translation initiation factor 3 subunit G),  :doc:`../../../../../gene/AGAP007669`,  :doc:`../../../../../gene/AGAP007670` (U2 small nuclear ribonucleoprotein A),  :doc:`../../../../../gene/AGAP007671`,  :doc:`../../../../../gene/AGAP007672` (pancreatic triacylglycerol lipase),  :doc:`../../../../../gene/AGAP007673`,  :doc:`../../../../../gene/AGAP007674` (GIPC PDZ domain containing family, member 2),  :doc:`../../../../../gene/AGAP007685`,  :doc:`../../../../../gene/AGAP007686` (50 kDa dystrophin-associated glycoprotein),  :doc:`../../../../../gene/AGAP007687` (Oxysterol-binding protein).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 636
        # variables        = 4
        chi-square         = 49.391
        reduced chi-square = 0.078
        Akaike info crit   = -1617.258
        Bayesian info crit = -1599.437
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.92943441 +/- 0.108928 (11.72%) (init= 3)
        decay:       0.17467717 +/- 0.031992 (18.32%) (init= 0.5)
        skew:        0.60097362 +/- 0.189482 (31.53%) (init= 0)
        baseline:    1.18944495 +/- 0.012136 (1.02%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.642 
        C(decay, skew)               = -0.364 
        C(decay, baseline)           = -0.269 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 635
        # variables        = 1
        chi-square         = 57.933
        reduced chi-square = 0.091
        Akaike info crit   = -1518.408
        Bayesian info crit = -1513.954
    [[Variables]]
        c:   1.22621306 +/- 0.011995 (0.98%) (init= 1)



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


