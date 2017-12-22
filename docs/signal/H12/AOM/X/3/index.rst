:orphan:




H12 / Angola *An. coluzzii* / Chromosome X / #3
===============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **18,420,001** and
**18,800,000**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).

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




The following 15 genes overlap the focal region: :doc:`../../../../../gene/AGAP000962`:sup:`2` (alpha7 - nicotinic acetylcholine receptor subunit alpha 7),  :doc:`../../../../../gene/AGAP000963`,  :doc:`../../../../../gene/AGAP000964`,  :doc:`../../../../../gene/AGAP000965` (ELAV (embryonic lethal, abnormal vision Drosophila)-like),  :doc:`../../../../../gene/AGAP000966`:sup:`2` (beta1 - nicotinic acetylcholine receptor beta 1),  :doc:`../../../../../gene/AGAP000967` (estrogen receptor binding site associated antigen 9 variant 1),  :doc:`../../../../../gene/AGAP000968`,  :doc:`../../../../../gene/AGAP000969` (tropomodulin),  :doc:`../../../../../gene/AGAP000970` (DnaJ homolog subfamily C),  :doc:`../../../../../gene/AGAP000971`:sup:`1` (prolyl 4-hydroxylase),  :doc:`../../../../../gene/AGAP000973` (neutral ceramidase),  :doc:`../../../../../gene/AGAP000974`,  :doc:`../../../../../gene/AGAP000975`,  :doc:`../../../../../gene/AGAP000976`,  :doc:`../../../../../gene/AGAP000977` (RNA-binding motif protein, X-linked 2).




The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000958` (calcium-binding mitochondrial carrier protein Aralar1),  :doc:`../../../../../gene/AGAP000960` (STAM-binding protein),  :doc:`../../../../../gene/AGAP000961`,  :doc:`../../../../../gene/AGAP000978` (origin recognition complex subunit 5),  :doc:`../../../../../gene/AGAP000979` (DNA polymerase gamma 2),  :doc:`../../../../../gene/AGAP013093` (Glutamyl-tRNA(Gln) amidotransferase subunit C, mitochondrial),  :doc:`../../../../../gene/AGAP000981` (nuclear receptor interaction protein),  :doc:`../../../../../gene/AGAP000982` (uncharacterized protein Enpp4),  :doc:`../../../../../gene/AGAP000983`.


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

    :doc:`../../../../../signal/H12/GAS/X/2/index`, "X:18,520,001-18,560,000", 85 (31 | 54)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 192
        # variables        = 3
        chi-square         = 0.073
        reduced chi-square = 0.000
        Akaike info crit   = -1506.146
        Bayesian info crit = -1496.373
    [[Variables]]
        amplitude:   0.06097871 +/- 0.012144 (19.92%) (init= 0.5)
        decay:       0.33265700 +/- 0.104388 (31.38%) (init= 0.5)
        c:           0.04876151 +/- 0.001559 (3.20%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.622 
        C(decay, c)                  = -0.308 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 44
        # data points      = 238
        # variables        = 3
        chi-square         = 0.088
        reduced chi-square = 0.000
        Akaike info crit   = -1874.498
        Bayesian info crit = -1864.081
    [[Variables]]
        amplitude:   0.07637445 +/- 0.013492 (17.67%) (init= 0.5)
        decay:       2.99999970 +/- 1.362077 (45.40%) (init= 0.5)
        c:           0.00650426 +/- 0.016475 (253.31%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.983 
        C(amplitude, c)              = -0.935 
        C(amplitude, decay)          =  0.865 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 191
        # variables        = 1
        chi-square         = 0.079
        reduced chi-square = 0.000
        Akaike info crit   = -1485.684
        Bayesian info crit = -1482.432
    [[Variables]]
        c:   0.05105069 +/- 0.001476 (2.89%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 237
        # variables        = 1
        chi-square         = 0.129
        reduced chi-square = 0.001
        Akaike info crit   = -1779.628
        Bayesian info crit = -1776.160
    [[Variables]]
        c:   0.03748007 +/- 0.001517 (4.05%) (init= 0.03)


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


