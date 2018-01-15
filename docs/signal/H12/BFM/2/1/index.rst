:orphan:




H12/BFM/2/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **2,474,895** and
**2,894,895**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

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




The following 23 genes overlap the focal region: :doc:`../../../../../gene/AGAP004709` (mRpL18 - 39S ribosomal protein L18, mitochondrial),  :doc:`../../../../../gene/AGAP004710`:sup:`1` (ubiquinol-cytochrome c reductase subunit 9),  :doc:`../../../../../gene/AGAP004711` (ATP-dependent RNA helicase DDX41),  :doc:`../../../../../gene/AGAP004712`,  :doc:`../../../../../gene/AGAP004713`,  :doc:`../../../../../gene/AGAP004714`,  :doc:`../../../../../gene/AGAP004715`:sup:`1` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`../../../../../gene/AGAP004716`:sup:`3` (Gr57 - gustatory receptor 57),  :doc:`../../../../../gene/AGAP004717`,  :doc:`../../../../../gene/AGAP004718`,  :doc:`../../../../../gene/AGAP004719` (CLIPC9 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP004720`,  :doc:`../../../../../gene/AGAP004721` (N-acetylglucosamine-6-sulfatase),  :doc:`../../../../../gene/AGAP004722`,  :doc:`../../../../../gene/AGAP004723` (chromobox protein homolog 1),  :doc:`../../../../../gene/AGAP004724` (Intraflagellar transport 74 homolog),  :doc:`../../../../../gene/AGAP004725` (eIF3c - Eukaryotic translation initiation factor 3 subunit C),  :doc:`../../../../../gene/AGAP004726` (Uncharacterized protein CG3556),  :doc:`../../../../../gene/AGAP004727`:sup:`3` (Gr25 - gustatory receptor 25),  :doc:`../../../../../gene/AGAP004728`,  :doc:`../../../../../gene/AGAP004729`,  :doc:`../../../../../gene/AGAP004730` (phospholipase A2, venom),  :doc:`../../../../../gene/AGAP004731` (secretory phospholipase A2).




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004707`:sup:`2` (para - voltage-gated sodium channel),  :doc:`../../../../../gene/AGAP004708` (arginyl-tRNA synthetase),  :doc:`../../../../../gene/AGAP029113`,  :doc:`../../../../../gene/AGAP004733`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

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
      - Peak Model :math:`\Delta_{i}`
      - Max Percentile
    * - :doc:`../../../../../signal/H12/BFS/2/1/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2L:1,454,895-2,694,895
      - 1,776
      - 100.0%
    * - :doc:`../../../../../signal/H12/GNS/2/1/index`
      - H12
      - Guinea *An. gambiae*
      - 2L:1,294,895-2,474,895
      - 1,685
      - 100.0%
    * - :doc:`../../../../../signal/H12/UGS/2/2/index`
      - H12
      - Uganda *An. gambiae*
      - 2L:1,814,895-3,094,895
      - 1,377
      - 100.0%
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/2/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2L:2,234,895-3,274,895
      - 938
      - 99.6%
    * - :doc:`../../../../../signal/H12/GAS/2/2/index`
      - H12
      - Gabon *An. gambiae*
      - 2L:2,734,895-3,094,895
      - 325
      - 99.8%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 589
        # variables        = 4
        chi-square         = 1.556
        reduced chi-square = 0.003
        Akaike info crit   = -3488.597
        Bayesian info crit = -3471.083
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.70373937 +/- 0.006883 (0.98%) (init= 0.5)
        sigma:       0.55230238 +/- 0.010639 (1.93%) (init= 0.5)
        skew:        0.93081982 +/- 0.025047 (2.69%) (init= 0)
        baseline:    0.03793625 +/- 0.002807 (7.40%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               = -0.764 
        C(amplitude, baseline)       = -0.308 
        C(sigma, baseline)           = -0.279 
        C(amplitude, sigma)          = -0.228 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 588
        # variables        = 1
        chi-square         = 33.188
        reduced chi-square = 0.057
        Akaike info crit   = -1688.228
        Bayesian info crit = -1683.851
    [[Variables]]
        c:   0.19033277 +/- 0.009805 (5.15%) (init= 0.03)



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


