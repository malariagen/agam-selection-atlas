:orphan:




IHS/AOM/2/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **8,160,000** and
**8,280,000**.
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


The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP001679`,  :doc:`../../../../../gene/AGAP001680`,  :doc:`../../../../../gene/AGAP001681` (ubiquitin conjugation factor E4 A),  :doc:`../../../../../gene/AGAP001682` (Mitochondrial inner membrane protease subunit 1),  :doc:`../../../../../gene/AGAP001683` (calcium/calmodulin-dependent serine protein kinase).



Gene :doc:`../../../../../gene/AGAP013310` is within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/H12/AOM/2/1/index`
      - H12
      - Angola *An. coluzzii*
      - 2R:8,280,000-8,340,000
      - 479
      - 97.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/2/5/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2R:8,140,000-8,240,000
      - 168
      - 89.0%
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
    <img src="../../../../../_static/data/signal/IHS/AOM/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/AOM/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/AOM/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 464
        # variables        = 4
        chi-square         = 92.431
        reduced chi-square = 0.201
        Akaike info crit   = -740.626
        Bayesian info crit = -724.066
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.74654184 +/- 0.122176 (7.00%) (init= 3)
        decay:       0.67862400 +/- 0.088614 (13.06%) (init= 0.5)
        skew:       -0.99999997 +/- 0.131122 (13.11%) (init= 0)
        baseline:    2.35261989 +/- 0.025754 (1.09%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.571 
        C(decay, baseline)           = -0.407 
        C(decay, skew)               =  0.389 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 463
        # variables        = 1
        chi-square         = 153.185
        reduced chi-square = 0.332
        Akaike info crit   = -510.114
        Bayesian info crit = -505.977
    [[Variables]]
        c:   2.53660000 +/- 0.026760 (1.05%) (init= 1)



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


