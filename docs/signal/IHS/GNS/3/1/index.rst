:orphan:




IHS/GNS/3/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **28,240,000** and
**28,420,000**.
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


Gene :doc:`../../../../../gene/AGAP009183` (defective proboscis extension response) overlaps the focal region.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009181`,  :doc:`../../../../../gene/AGAP009182` (protein transport protein SEC61 subunit alpha).


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
    * - :doc:`../../../../../signal/XPEHH/CMS.UGS/3/1/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 3R:28,240,000-28,380,000
      - 1,234
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/3/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 3R:28,320,000-28,360,000
      - 1,209
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/IHS/CMS/3/1/index`
      - IHS
      - Cameroon *An. gambiae*
      - 3R:28,320,000-28,700,000
      - 1,106
      - 100.0%
      - Gste
    * - :doc:`../../../../../signal/IHS/BFM/3/1/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 3R:28,260,000-28,620,000
      - 1,058
      - 100.0%
      - Gste
    * - :doc:`../../../../../signal/IHS/BFS/3/1/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3R:27,940,000-28,260,000
      - 749
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.BFM/3/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 3R:28,360,000-28,460,000
      - 257
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/CMS.GAS/3/2/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 3R:28,260,000-28,320,000
      - 232
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 605
        # variables        = 4
        chi-square         = 167.859
        reduced chi-square = 0.279
        Akaike info crit   = -767.673
        Bayesian info crit = -750.052
    [[Variables]]
        center:      0 (fixed)
        amplitude:   3.38063639 +/- 0.088777 (2.63%) (init= 3)
        decay:       1.69283693 +/- 0.093199 (5.51%) (init= 0.5)
        skew:       -0.72327903 +/- 0.040408 (5.59%) (init= 0)
        baseline:    2.03250270 +/- 0.040880 (2.01%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.708 
        C(amplitude, decay)          = -0.365 
        C(decay, skew)               =  0.172 
        C(amplitude, baseline)       = -0.168 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 604
        # variables        = 1
        chi-square         = 625.804
        reduced chi-square = 1.038
        Akaike info crit   = 23.420
        Bayesian info crit = 27.823
    [[Variables]]
        c:   2.81581427 +/- 0.041450 (1.47%) (init= 1)



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


