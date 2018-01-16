:orphan:




IHS/BFS/3/5
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **18,760,000** and
**18,920,000**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP008824`,  :doc:`../../../../../gene/AGAP008825`.



Gene :doc:`../../../../../gene/AGAP008826` is within 50 kbp of the focal region.



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
    * - :doc:`../../../../../signal/H12/UGS/3/4/index`
      - H12
      - Uganda *An. gambiae*
      - 3R:18,780,000-19,000,000
      - 210
      - 72.4%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 535
        # variables        = 4
        chi-square         = 40.845
        reduced chi-square = 0.077
        Akaike info crit   = -1368.282
        Bayesian info crit = -1351.153
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.95558839 +/- 0.153515 (7.85%) (init= 3)
        sigma:       0.33620568 +/- 0.018274 (5.44%) (init= 0.5)
        skew:        0.35151736 +/- 0.044891 (12.77%) (init= 0)
        baseline:    1.64610117 +/- 0.012813 (0.78%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.796 
        C(sigma, skew)               = -0.220 
        C(sigma, baseline)           = -0.215 
        C(amplitude, skew)           =  0.130 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 534
        # variables        = 1
        chi-square         = 71.684
        reduced chi-square = 0.134
        Akaike info crit   = -1070.340
        Bayesian info crit = -1066.060
    [[Variables]]
        c:   1.71754242 +/- 0.015870 (0.92%) (init= 1)



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


