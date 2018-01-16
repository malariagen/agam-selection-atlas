:orphan:




XPEHH/BFM.BFS/3/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3L** between positions **33,259,316** and
**33,299,316**.
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


The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP011785` (CLIPE6 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011786` (CLIPE7 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011787` (CLIPA5 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011788` (CLIPA14 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011789` (CLIPA6 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011790` (CLIPA2 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011791` (CLIPA1 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP028725` (SPCLIP1 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011792` (CLIPA7 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011793` (CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011794` (CLIPA1 protein).



The following 17 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP011779`,  :doc:`../../../../../gene/AGAP011780` (CLIPA4 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011781` (CLIPA12 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011782` (CLIPE2 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011783` (CLIPA13 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP011784`,  :doc:`../../../../../gene/AGAP011795`,  :doc:`../../../../../gene/AGAP011796` (solute carrier family 29 (equilibrative nucleoside transporter), member 4),  :doc:`../../../../../gene/AGAP011797`,  :doc:`../../../../../gene/AGAP011798`:sup:`1` (acyl-CoA oxidase),  :doc:`../../../../../gene/AGAP011799` (Anaphase-promoting complex subunit 10),  :doc:`../../../../../gene/AGAP011800` (Transaldolase),  :doc:`../../../../../gene/AGAP011801` (Coiled-coil domain-containing protein 22 homolog),  :doc:`../../../../../gene/AGAP011802` (RpL39 - 60S ribosomal protein L39),  :doc:`../../../../../gene/AGAP011803` (mRpS27 - 28S ribosomal protein S27, mitochondrial),  :doc:`../../../../../gene/AGAP011804` (translation initiation factor 2D),  :doc:`../../../../../gene/AGAP011805` (ornithine decarboxylase).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 81
        # data points      = 555
        # variables        = 4
        chi-square         = 314.314
        reduced chi-square = 0.570
        Akaike info crit   = -307.559
        Bayesian info crit = -290.283
    [[Variables]]
        center:      0 (fixed)
        amplitude:   5.15347559 +/- 0.404434 (7.85%) (init= 3)
        decay:       0.15000001 +/- 0.038109 (25.41%) (init= 0.5)
        skew:       -0.36209189 +/- 0.126254 (34.87%) (init= 0)
        baseline:    1.79208015 +/- 0.033439 (1.87%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.678 
        C(decay, skew)               = -0.253 
        C(decay, baseline)           =  0.187 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 554
        # variables        = 1
        chi-square         = 406.635
        reduced chi-square = 0.735
        Akaike info crit   = -169.323
        Bayesian info crit = -165.006
    [[Variables]]
        c:   1.89620847 +/- 0.036432 (1.92%) (init= 1)



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


