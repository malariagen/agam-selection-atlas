:orphan:




IHS/AOM/X/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**X** between positions **4,280,000** and
**4,360,000**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP000228` (netrin 1),  :doc:`../../../../../gene/AGAP000230`:sup:`3` (Or52 - odorant receptor 52),  :doc:`../../../../../gene/AGAP012975`:sup:`2` (histamine-gated chloride channel subunit),  :doc:`../../../../../gene/AGAP000232` (regulator of G-protein signaling).



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000225` (netrin 1),  :doc:`../../../../../gene/AGAP013512`,  :doc:`../../../../../gene/AGAP000226`:sup:`3` (Or41 - odorant receptor 41),  :doc:`../../../../../gene/AGAP000233`,  :doc:`../../../../../gene/AGAP000234`,  :doc:`../../../../../gene/AGAP013530`.


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
    * - :doc:`../../../../../signal/H12/AOM/X/1/index`
      - H12
      - Angola *An. coluzzii*
      - X:4,340,000-4,380,000
      - 519
      - 97.8%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/X/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:4,320,000-4,360,000
      - 292
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/X/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:4,340,000-4,380,000
      - 242
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GAS/X/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:4,340,000-4,420,000
      - 137
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/AOM/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/AOM/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/AOM/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 427
        # variables        = 4
        chi-square         = 88.964
        reduced chi-square = 0.210
        Akaike info crit   = -661.771
        Bayesian info crit = -645.544
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.59419983 +/- 0.188252 (7.26%) (init= 3)
        sigma:       0.19079701 +/- 0.016400 (8.60%) (init= 0.5)
        skew:       -0.83075072 +/- 0.102824 (12.38%) (init= 0)
        baseline:    2.40322306 +/- 0.023017 (0.96%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.525 
        C(sigma, skew)               =  0.400 
        C(sigma, baseline)           = -0.145 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 426
        # variables        = 1
        chi-square         = 136.239
        reduced chi-square = 0.321
        Akaike info crit   = -483.652
        Bayesian info crit = -479.597
    [[Variables]]
        c:   2.47764365 +/- 0.027431 (1.11%) (init= 1)



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


