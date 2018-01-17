:orphan:




XPEHH/GWA.UGS/3/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/UGS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **6,280,000** and
**6,340,000**.
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


The following 8 genes overlap the focal region: :doc:`../../../../../gene/AGAP008163` (U4/U6 small nuclear ribonucleoprotein SNU13),  :doc:`../../../../../gene/AGAP008164` (La-related protein 7),  :doc:`../../../../../gene/AGAP008165` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP008166` (heparan sulfate 2-O-sulfotransferase HS2ST1),  :doc:`../../../../../gene/AGAP008167` (abhydrolase domain containing 4),  :doc:`../../../../../gene/AGAP013740`,  :doc:`../../../../../gene/AGAP013774`,  :doc:`../../../../../gene/AGAP008168`.



The following 21 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008153`,  :doc:`../../../../../gene/AGAP008154`,  :doc:`../../../../../gene/AGAP008155` (forkhead box protein D),  :doc:`../../../../../gene/AGAP013750`,  :doc:`../../../../../gene/AGAP008156` (COP9 signalosome complex subunit 6),  :doc:`../../../../../gene/AGAP008157` (zinc finger protein 330 homolog),  :doc:`../../../../../gene/AGAP008158` (dCMP deaminase),  :doc:`../../../../../gene/AGAP008159` (ribosome biogenesis protein ENP2),  :doc:`../../../../../gene/AGAP008160` (myb proto-oncogene protein),  :doc:`../../../../../gene/AGAP008161` (ribonuclease H2 subunit B),  :doc:`../../../../../gene/AGAP008162` (SNARE-associated protein Snapin),  :doc:`../../../../../gene/AGAP008169`,  :doc:`../../../../../gene/AGAP008170`,  :doc:`../../../../../gene/AGAP028664`,  :doc:`../../../../../gene/AGAP028663`,  :doc:`../../../../../gene/AGAP028692`,  :doc:`../../../../../gene/AGAP028691`,  :doc:`../../../../../gene/AGAP008173`,  :doc:`../../../../../gene/AGAP013765`,  :doc:`../../../../../gene/AGAP008174`,  :doc:`../../../../../gene/AGAP008175`.


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
    * - :doc:`../../../../../signal/XPEHH/GWA.BFS/3/2/index`
      - XPEHH
      - Guinea Bissau
      - 3R:6,320,000-6,360,000
      - 295
      - 99.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 51
        # data points      = 933
        # variables        = 4
        chi-square         = 259.543
        reduced chi-square = 0.279
        Akaike info crit   = -1185.759
        Bayesian info crit = -1166.406
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.72307803 +/- 0.110460 (6.41%) (init= 3)
        sigma:       0.28942132 +/- 0.027340 (9.45%) (init= 0.5)
        skew:        0.99999550 +/- 0.112037 (11.20%) (init= 0)
        baseline:    1.66345486 +/- 0.018379 (1.10%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.601 
        C(amplitude, sigma)          = -0.407 
        C(sigma, baseline)           = -0.165 
        C(amplitude, baseline)       = -0.115 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 932
        # variables        = 1
        chi-square         = 325.387
        reduced chi-square = 0.350
        Akaike info crit   = -978.759
        Bayesian info crit = -973.922
    [[Variables]]
        c:   1.74492743 +/- 0.019364 (1.11%) (init= 1)



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


