:orphan:




XPEHH/GWA.BFS/3/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **6,320,000** and
**6,360,000**.
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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP013774`,  :doc:`../../../../../gene/AGAP008168`.



The following 24 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008160` (myb proto-oncogene protein),  :doc:`../../../../../gene/AGAP008161` (ribonuclease H2 subunit B),  :doc:`../../../../../gene/AGAP008162` (SNARE-associated protein Snapin),  :doc:`../../../../../gene/AGAP008163` (U4/U6 small nuclear ribonucleoprotein SNU13),  :doc:`../../../../../gene/AGAP008164` (La-related protein 7),  :doc:`../../../../../gene/AGAP008165` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP008166` (heparan sulfate 2-O-sulfotransferase HS2ST1),  :doc:`../../../../../gene/AGAP008167` (abhydrolase domain containing 4),  :doc:`../../../../../gene/AGAP013740`,  :doc:`../../../../../gene/AGAP008169`,  :doc:`../../../../../gene/AGAP008170`,  :doc:`../../../../../gene/AGAP028664`,  :doc:`../../../../../gene/AGAP028663`,  :doc:`../../../../../gene/AGAP028692`,  :doc:`../../../../../gene/AGAP028691`,  :doc:`../../../../../gene/AGAP008173`,  :doc:`../../../../../gene/AGAP013765`,  :doc:`../../../../../gene/AGAP008174`,  :doc:`../../../../../gene/AGAP008175`,  :doc:`../../../../../gene/AGAP008176` (dipeptidyl-peptidase 4),  :doc:`../../../../../gene/AGAP008177`,  :doc:`../../../../../gene/AGAP028550`,  :doc:`../../../../../gene/AGAP008178`,  :doc:`../../../../../gene/AGAP008179` (SCRBQ3 - Class B Scavenger Receptor (CD36 domain).).


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
    * - :doc:`../../../../../signal/XPEHH/GWA.UGS/3/2/index`
      - XPEHH
      - Guinea Bissau
      - 3R:6,280,000-6,340,000
      - 206
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.CMS/3/3/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:6,360,000-6,400,000
      - 201
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/3/4/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:6,360,000-6,400,000
      - 137
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.GWA/3/2/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:6,360,000-6,400,000
      - 120
      - 99.3%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 52
        # data points      = 787
        # variables        = 4
        chi-square         = 208.975
        reduced chi-square = 0.267
        Akaike info crit   = -1035.572
        Bayesian info crit = -1016.899
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.94501224 +/- 0.107991 (5.55%) (init= 3)
        sigma:       0.28384080 +/- 0.023949 (8.44%) (init= 0.5)
        skew:        0.99999993 +/- 0.104600 (10.46%) (init= 0)
        baseline:    1.42734526 +/- 0.019674 (1.38%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               = -0.570 
        C(amplitude, sigma)          = -0.459 
        C(sigma, baseline)           = -0.167 
        C(amplitude, baseline)       = -0.130 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 786
        # variables        = 1
        chi-square         = 305.964
        reduced chi-square = 0.390
        Akaike info crit   = -739.583
        Bayesian info crit = -734.916
    [[Variables]]
        c:   1.53944224 +/- 0.022268 (1.45%) (init= 1)



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


