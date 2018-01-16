:orphan:




XPEHH/BFS.UGS/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/UGS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **3,260,000** and
**3,600,000**.
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


The following 33 genes overlap the focal region: :doc:`../../../../../gene/AGAP001334`,  :doc:`../../../../../gene/AGAP001335` (dynein light chain LC8-type),  :doc:`../../../../../gene/AGAP001336`,  :doc:`../../../../../gene/AGAP001337`,  :doc:`../../../../../gene/AGAP001338` (DEAH (Asp-Glu-Ala-His) box polypeptide 34),  :doc:`../../../../../gene/AGAP001339` (phosphatidylinositol glycan, class V),  :doc:`../../../../../gene/AGAP001340`,  :doc:`../../../../../gene/AGAP001341` (bleomycin hydrolase),  :doc:`../../../../../gene/AGAP001342`,  :doc:`../../../../../gene/AGAP001343` (fatty acyl-CoA reductase 2),  :doc:`../../../../../gene/AGAP001344`,  :doc:`../../../../../gene/AGAP001345` (hexamerin),  :doc:`../../../../../gene/AGAP001346`,  :doc:`../../../../../gene/AGAP001347`,  :doc:`../../../../../gene/AGAP001348`,  :doc:`../../../../../gene/AGAP001349` (chronic lymphocytic leukemia deletion region gene 6 protein-like protein),  :doc:`../../../../../gene/AGAP001350`,  :doc:`../../../../../gene/AGAP001351`,  :doc:`../../../../../gene/AGAP001352`,  :doc:`../../../../../gene/AGAP001353`:sup:`3`,  :doc:`../../../../../gene/AGAP001354`:sup:`3`,  :doc:`../../../../../gene/AGAP001355`:sup:`3`,  :doc:`../../../../../gene/AGAP001356`:sup:`1` (ACE1 - Acetylcholinesterase),  :doc:`../../../../../gene/AGAP001357` (beta-catenin-like protein 1),  :doc:`../../../../../gene/AGAP001358`,  :doc:`../../../../../gene/AGAP001360`,  :doc:`../../../../../gene/AGAP001361` (WD repeat-containing protein),  :doc:`../../../../../gene/AGAP001362` (polyadenylation factor subunit 2),  :doc:`../../../../../gene/AGAP001363` (cohesin loading complex subunit SCC4 homolog),  :doc:`../../../../../gene/AGAP001364` (Ubiquitin-fold modifier 1),  :doc:`../../../../../gene/AGAP001365`,  :doc:`../../../../../gene/AGAP001366`,  :doc:`../../../../../gene/AGAP001367` (beta-1,3-glucuronyltransferase).



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP001331`,  :doc:`../../../../../gene/AGAP028467`,  :doc:`../../../../../gene/AGAP001332`,  :doc:`../../../../../gene/AGAP001333` (st - protein scarlet),  :doc:`../../../../../gene/AGAP001368`,  :doc:`../../../../../gene/AGAP001369`.


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
      - Peak Model :math:`\Delta_{i}`
      - Max Percentile
      - Known Loci
    * - :doc:`../../../../../signal/IHS/BFS/2/2/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 2R:3,380,000-3,900,000
      - 635
      - 99.2%
      - Ace1
    * - :doc:`../../../../../signal/IHS/GNS/2/2/index`
      - IHS
      - Guinea *An. gambiae*
      - 2R:3,020,000-3,280,000
      - 461
      - 98.4%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 1154
        # variables        = 4
        chi-square         = 50.637
        reduced chi-square = 0.044
        Akaike info crit   = -3599.750
        Bayesian info crit = -3579.546
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.76844901 +/- 0.040893 (5.32%) (init= 3)
        decay:       0.59521115 +/- 0.051654 (8.68%) (init= 0.5)
        skew:       -0.45820705 +/- 0.081756 (17.84%) (init= 0)
        baseline:    0.97448044 +/- 0.007732 (0.79%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.599 
        C(decay, baseline)           = -0.458 
        C(decay, skew)               =  0.250 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 1153
        # variables        = 1
        chi-square         = 73.813
        reduced chi-square = 0.064
        Akaike info crit   = -3167.119
        Bayesian info crit = -3162.069
    [[Variables]]
        c:   1.04344552 +/- 0.007454 (0.71%) (init= 1)



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


