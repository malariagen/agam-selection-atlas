:orphan:




IHS/CMS/X/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**X** between positions **15,520,000** and
**15,560,000**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP000840` (amiloride-sensitive sodium channel, other),  :doc:`../../../../../gene/AGAP000841` (Ras-related protein Rab-40),  :doc:`../../../../../gene/AGAP013101`,  :doc:`../../../../../gene/AGAP000842` (NADH dehydrogenase (ubiquinone) 1 alpha subcomplex, assembly factor 1).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013506`,  :doc:`../../../../../gene/AGAP000843` (cardiolipin synthase),  :doc:`../../../../../gene/AGAP000844` (Progestin and adipoQ receptor family member 4).


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
    * - :doc:`../../../../../signal/IHS/GNS/X/1/index`
      - IHS
      - Guinea *An. gambiae*
      - X:15,240,000-15,780,000
      - 553
      - 99.3%
      - Cyp9k1
    * - :doc:`../../../../../signal/IHS/BFM/X/1/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - X:14,760,000-15,620,000
      - 501
      - 100.0%
      - Cyp9k1
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 42
        # data points      = 317
        # variables        = 4
        chi-square         = 35.679
        reduced chi-square = 0.114
        Akaike info crit   = -684.432
        Bayesian info crit = -669.396
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.92560185 +/- 0.230581 (7.88%) (init= 3)
        decay:       0.15000000 +/- 0.003695 (2.46%) (init= 0.5)
        skew:        0.31768984 +/- 0.132781 (41.80%) (init= 0)
        baseline:    1.63467441 +/- 0.019747 (1.21%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.657 
        C(decay, baseline)           =  0.194 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 316
        # variables        = 1
        chi-square         = 60.234
        reduced chi-square = 0.191
        Akaike info crit   = -521.770
        Bayesian info crit = -518.014
    [[Variables]]
        c:   1.69250264 +/- 0.024599 (1.45%) (init= 1)



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


