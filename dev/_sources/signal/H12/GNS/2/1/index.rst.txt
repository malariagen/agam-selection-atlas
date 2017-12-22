:orphan:




H12 / Guinea *An. gambiae* / Chromosome 2 / #1
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **1,760,001** and
**2,700,000**.
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




The following 25 genes overlap the focal region: :doc:`../../../../../gene/AGAP028435`,  :doc:`../../../../../gene/AGAP004695` (ESCRT-I complex subunit MVB12),  :doc:`../../../../../gene/AGAP004696` (exd - Homeobox protein extradenticle),  :doc:`../../../../../gene/AGAP004698` (pre-mRNA-splicing factor 38B),  :doc:`../../../../../gene/AGAP004699` (RAF proto-oncogene serine/threonine-protein kinase),  :doc:`../../../../../gene/AGAP004700`,  :doc:`../../../../../gene/AGAP004701`,  :doc:`../../../../../gene/AGAP028436`,  :doc:`../../../../../gene/AGAP004702`,  :doc:`../../../../../gene/AGAP004703` (DNA-directed RNA polymerase III subunit RPC1),  :doc:`../../../../../gene/AGAP004704` (COMPASS component SPP1),  :doc:`../../../../../gene/AGAP028437`,  :doc:`../../../../../gene/AGAP004706`,  :doc:`../../../../../gene/AGAP004707`:sup:`2` (para - voltage-gated sodium channel),  :doc:`../../../../../gene/AGAP004708` (arginyl-tRNA synthetase),  :doc:`../../../../../gene/AGAP004709` (mRpL18 - 39S ribosomal protein L18, mitochondrial),  :doc:`../../../../../gene/AGAP004710`:sup:`1` (ubiquinol-cytochrome c reductase subunit 9),  :doc:`../../../../../gene/AGAP004711` (ATP-dependent RNA helicase DDX41),  :doc:`../../../../../gene/AGAP004712`,  :doc:`../../../../../gene/AGAP004713`,  :doc:`../../../../../gene/AGAP004714`,  :doc:`../../../../../gene/AGAP004715`:sup:`1` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`../../../../../gene/AGAP004716`:sup:`3` (Gr57 - gustatory receptor 57),  :doc:`../../../../../gene/AGAP004717`,  :doc:`../../../../../gene/AGAP004718`.




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004719` (CLIPC9 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP004720`,  :doc:`../../../../../gene/AGAP004721` (N-acetylglucosamine-6-sulfatase).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have an focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/BFM/2/1/index`, "2L:2,520,001-2,900,000", 1399 (800 | 599)
    :doc:`../../../../../signal/H12/BFS/2/1/index`, "2L:2,420,001-2,720,000", 1365 (680 | 685)
    :doc:`../../../../../signal/H12/UGS/2/2/index`, "2L:2,520,001-3,120,000", 982 (573 | 409)
    :doc:`../../../../../signal/H12/CMS/2/2/index`, "2L:2,420,001-2,920,000", 566 (461 | 104)
    :doc:`../../../../../signal/H12/GAS/2/2/index`, "2L:2,600,001-2,640,000", 274 (223 | 51)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 144
        # data points      = 310
        # variables        = 3
        chi-square         = 3.384
        reduced chi-square = 0.011
        Akaike info crit   = -1394.419
        Bayesian info crit = -1383.210
    [[Variables]]
        amplitude:   1.47883312 +/- 0.058806 (3.98%) (init= 0.5)
        decay:       0.94720432 +/- 0.054588 (5.76%) (init= 0.5)
        c:           0.05999999 +/- 0.022960 (38.27%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.788 
        C(decay, c)                  =  0.758 
        C(amplitude, c)              = -0.308 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 59
        # data points      = 179
        # variables        = 3
        chi-square         = 0.477
        reduced chi-square = 0.003
        Akaike info crit   = -1054.956
        Bayesian info crit = -1045.394
    [[Variables]]
        amplitude:   0.89482007 +/- 0.012836 (1.43%) (init= 0.5)
        decay:       1.24021888 +/- 0.048271 (3.89%) (init= 0.5)
        c:           0.05999999 +/- 0.007524 (12.54%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.748 
        C(amplitude, c)              = -0.303 
        C(amplitude, decay)          = -0.146 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 305
        # variables        = 1
        chi-square         = 28.489
        reduced chi-square = 0.094
        Akaike info crit   = -721.092
        Bayesian info crit = -717.372
    [[Variables]]
        c:   0.40071818 +/- 0.017528 (4.37%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 176
        # variables        = 1
        chi-square         = 11.947
        reduced chi-square = 0.068
        Akaike info crit   = -471.448
        Bayesian info crit = -468.277
    [[Variables]]
        c:   0.27741581 +/- 0.019694 (7.10%) (init= 0.03)


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


