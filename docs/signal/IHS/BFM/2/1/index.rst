:orphan:




IHS/BFM/2/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **28,700,000** and
**29,020,000**.
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


The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP002886` (GPRNNA2 - putative GPCR class a orphan receptor 2),  :doc:`../../../../../gene/AGAP002888` (GPRNNA3 - putative GPCR class a orphan receptor 3),  :doc:`../../../../../gene/AGAP013540`,  :doc:`../../../../../gene/AGAP002889`:sup:`1` (NADH dehydrogenase (ubiquinone) 1 subcomplex unknown 2),  :doc:`../../../../../gene/AGAP002890` (Lipid storage droplets surface-binding protein 1),  :doc:`../../../../../gene/AGAP002891` (GPRMGL4 - putative metabotropic glutamate receptor 4),  :doc:`../../../../../gene/AGAP002892` (heterogeneous nuclear ribonucleoprotein F/H),  :doc:`../../../../../gene/AGAP002893` (mRpS23 - 28S ribosomal protein S23, mitochondrial),  :doc:`../../../../../gene/AGAP002894`:sup:`1` (CYP6Z4 - cytochrome P450),  :doc:`../../../../../gene/AGAP002895` (mRNA (2'-O-methyladenosine-N6-)-methyltransferase),  :doc:`../../../../../gene/AGAP002896` (RNA-binding protein Nova).



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002881` (GPRNPR1 - putative neuropeptide receptor 1),  :doc:`../../../../../gene/AGAP002883`:sup:`1`,  :doc:`../../../../../gene/AGAP013115`,  :doc:`../../../../../gene/AGAP002884` (V-type H -transporting ATPase subunit B),  :doc:`../../../../../gene/AGAP002885`.


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
    * - :doc:`../../../../../signal/IHS/UGS/2/1/index`
      - IHS
      - Uganda *An. gambiae*
      - 2R:28,280,000-28,700,000
      - 1,661
      - 100.0%
      - Cyp6p
    * - :doc:`../../../../../signal/IHS/GNS/2/1/index`
      - IHS
      - Guinea *An. gambiae*
      - 2R:28,440,000-28,700,000
      - 1,134
      - 99.8%
      - Cyp6p
    * - :doc:`../../../../../signal/XPEHH/UGS.CMS/2/1/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2R:28,860,000-28,980,000
      - 645
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/CMS.GAS/2/3/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 2R:28,560,000-28,800,000
      - 191
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 683
        # variables        = 4
        chi-square         = 238.727
        reduced chi-square = 0.352
        Akaike info crit   = -709.951
        Bayesian info crit = -691.845
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.76358531 +/- 0.069413 (3.94%) (init= 3)
        sigma:       1.13907486 +/- 0.064215 (5.64%) (init= 0.5)
        skew:        0.99999793 +/- 0.062820 (6.28%) (init= 0)
        baseline:    3.82953914 +/- 0.032501 (0.85%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.463 
        C(sigma, skew)               = -0.427 
        C(amplitude, baseline)       = -0.341 
        C(amplitude, sigma)          = -0.251 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 13
        # data points      = 682
        # variables        = 1
        chi-square         = 477.234
        reduced chi-square = 0.701
        Akaike info crit   = -241.489
        Bayesian info crit = -236.964
    [[Variables]]
        c:   4.25640168 +/- 0.032055 (0.75%) (init= 1)



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


