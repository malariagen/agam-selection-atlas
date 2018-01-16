:orphan:




IHS/BFS/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **28,614,895** and
**28,814,895**.
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




The following 20 genes overlap the focal region: :doc:`../../../../../gene/AGAP006250` (eukaryotic elongation factor, selenocysteine-tRNA-specific),  :doc:`../../../../../gene/AGAP006251` (syntaxin 6),  :doc:`../../../../../gene/AGAP006252` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006253` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006254` (polypeptide N-acetylglucosaminyltransferase),  :doc:`../../../../../gene/AGAP006255`,  :doc:`../../../../../gene/AGAP006256` (Cad74A),  :doc:`../../../../../gene/AGAP028399`,  :doc:`../../../../../gene/AGAP028454`,  :doc:`../../../../../gene/AGAP006257`,  :doc:`../../../../../gene/AGAP006258`:sup:`1` (PPO2 - prophenoloxidase 2),  :doc:`../../../../../gene/AGAP006259`,  :doc:`../../../../../gene/AGAP006260` (Z band alternatively spliced PDZ-motif protein 66),  :doc:`../../../../../gene/AGAP006261`:sup:`4` (CPR135 - cuticular protein RR-2 family 135),  :doc:`../../../../../gene/AGAP006262`,  :doc:`../../../../../gene/AGAP006263` (ARR2 - arrestin Arr2-like),  :doc:`../../../../../gene/AGAP006264` (Peroxisomal targeting signal 2 receptor),  :doc:`../../../../../gene/AGAP006265`,  :doc:`../../../../../gene/AGAP006266` (HIV Tat-specific factor 1),  :doc:`../../../../../gene/AGAP006267` (CTL6 - C-type lectin (CTL)).




The following 20 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006232` (peroxin-14),  :doc:`../../../../../gene/AGAP006233`,  :doc:`../../../../../gene/AGAP006234` (protein SHQ1),  :doc:`../../../../../gene/AGAP006235`,  :doc:`../../../../../gene/AGAP006236`,  :doc:`../../../../../gene/AGAP006237` (Negative elongation factor E),  :doc:`../../../../../gene/AGAP006238` (ubiquitin-conjugating enzyme E2 C),  :doc:`../../../../../gene/AGAP006239` (Protein TSSC1),  :doc:`../../../../../gene/AGAP006240` (splicing factor 3B subunit 2),  :doc:`../../../../../gene/AGAP006241` (Innexin inx2),  :doc:`../../../../../gene/AGAP006242`,  :doc:`../../../../../gene/AGAP006243` (phosphatidylinositol-4,5-bisphosphate 4-phosphatase),  :doc:`../../../../../gene/AGAP029069`,  :doc:`../../../../../gene/AGAP006244` (CTL-like protein 1),  :doc:`../../../../../gene/AGAP006245` (zinc finger matrin-type protein 2),  :doc:`../../../../../gene/AGAP006246` (Sorcin),  :doc:`../../../../../gene/AGAP006247` (Survival of motor neuron-related-splicing factor 30),  :doc:`../../../../../gene/AGAP006248` (Med10 - Mediator of RNA polymerase II transcription subunit 10),  :doc:`../../../../../gene/AGAP006249` (solute carrier family 12 (potassium/chloride transporters), member 8),  :doc:`../../../../../gene/AGAP006268`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

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
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/2/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2L:28,374,895-28,694,895
      - 863
      - 98.0%
    * - :doc:`../../../../../signal/H12/BFS/2/3/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2L:28,494,895-28,634,895
      - 834
      - 98.3%
    * - :doc:`../../../../../signal/H12/GNS/2/3/index`
      - H12
      - Guinea *An. gambiae*
      - 2L:28,434,895-28,834,895
      - 301
      - 98.3%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 153
        # data points      = 390
        # variables        = 4
        chi-square         = 272.347
        reduced chi-square = 0.706
        Akaike info crit   = -132.038
        Bayesian info crit = -116.173
    [[Variables]]
        center:      0 (fixed)
        amplitude:   5.42894783 +/- 0.166519 (3.07%) (init= 3)
        decay:       1.74256695 +/- 0.112449 (6.45%) (init= 0.5)
        skew:        0.99999999 +/- 0.186530 (18.65%) (init= 0)
        baseline:    1.98408794 +/- 0.072994 (3.68%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.609 
        C(decay, skew)               =  0.416 
        C(amplitude, decay)          = -0.333 
        C(amplitude, baseline)       = -0.257 
        C(skew, baseline)            = -0.159 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 389
        # variables        = 1
        chi-square         = 1146.909
        reduced chi-square = 2.956
        Akaike info crit   = 422.605
        Bayesian info crit = 426.568
    [[Variables]]
        c:   3.34324100 +/- 0.087171 (2.61%) (init= 1)



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


