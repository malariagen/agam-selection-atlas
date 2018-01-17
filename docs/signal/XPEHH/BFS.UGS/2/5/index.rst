:orphan:




XPEHH/BFS.UGS/2/5
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/UGS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **34,420,000** and
**34,480,000**.
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


The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP003244` (GPRGHP2 - putative growth hormone releasing hormone receptor 2),  :doc:`../../../../../gene/AGAP003245` (CLIPA19 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003246` (CLIPB2 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003247` (CLIPB19 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003248`,  :doc:`../../../../../gene/AGAP013487`,  :doc:`../../../../../gene/AGAP003249` (CLIPB3 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003250` (CLIPB4 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003251` (CLIPB1 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003252` (CLIPB6 - CLIP-domain serine protease).



The following 14 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003239` (meiotic chromosome segregation protein),  :doc:`../../../../../gene/AGAP003240` (Protein jagunal),  :doc:`../../../../../gene/AGAP003241`,  :doc:`../../../../../gene/AGAP003242` (RNA polymerase-associated protein LEO1),  :doc:`../../../../../gene/AGAP003243`,  :doc:`../../../../../gene/AGAP013184` (CLIPB36 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003253` (Gr15 - gustatory receptor 15),  :doc:`../../../../../gene/AGAP003254` (Gr16 - gustatory receptor 16),  :doc:`../../../../../gene/AGAP003255` (Gr17 - gustatory receptor 17),  :doc:`../../../../../gene/AGAP003256` (Gr18 - gustatory receptor 18),  :doc:`../../../../../gene/AGAP003257`:sup:`1` (GSTU2 - glutathione S-transferase unclassified 2),  :doc:`../../../../../gene/AGAP003258` (Gustatory receptor),  :doc:`../../../../../gene/AGAP003259` (Gr20 - gustatory receptor 20),  :doc:`../../../../../gene/AGAP003260` (Gr21 - gustatory receptor 21).


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
    * - :doc:`../../../../../signal/IHS/AOM/2/3/index`
      - IHS
      - Angola *An. coluzzii*
      - 2R:33,940,000-34,440,000
      - 213
      - 99.8%
      - nan
    * - :doc:`../../../../../signal/H12/BFS/2/6/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2R:34,420,000-34,460,000
      - 114
      - 92.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/2/7/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2R:34,320,000-34,440,000
      - 108
      - 86.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 673
        # variables        = 4
        chi-square         = 46.115
        reduced chi-square = 0.069
        Akaike info crit   = -1796.041
        Bayesian info crit = -1777.995
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.29474254 +/- 0.129300 (9.99%) (init= 3)
        decay:       0.15000030 +/- 0.024722 (16.48%) (init= 0.5)
        skew:       -0.13577170 +/- 0.170706 (125.73%) (init= 0)
        baseline:    1.13667926 +/- 0.010470 (0.92%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.672 
        C(decay, baseline)           = -0.172 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 672
        # variables        = 1
        chi-square         = 53.307
        reduced chi-square = 0.079
        Akaike info crit   = -1700.970
        Bayesian info crit = -1696.460
    [[Variables]]
        c:   1.15991623 +/- 0.010872 (0.94%) (init= 1)



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


