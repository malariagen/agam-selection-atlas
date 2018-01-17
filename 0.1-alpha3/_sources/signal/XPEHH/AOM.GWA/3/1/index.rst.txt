:orphan:




XPEHH/AOM.GWA/3/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **44,320,000** and
**44,480,000**.
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


The following 9 genes overlap the focal region: :doc:`../../../../../gene/AGAP009850` (ABCG7 - ATP-binding cassette transporter (ABC transporter) family G member 7),  :doc:`../../../../../gene/AGAP009851`,  :doc:`../../../../../gene/AGAP009852` (mitochondrial fission 1 protein),  :doc:`../../../../../gene/AGAP009853`:sup:`3` (Gr5 - gustatory receptor 5),  :doc:`../../../../../gene/AGAP009854`:sup:`3` (Gr6 - gustatory receptor 6),  :doc:`../../../../../gene/AGAP009855`:sup:`3` (Gr7 - gustatory receptor 7),  :doc:`../../../../../gene/AGAP009856`:sup:`3` (Gr8 - gustatory receptor 8),  :doc:`../../../../../gene/AGAP009857`:sup:`3` (Gr4 - gustatory receptor 4),  :doc:`../../../../../gene/AGAP009858`:sup:`3` (Gr3 - gustatory receptor 3).



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009859`,  :doc:`../../../../../gene/AGAP009860`.


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
    * - :doc:`../../../../../signal/IHS/AOM/3/1/index`
      - IHS
      - Angola *An. coluzzii*
      - 3R:43,740,000-44,560,000
      - 112
      - 99.2%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/3/6/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:44,440,000-44,520,000
      - 95
      - 99.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 62
        # data points      = 578
        # variables        = 4
        chi-square         = 258.921
        reduced chi-square = 0.451
        Akaike info crit   = -456.163
        Bayesian info crit = -438.724
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.07906503 +/- 0.130839 (6.29%) (init= 3)
        decay:       0.82130914 +/- 0.123782 (15.07%) (init= 0.5)
        skew:        0.99999999 +/- 0.041898 (4.19%) (init= 0)
        baseline:    2.61615870 +/- 0.042094 (1.61%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.529 
        C(decay, skew)               = -0.528 
        C(amplitude, decay)          = -0.450 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 577
        # variables        = 1
        chi-square         = 404.691
        reduced chi-square = 0.703
        Akaike info crit   = -202.673
        Bayesian info crit = -198.315
    [[Variables]]
        c:   2.92857854 +/- 0.034893 (1.19%) (init= 1)



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


