:orphan:




XPEHH/BFM.AOM/2/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/AOM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **24,840,000** and
**24,880,000**.
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


The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP002638` (ABCH1 - ATP-binding cassette transporter (ABC transporter) family H member 1),  :doc:`../../../../../gene/AGAP002639`:sup:`3` (Or39 - odorant receptor 39),  :doc:`../../../../../gene/AGAP002640`:sup:`3` (Or38 - odorant receptor 38),  :doc:`../../../../../gene/AGAP013517`,  :doc:`../../../../../gene/AGAP013086`,  :doc:`../../../../../gene/AGAP013456`,  :doc:`../../../../../gene/AGAP013225`,  :doc:`../../../../../gene/AGAP013322`,  :doc:`../../../../../gene/AGAP013353`,  :doc:`../../../../../gene/AGAP013110`.



The following 11 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002635`:sup:`3` (Gr13 - gustatory receptor 13),  :doc:`../../../../../gene/AGAP002636`,  :doc:`../../../../../gene/AGAP002637`,  :doc:`../../../../../gene/AGAP013045`,  :doc:`../../../../../gene/AGAP013484`,  :doc:`../../../../../gene/AGAP013247`,  :doc:`../../../../../gene/AGAP013316`,  :doc:`../../../../../gene/AGAP002641`,  :doc:`../../../../../gene/AGAP002642` (DNA mismatch repair protein MSH5),  :doc:`../../../../../gene/AGAP002643`,  :doc:`../../../../../gene/AGAP002644` (phospholipid-translocating ATPase).


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
    * - :doc:`../../../../../signal/XPEHH/BFM.BFS/2/2/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - 2R:24,820,000-24,900,000
      - 360
      - 99.8%
      - nan
    * - :doc:`../../../../../signal/H12/BFM/2/5/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 2R:24,860,000-24,900,000
      - 267
      - 98.5%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.AOM/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.AOM/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.AOM/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 608
        # variables        = 4
        chi-square         = 87.301
        reduced chi-square = 0.145
        Akaike info crit   = -1172.015
        Bayesian info crit = -1154.374
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.58076155 +/- 0.158032 (10.00%) (init= 3)
        sigma:       0.15000000 +/- 0.016983 (11.32%) (init= 0.5)
        skew:       -0.20292802 +/- 0.117323 (57.82%) (init= 0)
        baseline:    1.60418061 +/- 0.015859 (0.99%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.585 
        C(sigma, skew)               =  0.171 
        C(sigma, baseline)           = -0.143 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 607
        # variables        = 1
        chi-square         = 105.008
        reduced chi-square = 0.173
        Akaike info crit   = -1062.976
        Bayesian info crit = -1058.567
    [[Variables]]
        c:   1.63688515 +/- 0.016895 (1.03%) (init= 1)



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


