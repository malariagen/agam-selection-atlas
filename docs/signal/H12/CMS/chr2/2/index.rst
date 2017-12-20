:orphan:

Cameroon *An. gambiae* | H12 | Chromosome 2 | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/CMS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **2,460,001** and
**2,960,000**.




The following 26 genes overlap the focal region: :doc:`/gene/AGAP004708` (arginyl-tRNA synthetase),  :doc:`/gene/AGAP004709` (mRpL18 - 39S ribosomal protein L18, mitochondrial),  :doc:`/gene/AGAP004710` (ubiquinol-cytochrome c reductase subunit 9),  :doc:`/gene/AGAP004711` (ATP-dependent RNA helicase DDX41),  :doc:`/gene/AGAP004712`,  :doc:`/gene/AGAP004713`,  :doc:`/gene/AGAP004714`,  :doc:`/gene/AGAP004715` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`/gene/AGAP004716` (Gr57 - gustatory receptor 57),  :doc:`/gene/AGAP004717`,  :doc:`/gene/AGAP004718`,  :doc:`/gene/AGAP004719` (CLIPC9 - CLIP-domain serine protease),  :doc:`/gene/AGAP004720`,  :doc:`/gene/AGAP004721` (N-acetylglucosamine-6-sulfatase),  :doc:`/gene/AGAP004722`,  :doc:`/gene/AGAP004723` (chromobox protein homolog 1),  :doc:`/gene/AGAP004724` (Intraflagellar transport 74 homolog),  :doc:`/gene/AGAP004725` (eIF3c - Eukaryotic translation initiation factor 3 subunit C),  :doc:`/gene/AGAP004726` (Uncharacterized protein CG3556),  :doc:`/gene/AGAP004727` (Gr25 - gustatory receptor 25),  :doc:`/gene/AGAP004728`,  :doc:`/gene/AGAP004729`,  :doc:`/gene/AGAP004730` (phospholipase A2, venom),  :doc:`/gene/AGAP004731` (secretory phospholipase A2),  :doc:`/gene/AGAP029113`,  :doc:`/gene/AGAP004733`.




The following 9 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP004707` (para - voltage-gated sodium channel),  :doc:`/gene/AGAP004735`,  :doc:`/gene/AGAP004736` (mitochondrial GTPase 1 homolog),  :doc:`/gene/AGAP004737` (Rhomboid-4, isoform B),  :doc:`/gene/AGAP004738` (IK cytokine),  :doc:`/gene/AGAP004739` (H/ACA ribonucleoprotein complex subunit 4),  :doc:`/gene/AGAP004740`,  :doc:`/gene/AGAP004741` (serine proteinase),  :doc:`/gene/AGAP004742` (Pyruvate carboxylase).


.. figure:: peak_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`/signal/H12/BFM/chr2/1/index`,"2L:2,500,001-2,900,000",1736
    :doc:`/signal/H12/BFS/chr2/1/index`,"2L:2,420,001-2,720,000",1728
    :doc:`/signal/H12/GNS/chr2/1/index`,"2L:1,720,001-2,700,000",1554
    :doc:`/signal/H12/UGS/chr2/2/index`,"2L:1,940,001-3,080,000",1332
    :doc:`/signal/H12/GAS/chr2/2/index`,"2L:2,600,001-2,640,000",321
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. figure:: peak_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: peak_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: peak_fit.png

    **Figure 4**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 106
        # data points      = 371
        # variables        = 3
        chi-square         = 0.242
        reduced chi-square = 0.001
        Akaike info crit   = -2715.166
        Bayesian info crit = -2703.417
    [[Variables]]
        amplitude:   0.15582893 +/- 0.004985 (3.20%) (init= 0.5)
        decay:       1.24593468 +/- 0.087706 (7.04%) (init= 0.5)
        c:           0.05999999 +/- 0.000801 (1.33%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.719 
        C(amplitude, decay)          = -0.290 
        C(amplitude, c)              =  0.266 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 61
        # data points      = 218
        # variables        = 3
        chi-square         = 0.192
        reduced chi-square = 0.001
        Akaike info crit   = -1527.145
        Bayesian info crit = -1516.992
    [[Variables]]
        amplitude:   0.15716046 +/- 0.008633 (5.49%) (init= 0.5)
        decay:       3          +/- 1.98e-05 (0.00%) (init= 0.5)
        c:           0.04211455 +/- 0.009337 (22.17%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.932 
        C(amplitude, c)              = -0.659 
        C(amplitude, decay)          = -0.425 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 370
        # variables        = 1
        chi-square         = 0.733
        reduced chi-square = 0.002
        Akaike info crit   = -2301.149
        Bayesian info crit = -2297.236
    [[Variables]]
        c:   0.10924940 +/- 0.002316 (2.12%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 217
        # variables        = 1
        chi-square         = 0.525
        reduced chi-square = 0.002
        Akaike info crit   = -1305.441
        Bayesian info crit = -1302.062
    [[Variables]]
        c:   0.09577581 +/- 0.003345 (3.49%) (init= 0.03)


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
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
