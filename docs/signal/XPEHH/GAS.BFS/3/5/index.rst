:orphan:




XPEHH/GAS.BFS/3/5
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **22,560,000** and
**22,600,000**.
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


Gene :doc:`../../../../../gene/AGAP008980` (LIM homeobox protein 2/9) overlaps the focal region.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008982` (CzcD (Cation-efflux system membrane protein)),  :doc:`../../../../../gene/AGAP008983`.


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
    * - :doc:`../../../../../signal/XPEHH/GAS.GWA/3/3/index`
      - XPEHH
      - Gabon *An. gambiae*
      - 3R:22,540,000-22,600,000
      - 110
      - 99.5%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/3/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 644
        # variables        = 4
        chi-square         = 193.292
        reduced chi-square = 0.302
        Akaike info crit   = -767.052
        Bayesian info crit = -749.182
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.78057049 +/- 0.194301 (10.91%) (init= 3)
        decay:       0.17762348 +/- 0.033278 (18.74%) (init= 0.5)
        skew:        0.90472813 +/- 0.205595 (22.72%) (init= 0)
        baseline:    1.99767738 +/- 0.023376 (1.17%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.590 
        C(decay, skew)               = -0.400 
        C(decay, baseline)           = -0.236 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 643
        # variables        = 1
        chi-square         = 233.379
        reduced chi-square = 0.364
        Akaike info crit   = -649.667
        Bayesian info crit = -645.201
    [[Variables]]
        c:   2.07217219 +/- 0.023777 (1.15%) (init= 1)



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


