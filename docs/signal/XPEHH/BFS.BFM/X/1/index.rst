:orphan:




XPEHH/BFS.BFM/X/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/BFM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**X** between positions **9,200,000** and
**9,240,000**.
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


Gene :doc:`../../../../../gene/AGAP000519` (diacylglycerol kinase (ATP dependent)) overlaps the focal region.



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
      - Peak Model :math:`\Delta_{i}`
      - Max Percentile
      - Known Loci
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,200,000-9,240,000
      - 744
      - 99.5%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/X/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,220,000-9,260,000
      - 678
      - 99.8%
      - nan
    * - :doc:`../../../../../signal/H12/BFS/X/2/index`
      - H12
      - Burkina Faso *An. gambiae*
      - X:9,180,000-9,240,000
      - 563
      - 97.8%
      - nan
    * - :doc:`../../../../../signal/IHS/BFS/X/1/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - X:9,160,000-9,680,000
      - 515
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/X/2/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - X:9,040,000-9,300,000
      - 394
      - 97.4%
      - nan
    * - :doc:`../../../../../signal/H12/BFM/X/2/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - X:9,220,000-9,260,000
      - 221
      - 96.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFM.GWA/X/2/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - X:9,200,000-9,240,000
      - 186
      - 71.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.BFM/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.BFM/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.BFM/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 54
        # data points      = 805
        # variables        = 4
        chi-square         = 79.507
        reduced chi-square = 0.099
        Akaike info crit   = -1855.570
        Bayesian info crit = -1836.806
    [[Variables]]
        center:      0 (fixed)
        amplitude:   3.48858105 +/- 0.101749 (2.92%) (init= 3)
        sigma:       0.15000000 +/- 0.002888 (1.93%) (init= 0.5)
        skew:       -0.01783724 +/- 0.041341 (231.77%) (init= 0)
        baseline:    1.05838524 +/- 0.011399 (1.08%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.547 
        C(sigma, baseline)           = -0.133 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 804
        # variables        = 1
        chi-square         = 229.139
        reduced chi-square = 0.285
        Akaike info crit   = -1007.239
        Bayesian info crit = -1002.549
    [[Variables]]
        c:   1.13876644 +/- 0.018839 (1.65%) (init= 1)



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


