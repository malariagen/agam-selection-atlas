:orphan:




H12 / Uganda *An. gambiae* / Chromosome 2 / #5
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **34,160,001** and
**34,340,000**.
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




The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP013304`:sup:`1`,  :doc:`../../../../../gene/AGAP003233`:sup:`1`,  :doc:`../../../../../gene/AGAP003235` (lachesin),  :doc:`../../../../../gene/AGAP003236`,  :doc:`../../../../../gene/AGAP003237` (tubulin, alpha 1),  :doc:`../../../../../gene/AGAP003238` (N-myc downstream regulated).




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003239` (meiotic chromosome segregation protein),  :doc:`../../../../../gene/AGAP003240` (Protein jagunal),  :doc:`../../../../../gene/AGAP003241`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/5/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 150
        # variables        = 3
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1707.639
        Bayesian info crit = -1698.607
    [[Variables]]
        amplitude:   0.02328401 +/- 0.002587 (11.11%) (init= 0.5)
        decay:       0.17482681 +/- 0.031616 (18.08%) (init= 0.5)
        c:           0.01069855 +/- 0.000290 (2.71%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.592 
        C(decay, c)                  = -0.249 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 40
        # data points      = 149
        # variables        = 3
        chi-square         = 0.012
        reduced chi-square = 0.000
        Akaike info crit   = -1398.259
        Bayesian info crit = -1389.248
    [[Variables]]
        amplitude:   0.04615984 +/- 0.012541 (27.17%) (init= 0.5)
        decay:       0.15000003 +/- 0.051491 (34.33%) (init= 0.5)
        c:           0.01965380 +/- 0.000784 (3.99%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.782 
        C(decay, c)                  = -0.231 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1646.769
        Bayesian info crit = -1643.765
    [[Variables]]
        c:   0.01128078 +/- 0.000325 (2.88%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.014
        reduced chi-square = 0.000
        Akaike info crit   = -1373.156
        Bayesian info crit = -1370.159
    [[Variables]]
        c:   0.02042917 +/- 0.000792 (3.88%) (init= 0.03)


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


