:orphan:




IHS/GWA/3/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **660,000** and
**700,000**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).





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


Gene :doc:`../../../../../gene/AGAP007776` overlaps the focal region.



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007775` (ATP-dependent DNA helicase PIF1),  :doc:`../../../../../gene/AGAP007777`,  :doc:`../../../../../gene/AGAP007778` (DNA-directed RNA polymerase, mitochondrial).


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
    * - :doc:`../../../../../signal/XPEHH/GWA.UGS/3/1/index`
      - XPEHH
      - Guinea Bissau
      - 3R:660,000-700,000
      - 346
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GWA.BFS/3/1/index`
      - XPEHH
      - Guinea Bissau
      - 3R:660,000-700,000
      - 313
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GAS.BFS/3/2/index`
      - XPEHH
      - Gabon *An. gambiae*
      - 3R:520,000-680,000
      - 178
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GWA/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GWA/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GWA/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 447
        # variables        = 4
        chi-square         = 48.367
        reduced chi-square = 0.109
        Akaike info crit   = -986.010
        Bayesian info crit = -969.600
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.24243614 +/- 0.122629 (5.47%) (init= 3)
        decay:       0.25774667 +/- 0.022867 (8.87%) (init= 0.5)
        skew:        0.99999881 +/- 0.090532 (9.05%) (init= 0)
        baseline:    2.12873991 +/- 0.017367 (0.82%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.636 
        C(decay, skew)               = -0.284 
        C(decay, baseline)           = -0.276 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 446
        # variables        = 1
        chi-square         = 110.055
        reduced chi-square = 0.247
        Akaike info crit   = -622.106
        Bayesian info crit = -618.006
    [[Variables]]
        c:   2.26967715 +/- 0.023548 (1.04%) (init= 1)



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


