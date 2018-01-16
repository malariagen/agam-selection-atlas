:orphan:




XPEHH/AOM.GWA/2/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **6,254,895** and
**6,434,895**.
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


The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP004940` (cAMP-dependent protein kinase regulator),  :doc:`../../../../../gene/AGAP004941`,  :doc:`../../../../../gene/AGAP004942` (poly(rC)-binding protein 2/3/4).



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004935`,  :doc:`../../../../../gene/AGAP004936`,  :doc:`../../../../../gene/AGAP004937`,  :doc:`../../../../../gene/AGAP004938` (zinc finger, DHHC-type containing 15).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 79
        # data points      = 401
        # variables        = 4
        chi-square         = 104.567
        reduced chi-square = 0.263
        Akaike info crit   = -530.996
        Bayesian info crit = -515.020
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.05316905 +/- 0.068428 (6.50%) (init= 3)
        sigma:       2.62320058 +/- 0.249441 (9.51%) (init= 0.5)
        skew:        0.99999973 +/- 0.385112 (38.51%) (init= 0)
        baseline:    1.75616941 +/- 0.050938 (2.90%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.667 
        C(sigma, baseline)           = -0.517 
        C(amplitude, skew)           =  0.180 
        C(sigma, skew)               =  0.153 
        C(skew, baseline)            = -0.131 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 400
        # variables        = 1
        chi-square         = 166.380
        reduced chi-square = 0.417
        Akaike info crit   = -348.876
        Bayesian info crit = -344.884
    [[Variables]]
        c:   2.30370099 +/- 0.032287 (1.40%) (init= 1)



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


