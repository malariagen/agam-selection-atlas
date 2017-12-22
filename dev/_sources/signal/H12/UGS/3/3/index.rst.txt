:orphan:




H12 / Uganda *An. gambiae* / Chromosome 3 / #3
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **44,000,001** and
**44,060,000**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).

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




The following 7 genes overlap the focal region: :doc:`../../../../../gene/AGAP009830`,  :doc:`../../../../../gene/AGAP009831`,  :doc:`../../../../../gene/AGAP009832` (CASPS8 - short caspase 8),  :doc:`../../../../../gene/AGAP028572` (Gustatory receptor),  :doc:`../../../../../gene/AGAP009833` (voltage-dependent anion-selective channel protein 2),  :doc:`../../../../../gene/AGAP009834` (COP9 signalosome subunit 4),  :doc:`../../../../../gene/AGAP009835` (ABCC14 - ATP-binding cassette transporter (ABC transporter) family C member 14).




The following 12 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009829` (beat protein),  :doc:`../../../../../gene/AGAP009836`,  :doc:`../../../../../gene/AGAP009837`,  :doc:`../../../../../gene/AGAP009838` (Non-imprinted in Prader-Willi/Angelman syndrome region protein 2-like protein),  :doc:`../../../../../gene/AGAP009839` (Phosphatase 1 regulatory subunit 7),  :doc:`../../../../../gene/AGAP009840` (USO1 vesicle docking protein homolog),  :doc:`../../../../../gene/AGAP009841`,  :doc:`../../../../../gene/AGAP009842` (ribonuclease T2),  :doc:`../../../../../gene/AGAP009843`,  :doc:`../../../../../gene/AGAP009844` (CLIPB15 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP009845`,  :doc:`../../../../../gene/AGAP009846` (Ras-related protein Rab-9A).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 239
        # variables        = 3
        chi-square         = 0.057
        reduced chi-square = 0.000
        Akaike info crit   = -1988.800
        Bayesian info crit = -1978.370
    [[Variables]]
        amplitude:   0.12376021 +/- 0.009017 (7.29%) (init= 0.5)
        decay:       0.38884782 +/- 0.044076 (11.34%) (init= 0.5)
        c:           0.04270052 +/- 0.001091 (2.56%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.634 
        C(decay, c)                  = -0.286 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 44
        # data points      = 148
        # variables        = 3
        chi-square         = 0.033
        reduced chi-square = 0.000
        Akaike info crit   = -1240.366
        Bayesian info crit = -1231.375
    [[Variables]]
        amplitude:   0.04846694 +/- 0.004866 (10.04%) (init= 0.5)
        decay:       1.99999914 +/- 0.623787 (31.19%) (init= 0.5)
        c:           0.04366467 +/- 0.004652 (10.65%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.906 
        C(amplitude, c)              = -0.423 
        C(amplitude, decay)          =  0.105 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 237
        # variables        = 1
        chi-square         = 0.110
        reduced chi-square = 0.000
        Akaike info crit   = -1817.527
        Bayesian info crit = -1814.059
    [[Variables]]
        c:   0.04707550 +/- 0.001400 (2.98%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.051
        reduced chi-square = 0.000
        Akaike info crit   = -1169.749
        Bayesian info crit = -1166.759
    [[Variables]]
        c:   0.05855992 +/- 0.001537 (2.63%) (init= 0.03)


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


