:orphan:




XPEHH/CMS.GWA/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,680,000** and
**40,760,000**.
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


The following 8 genes overlap the focal region: :doc:`../../../../../gene/AGAP029110`,  :doc:`../../../../../gene/AGAP003626`,  :doc:`../../../../../gene/AGAP013221`,  :doc:`../../../../../gene/AGAP012946`,  :doc:`../../../../../gene/AGAP003627`,  :doc:`../../../../../gene/AGAP003629`,  :doc:`../../../../../gene/AGAP003630`,  :doc:`../../../../../gene/AGAP003631` (GPRGRP2 - putative gastrin/bombesin receptor 2).



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003624`,  :doc:`../../../../../gene/AGAP003632` (U3 small nucleolar RNA-associated protein 14),  :doc:`../../../../../gene/AGAP003633`,  :doc:`../../../../../gene/AGAP003635`,  :doc:`../../../../../gene/AGAP003636`:sup:`1` (inositol oxygenase).


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
    * - :doc:`../../../../../signal/H12/CMS/2/3/index`
      - H12
      - Cameroon *An. gambiae*
      - 2R:40,300,000-40,740,000
      - 501
      - 98.7%
      - nan
    * - :doc:`../../../../../signal/H12/BFS/2/4/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2R:40,640,000-41,060,000
      - 384
      - 95.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GWA/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GWA/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GWA/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 277
        # data points      = 434
        # variables        = 4
        chi-square         = 103.334
        reduced chi-square = 0.240
        Akaike info crit   = -614.824
        Bayesian info crit = -598.532
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.02939858 +/- 0.092249 (8.96%) (init= 3)
        decay:       2.99994449 +/- 0.604325 (20.14%) (init= 0.5)
        skew:       -0.99999980 +/- 0.141134 (14.11%) (init= 0)
        baseline:    1.37600164 +/- 0.083851 (6.09%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.836 
        C(amplitude, baseline)       = -0.732 
        C(amplitude, decay)          =  0.357 
        C(decay, skew)               = -0.307 
        C(amplitude, skew)           = -0.267 
        C(skew, baseline)            =  0.263 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 433
        # variables        = 1
        chi-square         = 131.503
        reduced chi-square = 0.304
        Akaike info crit   = -514.008
        Bayesian info crit = -509.938
    [[Variables]]
        c:   1.84882268 +/- 0.026514 (1.43%) (init= 1)



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


