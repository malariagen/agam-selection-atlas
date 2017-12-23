:orphan:




H12 / Gabon *An. gambiae* / Chromosome 2 / #4
=============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **15,600,001** and
**15,680,000**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP005449` (E3 ubiquitin-protein ligase CBL),  :doc:`../../../../../gene/AGAP005450`.




The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP005448` (B9 domain-containing protein 2),  :doc:`../../../../../gene/AGAP028446`,  :doc:`../../../../../gene/AGAP005451`:sup:`4` (CPR11 - cuticular protein RR-1 family 11),  :doc:`../../../../../gene/AGAP005453`:sup:`4` (CPR12 - cuticular protein RR-1 family 12),  :doc:`../../../../../gene/AGAP005454`:sup:`4` (CPR13 - cuticular protein RR-1 family 13).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 36
        # data points      = 149
        # variables        = 3
        chi-square         = 0.091
        reduced chi-square = 0.001
        Akaike info crit   = -1097.478
        Bayesian info crit = -1088.466
    [[Variables]]
        amplitude:   0.07016546 +/- 0.007932 (11.31%) (init= 0.5)
        decay:       1.99999957 +/- 2.568802 (128.44%) (init= 0.5)
        c:           0.03766332 +/- 0.007552 (20.05%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.903 
        C(amplitude, c)              = -0.463 
        C(amplitude, decay)          = -0.147 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 149
        # variables        = 3
        chi-square         = 0.115
        reduced chi-square = 0.001
        Akaike info crit   = -1062.473
        Bayesian info crit = -1053.462
    [[Variables]]
        amplitude:   0.14294727 +/- 0.030278 (21.18%) (init= 0.5)
        decay:       0.20689163 +/- 0.058235 (28.15%) (init= 0.5)
        c:           0.05612639 +/- 0.002469 (4.40%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.752 
        C(decay, c)                  = -0.270 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.128
        reduced chi-square = 0.001
        Akaike info crit   = -1041.746
        Bayesian info crit = -1038.748
    [[Variables]]
        c:   0.05943942 +/- 0.002426 (4.08%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.137
        reduced chi-square = 0.001
        Akaike info crit   = -1031.819
        Bayesian info crit = -1028.821
    [[Variables]]
        c:   0.05971736 +/- 0.002509 (4.20%) (init= 0.03)


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


