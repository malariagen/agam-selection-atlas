:orphan:




IHS/GNS/2/5
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **42,274,895** and
**42,414,895**.
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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP007083`,  :doc:`../../../../../gene/AGAP007084`,  :doc:`../../../../../gene/AGAP007085`,  :doc:`../../../../../gene/AGAP007086`:sup:`2` (Sodium channel protein),  :doc:`../../../../../gene/AGAP007087` (RpL41 - 60s ribosomal protein L41),  :doc:`../../../../../gene/AGAP007088` (peptidyl-prolyl cis-trans isomerase B (cyclophilin B)).



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007079`,  :doc:`../../../../../gene/AGAP007080` (hexosaminidase),  :doc:`../../../../../gene/AGAP007081`,  :doc:`../../../../../gene/AGAP007082`:sup:`1` (NADH dehydrogenase (ubiquinone) Fe-S protein 4),  :doc:`../../../../../gene/AGAP007089`,  :doc:`../../../../../gene/AGAP007090`.


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
    * - :doc:`../../../../../signal/IHS/BFS/2/7/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 2L:42,314,895-42,454,895
      - 222
      - 95.5%
      - nan
    * - :doc:`../../../../../signal/IHS/CMS/2/6/index`
      - IHS
      - Cameroon *An. gambiae*
      - 2L:42,394,895-42,434,895
      - 90
      - 77.8%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 572
        # variables        = 4
        chi-square         = 57.170
        reduced chi-square = 0.101
        Akaike info crit   = -1309.379
        Bayesian info crit = -1291.982
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.82158270 +/- 0.084153 (10.24%) (init= 3)
        sigma:       0.24248233 +/- 0.032627 (13.46%) (init= 0.5)
        skew:        0.30435119 +/- 0.159959 (52.56%) (init= 0)
        baseline:    1.88617587 +/- 0.013938 (0.74%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.513 
        C(sigma, baseline)           = -0.177 
        C(amplitude, baseline)       = -0.124 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 571
        # variables        = 1
        chi-square         = 68.297
        reduced chi-square = 0.120
        Akaike info crit   = -1210.532
        Bayesian info crit = -1206.185
    [[Variables]]
        c:   1.92346258 +/- 0.014485 (0.75%) (init= 1)



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


