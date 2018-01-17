:orphan:




XPEHH/BFM.BFS/2/4
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **11,114,895** and
**11,534,895**.
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


The following 18 genes overlap the focal region: :doc:`../../../../../gene/AGAP005164`,  :doc:`../../../../../gene/AGAP005165`,  :doc:`../../../../../gene/AGAP005166`:sup:`1`,  :doc:`../../../../../gene/AGAP005167`:sup:`1` (short chain dehydrogenase/3-oxoacyl-(acyl-carrier protein) reductase),  :doc:`../../../../../gene/AGAP005168`,  :doc:`../../../../../gene/AGAP005169`:sup:`1`,  :doc:`../../../../../gene/AGAP005170`:sup:`1`,  :doc:`../../../../../gene/AGAP005171` (Tctex1 domain-containing protein 4),  :doc:`../../../../../gene/AGAP005172`,  :doc:`../../../../../gene/AGAP005173` (Px serine/threonine kinase),  :doc:`../../../../../gene/AGAP005174` (nucleoporin SEH1),  :doc:`../../../../../gene/AGAP005175` (acetyl-CoA carboxylase / biotin carboxylase),  :doc:`../../../../../gene/AGAP005176` (cell division control protein 6),  :doc:`../../../../../gene/AGAP005177` (Intraflagellar transport 46 homolog),  :doc:`../../../../../gene/AGAP005178`,  :doc:`../../../../../gene/AGAP005179`,  :doc:`../../../../../gene/AGAP005180`,  :doc:`../../../../../gene/AGAP005181`.



No genes are within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/H12/GWA/2/3/index`
      - H12
      - Guinea Bissau
      - 2L:11,234,895-11,334,895
      - 208
      - 98.1%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 586
        # variables        = 4
        chi-square         = 77.255
        reduced chi-square = 0.133
        Akaike info crit   = -1179.360
        Bayesian info crit = -1161.867
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.70973407 +/- 0.051995 (7.33%) (init= 3)
        sigma:       1.01963761 +/- 0.090915 (8.92%) (init= 0.5)
        skew:       -0.50711117 +/- 0.095293 (18.79%) (init= 0)
        baseline:    1.42827439 +/- 0.019803 (1.39%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.419 
        C(amplitude, sigma)          = -0.391 
        C(amplitude, baseline)       = -0.274 
        C(sigma, skew)               =  0.199 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 585
        # variables        = 1
        chi-square         = 103.960
        reduced chi-square = 0.178
        Akaike info crit   = -1008.647
        Bayesian info crit = -1004.276
    [[Variables]]
        c:   1.57102149 +/- 0.017444 (1.11%) (init= 1)



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


