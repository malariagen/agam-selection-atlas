:orphan:




IHS/UGS/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **18,760,000** and
**19,000,000**.
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


The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP008824`,  :doc:`../../../../../gene/AGAP008825`,  :doc:`../../../../../gene/AGAP008826`.



Gene :doc:`../../../../../gene/AGAP028025` is within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/IHS/BFS/3/5/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3R:18,760,000-18,920,000
      - 297
      - 90.4%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/3/3/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 3R:18,600,000-19,000,000
      - 215
      - 96.1%
      - nan
    * - :doc:`../../../../../signal/H12/UGS/3/4/index`
      - H12
      - Uganda *An. gambiae*
      - 3R:18,780,000-19,000,000
      - 210
      - 72.4%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 552
        # variables        = 4
        chi-square         = 33.839
        reduced chi-square = 0.062
        Akaike info crit   = -1533.144
        Bayesian info crit = -1515.890
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.41775529 +/- 0.099896 (7.05%) (init= 3)
        sigma:       0.44167177 +/- 0.025113 (5.69%) (init= 0.5)
        skew:        0.34935962 +/- 0.048605 (13.91%) (init= 0)
        baseline:    1.71833559 +/- 0.011533 (0.67%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.766 
        C(sigma, baseline)           = -0.238 
        C(sigma, skew)               = -0.172 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 551
        # variables        = 1
        chi-square         = 61.550
        reduced chi-square = 0.112
        Akaike info crit   = -1205.731
        Bayesian info crit = -1201.419
    [[Variables]]
        c:   1.79664053 +/- 0.014251 (0.79%) (init= 1)



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


