:orphan:




IHS/BFM/3/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **18,600,000** and
**19,000,000**.
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


The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP028559`,  :doc:`../../../../../gene/AGAP008823`,  :doc:`../../../../../gene/AGAP008824`,  :doc:`../../../../../gene/AGAP008825`,  :doc:`../../../../../gene/AGAP008826`.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008822` (FK506-binding protein 14),  :doc:`../../../../../gene/AGAP028025`.


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
    * - :doc:`../../../../../signal/IHS/UGS/3/2/index`
      - IHS
      - Uganda *An. gambiae*
      - 3R:18,760,000-19,000,000
      - 327
      - 92.9%
      - nan
    * - :doc:`../../../../../signal/IHS/BFS/3/5/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3R:18,760,000-18,920,000
      - 297
      - 90.4%
      - nan
    * - :doc:`../../../../../signal/H12/UGS/3/4/index`
      - H12
      - Uganda *An. gambiae*
      - 3R:18,780,000-19,000,000
      - 210
      - 72.4%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 592
        # variables        = 4
        chi-square         = 167.602
        reduced chi-square = 0.285
        Akaike info crit   = -739.055
        Bayesian info crit = -721.521
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.17425164 +/- 0.077218 (6.58%) (init= 3)
        sigma:       1.25026645 +/- 0.102383 (8.19%) (init= 0.5)
        skew:        0.14592530 +/- 0.084156 (57.67%) (init= 0)
        baseline:    1.97146072 +/- 0.028839 (1.46%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.433 
        C(sigma, baseline)           = -0.428 
        C(amplitude, baseline)       = -0.248 
        C(sigma, skew)               = -0.160 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 591
        # variables        = 1
        chi-square         = 242.728
        reduced chi-square = 0.411
        Akaike info crit   = -523.916
        Bayesian info crit = -519.534
    [[Variables]]
        c:   2.20386496 +/- 0.026383 (1.20%) (init= 1)



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


