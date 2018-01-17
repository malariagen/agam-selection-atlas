:orphan:




XPEHH/BFS.GWA/2/5
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,780,000** and
**40,820,000**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP003632` (U3 small nucleolar RNA-associated protein 14),  :doc:`../../../../../gene/AGAP003633`,  :doc:`../../../../../gene/AGAP003635`,  :doc:`../../../../../gene/AGAP003636`:sup:`1` (inositol oxygenase).



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003631` (GPRGRP2 - putative gastrin/bombesin receptor 2),  :doc:`../../../../../gene/AGAP003638`.


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
    * - :doc:`../../../../../signal/IHS/CMS/2/2/index`
      - IHS
      - Cameroon *An. gambiae*
      - 2R:40,060,000-40,780,000
      - 643
      - 100.0%
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
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 399
        # variables        = 4
        chi-square         = 67.588
        reduced chi-square = 0.171
        Akaike info crit   = -700.438
        Bayesian info crit = -684.482
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.80634668 +/- 0.134130 (7.43%) (init= 3)
        decay:       0.32487711 +/- 0.043890 (13.51%) (init= 0.5)
        skew:       -0.99999999 +/- 0.022109 (2.21%) (init= 0)
        baseline:    1.56261670 +/- 0.023649 (1.51%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.571 
        C(decay, baseline)           = -0.321 
        C(decay, skew)               = -0.285 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 398
        # variables        = 1
        chi-square         = 111.365
        reduced chi-square = 0.281
        Akaike info crit   = -504.909
        Bayesian info crit = -500.922
    [[Variables]]
        c:   1.69592922 +/- 0.026548 (1.57%) (init= 1)



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


