:orphan:




XPEHH/UGS.BFS/3/6
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **44,440,000** and
**44,520,000**.
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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP009859`,  :doc:`../../../../../gene/AGAP009860`.



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009861` (Profilin protein),  :doc:`../../../../../gene/AGAP009862`,  :doc:`../../../../../gene/AGAP009863` (eukaryotic translation initiation factor 4A, isoform 2).


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
    * - :doc:`../../../../../signal/H12/UGS/3/3/index`
      - H12
      - Uganda *An. gambiae*
      - 3R:44,380,000-45,140,000
      - 292
      - 95.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/3/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 3R:44,320,000-44,480,000
      - 253
      - 99.3%
      - nan
    * - :doc:`../../../../../signal/IHS/AOM/3/1/index`
      - IHS
      - Angola *An. coluzzii*
      - 3R:43,740,000-44,560,000
      - 112
      - 99.2%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/6/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 514
        # variables        = 4
        chi-square         = 475.822
        reduced chi-square = 0.933
        Akaike info crit   = -31.670
        Bayesian info crit = -14.701
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.32842077 +/- 0.238718 (10.25%) (init= 3)
        decay:       0.59524097 +/- 0.105088 (17.65%) (init= 0.5)
        skew:       -0.89804299 +/- 0.174536 (19.44%) (init= 0)
        baseline:    2.53814576 +/- 0.052419 (2.07%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.560 
        C(decay, baseline)           = -0.416 
        C(decay, skew)               =  0.177 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 513
        # variables        = 1
        chi-square         = 578.802
        reduced chi-square = 1.130
        Akaike info crit   = 63.911
        Bayesian info crit = 68.151
    [[Variables]]
        c:   2.77883062 +/- 0.046941 (1.69%) (init= 1)



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


