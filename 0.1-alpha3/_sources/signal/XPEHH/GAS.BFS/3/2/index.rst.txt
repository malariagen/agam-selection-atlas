:orphan:




XPEHH/GAS.BFS/3/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **520,000** and
**680,000**.
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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP007771`,  :doc:`../../../../../gene/AGAP007772`,  :doc:`../../../../../gene/AGAP007773`,  :doc:`../../../../../gene/AGAP007774`,  :doc:`../../../../../gene/AGAP007775` (ATP-dependent DNA helicase PIF1),  :doc:`../../../../../gene/AGAP007776`.



The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007761` (Complement control protein),  :doc:`../../../../../gene/AGAP007763`,  :doc:`../../../../../gene/AGAP007764`,  :doc:`../../../../../gene/AGAP007765`,  :doc:`../../../../../gene/AGAP007766` (jumonji domain containing 7),  :doc:`../../../../../gene/AGAP007767`,  :doc:`../../../../../gene/AGAP007768` (mitochondrial cytochrome c oxidase subunit VIC),  :doc:`../../../../../gene/AGAP007769` (Katanin-60).


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
    * - :doc:`../../../../../signal/IHS/GWA/3/1/index`
      - IHS
      - Guinea Bissau
      - 3R:660,000-700,000
      - 363
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GWA.UGS/3/1/index`
      - XPEHH
      - Guinea Bissau
      - 3R:660,000-700,000
      - 346
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GWA.BFS/3/1/index`
      - XPEHH
      - Guinea Bissau
      - 3R:660,000-700,000
      - 313
      - 99.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 291
        # variables        = 4
        chi-square         = 127.758
        reduced chi-square = 0.445
        Akaike info crit   = -231.548
        Bayesian info crit = -216.855
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.91885001 +/- 0.128862 (6.72%) (init= 3)
        sigma:       0.35055832 +/- 0.032731 (9.34%) (init= 0.5)
        skew:        0.82102616 +/- 0.108188 (13.18%) (init= 0)
        baseline:    2.06205726 +/- 0.047214 (2.29%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.405 
        C(amplitude, baseline)       = -0.319 
        C(sigma, baseline)           = -0.292 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 290
        # variables        = 1
        chi-square         = 239.458
        reduced chi-square = 0.829
        Akaike info crit   = -53.536
        Bayesian info crit = -49.866
    [[Variables]]
        c:   2.42060476 +/- 0.053451 (2.21%) (init= 1)



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


