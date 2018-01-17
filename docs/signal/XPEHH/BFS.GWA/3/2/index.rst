:orphan:




XPEHH/BFS.GWA/3/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3L** between positions **10,219,316** and
**10,379,316**.
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


The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP010778`,  :doc:`../../../../../gene/AGAP010779`,  :doc:`../../../../../gene/AGAP010780`,  :doc:`../../../../../gene/AGAP010781`,  :doc:`../../../../../gene/AGAP010782` (Ral guanine nucleotide exchange factor 2),  :doc:`../../../../../gene/AGAP010783`,  :doc:`../../../../../gene/AGAP010784` (dolichyl-phosphate-mannose-protein mannosyltransferase),  :doc:`../../../../../gene/AGAP010785` (fatty acyl CoA reductase 2),  :doc:`../../../../../gene/AGAP010786`,  :doc:`../../../../../gene/AGAP010787` (timeless),  :doc:`../../../../../gene/AGAP010788` (fatty acyl-CoA reductase 1).



The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010776`,  :doc:`../../../../../gene/AGAP010777` (hunchback),  :doc:`../../../../../gene/AGAP010789`,  :doc:`../../../../../gene/AGAP010790` (dynein heavy chain 2, cytosolic),  :doc:`../../../../../gene/AGAP010791` (polyribonucleotide nucleotidyltransferase),  :doc:`../../../../../gene/AGAP010792` (NADH dehydrogenase (ubiquinone) 1 alpha subcomplex 9),  :doc:`../../../../../gene/AGAP010793` (synembryn-A).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 49
        # data points      = 381
        # variables        = 4
        chi-square         = 388.206
        reduced chi-square = 1.030
        Akaike info crit   = 15.139
        Bayesian info crit = 30.910
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.21037256 +/- 0.194148 (8.78%) (init= 3)
        decay:       2.99999999 +/- 0.073092 (2.44%) (init= 0.5)
        skew:        0.57144202 +/- 0.130364 (22.81%) (init= 0)
        baseline:    3.34811371 +/- 0.166796 (4.98%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           =  0.860 
        C(amplitude, baseline)       = -0.512 
        C(skew, baseline)            =  0.305 
        C(decay, skew)               =  0.243 
        C(amplitude, skew)           = -0.241 
        C(amplitude, decay)          = -0.129 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 13
        # data points      = 380
        # variables        = 1
        chi-square         = 515.978
        reduced chi-square = 1.361
        Akaike info crit   = 118.239
        Bayesian info crit = 122.179
    [[Variables]]
        c:   4.10677566 +/- 0.059855 (1.46%) (init= 1)



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


