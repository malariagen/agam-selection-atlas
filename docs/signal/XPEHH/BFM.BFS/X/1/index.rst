:orphan:




XPEHH/BFM.BFS/X/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**X** between positions **15,580,000** and
**15,800,000**.
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


The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP000847` (CDC-like kinase),  :doc:`../../../../../gene/AGAP000848`,  :doc:`../../../../../gene/AGAP000849` (NADH dehydrogenase (ubiquinone) 1 beta subcomplex 1),  :doc:`../../../../../gene/AGAP000850`,  :doc:`../../../../../gene/AGAP000851`:sup:`1` (cytochrome c oxidase subunit 6a, mitochrondrial),  :doc:`../../../../../gene/AGAP000852` (Small ubiquitin-related modifier),  :doc:`../../../../../gene/AGAP000853` (gamma-glutamyltranspeptidase),  :doc:`../../../../../gene/AGAP000854`,  :doc:`../../../../../gene/AGAP000855`,  :doc:`../../../../../gene/AGAP000856`:sup:`1` (tRNA-dihydrouridine synthase 2),  :doc:`../../../../../gene/AGAP000857` (mRpL3 - 39S ribosomal protein L3, mitochondrial).



The following 12 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000840` (amiloride-sensitive sodium channel, other),  :doc:`../../../../../gene/AGAP000841` (Ras-related protein Rab-40),  :doc:`../../../../../gene/AGAP013101`,  :doc:`../../../../../gene/AGAP000842` (NADH dehydrogenase (ubiquinone) 1 alpha subcomplex, assembly factor 1),  :doc:`../../../../../gene/AGAP000843` (cardiolipin synthase),  :doc:`../../../../../gene/AGAP000844` (Progestin and adipoQ receptor family member 4),  :doc:`../../../../../gene/AGAP013097`,  :doc:`../../../../../gene/AGAP012991` (Fascin),  :doc:`../../../../../gene/AGAP000858`,  :doc:`../../../../../gene/AGAP000859`,  :doc:`../../../../../gene/AGAP013522`,  :doc:`../../../../../gene/AGAP000860` (Protein tweety homolog).


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
    * - :doc:`../../../../../signal/IHS/GNS/X/1/index`
      - IHS
      - Guinea *An. gambiae*
      - X:15,240,000-15,780,000
      - 553
      - 99.3%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/X/1/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - X:14,760,000-15,620,000
      - 501
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 414
        # variables        = 4
        chi-square         = 212.959
        reduced chi-square = 0.519
        Akaike info crit   = -267.213
        Bayesian info crit = -251.109
    [[Variables]]
        center:      0 (fixed)
        amplitude:   6.95495305 +/- 0.178542 (2.57%) (init= 3)
        decay:       0.85876760 +/- 0.039526 (4.60%) (init= 0.5)
        skew:        0.34935012 +/- 0.037781 (10.81%) (init= 0)
        baseline:    1.47798949 +/- 0.054542 (3.69%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.627 
        C(amplitude, decay)          = -0.495 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 413
        # variables        = 1
        chi-square         = 1225.392
        reduced chi-square = 2.974
        Akaike info crit   = 451.166
        Bayesian info crit = 455.189
    [[Variables]]
        c:   2.50549839 +/- 0.084861 (3.39%) (init= 1)



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


