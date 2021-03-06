:orphan:




XPEHH/BFM.BFS/3/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3L** between positions **11,579,316** and
**11,659,316**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP010830` (TEP9 - thioester-containing protein 9),  :doc:`../../../../../gene/AGAP010831` (TEP8 - thioester-containing protein 8),  :doc:`../../../../../gene/AGAP010832` (TEP19 - thioester-containing protein 19),  :doc:`../../../../../gene/AGAP010833` (CLIPB14 - CLIP-domain serine protease).



Gene :doc:`../../../../../gene/AGAP010829` (CASPS12 - short caspase 12) is within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/XPEHH/BFM.GWA/3/2/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - 3L:11,599,316-11,659,316
      - 230
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/H12/BFM/3/4/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 3L:11,619,316-11,659,316
      - 95
      - 99.6%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 68
        # data points      = 347
        # variables        = 4
        chi-square         = 467.072
        reduced chi-square = 1.362
        Akaike info crit   = 111.114
        Bayesian info crit = 126.512
    [[Variables]]
        center:      0 (fixed)
        amplitude:   6.27341862 +/- 0.414322 (6.60%) (init= 3)
        decay:       0.51197305 +/- 0.056930 (11.12%) (init= 0.5)
        skew:        1          +/- 0.048914 (4.89%) (init= 0)
        baseline:    2.86043029 +/- 0.073744 (2.58%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.669 
        C(decay, baseline)           = -0.335 
        C(decay, skew)               = -0.207 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 346
        # variables        = 1
        chi-square         = 982.397
        reduced chi-square = 2.848
        Akaike info crit   = 363.071
        Bayesian info crit = 366.917
    [[Variables]]
        c:   3.45719578 +/- 0.090718 (2.62%) (init= 1)



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


