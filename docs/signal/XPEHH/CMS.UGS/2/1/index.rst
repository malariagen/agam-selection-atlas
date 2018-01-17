:orphan:




XPEHH/CMS.UGS/2/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population
when compared with the :doc:`../../../../../population/UGS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **41,020,000** and
**41,400,000**.
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


The following 21 genes overlap the focal region: :doc:`../../../../../gene/AGAP003651` (Tyrosine-protein kinase Fes/Fps),  :doc:`../../../../../gene/AGAP012992`,  :doc:`../../../../../gene/AGAP013502`,  :doc:`../../../../../gene/AGAP003652`:sup:`1` (aldehyde dehydrogenase (NAD )),  :doc:`../../../../../gene/AGAP003654` (GPRCAL3 - putative calcitonin receptor 3),  :doc:`../../../../../gene/AGAP003655` (RNA methyltransferase like 1),  :doc:`../../../../../gene/AGAP013179`,  :doc:`../../../../../gene/AGAP003656` (Terribly reduced optic lobes, isoform B),  :doc:`../../../../../gene/AGAP003657`,  :doc:`../../../../../gene/AGAP003658` (GPRALS1 - putative allatostatin receptor 1),  :doc:`../../../../../gene/AGAP003660`,  :doc:`../../../../../gene/AGAP003661`,  :doc:`../../../../../gene/AGAP003662` (Prenylated Rab acceptor protein 1),  :doc:`../../../../../gene/AGAP013323`,  :doc:`../../../../../gene/AGAP003663` (ATP-dependent RNA helicase DBP2),  :doc:`../../../../../gene/AGAP013457` (CDC-like kinase 2),  :doc:`../../../../../gene/AGAP003664` (Envelysin),  :doc:`../../../../../gene/AGAP013358`,  :doc:`../../../../../gene/AGAP003665`,  :doc:`../../../../../gene/AGAP003666` (E3 ubiquitin-protein ligase RNF139),  :doc:`../../../../../gene/AGAP003667`.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003649`,  :doc:`../../../../../gene/AGAP003650` (translation initiation factor eIF-2B subunit alpha).


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
    * - :doc:`../../../../../signal/H12/BFS/2/4/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2R:40,640,000-41,060,000
      - 384
      - 95.9%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/2/2/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 2R:40,880,000-41,160,000
      - 312
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/CMS.GAS/2/2/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 2R:41,220,000-41,320,000
      - 236
      - 99.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.UGS/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.UGS/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.UGS/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 621
        # variables        = 4
        chi-square         = 198.911
        reduced chi-square = 0.322
        Akaike info crit   = -698.992
        Bayesian info crit = -681.267
    [[Variables]]
        center:      0 (fixed)
        amplitude:   3.77883680 +/- 0.089721 (2.37%) (init= 3)
        sigma:       0.66227186 +/- 0.023784 (3.59%) (init= 0.5)
        skew:        0.70319426 +/- 0.042851 (6.09%) (init= 0)
        baseline:    1.45032834 +/- 0.027424 (1.89%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               = -0.604 
        C(amplitude, sigma)          = -0.408 
        C(sigma, baseline)           = -0.294 
        C(amplitude, baseline)       = -0.214 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 620
        # variables        = 1
        chi-square         = 916.100
        reduced chi-square = 1.480
        Akaike info crit   = 244.052
        Bayesian info crit = 248.482
    [[Variables]]
        c:   2.01451466 +/- 0.048857 (2.43%) (init= 1)



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


