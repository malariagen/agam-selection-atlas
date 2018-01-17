:orphan:




XPEHH/AOM.GWA/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **33,434,895** and
**33,594,895**.
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


Gene :doc:`../../../../../gene/AGAP006514` overlaps the focal region.



Gene :doc:`../../../../../gene/AGAP006515` (Multiplexin transcript 1) is within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/IHS/AOM/2/4/index`
      - IHS
      - Angola *An. coluzzii*
      - 2L:33,414,895-33,634,895
      - 156
      - 99.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 183
        # variables        = 4
        chi-square         = 36.766
        reduced chi-square = 0.205
        Akaike info crit   = -285.700
        Bayesian info crit = -272.862
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.58325070 +/- 0.102600 (6.48%) (init= 3)
        sigma:       0.53949479 +/- 0.058312 (10.81%) (init= 0.5)
        skew:       -0.99999999 +/- 0.073252 (7.33%) (init= 0)
        baseline:    1.45278437 +/- 0.042976 (2.96%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               = -0.487 
        C(amplitude, sigma)          = -0.345 
        C(amplitude, baseline)       = -0.335 
        C(sigma, baseline)           = -0.312 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 182
        # variables        = 1
        chi-square         = 91.015
        reduced chi-square = 0.503
        Akaike info crit   = -124.123
        Bayesian info crit = -120.919
    [[Variables]]
        c:   1.81513421 +/- 0.052563 (2.90%) (init= 1)



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


