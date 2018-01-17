:orphan:




H12/AOM/2/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **8,280,000** and
**8,340,000**.
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


Gene :doc:`../../../../../gene/AGAP001683` (calcium/calmodulin-dependent serine protein kinase) overlaps the focal region.



Gene :doc:`../../../../../gene/AGAP001684` (Alkaline phosphatase) is within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/IHS/AOM/2/2/index`
      - IHS
      - Angola *An. coluzzii*
      - 2R:8,160,000-8,280,000
      - 230
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/2/4/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2R:8,120,000-8,320,000
      - 107
      - 78.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 383
        # variables        = 4
        chi-square         = 0.045
        reduced chi-square = 0.000
        Akaike info crit   = -3455.311
        Bayesian info crit = -3439.519
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.10816294 +/- 0.004316 (3.99%) (init= 0.5)
        decay:       0.51483367 +/- 0.031552 (6.13%) (init= 0.5)
        skew:        0.06628217 +/- 0.057518 (86.78%) (init= 0)
        baseline:    0.02625101 +/- 0.000652 (2.48%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.651 
        C(decay, baseline)           = -0.390 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 382
        # variables        = 1
        chi-square         = 0.157
        reduced chi-square = 0.000
        Akaike info crit   = -2975.577
        Bayesian info crit = -2971.631
    [[Variables]]
        c:   0.03316572 +/- 0.001039 (3.14%) (init= 0.03)



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


