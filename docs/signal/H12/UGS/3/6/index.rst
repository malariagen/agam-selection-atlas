:orphan:

H12 / Uganda *An. gambiae* / Chromosome 3 / #6
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **36,320,001** and
**36,560,000**.
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
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>




The following 16 genes overlap the focal region: :doc:`../../../../../gene/AGAP009566` (zinc finger protein 271),  :doc:`../../../../../gene/AGAP009567` (mitochondrial inner membrane protease ATP23 homolog),  :doc:`../../../../../gene/AGAP009568` (dynein heavy chain),  :doc:`../../../../../gene/AGAP009569` (syntenin-1 isoform 1),  :doc:`../../../../../gene/AGAP009570` (RNA-binding protein with serine-rich domain 1),  :doc:`../../../../../gene/AGAP009571`,  :doc:`../../../../../gene/AGAP009572` (RpS15a-2 - 40S ribosomal protein S15a),  :doc:`../../../../../gene/AGAP009573`,  :doc:`../../../../../gene/AGAP009574` (WD repeat-containing protein 69),  :doc:`../../../../../gene/AGAP009575` (nuclear receptor subfamily 2 group A),  :doc:`../../../../../gene/AGAP009576` (collagen alpha 1),  :doc:`../../../../../gene/AGAP009577`,  :doc:`../../../../../gene/AGAP009578` (adenosine monophosphate-protein transferase FICD homolog),  :doc:`../../../../../gene/AGAP009579` (dihydropyridine-sensitive l-type calcium channel),  :doc:`../../../../../gene/AGAP009580`,  :doc:`../../../../../gene/AGAP009581` (collagen type I/II/III/V/XI/XXIV/XXVII alpha).



Gene :doc:`../../../../../gene/AGAP009582` is within 50 kbp of the focal region.



Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/6/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/6/peak_fit.png"/>
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
        chi-square         = 0.014
        reduced chi-square = 0.000
        Akaike info crit   = -1368.153
        Bayesian info crit = -1359.162
    [[Variables]]
        amplitude:   0.03645190 +/- 0.003069 (8.42%) (init= 0.5)
        decay:       1.81939135 +/- 0.447513 (24.60%) (init= 0.5)
        c:           0.01872793 +/- 0.002604 (13.91%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.885 
        C(amplitude, c)              = -0.362 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 206
        # variables        = 3
        chi-square         = 0.077
        reduced chi-square = 0.000
        Akaike info crit   = -1620.784
        Bayesian info crit = -1610.800
    [[Variables]]
        amplitude:   0.03381160 +/- 0.005624 (16.63%) (init= 0.5)
        decay:       1.99999931 +/- 0.991137 (49.56%) (init= 0.5)
        c:           0.03627771 +/- 0.004282 (11.81%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.894 
        C(amplitude, c)              = -0.168 
        C(amplitude, decay)          = -0.163 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.022
        reduced chi-square = 0.000
        Akaike info crit   = -1291.971
        Bayesian info crit = -1288.981
    [[Variables]]
        c:   0.02910729 +/- 0.001014 (3.49%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 205
        # variables        = 1
        chi-square         = 0.083
        reduced chi-square = 0.000
        Akaike info crit   = -1600.360
        Bayesian info crit = -1597.037
    [[Variables]]
        c:   0.04414337 +/- 0.001405 (3.18%) (init= 0.03)


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
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
