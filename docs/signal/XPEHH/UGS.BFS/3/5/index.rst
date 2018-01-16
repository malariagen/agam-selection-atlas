:orphan:




XPEHH/UGS.BFS/3/5
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **49,540,000** and
**49,660,000**.
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


The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP013739`,  :doc:`../../../../../gene/AGAP010156` (ATP citrate lyase),  :doc:`../../../../../gene/AGAP013762`,  :doc:`../../../../../gene/AGAP010157` (Ast2 - allatostatin 2),  :doc:`../../../../../gene/AGAP010158`.



The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010149` (cytochrome b5-related),  :doc:`../../../../../gene/AGAP010150`:sup:`1` (cytochrome b5-related),  :doc:`../../../../../gene/AGAP010151`,  :doc:`../../../../../gene/AGAP010152` (gem associated protein 5),  :doc:`../../../../../gene/AGAP010155`,  :doc:`../../../../../gene/AGAP010159` (dUTP pyrophosphatase),  :doc:`../../../../../gene/AGAP010160` (myosin I),  :doc:`../../../../../gene/AGAP010161`.


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
    * - :doc:`../../../../../signal/H12/UGS/3/2/index`
      - H12
      - Uganda *An. gambiae*
      - 3R:49,660,000-49,880,000
      - 427
      - 93.3%
      - nan
    * - :doc:`../../../../../signal/H12/GWA/3/1/index`
      - H12
      - Guinea Bissau
      - 3R:49,480,000-49,620,000
      - 165
      - 93.8%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 294
        # variables        = 4
        chi-square         = 310.138
        reduced chi-square = 1.069
        Akaike info crit   = 23.711
        Bayesian info crit = 38.445
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.65141422 +/- 0.242118 (9.13%) (init= 3)
        decay:       1.54995334 +/- 0.322812 (20.83%) (init= 0.5)
        skew:        0.00080005 +/- 0.139208 (17399.94%) (init= 0)
        baseline:    2.45517662 +/- 0.125477 (5.11%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.753 
        C(amplitude, decay)          = -0.344 
        C(amplitude, baseline)       = -0.162 
        C(decay, skew)               =  0.127 
        C(skew, baseline)            = -0.111 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 293
        # variables        = 1
        chi-square         = 433.901
        reduced chi-square = 1.486
        Akaike info crit   = 117.044
        Bayesian info crit = 120.725
    [[Variables]]
        c:   3.10251982 +/- 0.071210 (2.30%) (init= 1)



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


