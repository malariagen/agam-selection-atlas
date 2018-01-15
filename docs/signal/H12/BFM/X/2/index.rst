:orphan:




H12/BFM/X/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **9,220,000** and
**9,260,000**.
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



Gene :doc:`../../../../../gene/AGAP000519` (diacylglycerol kinase (ATP dependent)) overlaps the focal region.





The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000520`,  :doc:`../../../../../gene/AGAP000521`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

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
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,200,000-9,240,000
      - 744
      - 99.5%
    * - :doc:`../../../../../signal/H12/BFS/X/2/index`
      - H12
      - Burkina Faso *An. gambiae*
      - X:9,180,000-9,240,000
      - 563
      - 97.8%
    * - :doc:`../../../../../signal/IHS/BFS/X/1/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - X:9,160,000-9,680,000
      - 515
      - 99.7%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/X/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/X/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/X/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 60
        # data points      = 399
        # variables        = 4
        chi-square         = 0.060
        reduced chi-square = 0.000
        Akaike info crit   = -3501.278
        Bayesian info crit = -3485.322
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.13555236 +/- 0.009172 (6.77%) (init= 0.5)
        decay:       0.15000000 +/- 0.003929 (2.62%) (init= 0.5)
        skew:        0.26603964 +/- 0.096924 (36.43%) (init= 0)
        baseline:    0.02063486 +/- 0.000645 (3.12%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.701 
        C(decay, baseline)           = -0.198 
        C(decay, skew)               = -0.128 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 398
        # variables        = 1
        chi-square         = 0.104
        reduced chi-square = 0.000
        Akaike info crit   = -3279.890
        Bayesian info crit = -3275.904
    [[Variables]]
        c:   0.02284119 +/- 0.000813 (3.56%) (init= 0.03)



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


