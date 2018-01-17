:orphan:




XPEHH/GAS.GWA/X/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**X** between positions **14,460,000** and
**14,860,000**.
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


The following 13 genes overlap the focal region: :doc:`../../../../../gene/AGAP000795`,  :doc:`../../../../../gene/AGAP000797` (E3 ubiquitin-protein ligase HECW2),  :doc:`../../../../../gene/AGAP000798`:sup:`2` (GLURIIc - ionotropic receptor GLURIIc),  :doc:`../../../../../gene/AGAP000801`:sup:`2` (GLURIIb - ionotropic receptor GLURIIb),  :doc:`../../../../../gene/AGAP000803`:sup:`2` (GLURIIa - ionotropic receptor GLURIIa),  :doc:`../../../../../gene/AGAP000804`:sup:`1` (GPXH2 - glutathione peroxidase 2),  :doc:`../../../../../gene/AGAP000805` (BTB/POZ domain-containing protein KCTD16),  :doc:`../../../../../gene/AGAP000806` (Angiopoietin-like 1),  :doc:`../../../../../gene/AGAP000807` (helix-loop-helix transcription factor),  :doc:`../../../../../gene/AGAP000808` (DNA damage-regulated autophagy modulator protein 2),  :doc:`../../../../../gene/AGAP013022`,  :doc:`../../../../../gene/AGAP000809` (Proteasome 26S non-ATPase subunit 10),  :doc:`../../../../../gene/AGAP000810`.



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000791` (Tango10),  :doc:`../../../../../gene/AGAP000792` (Adenosylhomocysteinase),  :doc:`../../../../../gene/AGAP000793`,  :doc:`../../../../../gene/AGAP000794`:sup:`1` (NADH dehydrogenase (ubiquinone) Fe-S protein 2),  :doc:`../../../../../gene/AGAP013289`,  :doc:`../../../../../gene/AGAP000812` (calcium binding protein).


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
    * - :doc:`../../../../../signal/IHS/UGS/X/1/index`
      - IHS
      - Uganda *An. gambiae*
      - X:14,640,000-15,360,000
      - 517
      - 96.7%
      - Cyp9k1
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
    * - :doc:`../../../../../signal/H12/AOM/X/2/index`
      - H12
      - Angola *An. coluzzii*
      - X:14,500,000-14,600,000
      - 243
      - 96.4%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/X/2/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:14,500,000-15,180,000
      - 228
      - 98.5%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.GWA/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.GWA/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.GWA/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 57
        # data points      = 386
        # variables        = 4
        chi-square         = 87.094
        reduced chi-square = 0.228
        Akaike info crit   = -566.698
        Bayesian info crit = -550.874
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.72267028 +/- 0.100249 (5.82%) (init= 3)
        sigma:       2.99999999 +/- 0.008305 (0.28%) (init= 0.5)
        skew:        0.78611878 +/- 0.052057 (6.62%) (init= 0)
        baseline:    1.00918523 +/- 0.097606 (9.67%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.908 
        C(sigma, baseline)           =  0.809 
        C(amplitude, sigma)          = -0.604 
        C(sigma, skew)               =  0.380 
        C(amplitude, skew)           = -0.331 
        C(skew, baseline)            =  0.300 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 385
        # variables        = 1
        chi-square         = 192.521
        reduced chi-square = 0.501
        Akaike info crit   = -264.821
        Bayesian info crit = -260.867
    [[Variables]]
        c:   2.13708456 +/- 0.036086 (1.69%) (init= 1)



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


