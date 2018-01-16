:orphan:




H12/UGS/2/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **34,074,895** and
**34,134,895**.
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


The following 18 genes overlap the focal region: :doc:`../../../../../gene/AGAP006540` (LIM homeobox protein),  :doc:`../../../../../gene/AGAP006541` (Transcriptional regulators containing a dna-binding hth domain and an aminotransferase domain transcription regulator protein),  :doc:`../../../../../gene/AGAP006542` (cactin),  :doc:`../../../../../gene/AGAP006543`,  :doc:`../../../../../gene/AGAP028608`,  :doc:`../../../../../gene/AGAP006546`,  :doc:`../../../../../gene/AGAP006547`,  :doc:`../../../../../gene/AGAP006548` (glycine cleavage system H protein),  :doc:`../../../../../gene/AGAP006549`,  :doc:`../../../../../gene/AGAP006550`,  :doc:`../../../../../gene/AGAP006551`,  :doc:`../../../../../gene/AGAP006552`,  :doc:`../../../../../gene/AGAP006553`,  :doc:`../../../../../gene/AGAP006554`,  :doc:`../../../../../gene/AGAP006555`,  :doc:`../../../../../gene/AGAP006556`,  :doc:`../../../../../gene/AGAP006557`,  :doc:`../../../../../gene/AGAP006558`.



The following 15 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006539` (eupolytin),  :doc:`../../../../../gene/AGAP006559`,  :doc:`../../../../../gene/AGAP006560`,  :doc:`../../../../../gene/AGAP006561`,  :doc:`../../../../../gene/AGAP006562`,  :doc:`../../../../../gene/AGAP006563`,  :doc:`../../../../../gene/AGAP006564`,  :doc:`../../../../../gene/AGAP028429`,  :doc:`../../../../../gene/AGAP006566`,  :doc:`../../../../../gene/AGAP028428`,  :doc:`../../../../../gene/AGAP006567`,  :doc:`../../../../../gene/AGAP006568`,  :doc:`../../../../../gene/AGAP006569` (acetyl-CoA synthetase),  :doc:`../../../../../gene/AGAP006570` (myo-inositol-1(or 4)-monophosphatase),  :doc:`../../../../../gene/AGAP006571` (nuclear receptor subfamily 1 group D member 3).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping selection signals
-----------------------------

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
      - Known Loci
    * - :doc:`../../../../../signal/IHS/UGS/2/2/index`
      - IHS
      - Uganda *An. gambiae*
      - 2L:33,934,895-34,194,895
      - 860
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/2/2/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2L:34,134,895-34,234,895
      - 487
      - 98.3%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.GWA/2/2/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2L:34,114,895-34,214,895
      - 422
      - 95.2%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.CMS/2/3/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2L:34,134,895-34,234,895
      - 342
      - 99.2%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/3/peak_finding.png"/>
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

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 396
        # variables        = 4
        chi-square         = 0.070
        reduced chi-square = 0.000
        Akaike info crit   = -3411.239
        Bayesian info crit = -3395.313
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.38628754 +/- 0.005626 (1.46%) (init= 0.5)
        decay:       0.44678380 +/- 0.009938 (2.22%) (init= 0.5)
        skew:        0.26836316 +/- 0.021367 (7.96%) (init= 0)
        baseline:    0.01734492 +/- 0.000767 (4.42%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.655 
        C(decay, baseline)           = -0.357 
        C(decay, skew)               = -0.122 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 395
        # variables        = 1
        chi-square         = 1.431
        reduced chi-square = 0.004
        Akaike info crit   = -2218.090
        Bayesian info crit = -2214.111
    [[Variables]]
        c:   0.03856684 +/- 0.003032 (7.86%) (init= 0.03)



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


