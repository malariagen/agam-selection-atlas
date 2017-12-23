:orphan:




H12 / Burkina Faso *An. gambiae* / Chromosome 2 / #2
====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **28,500,001** and
**28,640,000**.
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




The following 36 genes overlap the focal region: :doc:`../../../../../gene/AGAP006219` (receptor tyrosine kinase-like orphan receptor 1),  :doc:`../../../../../gene/AGAP006220`:sup:`1` (aldehyde oxidase),  :doc:`../../../../../gene/AGAP006221`:sup:`1` (aldehyde oxidase),  :doc:`../../../../../gene/AGAP006222` (glucosyl/glucuronosyl transferases),  :doc:`../../../../../gene/AGAP006223` (glucosyl/glucuronosyl transferases),  :doc:`../../../../../gene/AGAP006224`:sup:`1` (aldehyde oxidase),  :doc:`../../../../../gene/AGAP006225`:sup:`1` (aldehyde oxidase),  :doc:`../../../../../gene/AGAP006226`:sup:`1` (Aldehyde_oxidase),  :doc:`../../../../../gene/AGAP006227`:sup:`1` (alpha esterase),  :doc:`../../../../../gene/AGAP006228`:sup:`1` (COEAE2F - carboxylesterase),  :doc:`../../../../../gene/AGAP006229` (Vps20 - vacuolar protein sorting 20),  :doc:`../../../../../gene/AGAP006231` (serine/threonine-protein phosphatase dullard homolog),  :doc:`../../../../../gene/AGAP006232` (peroxin-14),  :doc:`../../../../../gene/AGAP006233`,  :doc:`../../../../../gene/AGAP006234` (protein SHQ1),  :doc:`../../../../../gene/AGAP006235`,  :doc:`../../../../../gene/AGAP006236`,  :doc:`../../../../../gene/AGAP006237` (Negative elongation factor E),  :doc:`../../../../../gene/AGAP006238` (ubiquitin-conjugating enzyme E2 C),  :doc:`../../../../../gene/AGAP006239` (Protein TSSC1),  :doc:`../../../../../gene/AGAP006240` (splicing factor 3B subunit 2),  :doc:`../../../../../gene/AGAP006241` (Innexin inx2),  :doc:`../../../../../gene/AGAP006242`,  :doc:`../../../../../gene/AGAP006243` (phosphatidylinositol-4,5-bisphosphate 4-phosphatase),  :doc:`../../../../../gene/AGAP029069`,  :doc:`../../../../../gene/AGAP006244` (CTL-like protein 1),  :doc:`../../../../../gene/AGAP006245` (zinc finger matrin-type protein 2),  :doc:`../../../../../gene/AGAP006246` (Sorcin),  :doc:`../../../../../gene/AGAP006247` (Survival of motor neuron-related-splicing factor 30),  :doc:`../../../../../gene/AGAP006248` (Med10 - Mediator of RNA polymerase II transcription subunit 10),  :doc:`../../../../../gene/AGAP006249` (solute carrier family 12 (potassium/chloride transporters), member 8),  :doc:`../../../../../gene/AGAP006250` (eukaryotic elongation factor, selenocysteine-tRNA-specific),  :doc:`../../../../../gene/AGAP006251` (syntaxin 6),  :doc:`../../../../../gene/AGAP006252` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006253` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006254` (polypeptide N-acetylglucosaminyltransferase).




The following 11 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP028453`,  :doc:`../../../../../gene/AGAP006214`,  :doc:`../../../../../gene/AGAP006215` (GPRMTH1 - methuselah receptor 1),  :doc:`../../../../../gene/AGAP006216` (GPRMTH2 - methuselah receptor 2),  :doc:`../../../../../gene/AGAP006217`,  :doc:`../../../../../gene/AGAP006218` (GPRMTH4 - methuselah receptor 4),  :doc:`../../../../../gene/AGAP006255`,  :doc:`../../../../../gene/AGAP006256` (Cad74A),  :doc:`../../../../../gene/AGAP028399`,  :doc:`../../../../../gene/AGAP028454`,  :doc:`../../../../../gene/AGAP006257`.


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

    :doc:`../../../../../signal/H12/GAS/2/5/index`, "2L:28,440,001-28,580,000", 80 (20 | 60)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 151
        # variables        = 3
        chi-square         = 0.055
        reduced chi-square = 0.000
        Akaike info crit   = -1190.502
        Bayesian info crit = -1181.451
    [[Variables]]
        amplitude:   0.33202388 +/- 0.007283 (2.19%) (init= 0.5)
        decay:       1.03514942 +/- 0.045489 (4.39%) (init= 0.5)
        c:           0.02994954 +/- 0.002678 (8.94%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.695 
        C(amplitude, decay)          = -0.463 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 143
        # variables        = 3
        chi-square         = 0.014
        reduced chi-square = 0.000
        Akaike info crit   = -1315.591
        Bayesian info crit = -1306.702
    [[Variables]]
        amplitude:   0.31418227 +/- 0.005330 (1.70%) (init= 0.5)
        decay:       0.63545214 +/- 0.017267 (2.72%) (init= 0.5)
        c:           0.01037982 +/- 0.001099 (10.59%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.633 
        C(decay, c)                  = -0.516 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.939
        reduced chi-square = 0.006
        Akaike info crit   = -759.059
        Bayesian info crit = -756.048
    [[Variables]]
        c:   0.08576436 +/- 0.006481 (7.56%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 142
        # variables        = 1
        chi-square         = 0.528
        reduced chi-square = 0.004
        Akaike info crit   = -792.472
        Bayesian info crit = -789.516
    [[Variables]]
        c:   0.04233241 +/- 0.005134 (12.13%) (init= 0.03)


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


