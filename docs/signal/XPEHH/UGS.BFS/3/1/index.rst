:orphan:




XPEHH/UGS.BFS/3/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **37,140,000** and
**37,220,000**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP009622` (6-phosphofructo-2-kinase / fructose-2,6-bisphosphatase),  :doc:`../../../../../gene/AGAP009623`:sup:`1` (GAPDH - glyceraldehyde 3-phosphate dehydrogenase),  :doc:`../../../../../gene/AGAP009624` (CTPsyn - CTP synthase),  :doc:`../../../../../gene/AGAP009625`.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009626` (Kv channel-interacting protein 4 isoform 2),  :doc:`../../../../../gene/AGAP009627`.


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
    * - :doc:`../../../../../signal/XPEHH/UGS.CMS/3/1/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:37,120,000-37,200,000
      - 300
      - 99.5%
      - nan
    * - :doc:`../../../../../signal/H12/UGS/3/5/index`
      - H12
      - Uganda *An. gambiae*
      - 3R:36,460,000-37,520,000
      - 206
      - 94.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 69
        # data points      = 666
        # variables        = 4
        chi-square         = 597.531
        reduced chi-square = 0.903
        Akaike info crit   = -64.250
        Bayesian info crit = -46.245
    [[Variables]]
        center:      0 (fixed)
        amplitude:   4.29928750 +/- 0.283664 (6.60%) (init= 3)
        sigma:       0.15000000 +/- 3.00e-07 (0.00%) (init= 0.5)
        skew:       -0.64090888 +/- 0.107061 (16.70%) (init= 0)
        baseline:    2.32045383 +/- 0.037973 (1.64%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          =  0.553 
        C(sigma, skew)               = -0.175 
        C(sigma, baseline)           =  0.120 
        C(amplitude, baseline)       = -0.105 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 665
        # variables        = 1
        chi-square         = 873.040
        reduced chi-square = 1.315
        Akaike info crit   = 183.009
        Bayesian info crit = 187.509
    [[Variables]]
        c:   2.46073930 +/- 0.044464 (1.81%) (init= 1)



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


