:orphan:




H12 / Burkina Faso *An. coluzzii* / Chromosome 2 / #1
=====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **2,520,001** and
**2,900,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 20 genes overlap the focal region: :doc:`../../../../../gene/AGAP004713`,  :doc:`../../../../../gene/AGAP004714`,  :doc:`../../../../../gene/AGAP004715`:sup:`1` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`../../../../../gene/AGAP004716`:sup:`3` (Gr57 - gustatory receptor 57),  :doc:`../../../../../gene/AGAP004717`,  :doc:`../../../../../gene/AGAP004718`,  :doc:`../../../../../gene/AGAP004719` (CLIPC9 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP004720`,  :doc:`../../../../../gene/AGAP004721` (N-acetylglucosamine-6-sulfatase),  :doc:`../../../../../gene/AGAP004722`,  :doc:`../../../../../gene/AGAP004723` (chromobox protein homolog 1),  :doc:`../../../../../gene/AGAP004724` (Intraflagellar transport 74 homolog),  :doc:`../../../../../gene/AGAP004725` (eIF3c - Eukaryotic translation initiation factor 3 subunit C),  :doc:`../../../../../gene/AGAP004726` (Uncharacterized protein CG3556),  :doc:`../../../../../gene/AGAP004727`:sup:`3` (Gr25 - gustatory receptor 25),  :doc:`../../../../../gene/AGAP004728`,  :doc:`../../../../../gene/AGAP004729`,  :doc:`../../../../../gene/AGAP004730` (phospholipase A2, venom),  :doc:`../../../../../gene/AGAP004731` (secretory phospholipase A2),  :doc:`../../../../../gene/AGAP029113`.




The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004708` (arginyl-tRNA synthetase),  :doc:`../../../../../gene/AGAP004709` (mRpL18 - 39S ribosomal protein L18, mitochondrial),  :doc:`../../../../../gene/AGAP004710`:sup:`1` (ubiquinol-cytochrome c reductase subunit 9),  :doc:`../../../../../gene/AGAP004711` (ATP-dependent RNA helicase DDX41),  :doc:`../../../../../gene/AGAP004712`,  :doc:`../../../../../gene/AGAP004733`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/BFS/2/1/index`, "2L:2,420,001-2,720,000", 1365 (680 | 685)
    :doc:`../../../../../signal/H12/GNS/2/1/index`, "2L:1,760,001-2,700,000", 1256 (673 | 583)
    :doc:`../../../../../signal/H12/UGS/2/2/index`, "2L:2,520,001-3,120,000", 982 (573 | 409)
    :doc:`../../../../../signal/H12/CMS/2/2/index`, "2L:2,420,001-2,920,000", 566 (461 | 104)
    :doc:`../../../../../signal/H12/GAS/2/2/index`, "2L:2,600,001-2,640,000", 274 (223 | 51)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/1/peak_context.png"/>
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

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 325
        # variables        = 3
        chi-square         = 1.799
        reduced chi-square = 0.006
        Akaike info crit   = -1682.821
        Bayesian info crit = -1671.470
    [[Variables]]
        amplitude:   0.89089290 +/- 0.015062 (1.69%) (init= 0.5)
        decay:       1.30548182 +/- 0.057172 (4.38%) (init= 0.5)
        c:           2.1891e-08 +/- 0.011677 (53345783.94%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.828 
        C(amplitude, c)              = -0.414 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 164
        # variables        = 3
        chi-square         = 0.076
        reduced chi-square = 0.000
        Akaike info crit   = -1253.243
        Bayesian info crit = -1243.944
    [[Variables]]
        amplitude:   0.96587632 +/- 0.016018 (1.66%) (init= 0.5)
        decay:       0.36840229 +/- 0.008741 (2.37%) (init= 0.5)
        c:           0.02685048 +/- 0.001924 (7.17%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.706 
        C(decay, c)                  = -0.355 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 323
        # variables        = 1
        chi-square         = 20.902
        reduced chi-square = 0.065
        Akaike info crit   = -882.305
        Bayesian info crit = -878.528
    [[Variables]]
        c:   0.29555444 +/- 0.014176 (4.80%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 163
        # variables        = 1
        chi-square         = 2.915
        reduced chi-square = 0.018
        Akaike info crit   = -653.909
        Bayesian info crit = -650.815
    [[Variables]]
        c:   0.07354618 +/- 0.010506 (14.29%) (init= 0.03)


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


