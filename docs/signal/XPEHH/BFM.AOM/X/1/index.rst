:orphan:




XPEHH/BFM.AOM/X/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/AOM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**X** between positions **15,040,000** and
**15,180,000**.
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


The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP013173`,  :doc:`../../../../../gene/AGAP013424`,  :doc:`../../../../../gene/AGAP012997`.



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000817`,  :doc:`../../../../../gene/AGAP000816`,  :doc:`../../../../../gene/AGAP013474`.


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
      - Peak model :math:`\Delta_{i}`
      - Max. percentile
      - Known locus
    * - :doc:`../../../../../signal/H12/BFM/X/1/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - X:15,100,000-15,300,000
      - 1,267
      - 100.0%
      - Cyp9k1
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/X/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:14,960,000-15,140,000
      - 961
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:15,060,000-15,220,000
      - 866
      - 99.6%
      - Cyp9k1
    * - :doc:`../../../../../signal/XPEHH/BFM.GWA/X/1/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - X:15,060,000-15,260,000
      - 852
      - 99.4%
      - Cyp9k1
    * - :doc:`../../../../../signal/H12/BFS/X/1/index`
      - H12
      - Burkina Faso *An. gambiae*
      - X:15,100,000-15,240,000
      - 815
      - 98.5%
      - Cyp9k1
    * - :doc:`../../../../../signal/IHS/UGS/X/1/index`
      - IHS
      - Uganda *An. gambiae*
      - X:14,640,000-15,360,000
      - 517
      - 96.7%
      - Cyp9k1
    * - :doc:`../../../../../signal/IHS/BFM/X/1/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - X:14,760,000-15,620,000
      - 501
      - 100.0%
      - Cyp9k1
    * - :doc:`../../../../../signal/H12/GNS/X/1/index`
      - H12
      - Guinea *An. gambiae*
      - X:14,960,000-15,160,000
      - 419
      - 97.8%
      - nan
    * - :doc:`../../../../../signal/H12/UGS/X/1/index`
      - H12
      - Uganda *An. gambiae*
      - X:15,160,000-15,480,000
      - 348
      - 94.9%
      - Cyp9k1
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/X/2/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:14,500,000-15,180,000
      - 228
      - 98.5%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/X/1/index`
      - XPEHH
      - Uganda *An. gambiae*
      - X:14,960,000-15,320,000
      - 204
      - 89.8%
      - Cyp9k1
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.AOM/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.AOM/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.AOM/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 241
        # variables        = 4
        chi-square         = 46.241
        reduced chi-square = 0.195
        Akaike info crit   = -389.876
        Bayesian info crit = -375.937
    [[Variables]]
        center:      0 (fixed)
        amplitude:   5.75578583 +/- 0.170163 (2.96%) (init= 3)
        sigma:       0.58518396 +/- 0.015702 (2.68%) (init= 0.5)
        skew:       -0.95236071 +/- 0.029194 (3.07%) (init= 0)
        baseline:    1.29459003 +/- 0.032875 (2.54%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.551 
        C(sigma, skew)               =  0.361 
        C(sigma, baseline)           = -0.298 
        C(amplitude, baseline)       = -0.115 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 240
        # variables        = 1
        chi-square         = 394.645
        reduced chi-square = 1.651
        Akaike info crit   = 121.363
        Bayesian info crit = 124.844
    [[Variables]]
        c:   1.83946523 +/- 0.082946 (4.51%) (init= 1)



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


