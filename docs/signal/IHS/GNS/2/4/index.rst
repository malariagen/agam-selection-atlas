:orphan:




IHS/GNS/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **39,274,895** and
**39,314,895**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).





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


The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP006868`:sup:`4` (CPR140 - cuticular protein RR-1 family 140),  :doc:`../../../../../gene/AGAP006869` (eupolytin),  :doc:`../../../../../gene/AGAP006870`:sup:`3`,  :doc:`../../../../../gene/AGAP006871` (RpS4 - 40S ribosomal protein S4),  :doc:`../../../../../gene/AGAP006872` (NIMA (never in mitosis gene a)-related kinase),  :doc:`../../../../../gene/AGAP006873` (Ras-related protein Rab-8A),  :doc:`../../../../../gene/AGAP006874`:sup:`3` (Gr29 - gustatory receptor 29),  :doc:`../../../../../gene/AGAP006875`:sup:`3` (Gr30 - gustatory receptor 30),  :doc:`../../../../../gene/AGAP006876`:sup:`3` (Gr31 - gustatory receptor 31),  :doc:`../../../../../gene/AGAP006877`:sup:`3` (Gr32 - gustatory receptor 32).



The following 10 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006866`:sup:`4` (CPR63 - cuticular protein RR-1 family 63),  :doc:`../../../../../gene/AGAP006867`:sup:`4` (CPR141 - cuticular protein RR-1 family 141),  :doc:`../../../../../gene/AGAP006878` (mitochondrial complex I protein Fmp36),  :doc:`../../../../../gene/AGAP006879` (F-type H -transporting ATPase subunit e),  :doc:`../../../../../gene/AGAP006880` (Protein LMBR1L),  :doc:`../../../../../gene/AGAP006881` (Polypeptide N-acetylgalactosaminyltransferase (Fragment)),  :doc:`../../../../../gene/AGAP006882`,  :doc:`../../../../../gene/AGAP006883`,  :doc:`../../../../../gene/AGAP006884`,  :doc:`../../../../../gene/AGAP006885` (pre-mRNA-processing factor 8).


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
    * - :doc:`../../../../../signal/IHS/CMS/2/5/index`
      - IHS
      - Cameroon *An. gambiae*
      - 2L:39,274,895-39,314,895
      - 137
      - 95.6%
      - nan
    * - :doc:`../../../../../signal/H12/CMS/2/4/index`
      - H12
      - Cameroon *An. gambiae*
      - 2L:39,274,895-39,314,895
      - 112
      - 98.7%
      - nan
    * - :doc:`../../../../../signal/H12/GNS/2/5/index`
      - H12
      - Guinea *An. gambiae*
      - 2L:39,254,895-39,294,895
      - 110
      - 94.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 493
        # variables        = 4
        chi-square         = 74.955
        reduced chi-square = 0.153
        Akaike info crit   = -920.626
        Bayesian info crit = -903.824
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.36146375 +/- 0.252986 (10.71%) (init= 3)
        decay:       0.15000010 +/- 0.024192 (16.13%) (init= 0.5)
        skew:        0.40500880 +/- 0.160074 (39.52%) (init= 0)
        baseline:    1.99754020 +/- 0.018369 (0.92%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.702 
        C(decay, skew)               = -0.215 
        C(decay, baseline)           = -0.196 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 492
        # variables        = 1
        chi-square         = 96.248
        reduced chi-square = 0.196
        Akaike info crit   = -800.720
        Bayesian info crit = -796.522
    [[Variables]]
        c:   2.03979176 +/- 0.019960 (0.98%) (init= 1)



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


