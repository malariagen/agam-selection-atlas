:orphan:




XPEHH/GWA.BFS/2/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **31,874,895** and
**32,014,895**.
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


The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP028457`,  :doc:`../../../../../gene/AGAP006437`,  :doc:`../../../../../gene/AGAP006438` (ribosomal biogenesis protein LAS1),  :doc:`../../../../../gene/AGAP006439` (fringe),  :doc:`../../../../../gene/AGAP006440` (IR136 - ionotropic receptor IR136).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006436` (Med13 - mediator of RNA polymerase II transcription subunit 13),  :doc:`../../../../../gene/AGAP006441` (GTP cyclohydrolase I),  :doc:`../../../../../gene/AGAP006442`.


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
    * - :doc:`../../../../../signal/XPEHH/GWA.UGS/2/1/index`
      - XPEHH
      - Guinea Bissau
      - 2L:31,914,895-32,034,895
      - 430
      - 93.3%
      - nan
    * - :doc:`../../../../../signal/H12/GWA/2/1/index`
      - H12
      - Guinea Bissau
      - 2L:31,954,895-31,994,895
      - 382
      - 99.2%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GWA.BFM/2/3/index`
      - XPEHH
      - Guinea Bissau
      - 2L:31,934,895-32,014,895
      - 175
      - 99.6%
      - nan
    * - :doc:`../../../../../signal/IHS/GWA/2/2/index`
      - IHS
      - Guinea Bissau
      - 2L:31,834,895-31,914,895
      - 93
      - 99.8%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 490
        # variables        = 4
        chi-square         = 45.660
        reduced chi-square = 0.094
        Akaike info crit   = -1154.860
        Bayesian info crit = -1138.082
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.35640193 +/- 0.079007 (5.82%) (init= 3)
        sigma:       0.19166225 +/- 0.017461 (9.11%) (init= 0.5)
        skew:        0.47623514 +/- 0.109127 (22.91%) (init= 0)
        baseline:    1.51990313 +/- 0.014529 (0.96%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.513 
        C(sigma, skew)               = -0.236 
        C(amplitude, baseline)       = -0.154 
        C(sigma, baseline)           = -0.138 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 489
        # variables        = 1
        chi-square         = 78.437
        reduced chi-square = 0.161
        Akaike info crit   = -892.902
        Bayesian info crit = -888.709
    [[Variables]]
        c:   1.59325148 +/- 0.018129 (1.14%) (init= 1)



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


