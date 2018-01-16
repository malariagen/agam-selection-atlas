:orphan:




IHS/GNS/2/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **3,020,000** and
**3,280,000**.
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


The following 9 genes overlap the focal region: :doc:`../../../../../gene/AGAP001328` (tripartite motif-containing protein 33),  :doc:`../../../../../gene/AGAP001329` (CPLCX1 - cuticular protein unclassified),  :doc:`../../../../../gene/AGAP001330` (furin),  :doc:`../../../../../gene/AGAP001331`,  :doc:`../../../../../gene/AGAP028467`,  :doc:`../../../../../gene/AGAP001332`,  :doc:`../../../../../gene/AGAP001333` (st - protein scarlet),  :doc:`../../../../../gene/AGAP001334`,  :doc:`../../../../../gene/AGAP001335` (dynein light chain LC8-type).



The following 16 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP001315`,  :doc:`../../../../../gene/AGAP001318`:sup:`1` (acetyl-CoA C-acetyltransferase),  :doc:`../../../../../gene/AGAP001319` (5'-nucleotidase domain-containing protein 1),  :doc:`../../../../../gene/AGAP001320` (golgi apparatus protein 1),  :doc:`../../../../../gene/AGAP001321`,  :doc:`../../../../../gene/AGAP001322`,  :doc:`../../../../../gene/AGAP001323`,  :doc:`../../../../../gene/AGAP001324` (Erythroid differentiation-related factor 1),  :doc:`../../../../../gene/AGAP001325`:sup:`1` (peroxiredoxin 5, atypical 2-Cys peroxiredoxin),  :doc:`../../../../../gene/AGAP001326` (mitotic spindle assembly checkpoint protein MAD2B),  :doc:`../../../../../gene/AGAP001336`,  :doc:`../../../../../gene/AGAP001337`,  :doc:`../../../../../gene/AGAP001338` (DEAH (Asp-Glu-Ala-His) box polypeptide 34),  :doc:`../../../../../gene/AGAP001339` (phosphatidylinositol glycan, class V),  :doc:`../../../../../gene/AGAP001340`,  :doc:`../../../../../gene/AGAP001341` (bleomycin hydrolase).


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
    <img src="../../../../../_static/data/signal/IHS/GNS/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 577
        # variables        = 4
        chi-square         = 111.434
        reduced chi-square = 0.194
        Akaike info crit   = -940.824
        Bayesian info crit = -923.392
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.35809624 +/- 0.108079 (4.58%) (init= 3)
        decay:       0.79883552 +/- 0.062402 (7.81%) (init= 0.5)
        skew:       -0.57959196 +/- 0.066970 (11.55%) (init= 0)
        baseline:    1.85941792 +/- 0.025761 (1.39%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.590 
        C(decay, baseline)           = -0.550 
        C(decay, skew)               =  0.234 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 576
        # variables        = 1
        chi-square         = 249.759
        reduced chi-square = 0.434
        Akaike info crit   = -479.313
        Bayesian info crit = -474.956
    [[Variables]]
        c:   2.15083983 +/- 0.027460 (1.28%) (init= 1)



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


