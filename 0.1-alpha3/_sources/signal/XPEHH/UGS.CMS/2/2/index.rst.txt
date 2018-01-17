:orphan:




XPEHH/UGS.CMS/2/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/CMS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **58,120,000** and
**58,520,000**.
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


The following 32 genes overlap the focal region: :doc:`../../../../../gene/AGAP004587`,  :doc:`../../../../../gene/AGAP004588`,  :doc:`../../../../../gene/AGAP004589`,  :doc:`../../../../../gene/AGAP004590`,  :doc:`../../../../../gene/AGAP013326`,  :doc:`../../../../../gene/AGAP004591` (acid phosphatase),  :doc:`../../../../../gene/AGAP004592` (splicing factor, arginine/serine-rich 4/5/6),  :doc:`../../../../../gene/AGAP004593` (EH domain-containing protein 1),  :doc:`../../../../../gene/AGAP004594` (cell division protein kinase 2),  :doc:`../../../../../gene/AGAP004595`:sup:`2` (GPRGBB2 - putative GABA-B receptor 2),  :doc:`../../../../../gene/AGAP004596` (PyK - pyruvate kinase),  :doc:`../../../../../gene/AGAP004597` (guanosine-3',5'-bis(diphosphate) 3'-pyrophosphohydrolase),  :doc:`../../../../../gene/AGAP004598` (Phosphoserine aminotransferase),  :doc:`../../../../../gene/AGAP004599` (defense protein 3),  :doc:`../../../../../gene/AGAP004604`,  :doc:`../../../../../gene/AGAP004600` (ABCC6 - ATP-binding cassette transporter (ABC transporter) family C member 6),  :doc:`../../../../../gene/AGAP004602` (ABCC4 - ATP-binding cassette transporter (ABC transporter) family C member 4),  :doc:`../../../../../gene/AGAP004603` (ABCG4 - ATP-binding cassette transporter (ABC transporter) family G member 4),  :doc:`../../../../../gene/AGAP004605` (zinc finger protein 830),  :doc:`../../../../../gene/AGAP004606` (HYPK),  :doc:`../../../../../gene/AGAP004607`,  :doc:`../../../../../gene/AGAP004608`,  :doc:`../../../../../gene/AGAP004609` (protein kinase C substrate 80K-H),  :doc:`../../../../../gene/AGAP004610` (signal recognition particle subunit SRP54),  :doc:`../../../../../gene/AGAP013073`,  :doc:`../../../../../gene/AGAP004611`:sup:`1` (prolyl 4-hydroxylase),  :doc:`../../../../../gene/AGAP013331`,  :doc:`../../../../../gene/AGAP004612` (phosphotransferase LOC123688),  :doc:`../../../../../gene/AGAP004613` (GPRDOP1 - GPCR Dopamine Family 1),  :doc:`../../../../../gene/AGAP004614` (DNA polymerase epsilon subunit 2),  :doc:`../../../../../gene/AGAP004615` (DNA polymerase epsilon subunit 1),  :doc:`../../../../../gene/AGAP004616` (F-type H -transporting ATPase subunit 6).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004586` (ADP-ribosylation factor related protein 1),  :doc:`../../../../../gene/AGAP013140`,  :doc:`../../../../../gene/AGAP004618`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 313
        # variables        = 4
        chi-square         = 295.146
        reduced chi-square = 0.955
        Akaike info crit   = -10.384
        Bayesian info crit = 4.601
    [[Variables]]
        center:      0 (fixed)
        amplitude:   4.71366317 +/- 0.203556 (4.32%) (init= 3)
        sigma:       2.73106252 +/- 0.129513 (4.74%) (init= 0.5)
        skew:       -0.85059301 +/- 0.033079 (3.89%) (init= 0)
        baseline:    1.68268633 +/- 0.184971 (10.99%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.816 
        C(sigma, baseline)           = -0.799 
        C(amplitude, sigma)          =  0.441 
        C(sigma, skew)               =  0.255 
        C(skew, baseline)            = -0.154 
        C(amplitude, skew)           =  0.149 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 13
        # data points      = 312
        # variables        = 1
        chi-square         = 916.214
        reduced chi-square = 2.946
        Akaike info crit   = 338.101
        Bayesian info crit = 341.844
    [[Variables]]
        c:   4.14870045 +/- 0.097171 (2.34%) (init= 1)



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


