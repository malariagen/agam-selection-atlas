:orphan:




IHS/UGS/2/5
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,160,000** and
**40,200,000**.
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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP003578`:sup:`1` (aldehyde dehydrogenase (NAD )),  :doc:`../../../../../gene/AGAP003579` (cadherin-87A).



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
    * - :doc:`../../../../../signal/IHS/CMS/2/2/index`
      - IHS
      - Cameroon *An. gambiae*
      - 2R:40,060,000-40,780,000
      - 643
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/IHS/GNS/2/3/index`
      - IHS
      - Guinea *An. gambiae*
      - 2R:40,200,000-40,420,000
      - 450
      - 99.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 65
        # data points      = 572
        # variables        = 4
        chi-square         = 110.807
        reduced chi-square = 0.195
        Akaike info crit   = -930.853
        Bayesian info crit = -913.457
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.37530358 +/- 0.138506 (10.07%) (init= 3)
        decay:       0.35094332 +/- 0.060638 (17.28%) (init= 0.5)
        skew:       -0.99999999 +/- 0.059371 (5.94%) (init= 0)
        baseline:    2.35799341 +/- 0.021225 (0.90%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.595 
        C(decay, skew)               =  0.433 
        C(decay, baseline)           = -0.319 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 571
        # variables        = 1
        chi-square         = 140.592
        reduced chi-square = 0.247
        Akaike info crit   = -798.270
        Bayesian info crit = -793.923
    [[Variables]]
        c:   2.45453942 +/- 0.020783 (0.85%) (init= 1)



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


