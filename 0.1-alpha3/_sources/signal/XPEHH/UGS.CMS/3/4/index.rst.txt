:orphan:




XPEHH/UGS.CMS/3/4
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/CMS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3L** between positions **16,319,316** and
**16,359,316**.
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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP011080` (hydroxymethylbilane synthase),  :doc:`../../../../../gene/AGAP011081` (Protein anon-73B1),  :doc:`../../../../../gene/AGAP011082` (heat shock transcription factor, invertebrate),  :doc:`../../../../../gene/AGAP011083`,  :doc:`../../../../../gene/AGAP011084` (ATP-dependent RNA helicase DDX27),  :doc:`../../../../../gene/AGAP011085`.



The following 19 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP028506`,  :doc:`../../../../../gene/AGAP011072`,  :doc:`../../../../../gene/AGAP028507`,  :doc:`../../../../../gene/AGAP011073`,  :doc:`../../../../../gene/AGAP028508`,  :doc:`../../../../../gene/AGAP028509`,  :doc:`../../../../../gene/AGAP011074`,  :doc:`../../../../../gene/AGAP028686`,  :doc:`../../../../../gene/AGAP028685`,  :doc:`../../../../../gene/AGAP028687`,  :doc:`../../../../../gene/AGAP028688`,  :doc:`../../../../../gene/AGAP028689`,  :doc:`../../../../../gene/AGAP028690`,  :doc:`../../../../../gene/AGAP011076` (ubiquitin-conjugating enzyme E2 I),  :doc:`../../../../../gene/AGAP011077` (RpS12 - 40S ribosomal protein S12),  :doc:`../../../../../gene/AGAP011078` (zinc finger MYND domain-containing protein 10),  :doc:`../../../../../gene/AGAP011079`,  :doc:`../../../../../gene/AGAP011086`,  :doc:`../../../../../gene/AGAP028510`.


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
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/3/3/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3L:16,319,316-16,359,316
      - 138
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 75
        # data points      = 593
        # variables        = 4
        chi-square         = 1106.567
        reduced chi-square = 1.879
        Akaike info crit   = 377.927
        Bayesian info crit = 395.468
    [[Variables]]
        center:      0 (fixed)
        amplitude:   7.07442801 +/- 0.621190 (8.78%) (init= 3)
        decay:       0.15000000 +/- 0.006246 (4.16%) (init= 0.5)
        skew:        0.61094771 +/- 0.173079 (28.33%) (init= 0)
        baseline:    2.94167092 +/- 0.058459 (1.99%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.678 
        C(decay, baseline)           =  0.179 
        C(amplitude, skew)           = -0.126 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 592
        # variables        = 1
        chi-square         = 1437.808
        reduced chi-square = 2.433
        Akaike info crit   = 527.322
        Bayesian info crit = 531.706
    [[Variables]]
        c:   3.10652848 +/- 0.064102 (2.06%) (init= 1)



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


