:orphan:




H12 / Cameroon *An. gambiae* / Chromosome 2 / #2
================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **2,420,001** and
**2,920,000**.
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




The following 27 genes overlap the focal region: :doc:`../../../../../gene/AGAP004707`:sup:`2` (para - voltage-gated sodium channel),  :doc:`../../../../../gene/AGAP004708` (arginyl-tRNA synthetase),  :doc:`../../../../../gene/AGAP004709` (mRpL18 - 39S ribosomal protein L18, mitochondrial),  :doc:`../../../../../gene/AGAP004710`:sup:`1` (ubiquinol-cytochrome c reductase subunit 9),  :doc:`../../../../../gene/AGAP004711` (ATP-dependent RNA helicase DDX41),  :doc:`../../../../../gene/AGAP004712`,  :doc:`../../../../../gene/AGAP004713`,  :doc:`../../../../../gene/AGAP004714`,  :doc:`../../../../../gene/AGAP004715`:sup:`1` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`../../../../../gene/AGAP004716`:sup:`3` (Gr57 - gustatory receptor 57),  :doc:`../../../../../gene/AGAP004717`,  :doc:`../../../../../gene/AGAP004718`,  :doc:`../../../../../gene/AGAP004719` (CLIPC9 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP004720`,  :doc:`../../../../../gene/AGAP004721` (N-acetylglucosamine-6-sulfatase),  :doc:`../../../../../gene/AGAP004722`,  :doc:`../../../../../gene/AGAP004723` (chromobox protein homolog 1),  :doc:`../../../../../gene/AGAP004724` (Intraflagellar transport 74 homolog),  :doc:`../../../../../gene/AGAP004725` (eIF3c - Eukaryotic translation initiation factor 3 subunit C),  :doc:`../../../../../gene/AGAP004726` (Uncharacterized protein CG3556),  :doc:`../../../../../gene/AGAP004727`:sup:`3` (Gr25 - gustatory receptor 25),  :doc:`../../../../../gene/AGAP004728`,  :doc:`../../../../../gene/AGAP004729`,  :doc:`../../../../../gene/AGAP004730` (phospholipase A2, venom),  :doc:`../../../../../gene/AGAP004731` (secretory phospholipase A2),  :doc:`../../../../../gene/AGAP029113`,  :doc:`../../../../../gene/AGAP004733`.




The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004735`,  :doc:`../../../../../gene/AGAP004736` (mitochondrial GTPase 1 homolog).


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

    :doc:`../../../../../signal/H12/BFM/2/1/index`, "2L:2,520,001-2,900,000", 1399 (800 | 599)
    :doc:`../../../../../signal/H12/BFS/2/1/index`, "2L:2,420,001-2,720,000", 1365 (680 | 685)
    :doc:`../../../../../signal/H12/GNS/2/1/index`, "2L:1,760,001-2,700,000", 1256 (673 | 583)
    :doc:`../../../../../signal/H12/UGS/2/2/index`, "2L:2,520,001-3,120,000", 982 (573 | 409)
    :doc:`../../../../../signal/H12/GAS/2/2/index`, "2L:2,600,001-2,640,000", 274 (223 | 51)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 76
        # data points      = 320
        # variables        = 3
        chi-square         = 0.154
        reduced chi-square = 0.000
        Akaike info crit   = -2438.641
        Bayesian info crit = -2427.336
    [[Variables]]
        amplitude:   0.15408008 +/- 0.004481 (2.91%) (init= 0.5)
        decay:       1.24084955 +/- 0.091573 (7.38%) (init= 0.5)
        c:           0.05999999 +/- 0.001442 (2.40%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.816 
        C(amplitude, c)              =  0.382 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 116
        # data points      = 169
        # variables        = 3
        chi-square         = 0.216
        reduced chi-square = 0.001
        Akaike info crit   = -1119.632
        Bayesian info crit = -1110.242
    [[Variables]]
        amplitude:   0.15080745 +/- 0.010456 (6.93%) (init= 0.5)
        decay:       1.99999997 +/- 0.373412 (18.67%) (init= 0.5)
        c:           0.05999999 +/- 0.000361 (0.60%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.906 
        C(amplitude, c)              =  0.509 
        C(amplitude, decay)          =  0.220 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 319
        # variables        = 1
        chi-square         = 0.645
        reduced chi-square = 0.002
        Akaike info crit   = -1976.819
        Bayesian info crit = -1973.053
    [[Variables]]
        c:   0.11189674 +/- 0.002522 (2.25%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 168
        # variables        = 1
        chi-square         = 0.395
        reduced chi-square = 0.002
        Akaike info crit   = -1015.028
        Bayesian info crit = -1011.904
    [[Variables]]
        c:   0.11076765 +/- 0.003750 (3.39%) (init= 0.03)


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


