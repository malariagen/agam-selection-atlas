:orphan:




H12 / Gabon *An. gambiae* / Chromosome 2 / #5
=============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **28,440,001** and
**28,580,000**.
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




The following 26 genes overlap the focal region: :doc:`../../../../../gene/AGAP028453`,  :doc:`../../../../../gene/AGAP006214`,  :doc:`../../../../../gene/AGAP006215` (GPRMTH1 - methuselah receptor 1),  :doc:`../../../../../gene/AGAP006216` (GPRMTH2 - methuselah receptor 2),  :doc:`../../../../../gene/AGAP006217`,  :doc:`../../../../../gene/AGAP006218` (GPRMTH4 - methuselah receptor 4),  :doc:`../../../../../gene/AGAP006219` (receptor tyrosine kinase-like orphan receptor 1),  :doc:`../../../../../gene/AGAP006220`:sup:`1` (aldehyde oxidase),  :doc:`../../../../../gene/AGAP006221`:sup:`1` (aldehyde oxidase),  :doc:`../../../../../gene/AGAP006222` (glucosyl/glucuronosyl transferases),  :doc:`../../../../../gene/AGAP006223` (glucosyl/glucuronosyl transferases),  :doc:`../../../../../gene/AGAP006224`:sup:`1` (aldehyde oxidase),  :doc:`../../../../../gene/AGAP006225`:sup:`1` (aldehyde oxidase),  :doc:`../../../../../gene/AGAP006226`:sup:`1` (Aldehyde_oxidase),  :doc:`../../../../../gene/AGAP006227`:sup:`1` (alpha esterase),  :doc:`../../../../../gene/AGAP006228`:sup:`1` (COEAE2F - carboxylesterase),  :doc:`../../../../../gene/AGAP006229` (Vps20 - vacuolar protein sorting 20),  :doc:`../../../../../gene/AGAP006231` (serine/threonine-protein phosphatase dullard homolog),  :doc:`../../../../../gene/AGAP006232` (peroxin-14),  :doc:`../../../../../gene/AGAP006233`,  :doc:`../../../../../gene/AGAP006234` (protein SHQ1),  :doc:`../../../../../gene/AGAP006235`,  :doc:`../../../../../gene/AGAP006236`,  :doc:`../../../../../gene/AGAP006237` (Negative elongation factor E),  :doc:`../../../../../gene/AGAP006238` (ubiquitin-conjugating enzyme E2 C),  :doc:`../../../../../gene/AGAP006239` (Protein TSSC1).




The following 16 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006240` (splicing factor 3B subunit 2),  :doc:`../../../../../gene/AGAP006241` (Innexin inx2),  :doc:`../../../../../gene/AGAP006242`,  :doc:`../../../../../gene/AGAP006243` (phosphatidylinositol-4,5-bisphosphate 4-phosphatase),  :doc:`../../../../../gene/AGAP029069`,  :doc:`../../../../../gene/AGAP006244` (CTL-like protein 1),  :doc:`../../../../../gene/AGAP006245` (zinc finger matrin-type protein 2),  :doc:`../../../../../gene/AGAP006246` (Sorcin),  :doc:`../../../../../gene/AGAP006247` (Survival of motor neuron-related-splicing factor 30),  :doc:`../../../../../gene/AGAP006248` (Med10 - Mediator of RNA polymerase II transcription subunit 10),  :doc:`../../../../../gene/AGAP006249` (solute carrier family 12 (potassium/chloride transporters), member 8),  :doc:`../../../../../gene/AGAP006250` (eukaryotic elongation factor, selenocysteine-tRNA-specific),  :doc:`../../../../../gene/AGAP006251` (syntaxin 6),  :doc:`../../../../../gene/AGAP006252` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006253` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006254` (polypeptide N-acetylglucosaminyltransferase).


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

    :doc:`../../../../../signal/H12/BFS/2/2/index`, "2L:28,500,001-28,640,000", 954 (431 | 523)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/5/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 36
        # data points      = 151
        # variables        = 3
        chi-square         = 0.079
        reduced chi-square = 0.001
        Akaike info crit   = -1135.006
        Bayesian info crit = -1125.954
    [[Variables]]
        amplitude:   0.08020083 +/- 0.018721 (23.34%) (init= 0.5)
        decay:       0.15000000 +/- 0.090357 (60.24%) (init= 0.5)
        c:           0.04792015 +/- 0.001981 (4.13%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.581 
        C(decay, c)                  =  0.229 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 143
        # variables        = 3
        chi-square         = 0.024
        reduced chi-square = 0.000
        Akaike info crit   = -1238.680
        Bayesian info crit = -1229.792
    [[Variables]]
        amplitude:   0.07102244 +/- 0.011021 (15.52%) (init= 0.5)
        decay:       0.29636133 +/- 0.064504 (21.77%) (init= 0.5)
        c:           0.03308017 +/- 0.001222 (3.70%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.719 
        C(decay, c)                  = -0.340 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.088
        reduced chi-square = 0.001
        Akaike info crit   = -1114.756
        Bayesian info crit = -1111.745
    [[Variables]]
        c:   0.04967137 +/- 0.001980 (3.99%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 142
        # variables        = 1
        chi-square         = 0.035
        reduced chi-square = 0.000
        Akaike info crit   = -1178.313
        Bayesian info crit = -1175.357
    [[Variables]]
        c:   0.03610502 +/- 0.001319 (3.65%) (init= 0.03)


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


