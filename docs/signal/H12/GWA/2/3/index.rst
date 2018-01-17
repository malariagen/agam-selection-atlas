:orphan:




H12/GWA/2/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **11,234,895** and
**11,334,895**.
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


The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP005165`,  :doc:`../../../../../gene/AGAP005169`:sup:`1`,  :doc:`../../../../../gene/AGAP005170`:sup:`1`.



The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP005166`:sup:`1`,  :doc:`../../../../../gene/AGAP005167`:sup:`1` (short chain dehydrogenase/3-oxoacyl-(acyl-carrier protein) reductase),  :doc:`../../../../../gene/AGAP005168`,  :doc:`../../../../../gene/AGAP005171` (Tctex1 domain-containing protein 4),  :doc:`../../../../../gene/AGAP005172`,  :doc:`../../../../../gene/AGAP005173` (Px serine/threonine kinase),  :doc:`../../../../../gene/AGAP005174` (nucleoporin SEH1),  :doc:`../../../../../gene/AGAP005175` (acetyl-CoA carboxylase / biotin carboxylase).


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
    * - :doc:`../../../../../signal/XPEHH/GWA.BFS/2/1/index`
      - XPEHH
      - Guinea Bissau
      - 2L:11,294,895-11,354,895
      - 309
      - 98.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GWA.BFM/2/1/index`
      - XPEHH
      - Guinea Bissau
      - 2L:11,274,895-11,354,895
      - 304
      - 99.8%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFM.BFS/2/4/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - 2L:11,114,895-11,534,895
      - 170
      - 88.1%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 389
        # variables        = 4
        chi-square         = 0.267
        reduced chi-square = 0.001
        Akaike info crit   = -2826.231
        Bayesian info crit = -2810.377
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.17859913 +/- 0.013447 (7.53%) (init= 0.5)
        decay:       0.29114147 +/- 0.033252 (11.42%) (init= 0.5)
        skew:       -0.47836207 +/- 0.114459 (23.93%) (init= 0)
        baseline:    0.05445297 +/- 0.001453 (2.67%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.660 
        C(decay, baseline)           = -0.286 
        C(decay, skew)               =  0.223 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 388
        # variables        = 1
        chi-square         = 0.453
        reduced chi-square = 0.001
        Akaike info crit   = -2618.109
        Bayesian info crit = -2614.148
    [[Variables]]
        c:   0.06099757 +/- 0.001736 (2.85%) (init= 0.03)



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


