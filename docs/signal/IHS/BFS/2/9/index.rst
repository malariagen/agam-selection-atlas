:orphan:




IHS/BFS/2/9
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **39,020,000** and
**39,140,000**.
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




The following 14 genes overlap the focal region: :doc:`../../../../../gene/AGAP003512`,  :doc:`../../../../../gene/AGAP003513`,  :doc:`../../../../../gene/AGAP003514`,  :doc:`../../../../../gene/AGAP003515`:sup:`1` (NIT8537),  :doc:`../../../../../gene/AGAP013231` (Nitrilase homolog 2),  :doc:`../../../../../gene/AGAP003516`:sup:`1` (NIT8492),  :doc:`../../../../../gene/AGAP003517` (phenylalanyl-tRNA synthetase beta chain),  :doc:`../../../../../gene/AGAP003519` (ankyrin repeat domain-containing protein 17),  :doc:`../../../../../gene/AGAP003521` (alpha-2-macroglobulin receptor-associated protein),  :doc:`../../../../../gene/AGAP012974`,  :doc:`../../../../../gene/AGAP003522`:sup:`1` (CYP329A1 - cytochrome P450),  :doc:`../../../../../gene/AGAP003523`:sup:`1` (hypoxia-inducible factor prolyl hydroxylase),  :doc:`../../../../../gene/AGAP003524` (transcription initiation factor TFIID subunit 5),  :doc:`../../../../../gene/AGAP003525` (CCR4-NOT transcription complex, subunit 2).




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003509` (Complexin, isoform V),  :doc:`../../../../../gene/AGAP003526` (asterless),  :doc:`../../../../../gene/AGAP003527` (O-phospho-L-seryl-tRNASec:L-selenocysteinyl-tRNA synthase).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/9/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/9/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/9/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 57
        # data points      = 572
        # variables        = 4
        chi-square         = 141.482
        reduced chi-square = 0.249
        Akaike info crit   = -791.064
        Bayesian info crit = -773.668
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.97598408 +/- 0.096930 (9.93%) (init= 3)
        sigma:       0.53561296 +/- 0.063152 (11.79%) (init= 0.5)
        skew:        0.43784971 +/- 0.133871 (30.57%) (init= 0)
        baseline:    1.95957883 +/- 0.023378 (1.19%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.499 
        C(sigma, baseline)           = -0.266 
        C(amplitude, baseline)       = -0.182 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 571
        # variables        = 1
        chi-square         = 170.938
        reduced chi-square = 0.300
        Akaike info crit   = -686.675
        Bayesian info crit = -682.328
    [[Variables]]
        c:   2.05485445 +/- 0.022917 (1.12%) (init= 1)



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


