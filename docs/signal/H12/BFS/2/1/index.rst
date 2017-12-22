:orphan:




H12 / Burkina Faso *An. gambiae* / Chromosome 2 / #1
====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **2,420,001** and
**2,720,000**.
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




The following 13 genes overlap the focal region: :doc:`../../../../../gene/AGAP004707`:sup:`2` (para - voltage-gated sodium channel),  :doc:`../../../../../gene/AGAP004708` (arginyl-tRNA synthetase),  :doc:`../../../../../gene/AGAP004709` (mRpL18 - 39S ribosomal protein L18, mitochondrial),  :doc:`../../../../../gene/AGAP004710`:sup:`1` (ubiquinol-cytochrome c reductase subunit 9),  :doc:`../../../../../gene/AGAP004711` (ATP-dependent RNA helicase DDX41),  :doc:`../../../../../gene/AGAP004712`,  :doc:`../../../../../gene/AGAP004713`,  :doc:`../../../../../gene/AGAP004714`,  :doc:`../../../../../gene/AGAP004715`:sup:`1` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`../../../../../gene/AGAP004716`:sup:`3` (Gr57 - gustatory receptor 57),  :doc:`../../../../../gene/AGAP004717`,  :doc:`../../../../../gene/AGAP004718`,  :doc:`../../../../../gene/AGAP004719` (CLIPC9 - CLIP-domain serine protease).




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004720`,  :doc:`../../../../../gene/AGAP004721` (N-acetylglucosamine-6-sulfatase),  :doc:`../../../../../gene/AGAP004722`,  :doc:`../../../../../gene/AGAP004723` (chromobox protein homolog 1).


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
    <img src="../../../../../_static/data/signal/H12/BFS/2/1/peak_context.png"/>
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

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 75
        # data points      = 310
        # variables        = 3
        chi-square         = 3.287
        reduced chi-square = 0.011
        Akaike info crit   = -1403.479
        Bayesian info crit = -1392.269
    [[Variables]]
        amplitude:   1.26033111 +/- 0.037991 (3.01%) (init= 0.5)
        decay:       1.15507536 +/- 0.067225 (5.82%) (init= 0.5)
        c:           0.05163914 +/- 0.015908 (30.81%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.797 
        C(amplitude, decay)          = -0.628 
        C(amplitude, c)              =  0.141 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 50
        # data points      = 179
        # variables        = 3
        chi-square         = 0.342
        reduced chi-square = 0.002
        Akaike info crit   = -1114.752
        Bayesian info crit = -1105.190
    [[Variables]]
        amplitude:   0.96862431 +/- 0.010744 (1.11%) (init= 0.5)
        decay:       1.31892343 +/- 0.040764 (3.09%) (init= 0.5)
        c:           0.02932022 +/- 0.006776 (23.11%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.773 
        C(amplitude, c)              = -0.327 
        C(amplitude, decay)          = -0.101 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 308
        # variables        = 1
        chi-square         = 29.218
        reduced chi-square = 0.095
        Akaike info crit   = -723.440
        Bayesian info crit = -719.710
    [[Variables]]
        c:   0.41346148 +/- 0.017578 (4.25%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 178
        # variables        = 1
        chi-square         = 15.796
        reduced chi-square = 0.089
        Akaike info crit   = -429.123
        Bayesian info crit = -425.941
    [[Variables]]
        c:   0.27525521 +/- 0.022391 (8.13%) (init= 0.03)


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


