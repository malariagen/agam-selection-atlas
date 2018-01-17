:orphan:




H12/BFS/2/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **1,454,895** and
**2,694,895**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).


This signal overlaps the :doc:`../../../../../known-locus/vgsc`, a genome
region with prior evidence of an association with insecticide resistance and/or recent positive selection in
*Anopheles* mosquitoes.




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


The following 28 genes overlap the focal region: :doc:`../../../../../gene/AGAP004693` (nuclear receptor subfamily 6 group A),  :doc:`../../../../../gene/AGAP004694`,  :doc:`../../../../../gene/AGAP028434`,  :doc:`../../../../../gene/AGAP028435`,  :doc:`../../../../../gene/AGAP004695` (ESCRT-I complex subunit MVB12),  :doc:`../../../../../gene/AGAP004696` (exd - Homeobox protein extradenticle),  :doc:`../../../../../gene/AGAP004698` (pre-mRNA-splicing factor 38B),  :doc:`../../../../../gene/AGAP004699` (RAF proto-oncogene serine/threonine-protein kinase),  :doc:`../../../../../gene/AGAP004700`,  :doc:`../../../../../gene/AGAP004701`,  :doc:`../../../../../gene/AGAP028436`,  :doc:`../../../../../gene/AGAP004702`,  :doc:`../../../../../gene/AGAP004703` (DNA-directed RNA polymerase III subunit RPC1),  :doc:`../../../../../gene/AGAP004704` (COMPASS component SPP1),  :doc:`../../../../../gene/AGAP028437`,  :doc:`../../../../../gene/AGAP004706`,  :doc:`../../../../../gene/AGAP004707`:sup:`2` (para - voltage-gated sodium channel),  :doc:`../../../../../gene/AGAP004708` (arginyl-tRNA synthetase),  :doc:`../../../../../gene/AGAP004709` (mRpL18 - 39S ribosomal protein L18, mitochondrial),  :doc:`../../../../../gene/AGAP004710`:sup:`1` (ubiquinol-cytochrome c reductase subunit 9),  :doc:`../../../../../gene/AGAP004711` (ATP-dependent RNA helicase DDX41),  :doc:`../../../../../gene/AGAP004712`,  :doc:`../../../../../gene/AGAP004713`,  :doc:`../../../../../gene/AGAP004714`,  :doc:`../../../../../gene/AGAP004715`:sup:`1` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`../../../../../gene/AGAP004716`:sup:`3` (Gr57 - gustatory receptor 57),  :doc:`../../../../../gene/AGAP004717`,  :doc:`../../../../../gene/AGAP004718`.



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004692`,  :doc:`../../../../../gene/AGAP004719` (CLIPC9 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP004720`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping selection signals
-----------------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. list-table::
    :widths: auto
    :header-rows: 1

    * - Signal
      - Statistic
      - Population
      - Focus
      - Peak model :math:`\Delta_{i}`
      - Max. percentile
      - Known locus
    * - :doc:`../../../../../signal/H12/BFM/2/1/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 2L:2,474,895-2,894,895
      - 1,800
      - 99.9%
      - Vgsc
    * - :doc:`../../../../../signal/H12/GNS/2/1/index`
      - H12
      - Guinea *An. gambiae*
      - 2L:1,294,895-2,474,895
      - 1,685
      - 100.0%
      - Vgsc
    * - :doc:`../../../../../signal/H12/UGS/2/2/index`
      - H12
      - Uganda *An. gambiae*
      - 2L:1,814,895-3,094,895
      - 1,377
      - 100.0%
      - Vgsc
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/2/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2L:2,234,895-3,274,895
      - 938
      - 99.6%
      - Vgsc
    * - :doc:`../../../../../signal/XPEHH/BFM.GWA/2/1/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - 2L:2,334,895-2,974,895
      - 917
      - 99.8%
      - Vgsc
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 589
        # variables        = 4
        chi-square         = 2.703
        reduced chi-square = 0.005
        Akaike info crit   = -3163.177
        Bayesian info crit = -3145.664
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.80805837 +/- 0.007684 (0.95%) (init= 0.5)
        sigma:       1.04187069 +/- 0.014929 (1.43%) (init= 0.5)
        skew:       -0.09618051 +/- 0.016393 (17.04%) (init= 0)
        baseline:    0.08112295 +/- 0.004035 (4.98%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.442 
        C(amplitude, baseline)       = -0.438 
        C(sigma, skew)               = -0.403 
        C(amplitude, sigma)          = -0.184 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 588
        # variables        = 1
        chi-square         = 55.413
        reduced chi-square = 0.094
        Akaike info crit   = -1386.804
        Bayesian info crit = -1382.427
    [[Variables]]
        c:   0.31464645 +/- 0.012669 (4.03%) (init= 0.03)



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


