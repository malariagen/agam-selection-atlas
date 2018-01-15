:orphan:




H12/BFS/2/5
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **25,454,895** and
**25,534,895**.
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




The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP006030` (mfrn - mitoferrin),  :doc:`../../../../../gene/AGAP006031` (nuclear pore complex protein Nup54),  :doc:`../../../../../gene/AGAP006032`,  :doc:`../../../../../gene/AGAP006033`,  :doc:`../../../../../gene/AGAP006034`,  :doc:`../../../../../gene/AGAP006035` (Ras-related protein Rab-36),  :doc:`../../../../../gene/AGAP006036` (axonemal dynein intermediate chain inner arm i1),  :doc:`../../../../../gene/AGAP006037` (RpL24 - 60S ribosomal protein L24),  :doc:`../../../../../gene/AGAP006038` (serine/arginine repetitive matrix protein 2),  :doc:`../../../../../gene/AGAP006039`.




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006028`:sup:`2` (Rdl - GABA-gated chloride channel subunit),  :doc:`../../../../../gene/AGAP006029`,  :doc:`../../../../../gene/AGAP006040` (peroxisomal membrane protein 2),  :doc:`../../../../../gene/AGAP006041` (E3 ubiquitin-protein ligase RNF5),  :doc:`../../../../../gene/AGAP006042`,  :doc:`../../../../../gene/AGAP029130`,  :doc:`../../../../../gene/AGAP029102`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

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
    * - :doc:`../../../../../signal/H12/BFM/2/2/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 2L:25,434,895-25,494,895
      - 1,172
      - 98.4%
    * - :doc:`../../../../../signal/H12/GAS/2/1/index`
      - H12
      - Gabon *An. gambiae*
      - 2L:25,454,895-25,514,895
      - 529
      - 100.0%
    * - :doc:`../../../../../signal/H12/GNS/2/4/index`
      - H12
      - Guinea *An. gambiae*
      - 2L:25,534,895-25,814,895
      - 332
      - 97.8%
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/2/6/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2L:25,434,895-25,474,895
      - 138
      - 95.3%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 400
        # variables        = 4
        chi-square         = 0.080
        reduced chi-square = 0.000
        Akaike info crit   = -3398.830
        Bayesian info crit = -3382.864
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.11275310 +/- 0.005608 (4.97%) (init= 0.5)
        decay:       0.50705590 +/- 0.038859 (7.66%) (init= 0.5)
        skew:        0.24344101 +/- 0.072751 (29.88%) (init= 0)
        baseline:    0.01938939 +/- 0.000825 (4.25%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.649 
        C(decay, baseline)           = -0.382 
        C(decay, skew)               = -0.110 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 399
        # variables        = 1
        chi-square         = 0.203
        reduced chi-square = 0.001
        Akaike info crit   = -3022.891
        Bayesian info crit = -3018.902
    [[Variables]]
        c:   0.02629295 +/- 0.001131 (4.31%) (init= 0.03)



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


