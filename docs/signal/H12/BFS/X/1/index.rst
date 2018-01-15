:orphan:




H12/BFS/X/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **15,100,000** and
**15,240,000**.
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



Gene :doc:`../../../../../gene/AGAP012997` overlaps the focal region.





The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013173`,  :doc:`../../../../../gene/AGAP013424`,  :doc:`../../../../../gene/AGAP000818`:sup:`1` (CYP9K1 - cytochrome P450),  :doc:`../../../../../gene/AGAP000819` (nuclear receptor subfamily 2 group E member (Tailless)),  :doc:`../../../../../gene/AGAP000820`:sup:`4` (CPR125 - cuticular protein RR-2 family 125).


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
    * - :doc:`../../../../../signal/H12/BFM/X/1/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - X:15,100,000-15,300,000
      - 1,267
      - 100.0%
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:15,060,000-15,220,000
      - 866
      - 99.6%
    * - :doc:`../../../../../signal/H12/GNS/X/1/index`
      - H12
      - Guinea *An. gambiae*
      - X:14,960,000-15,160,000
      - 419
      - 97.8%
    * - :doc:`../../../../../signal/H12/UGS/X/1/index`
      - H12
      - Uganda *An. gambiae*
      - X:15,160,000-15,480,000
      - 348
      - 94.9%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 390
        # variables        = 4
        chi-square         = 0.270
        reduced chi-square = 0.001
        Akaike info crit   = -2829.987
        Bayesian info crit = -2814.122
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.45779005 +/- 0.010859 (2.37%) (init= 0.5)
        decay:       0.55030854 +/- 0.019193 (3.49%) (init= 0.5)
        skew:       -0.00978529 +/- 0.033310 (340.41%) (init= 0)
        baseline:    0.03622306 +/- 0.001565 (4.32%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.635 
        C(decay, baseline)           = -0.403 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 389
        # variables        = 1
        chi-square         = 2.180
        reduced chi-square = 0.006
        Akaike info crit   = -2014.602
        Bayesian info crit = -2010.638
    [[Variables]]
        c:   0.06318650 +/- 0.003800 (6.02%) (init= 0.03)



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


