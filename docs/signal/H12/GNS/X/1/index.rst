:orphan:




H12/GNS/X/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **14,960,000** and
**15,160,000**.
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


The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP000817`,  :doc:`../../../../../gene/AGAP000816`,  :doc:`../../../../../gene/AGAP013474`,  :doc:`../../../../../gene/AGAP013173`,  :doc:`../../../../../gene/AGAP013424`.



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000813`:sup:`1` (Frataxin homolog, mitochondrial),  :doc:`../../../../../gene/AGAP000814`,  :doc:`../../../../../gene/AGAP000815` (INTB - integrin beta subunit),  :doc:`../../../../../gene/AGAP012997`.


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
    * - :doc:`../../../../../signal/H12/BFM/X/1/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - X:15,100,000-15,300,000
      - 1,267
      - 100.0%
      - Cyp9k1
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/X/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:14,960,000-15,140,000
      - 961
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:15,060,000-15,220,000
      - 866
      - 99.6%
      - Cyp9k1
    * - :doc:`../../../../../signal/XPEHH/BFM.GWA/X/1/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - X:15,060,000-15,260,000
      - 852
      - 99.4%
      - Cyp9k1
    * - :doc:`../../../../../signal/H12/BFS/X/1/index`
      - H12
      - Burkina Faso *An. gambiae*
      - X:15,100,000-15,240,000
      - 815
      - 98.5%
      - Cyp9k1
    * - :doc:`../../../../../signal/IHS/UGS/X/1/index`
      - IHS
      - Uganda *An. gambiae*
      - X:14,640,000-15,360,000
      - 517
      - 96.7%
      - Cyp9k1
    * - :doc:`../../../../../signal/XPEHH/BFM.AOM/X/1/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - X:15,040,000-15,180,000
      - 511
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/X/1/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - X:14,760,000-15,620,000
      - 501
      - 100.0%
      - Cyp9k1
    * - :doc:`../../../../../signal/IHS/BFS/X/2/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - X:14,660,000-14,980,000
      - 477
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/H12/UGS/X/1/index`
      - H12
      - Uganda *An. gambiae*
      - X:15,160,000-15,480,000
      - 348
      - 94.9%
      - Cyp9k1
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/X/2/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:14,500,000-15,180,000
      - 228
      - 98.5%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/X/1/index`
      - XPEHH
      - Uganda *An. gambiae*
      - X:14,960,000-15,320,000
      - 204
      - 89.8%
      - Cyp9k1
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 390
        # variables        = 4
        chi-square         = 0.319
        reduced chi-square = 0.001
        Akaike info crit   = -2763.853
        Bayesian info crit = -2747.988
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.20975127 +/- 0.009350 (4.46%) (init= 0.5)
        sigma:       0.43477158 +/- 0.021609 (4.97%) (init= 0.5)
        skew:       -0.79004841 +/- 0.055960 (7.08%) (init= 0)
        baseline:    0.04788523 +/- 0.001586 (3.31%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.557 
        C(sigma, skew)               =  0.389 
        C(sigma, baseline)           = -0.229 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 389
        # variables        = 1
        chi-square         = 0.935
        reduced chi-square = 0.002
        Akaike info crit   = -2344.157
        Bayesian info crit = -2340.194
    [[Variables]]
        c:   0.06114961 +/- 0.002488 (4.07%) (init= 0.03)



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


