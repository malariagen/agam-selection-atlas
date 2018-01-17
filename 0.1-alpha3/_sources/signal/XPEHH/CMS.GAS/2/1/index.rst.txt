:orphan:




XPEHH/CMS.GAS/2/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population
when compared with the :doc:`../../../../../population/GAS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **45,374,895** and
**45,454,895**.
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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP007326`,  :doc:`../../../../../gene/AGAP007327` (E74-like factor 1/2/4).



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007317`,  :doc:`../../../../../gene/AGAP007318`,  :doc:`../../../../../gene/AGAP007319`,  :doc:`../../../../../gene/AGAP007320`,  :doc:`../../../../../gene/AGAP007321`,  :doc:`../../../../../gene/AGAP007322`,  :doc:`../../../../../gene/AGAP007323`,  :doc:`../../../../../gene/AGAP007324`,  :doc:`../../../../../gene/AGAP007325`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 78
        # data points      = 783
        # variables        = 4
        chi-square         = 166.403
        reduced chi-square = 0.214
        Akaike info crit   = -1204.647
        Bayesian info crit = -1185.994
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.78192699 +/- 0.045636 (5.84%) (init= 3)
        sigma:       2.50903586 +/- 0.199956 (7.97%) (init= 0.5)
        skew:       -0.97418369 +/- 0.079434 (8.15%) (init= 0)
        baseline:    1.23808627 +/- 0.035658 (2.88%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.710 
        C(sigma, baseline)           = -0.589 
        C(sigma, skew)               =  0.306 
        C(amplitude, skew)           =  0.188 
        C(skew, baseline)            = -0.168 
        C(amplitude, sigma)          =  0.105 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 782
        # variables        = 1
        chi-square         = 230.297
        reduced chi-square = 0.295
        Akaike info crit   = -953.982
        Bayesian info crit = -949.321
    [[Variables]]
        c:   1.64947086 +/- 0.019418 (1.18%) (init= 1)



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


