:orphan:




XPEHH/GAS.BFS/3/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **17,960,000** and
**18,080,000**.
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


The following 8 genes overlap the focal region: :doc:`../../../../../gene/AGAP008799`,  :doc:`../../../../../gene/AGAP008800`,  :doc:`../../../../../gene/AGAP008801` (trafficking kinesin-binding protein 1),  :doc:`../../../../../gene/AGAP008802` (Pgk - Phosphoglycerate kinase),  :doc:`../../../../../gene/AGAP008803`,  :doc:`../../../../../gene/AGAP008804` (peroxin-19),  :doc:`../../../../../gene/AGAP008805` (ubiquitin carboxyl-terminal hydrolase 3),  :doc:`../../../../../gene/AGAP008806` (beta-1,3-glucuronyltransferase).



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008794`,  :doc:`../../../../../gene/AGAP008795`,  :doc:`../../../../../gene/AGAP008797` (Immunoglobulin (CD79A) binding protein 1),  :doc:`../../../../../gene/AGAP028220`,  :doc:`../../../../../gene/AGAP008796`,  :doc:`../../../../../gene/AGAP008798` (guanine nucleotide exchange factor MSS4),  :doc:`../../../../../gene/AGAP008807`,  :doc:`../../../../../gene/AGAP008808`,  :doc:`../../../../../gene/AGAP008810`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 575
        # variables        = 4
        chi-square         = 181.112
        reduced chi-square = 0.317
        Akaike info crit   = -656.271
        Bayesian info crit = -638.854
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.53049475 +/- 0.156452 (10.22%) (init= 3)
        decay:       0.29846944 +/- 0.056474 (18.92%) (init= 0.5)
        skew:        0.81601836 +/- 0.206534 (25.31%) (init= 0)
        baseline:    2.04459201 +/- 0.026652 (1.30%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.553 
        C(decay, skew)               = -0.421 
        C(decay, baseline)           = -0.308 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 574
        # variables        = 1
        chi-square         = 226.856
        reduced chi-square = 0.396
        Akaike info crit   = -530.852
        Bayesian info crit = -526.499
    [[Variables]]
        c:   2.15652311 +/- 0.026262 (1.22%) (init= 1)



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


