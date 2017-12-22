:orphan:




H12 / Gabon *An. gambiae* / Chromosome 3 / #5
=============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **41,500,001** and
**41,860,000**.
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




The following 34 genes overlap the focal region: :doc:`../../../../../gene/AGAP012388`,  :doc:`../../../../../gene/AGAP012389` (Pangolin),  :doc:`../../../../../gene/AGAP012390` (Mpv17-like protein),  :doc:`../../../../../gene/AGAP012391`,  :doc:`../../../../../gene/AGAP012392`,  :doc:`../../../../../gene/AGAP012393`,  :doc:`../../../../../gene/AGAP012394`:sup:`1` (peptide-methionine (S)-S-oxide reductase),  :doc:`../../../../../gene/AGAP012395`:sup:`1` (peptide-methionine (S)-S-oxide reductase),  :doc:`../../../../../gene/AGAP012396` (4.3 kDa secreted salivary peptide),  :doc:`../../../../../gene/AGAP012397` (DNA-directed RNA polymerases I, II, and III subunit RPABC3),  :doc:`../../../../../gene/AGAP012398` (COP9 complex subunit 7a),  :doc:`../../../../../gene/AGAP012399` (maltase),  :doc:`../../../../../gene/AGAP012400` (alpha-glucosidase),  :doc:`../../../../../gene/AGAP012401`:sup:`1` (AGM1),  :doc:`../../../../../gene/AGAP012402` (exosome complex component RRP43),  :doc:`../../../../../gene/AGAP012403`,  :doc:`../../../../../gene/AGAP012404` (alanine--glyoxylate aminotransferase 2, mitochondrial),  :doc:`../../../../../gene/AGAP012405`,  :doc:`../../../../../gene/AGAP012406` (uncharacterized protein slr0305),  :doc:`../../../../../gene/AGAP012407` (protein disulfide-isomerase A1),  :doc:`../../../../../gene/AGAP012408` (tRNA (uracil-5-)-methyltransferase),  :doc:`../../../../../gene/AGAP012409` (GNBPA2 - 3-glucan binding protein),  :doc:`../../../../../gene/AGAP012410`,  :doc:`../../../../../gene/AGAP012411` (T-cell specific transcription factor),  :doc:`../../../../../gene/AGAP012412` (ceramide glucosyltransferase),  :doc:`../../../../../gene/AGAP012413` (CycA - cyclin A),  :doc:`../../../../../gene/AGAP012414` (Polypeptide N-acetylgalactosaminyltransferase (Fragment)),  :doc:`../../../../../gene/AGAP012415`,  :doc:`../../../../../gene/AGAP012416` (DNA-directed RNA polymerase III subunit RPC7),  :doc:`../../../../../gene/AGAP012417` (Exo1 - exocyst complex component 1),  :doc:`../../../../../gene/AGAP012418`,  :doc:`../../../../../gene/AGAP012419` (Feline leukemia virus subgroup C receptor-related protein 1),  :doc:`../../../../../gene/AGAP012420`,  :doc:`../../../../../gene/AGAP012421`.




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP012387` (TOLL6 - TOLL-like receptor 6),  :doc:`../../../../../gene/AGAP012422` (WNK lysine deficient protein kinase),  :doc:`../../../../../gene/AGAP012423`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/5/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 55
        # data points      = 148
        # variables        = 3
        chi-square         = 0.020
        reduced chi-square = 0.000
        Akaike info crit   = -1309.190
        Bayesian info crit = -1300.198
    [[Variables]]
        amplitude:   0.04145743 +/- 0.005360 (12.93%) (init= 0.5)
        decay:       0.70374472 +/- 0.159113 (22.61%) (init= 0.5)
        c:           0.02830591 +/- 0.001345 (4.75%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.556 
        C(amplitude, decay)          = -0.555 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 110
        # data points      = 19
        # variables        = 3
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -168.518
        Bayesian info crit = -165.685
    [[Variables]]
        amplitude:   0.10166609 +/- 0.138658 (136.39%) (init= 0.5)
        decay:       1.10165017 +/- 2.229539 (202.38%) (init= 0.5)
        c:           3.4234e-10 +/- 0.006166 (1801337598.03%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, c)              = -0.999 
        C(decay, c)                  = -0.996 
        C(amplitude, decay)          =  0.992 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.030
        reduced chi-square = 0.000
        Akaike info crit   = -1246.392
        Bayesian info crit = -1243.401
    [[Variables]]
        c:   0.03303419 +/- 0.001184 (3.59%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 18
        # variables        = 1
        chi-square         = 0.005
        reduced chi-square = 0.000
        Akaike info crit   = -146.980
        Bayesian info crit = -146.090
    [[Variables]]
        c:   0.07017963 +/- 0.003868 (5.51%) (init= 0.03)


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


