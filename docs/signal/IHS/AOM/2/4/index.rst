:orphan:




IHS/AOM/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **33,414,895** and
**33,634,895**.
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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP006514`,  :doc:`../../../../../gene/AGAP006515` (Multiplexin transcript 1).



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
      - Peak model :math:`\Delta_{i}`
      - Max. percentile
      - Known locus
    * - :doc:`../../../../../signal/H12/AOM/2/5/index`
      - H12
      - Angola *An. coluzzii*
      - 2L:33,434,895-33,514,895
      - 290
      - 96.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/2/4/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2L:33,454,895-33,594,895
      - 173
      - 98.8%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/2/3/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2L:33,434,895-33,594,895
      - 161
      - 92.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/AOM/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/AOM/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/AOM/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 335
        # variables        = 4
        chi-square         = 89.153
        reduced chi-square = 0.269
        Akaike info crit   = -435.466
        Bayesian info crit = -420.210
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.55833174 +/- 0.215683 (8.43%) (init= 3)
        decay:       0.51889341 +/- 0.073239 (14.11%) (init= 0.5)
        skew:       -0.90963550 +/- 0.142560 (15.67%) (init= 0)
        baseline:    2.56715306 +/- 0.034696 (1.35%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.585 
        C(decay, baseline)           = -0.430 
        C(decay, skew)               =  0.387 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 334
        # variables        = 1
        chi-square         = 144.222
        reduced chi-square = 0.433
        Akaike info crit   = -278.489
        Bayesian info crit = -274.678
    [[Variables]]
        c:   2.74027063 +/- 0.036008 (1.31%) (init= 1)



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


