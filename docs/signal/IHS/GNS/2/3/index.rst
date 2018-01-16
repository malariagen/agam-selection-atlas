:orphan:




IHS/GNS/2/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,200,000** and
**40,420,000**.
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


The following 23 genes overlap the focal region: :doc:`../../../../../gene/AGAP003579` (cadherin-87A),  :doc:`../../../../../gene/AGAP003580`,  :doc:`../../../../../gene/AGAP003581`:sup:`1` (D-xylulose reductase A),  :doc:`../../../../../gene/AGAP003582`:sup:`1` (D-xylulose reductase A),  :doc:`../../../../../gene/AGAP003583`:sup:`1` (L-iditol 2-dehydrogenase),  :doc:`../../../../../gene/AGAP003584`:sup:`1` (L-iditol 2-dehydrogenase),  :doc:`../../../../../gene/AGAP003585`,  :doc:`../../../../../gene/AGAP003586` (Phosphate carrier, mitochondrial),  :doc:`../../../../../gene/AGAP013333` (Phosphate carrier, mitochondrial),  :doc:`../../../../../gene/AGAP003587` (solute carrier family 26 (sodium-independent sulfate anion transporter)),  :doc:`../../../../../gene/AGAP003588` (VATH - V-type H -transporting ATPase subunit H),  :doc:`../../../../../gene/AGAP003589` (prolyl-tRNA synthetase),  :doc:`../../../../../gene/AGAP003590`,  :doc:`../../../../../gene/AGAP003591` (LRR-repeat protein 1),  :doc:`../../../../../gene/AGAP003592` (RpLP0 - 60S ribosomal protein LP0),  :doc:`../../../../../gene/AGAP003593` (Protein arginine methyltransferase RmtB),  :doc:`../../../../../gene/AGAP003594`,  :doc:`../../../../../gene/AGAP003595` (rRNA biogenesis protein RRP5),  :doc:`../../../../../gene/AGAP003596`,  :doc:`../../../../../gene/AGAP003597` (histone-lysine N-methyltransferase SUV39H),  :doc:`../../../../../gene/AGAP003598` (template-activating factor I),  :doc:`../../../../../gene/AGAP003599` (F-type H -transporting ATPase oligomycin sensitivity conferral protein),  :doc:`../../../../../gene/AGAP003600` (Elongation of very long chain fatty acids protein).



The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003578`:sup:`1` (aldehyde dehydrogenase (NAD )),  :doc:`../../../../../gene/AGAP003601` (alpha-1,2-mannosyltransferase),  :doc:`../../../../../gene/AGAP003602` (methyltransferase-like protein 9),  :doc:`../../../../../gene/AGAP003603`,  :doc:`../../../../../gene/AGAP003604`,  :doc:`../../../../../gene/AGAP003605` (cullin 2),  :doc:`../../../../../gene/AGAP003606` (Fatty acyl-CoA reductase).


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
    * - :doc:`../../../../../signal/IHS/CMS/2/2/index`
      - IHS
      - Cameroon *An. gambiae*
      - 2R:40,060,000-40,780,000
      - 643
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/IHS/BFS/2/3/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 2R:40,320,000-40,560,000
      - 557
      - 99.5%
      - nan
    * - :doc:`../../../../../signal/H12/CMS/2/3/index`
      - H12
      - Cameroon *An. gambiae*
      - 2R:40,300,000-40,740,000
      - 501
      - 98.7%
      - nan
    * - :doc:`../../../../../signal/IHS/UGS/2/5/index`
      - IHS
      - Uganda *An. gambiae*
      - 2R:40,160,000-40,200,000
      - 132
      - 98.3%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 549
        # variables        = 4
        chi-square         = 141.163
        reduced chi-square = 0.259
        Akaike info crit   = -737.642
        Bayesian info crit = -720.410
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.17339499 +/- 0.085659 (3.94%) (init= 3)
        decay:       1.45937367 +/- 0.126864 (8.69%) (init= 0.5)
        skew:       -0.63477604 +/- 0.067673 (10.66%) (init= 0)
        baseline:    2.24720608 +/- 0.039143 (1.74%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.703 
        C(amplitude, decay)          = -0.333 
        C(amplitude, baseline)       = -0.175 
        C(decay, skew)               =  0.115 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 548
        # variables        = 1
        chi-square         = 323.422
        reduced chi-square = 0.591
        Akaike info crit   = -286.971
        Bayesian info crit = -282.664
    [[Variables]]
        c:   2.70872392 +/- 0.032846 (1.21%) (init= 1)



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


