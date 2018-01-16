:orphan:




IHS/BFS/2/7
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **42,314,895** and
**42,454,895**.
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




The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP007086`:sup:`2` (Sodium channel protein),  :doc:`../../../../../gene/AGAP007087` (RpL41 - 60s ribosomal protein L41),  :doc:`../../../../../gene/AGAP007088` (peptidyl-prolyl cis-trans isomerase B (cyclophilin B)),  :doc:`../../../../../gene/AGAP007089`,  :doc:`../../../../../gene/AGAP007090`.




The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007082`:sup:`1` (NADH dehydrogenase (ubiquinone) Fe-S protein 4),  :doc:`../../../../../gene/AGAP007083`,  :doc:`../../../../../gene/AGAP007084`,  :doc:`../../../../../gene/AGAP007085`,  :doc:`../../../../../gene/AGAP007091` (netrin receptor DSCAM).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/7/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/7/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/7/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 46
        # data points      = 555
        # variables        = 4
        chi-square         = 73.704
        reduced chi-square = 0.134
        Akaike info crit   = -1112.493
        Bayesian info crit = -1095.217
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.44369855 +/- 0.097194 (6.73%) (init= 3)
        sigma:       0.19751117 +/- 0.017968 (9.10%) (init= 0.5)
        skew:       -0.99999698 +/- 0.111863 (11.19%) (init= 0)
        baseline:    1.81062054 +/- 0.016523 (0.91%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.539 
        C(amplitude, sigma)          = -0.472 
        C(sigma, baseline)           = -0.166 
        C(amplitude, baseline)       = -0.125 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 554
        # variables        = 1
        chi-square         = 110.630
        reduced chi-square = 0.200
        Akaike info crit   = -890.478
        Bayesian info crit = -886.161
    [[Variables]]
        c:   1.88824447 +/- 0.019002 (1.01%) (init= 1)



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


