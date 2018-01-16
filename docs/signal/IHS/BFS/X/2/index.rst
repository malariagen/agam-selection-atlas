:orphan:




IHS/BFS/X/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**X** between positions **14,660,000** and
**14,980,000**.
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


The following 14 genes overlap the focal region: :doc:`../../../../../gene/AGAP000801`:sup:`2` (GLURIIb - ionotropic receptor GLURIIb),  :doc:`../../../../../gene/AGAP000803`:sup:`2` (GLURIIa - ionotropic receptor GLURIIa),  :doc:`../../../../../gene/AGAP000804`:sup:`1` (GPXH2 - glutathione peroxidase 2),  :doc:`../../../../../gene/AGAP000805` (BTB/POZ domain-containing protein KCTD16),  :doc:`../../../../../gene/AGAP000806` (Angiopoietin-like 1),  :doc:`../../../../../gene/AGAP000807` (helix-loop-helix transcription factor),  :doc:`../../../../../gene/AGAP000808` (DNA damage-regulated autophagy modulator protein 2),  :doc:`../../../../../gene/AGAP013022`,  :doc:`../../../../../gene/AGAP000809` (Proteasome 26S non-ATPase subunit 10),  :doc:`../../../../../gene/AGAP000810`,  :doc:`../../../../../gene/AGAP000812` (calcium binding protein),  :doc:`../../../../../gene/AGAP000813`:sup:`1` (Frataxin homolog, mitochondrial),  :doc:`../../../../../gene/AGAP000814`,  :doc:`../../../../../gene/AGAP000815` (INTB - integrin beta subunit).



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000798`:sup:`2` (GLURIIc - ionotropic receptor GLURIIc),  :doc:`../../../../../gene/AGAP000817`,  :doc:`../../../../../gene/AGAP000816`,  :doc:`../../../../../gene/AGAP013474`.


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
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/X/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:14,960,000-15,140,000
      - 961
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/IHS/UGS/X/1/index`
      - IHS
      - Uganda *An. gambiae*
      - X:14,640,000-15,360,000
      - 517
      - 96.7%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/X/1/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - X:14,760,000-15,620,000
      - 501
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/H12/GNS/X/1/index`
      - H12
      - Guinea *An. gambiae*
      - X:14,960,000-15,160,000
      - 419
      - 97.8%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GAS.GWA/X/1/index`
      - XPEHH
      - Gabon *An. gambiae*
      - X:14,460,000-14,860,000
      - 301
      - 98.5%
      - nan
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
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/X/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/X/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/X/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 323
        # variables        = 4
        chi-square         = 180.883
        reduced chi-square = 0.567
        Akaike info crit   = -179.275
        Bayesian info crit = -164.165
    [[Variables]]
        center:      0 (fixed)
        amplitude:   4.14599474 +/- 0.134300 (3.24%) (init= 3)
        sigma:       1.57460529 +/- 0.063254 (4.02%) (init= 0.5)
        skew:       -0.98249570 +/- 0.041246 (4.20%) (init= 0)
        baseline:    1.85638222 +/- 0.061354 (3.31%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.457 
        C(amplitude, sigma)          = -0.347 
        C(amplitude, baseline)       = -0.346 
        C(sigma, skew)               =  0.278 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 322
        # variables        = 1
        chi-square         = 808.107
        reduced chi-square = 2.517
        Akaike info crit   = 298.286
        Bayesian info crit = 302.060
    [[Variables]]
        c:   3.01396105 +/- 0.088416 (2.93%) (init= 1)



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


