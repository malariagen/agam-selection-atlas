:orphan:




XPEHH/AOM.GWA/2/5
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **27,980,000** and
**28,040,000**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP002822`,  :doc:`../../../../../gene/AGAP002823` (Med7 - Mediator of RNA polymerase II transcription subunit 7),  :doc:`../../../../../gene/AGAP002824` (GPRTAK1 - putative tachykinin receptor 1),  :doc:`../../../../../gene/AGAP002825`:sup:`1` (PPO1 - prophenoloxidase 1).



The following 13 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002815` (CLIPA15 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP002816`:sup:`1` (ERO1-like protein alpha),  :doc:`../../../../../gene/AGAP002817`,  :doc:`../../../../../gene/AGAP002818`,  :doc:`../../../../../gene/AGAP002819`,  :doc:`../../../../../gene/AGAP002820`,  :doc:`../../../../../gene/AGAP002821`,  :doc:`../../../../../gene/AGAP002826`,  :doc:`../../../../../gene/AGAP002828`,  :doc:`../../../../../gene/AGAP002829` (SPN-E - ATP-dependent RNA helicase spindle-E),  :doc:`../../../../../gene/AGAP002830`:sup:`1` (C-1-tetrahydrofolate synthase, mitochondrial precursor),  :doc:`../../../../../gene/AGAP002831` (ribosomal RNA small subunit methyltransferase H),  :doc:`../../../../../gene/AGAP013130`.


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
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/2/1/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2R:27,980,000-28,280,000
      - 753
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/H12/AOM/2/2/index`
      - H12
      - Angola *An. coluzzii*
      - 2R:28,040,000-28,080,000
      - 478
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/IHS/AOM/2/1/index`
      - IHS
      - Angola *An. coluzzii*
      - 2R:27,980,000-28,040,000
      - 324
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/2/3/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2R:28,000,000-28,060,000
      - 295
      - 99.4%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 93
        # data points      = 103
        # variables        = 4
        chi-square         = 28.014
        reduced chi-square = 0.283
        Akaike info crit   = -126.107
        Bayesian info crit = -115.568
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.47886289 +/- 0.207150 (8.36%) (init= 3)
        sigma:       0.16960648 +/- 0.018286 (10.78%) (init= 0.5)
        skew:        0.13207729 +/- 0.120388 (91.15%) (init= 0)
        baseline:    1.28463234 +/- 0.061315 (4.77%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.475 
        C(sigma, baseline)           = -0.304 
        C(amplitude, baseline)       = -0.222 
        C(sigma, skew)               = -0.160 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 102
        # variables        = 1
        chi-square         = 75.013
        reduced chi-square = 0.743
        Akaike info crit   = -29.345
        Bayesian info crit = -26.720
    [[Variables]]
        c:   1.61263803 +/- 0.085331 (5.29%) (init= 1)



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


