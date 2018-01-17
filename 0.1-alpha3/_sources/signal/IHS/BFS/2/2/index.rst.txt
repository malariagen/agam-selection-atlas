:orphan:




IHS/BFS/2/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **3,380,000** and
**3,900,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).


This signal overlaps the :doc:`../../../../../known-locus/ace1`, a genome
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


The following 27 genes overlap the focal region: :doc:`../../../../../gene/AGAP001346`,  :doc:`../../../../../gene/AGAP001347`,  :doc:`../../../../../gene/AGAP001348`,  :doc:`../../../../../gene/AGAP001349` (chronic lymphocytic leukemia deletion region gene 6 protein-like protein),  :doc:`../../../../../gene/AGAP001350`,  :doc:`../../../../../gene/AGAP001351`,  :doc:`../../../../../gene/AGAP001352`,  :doc:`../../../../../gene/AGAP001353`:sup:`3`,  :doc:`../../../../../gene/AGAP001354`:sup:`3`,  :doc:`../../../../../gene/AGAP001355`:sup:`3`,  :doc:`../../../../../gene/AGAP001356`:sup:`2` (ACE1 - Acetylcholinesterase),  :doc:`../../../../../gene/AGAP001357` (beta-catenin-like protein 1),  :doc:`../../../../../gene/AGAP001358`,  :doc:`../../../../../gene/AGAP001360`,  :doc:`../../../../../gene/AGAP001361` (WD repeat-containing protein),  :doc:`../../../../../gene/AGAP001362` (polyadenylation factor subunit 2),  :doc:`../../../../../gene/AGAP001363` (cohesin loading complex subunit SCC4 homolog),  :doc:`../../../../../gene/AGAP001364` (Ubiquitin-fold modifier 1),  :doc:`../../../../../gene/AGAP001365`,  :doc:`../../../../../gene/AGAP001366`,  :doc:`../../../../../gene/AGAP001367` (beta-1,3-glucuronyltransferase),  :doc:`../../../../../gene/AGAP001368`,  :doc:`../../../../../gene/AGAP001369`,  :doc:`../../../../../gene/AGAP028468`,  :doc:`../../../../../gene/AGAP001370` (Ras association domain-containing protein 7/8),  :doc:`../../../../../gene/AGAP001371` (D-tyrosyl-tRNA(Tyr) deacylase),  :doc:`../../../../../gene/AGAP001372`.



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP001341` (bleomycin hydrolase),  :doc:`../../../../../gene/AGAP001342`,  :doc:`../../../../../gene/AGAP001343` (fatty acyl-CoA reductase 2),  :doc:`../../../../../gene/AGAP001344`,  :doc:`../../../../../gene/AGAP001345` (hexamerin).


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
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/2/3/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2R:3,260,000-3,600,000
      - 432
      - 90.3%
      - Ace1
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 635
        # variables        = 4
        chi-square         = 157.788
        reduced chi-square = 0.250
        Akaike info crit   = -876.159
        Bayesian info crit = -858.344
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.06886522 +/- 0.065214 (3.15%) (init= 3)
        sigma:       1.13220533 +/- 0.046659 (4.12%) (init= 0.5)
        skew:        0.68771886 +/- 0.044771 (6.51%) (init= 0)
        baseline:    1.74626514 +/- 0.027021 (1.55%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.439 
        C(amplitude, sigma)          = -0.339 
        C(sigma, skew)               = -0.329 
        C(amplitude, baseline)       = -0.295 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 634
        # variables        = 1
        chi-square         = 432.659
        reduced chi-square = 0.684
        Akaike info crit   = -240.252
        Bayesian info crit = -235.799
    [[Variables]]
        c:   2.19260463 +/- 0.032834 (1.50%) (init= 1)



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


