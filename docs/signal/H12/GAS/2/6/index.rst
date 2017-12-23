:orphan:




H12 / Gabon *An. gambiae* / Chromosome 2 / #6
=============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **44,380,001** and
**44,580,000**.
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




The following 7 genes overlap the focal region: :doc:`../../../../../gene/AGAP003849`,  :doc:`../../../../../gene/AGAP013134`,  :doc:`../../../../../gene/AGAP003851` (26 proteasome complex subunit DSS1),  :doc:`../../../../../gene/AGAP003852` (snRNA-activating protein complex subunit 3),  :doc:`../../../../../gene/AGAP003853` (ubiquitin thioesterase ZRANB1),  :doc:`../../../../../gene/AGAP029103`,  :doc:`../../../../../gene/AGAP003855`.




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003844` (Class b basic helix-loop-helix protein),  :doc:`../../../../../gene/AGAP003845` (bromodomain-containing protein 8),  :doc:`../../../../../gene/AGAP003846` (secretory phospholipase A2),  :doc:`../../../../../gene/AGAP003847` (RNA exonuclease 1),  :doc:`../../../../../gene/AGAP003848` (acyl-CoA thioesterase 9.1),  :doc:`../../../../../gene/AGAP013342`,  :doc:`../../../../../gene/AGAP013408`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/6/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 148
        # variables        = 3
        chi-square         = 0.025
        reduced chi-square = 0.000
        Akaike info crit   = -1279.573
        Bayesian info crit = -1270.581
    [[Variables]]
        amplitude:   0.03584757 +/- 0.004211 (11.75%) (init= 0.5)
        decay:       1.99999993 +/- 0.723105 (36.16%) (init= 0.5)
        c:           0.03451687 +/- 0.004065 (11.78%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.906 
        C(amplitude, c)              = -0.474 
        C(amplitude, decay)          =  0.164 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 139
        # variables        = 3
        chi-square         = 0.055
        reduced chi-square = 0.000
        Akaike info crit   = -1081.967
        Bayesian info crit = -1073.164
    [[Variables]]
        amplitude:   0.06004666 +/- 0.016489 (27.46%) (init= 0.5)
        decay:       0.31321126 +/- 0.121904 (38.92%) (init= 0.5)
        c:           0.05186095 +/- 0.001945 (3.75%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.713 
        C(decay, c)                  = -0.356 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.036
        reduced chi-square = 0.000
        Akaike info crit   = -1222.085
        Bayesian info crit = -1219.094
    [[Variables]]
        c:   0.04576977 +/- 0.001287 (2.81%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 138
        # variables        = 1
        chi-square         = 0.063
        reduced chi-square = 0.000
        Akaike info crit   = -1059.324
        Bayesian info crit = -1056.396
    [[Variables]]
        c:   0.05461355 +/- 0.001826 (3.34%) (init= 0.03)


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


