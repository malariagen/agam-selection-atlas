:orphan:




H12/BFS/X/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **9,180,000** and
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
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:9,200,000-9,240,000
      - 744
      - 99.5%
    * - :doc:`../../../../../signal/IHS/BFS/X/1/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - X:9,160,000-9,680,000
      - 515
      - 99.7%
    * - :doc:`../../../../../signal/H12/BFM/X/2/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - X:9,220,000-9,260,000
      - 221
      - 96.9%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 399
        # variables        = 4
        chi-square         = 0.082
        reduced chi-square = 0.000
        Akaike info crit   = -3379.810
        Bayesian info crit = -3363.854
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.22379636 +/- 0.006861 (3.07%) (init= 0.5)
        sigma:       0.15000000 +/- 0.000954 (0.64%) (init= 0.5)
        skew:        0.00980240 +/- 0.041584 (424.22%) (init= 0)
        baseline:    0.02042294 +/- 0.000739 (3.62%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          =  0.561 
        C(sigma, baseline)           =  0.131 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 398
        # variables        = 1
        chi-square         = 0.335
        reduced chi-square = 0.001
        Akaike info crit   = -2816.113
        Bayesian info crit = -2812.126
    [[Variables]]
        c:   0.02503642 +/- 0.001455 (5.81%) (init= 0.03)



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


