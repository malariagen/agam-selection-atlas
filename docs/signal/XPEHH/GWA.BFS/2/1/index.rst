:orphan:




XPEHH/GWA.BFS/2/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **11,294,895** and
**11,354,895**.
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


The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP005170`:sup:`1`,  :doc:`../../../../../gene/AGAP005171` (Tctex1 domain-containing protein 4),  :doc:`../../../../../gene/AGAP005172`.



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP005169`:sup:`1`,  :doc:`../../../../../gene/AGAP005173` (Px serine/threonine kinase),  :doc:`../../../../../gene/AGAP005174` (nucleoporin SEH1),  :doc:`../../../../../gene/AGAP005175` (acetyl-CoA carboxylase / biotin carboxylase).


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
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 617
        # variables        = 4
        chi-square         = 107.244
        reduced chi-square = 0.175
        Akaike info crit   = -1071.604
        Bayesian info crit = -1053.904
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.34112504 +/- 0.131138 (5.60%) (init= 3)
        sigma:       0.15912420 +/- 0.011227 (7.06%) (init= 0.5)
        skew:       -0.01572317 +/- 0.083995 (534.21%) (init= 0)
        baseline:    1.23059904 +/- 0.017425 (1.42%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.537 
        C(sigma, skew)               = -0.229 
        C(sigma, baseline)           = -0.142 
        C(amplitude, baseline)       = -0.101 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 616
        # variables        = 1
        chi-square         = 178.113
        reduced chi-square = 0.290
        Akaike info crit   = -762.351
        Bayesian info crit = -757.928
    [[Variables]]
        c:   1.30420236 +/- 0.021682 (1.66%) (init= 1)



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


