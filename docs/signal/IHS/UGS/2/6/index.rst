:orphan:




IHS/UGS/2/6
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **43,554,895** and
**43,674,895**.
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


The following 27 genes overlap the focal region: :doc:`../../../../../gene/AGAP007138` (Wurst),  :doc:`../../../../../gene/AGAP007139` (Ser/Thr protein phosphatase/nucleotidase),  :doc:`../../../../../gene/AGAP007140` (Ser/Thr protein phosphatase/nucleotidase),  :doc:`../../../../../gene/AGAP007141` (Serine-type enodpeptidase),  :doc:`../../../../../gene/AGAP007142` (Serine-type enodpeptidase),  :doc:`../../../../../gene/AGAP007143`,  :doc:`../../../../../gene/AGAP007144`,  :doc:`../../../../../gene/AGAP007145`,  :doc:`../../../../../gene/AGAP007146`,  :doc:`../../../../../gene/AGAP007147` (exosome complex protein LRP1),  :doc:`../../../../../gene/AGAP007148`,  :doc:`../../../../../gene/AGAP007149`,  :doc:`../../../../../gene/AGAP007150`,  :doc:`../../../../../gene/AGAP007151`,  :doc:`../../../../../gene/AGAP007152`,  :doc:`../../../../../gene/AGAP007153`,  :doc:`../../../../../gene/AGAP007154`,  :doc:`../../../../../gene/AGAP007155`,  :doc:`../../../../../gene/AGAP007156`,  :doc:`../../../../../gene/AGAP007157` (RpS27 - 40S ribosomal protein S27),  :doc:`../../../../../gene/AGAP007158` (alpha-crystallin B chain),  :doc:`../../../../../gene/AGAP007159` (alpha-crystallin B chain),  :doc:`../../../../../gene/AGAP007160` (alpha-crystallin chain B),  :doc:`../../../../../gene/AGAP007161` (alpha-crystallin chain A),  :doc:`../../../../../gene/AGAP007162` (alpha-crystallin chain A),  :doc:`../../../../../gene/AGAP007163` (3',5'-cyclic-nucleotide phosphodiesterase),  :doc:`../../../../../gene/AGAP007164`.



Gene :doc:`../../../../../gene/AGAP007137` is within 50 kbp of the focal region.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/6/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 56
        # data points      = 645
        # variables        = 4
        chi-square         = 97.046
        reduced chi-square = 0.151
        Akaike info crit   = -1213.674
        Bayesian info crit = -1195.797
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.32361556 +/- 0.121481 (9.18%) (init= 3)
        sigma:       0.15000023 +/- 0.017519 (11.68%) (init= 0.5)
        skew:       -0.72177138 +/- 0.140558 (19.47%) (init= 0)
        baseline:    1.88447134 +/- 0.015867 (0.84%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.518 
        C(sigma, skew)               =  0.352 
        C(sigma, baseline)           = -0.137 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 644
        # variables        = 1
        chi-square         = 117.228
        reduced chi-square = 0.182
        Akaike info crit   = -1095.104
        Bayesian info crit = -1090.636
    [[Variables]]
        c:   1.92533379 +/- 0.016825 (0.87%) (init= 1)



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


