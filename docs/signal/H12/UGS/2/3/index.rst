:orphan:




H12 / Uganda *An. gambiae* / Chromosome 2 / #3
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **34,040,001** and
**34,140,000**.
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




The following 20 genes overlap the focal region: :doc:`../../../../../gene/AGAP006539` (eupolytin),  :doc:`../../../../../gene/AGAP006540` (LIM homeobox protein),  :doc:`../../../../../gene/AGAP006541` (Transcriptional regulators containing a dna-binding hth domain and an aminotransferase domain transcription regulator protein),  :doc:`../../../../../gene/AGAP006542` (cactin),  :doc:`../../../../../gene/AGAP006543`,  :doc:`../../../../../gene/AGAP028608`,  :doc:`../../../../../gene/AGAP006546`,  :doc:`../../../../../gene/AGAP006547`,  :doc:`../../../../../gene/AGAP006548` (glycine cleavage system H protein),  :doc:`../../../../../gene/AGAP006549`,  :doc:`../../../../../gene/AGAP006550`,  :doc:`../../../../../gene/AGAP006551`,  :doc:`../../../../../gene/AGAP006552`,  :doc:`../../../../../gene/AGAP006553`,  :doc:`../../../../../gene/AGAP006554`,  :doc:`../../../../../gene/AGAP006555`,  :doc:`../../../../../gene/AGAP006556`,  :doc:`../../../../../gene/AGAP006557`,  :doc:`../../../../../gene/AGAP006558`,  :doc:`../../../../../gene/AGAP006559`.




The following 15 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006536` (Arrowhead),  :doc:`../../../../../gene/AGAP006537` (Arrowhead),  :doc:`../../../../../gene/AGAP006560`,  :doc:`../../../../../gene/AGAP006561`,  :doc:`../../../../../gene/AGAP006562`,  :doc:`../../../../../gene/AGAP006563`,  :doc:`../../../../../gene/AGAP006564`,  :doc:`../../../../../gene/AGAP028429`,  :doc:`../../../../../gene/AGAP006566`,  :doc:`../../../../../gene/AGAP028428`,  :doc:`../../../../../gene/AGAP006567`,  :doc:`../../../../../gene/AGAP006568`,  :doc:`../../../../../gene/AGAP006569` (acetyl-CoA synthetase),  :doc:`../../../../../gene/AGAP006570` (myo-inositol-1(or 4)-monophosphatase),  :doc:`../../../../../gene/AGAP006571` (nuclear receptor subfamily 1 group D member 3).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 151
        # variables        = 3
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1215.868
        Bayesian info crit = -1206.816
    [[Variables]]
        amplitude:   0.36775416 +/- 0.009163 (2.49%) (init= 0.5)
        decay:       0.51129363 +/- 0.020977 (4.10%) (init= 0.5)
        c:           0.01722412 +/- 0.001768 (10.27%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.593 
        C(decay, c)                  = -0.451 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 149
        # variables        = 3
        chi-square         = 0.015
        reduced chi-square = 0.000
        Akaike info crit   = -1368.419
        Bayesian info crit = -1359.407
    [[Variables]]
        amplitude:   0.41706546 +/- 0.007191 (1.72%) (init= 0.5)
        decay:       0.38610396 +/- 0.009678 (2.51%) (init= 0.5)
        c:           0.01843425 +/- 0.000955 (5.18%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.697 
        C(decay, c)                  = -0.386 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.689
        reduced chi-square = 0.005
        Akaike info crit   = -805.529
        Bayesian info crit = -802.518
    [[Variables]]
        c:   0.04716467 +/- 0.005551 (11.77%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.556
        reduced chi-square = 0.004
        Akaike info crit   = -824.442
        Bayesian info crit = -821.445
    [[Variables]]
        c:   0.04178215 +/- 0.005055 (12.10%) (init= 0.03)


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


