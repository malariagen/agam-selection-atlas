:orphan:




XPEHH/BFS.UGS/X/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/UGS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
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
    * - :doc:`../../../../../signal/XPEHH/BFS.BFM/X/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,200,000-9,240,000
      - 848
      - 97.6%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,200,000-9,240,000
      - 744
      - 99.5%
      - nan
    * - :doc:`../../../../../signal/H12/BFS/X/2/index`
      - H12
      - Burkina Faso *An. gambiae*
      - X:9,180,000-9,240,000
      - 563
      - 97.8%
      - nan
    * - :doc:`../../../../../signal/IHS/BFS/X/1/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - X:9,160,000-9,680,000
      - 515
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/X/2/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - X:9,040,000-9,300,000
      - 394
      - 97.4%
      - nan
    * - :doc:`../../../../../signal/H12/BFM/X/2/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - X:9,220,000-9,260,000
      - 221
      - 96.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFM.GWA/X/2/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - X:9,200,000-9,240,000
      - 186
      - 71.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/X/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/X/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/X/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 70
        # data points      = 372
        # variables        = 4
        chi-square         = 137.794
        reduced chi-square = 0.374
        Akaike info crit   = -361.445
        Bayesian info crit = -345.770
    [[Variables]]
        center:      0 (fixed)
        amplitude:   9.55663888 +/- 0.295750 (3.09%) (init= 3)
        decay:       0.15000000 +/- 0.008584 (5.72%) (init= 0.5)
        skew:        0.28832645 +/- 0.049939 (17.32%) (init= 0)
        baseline:    0.98180646 +/- 0.034134 (3.48%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.703 
        C(decay, baseline)           = -0.240 
        C(decay, skew)               = -0.131 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 371
        # variables        = 1
        chi-square         = 867.173
        reduced chi-square = 2.344
        Akaike info crit   = 316.993
        Bayesian info crit = 320.909
    [[Variables]]
        c:   1.40014691 +/- 0.079473 (5.68%) (init= 1)



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


