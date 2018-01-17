:orphan:




XPEHH/UGS.CMS/3/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/CMS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **43,940,000** and
**43,980,000**.
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


No genes overlap the focal region.



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009828`,  :doc:`../../../../../gene/AGAP009829` (beat protein),  :doc:`../../../../../gene/AGAP009830`.


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
    * - :doc:`../../../../../signal/XPEHH/AOM.GAS/3/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 3R:43,460,000-44,120,000
      - 605
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/CMS.GAS/3/1/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 3R:43,920,000-44,560,000
      - 538
      - 99.5%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/3/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 3R:43,860,000-44,500,000
      - 314
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/3/2/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:43,920,000-43,980,000
      - 214
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/IHS/AOM/3/1/index`
      - IHS
      - Angola *An. coluzzii*
      - 3R:43,740,000-44,560,000
      - 112
      - 99.2%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.GWA/3/3/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:43,940,000-44,000,000
      - 93
      - 99.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 83
        # data points      = 623
        # variables        = 4
        chi-square         = 589.233
        reduced chi-square = 0.952
        Akaike info crit   = -26.717
        Bayesian info crit = -8.979
    [[Variables]]
        center:      0 (fixed)
        amplitude:   5.34211305 +/- 0.359130 (6.72%) (init= 3)
        sigma:       0.17591492 +/- 0.012099 (6.88%) (init= 0.5)
        skew:        0.46442248 +/- 0.075323 (16.22%) (init= 0)
        baseline:    2.56374278 +/- 0.040524 (1.58%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.621 
        C(sigma, skew)               = -0.190 
        C(sigma, baseline)           = -0.146 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 622
        # variables        = 1
        chi-square         = 907.860
        reduced chi-square = 1.462
        Akaike info crit   = 237.210
        Bayesian info crit = 241.643
    [[Variables]]
        c:   2.72519420 +/- 0.048479 (1.78%) (init= 1)



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


