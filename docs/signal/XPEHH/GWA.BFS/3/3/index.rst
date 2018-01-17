:orphan:




XPEHH/GWA.BFS/3/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3L** between positions **37,959,316** and
**37,999,316**.
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


The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP012131`,  :doc:`../../../../../gene/AGAP028721`,  :doc:`../../../../../gene/AGAP012132`,  :doc:`../../../../../gene/AGAP028746`,  :doc:`../../../../../gene/AGAP028747`,  :doc:`../../../../../gene/AGAP028748`,  :doc:`../../../../../gene/AGAP028751`,  :doc:`../../../../../gene/AGAP028750`,  :doc:`../../../../../gene/AGAP028749`,  :doc:`../../../../../gene/AGAP012134` (HIV-1 Vpr-binding protein).



The following 17 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP012125` (ribonuclease P/MRP protein subunit POP1),  :doc:`../../../../../gene/AGAP012126` (lysophospholipase II),  :doc:`../../../../../gene/AGAP012127` (F-box protein 25/32),  :doc:`../../../../../gene/AGAP012128`,  :doc:`../../../../../gene/AGAP012129` (dimethyladenosine transferase 1, mitochondrial),  :doc:`../../../../../gene/AGAP012130` (ATN - allatotropin),  :doc:`../../../../../gene/AGAP012135` (26S proteasome regulatory subunit N8),  :doc:`../../../../../gene/AGAP012136` (mRpS25 - 28S ribosomal protein S25, mitochondrial),  :doc:`../../../../../gene/AGAP012137` (RNA binding motif protein 18),  :doc:`../../../../../gene/AGAP012138` (RpL21 - 60S ribosomal protein L21),  :doc:`../../../../../gene/AGAP012139` (ubiquitin carboxyl-terminal hydrolase 12/46),  :doc:`../../../../../gene/AGAP012140` (eIF3b - Eukaryotic translation initiation factor 3 subunit B),  :doc:`../../../../../gene/AGAP012141` (ankyrin repeat-rich membrane spanning protein),  :doc:`../../../../../gene/AGAP012142` (U4/U6 small nuclear ribonucleoprotein Prp31),  :doc:`../../../../../gene/AGAP012143` (mTERF domain-containing protein, mitochondrial),  :doc:`../../../../../gene/AGAP012144` (endoplasmic reticulum-Golgi intermediate compartment protein 3),  :doc:`../../../../../gene/AGAP012145` (Reactive oxygen species modulator 1).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 50
        # data points      = 607
        # variables        = 4
        chi-square         = 198.633
        reduced chi-square = 0.329
        Akaike info crit   = -670.062
        Bayesian info crit = -652.428
    [[Variables]]
        center:      0 (fixed)
        amplitude:   3.44827114 +/- 0.303411 (8.80%) (init= 3)
        decay:       0.15000000 +/- 0.004013 (2.68%) (init= 0.5)
        skew:       -0.52974027 +/- 0.155676 (29.39%) (init= 0)
        baseline:    2.11514185 +/- 0.024211 (1.14%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.644 
        C(decay, skew)               = -0.312 
        C(decay, baseline)           =  0.187 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 606
        # variables        = 1
        chi-square         = 253.007
        reduced chi-square = 0.418
        Akaike info crit   = -527.317
        Bayesian info crit = -522.910
    [[Variables]]
        c:   2.17965306 +/- 0.026269 (1.21%) (init= 1)



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


