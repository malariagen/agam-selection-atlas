:orphan:




H12/BFS/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,640,000** and
**41,060,000**.
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




The following 31 genes overlap the focal region: :doc:`../../../../../gene/AGAP003624`,  :doc:`../../../../../gene/AGAP029110`,  :doc:`../../../../../gene/AGAP003626`,  :doc:`../../../../../gene/AGAP013221`,  :doc:`../../../../../gene/AGAP012946`,  :doc:`../../../../../gene/AGAP003627`,  :doc:`../../../../../gene/AGAP003629`,  :doc:`../../../../../gene/AGAP003630`,  :doc:`../../../../../gene/AGAP003631` (GPRGRP2 - putative gastrin/bombesin receptor 2),  :doc:`../../../../../gene/AGAP003632` (U3 small nucleolar RNA-associated protein 14),  :doc:`../../../../../gene/AGAP003633`,  :doc:`../../../../../gene/AGAP003635`,  :doc:`../../../../../gene/AGAP003636`:sup:`1` (inositol oxygenase),  :doc:`../../../../../gene/AGAP003638`,  :doc:`../../../../../gene/AGAP003639` (Prolylcarboxypeptidase),  :doc:`../../../../../gene/AGAP003640`:sup:`1` (SP8905),  :doc:`../../../../../gene/AGAP003641`:sup:`1` (SP8907),  :doc:`../../../../../gene/AGAP003642`:sup:`1` (SP8898),  :doc:`../../../../../gene/AGAP003643` (ubiquitin carboxyl-terminal hydrolase 34),  :doc:`../../../../../gene/AGAP003644` (mRpS11 - 28S ribosomal protein S11, mitochondrial),  :doc:`../../../../../gene/AGAP003645` (kelch-like protein 19),  :doc:`../../../../../gene/AGAP013307`,  :doc:`../../../../../gene/AGAP003646`,  :doc:`../../../../../gene/AGAP003647`,  :doc:`../../../../../gene/AGAP003648` (DNA-directed RNA polymerase II subunit RPB2),  :doc:`../../../../../gene/AGAP003649`,  :doc:`../../../../../gene/AGAP003650` (translation initiation factor eIF-2B subunit alpha),  :doc:`../../../../../gene/AGAP003651` (Tyrosine-protein kinase Fes/Fps),  :doc:`../../../../../gene/AGAP012992`,  :doc:`../../../../../gene/AGAP013502`,  :doc:`../../../../../gene/AGAP003652`:sup:`1` (aldehyde dehydrogenase (NAD )).




The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003620`,  :doc:`../../../../../gene/AGAP003621` (coiled-coil domain-containing protein 25),  :doc:`../../../../../gene/AGAP003622` (Queuine tRNA-ribosyltransferase catalytic subunit 1),  :doc:`../../../../../gene/AGAP003623` (long-chain acyl-CoA synthetase),  :doc:`../../../../../gene/AGAP003654` (GPRCAL3 - putative calcitonin receptor 3),  :doc:`../../../../../gene/AGAP003655` (RNA methyltransferase like 1).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

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
    * - :doc:`../../../../../signal/H12/BFM/2/3/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 2R:40,920,000-40,960,000
      - 512
      - 97.6%
    * - :doc:`../../../../../signal/H12/CMS/2/3/index`
      - H12
      - Cameroon *An. gambiae*
      - 2R:40,300,000-40,740,000
      - 501
      - 98.7%
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/2/5/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2R:40,780,000-40,820,000
      - 195
      - 94.0%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 396
        # variables        = 4
        chi-square         = 0.136
        reduced chi-square = 0.000
        Akaike info crit   = -3150.494
        Bayesian info crit = -3134.568
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.11629361 +/- 0.005495 (4.73%) (init= 0.5)
        decay:       0.87729857 +/- 0.071284 (8.13%) (init= 0.5)
        skew:       -0.46214774 +/- 0.071846 (15.55%) (init= 0)
        baseline:    0.03180019 +/- 0.001268 (3.99%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.581 
        C(decay, baseline)           = -0.532 
        C(decay, skew)               =  0.183 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 10
        # data points      = 395
        # variables        = 1
        chi-square         = 0.357
        reduced chi-square = 0.001
        Akaike info crit   = -2766.177
        Bayesian info crit = -2762.198
    [[Variables]]
        c:   0.04489648 +/- 0.001515 (3.37%) (init= 0.03)



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


