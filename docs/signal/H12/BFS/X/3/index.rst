:orphan:




H12/BFS/X/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **9,660,000** and
**9,760,000**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).





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


The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP000540` (proton-coupled amino acid transporter),  :doc:`../../../../../gene/AGAP000541` (RpS15a-1 - 40S ribosomal protein S15a),  :doc:`../../../../../gene/AGAP013055`.



The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP012976`,  :doc:`../../../../../gene/AGAP013521`,  :doc:`../../../../../gene/AGAP000536` (PGRPS1 - peptidoglycan recognition protein (short)),  :doc:`../../../../../gene/AGAP000537` (TWDL8 - cuticular protein TWDL family (TWDL8)),  :doc:`../../../../../gene/AGAP000538` (TWDL9 - cuticular protein TWDL family (TWDL9)),  :doc:`../../../../../gene/AGAP000539`,  :doc:`../../../../../gene/AGAP000543` (vitamin-K-epoxide reductase (warfarin-sensitive)),  :doc:`../../../../../gene/AGAP000544` (solute carrier family 35, member E1).


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
    * - :doc:`../../../../../signal/IHS/BFS/X/1/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - X:9,160,000-9,680,000
      - 515
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.BFM/X/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,660,000-9,700,000
      - 214
      - 88.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/X/3/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,660,000-9,700,000
      - 183
      - 97.8%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/3/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,660,000-9,700,000
      - 97
      - 91.2%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 399
        # variables        = 4
        chi-square         = 0.037
        reduced chi-square = 0.000
        Akaike info crit   = -3695.263
        Bayesian info crit = -3679.307
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.07228987 +/- 0.004800 (6.64%) (init= 0.5)
        decay:       0.32639795 +/- 0.032255 (9.88%) (init= 0.5)
        skew:       -0.20958368 +/- 0.096333 (45.96%) (init= 0)
        baseline:    0.01763318 +/- 0.000532 (3.01%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.674 
        C(decay, baseline)           = -0.299 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 10
        # data points      = 398
        # variables        = 1
        chi-square         = 0.072
        reduced chi-square = 0.000
        Akaike info crit   = -3427.768
        Bayesian info crit = -3423.782
    [[Variables]]
        c:   0.02044933 +/- 0.000675 (3.30%) (init= 0.03)



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


