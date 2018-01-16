:orphan:




XPEHH/UGS.CMS/3/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/CMS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **6,360,000** and
**6,400,000**.
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


The following 13 genes overlap the focal region: :doc:`../../../../../gene/AGAP008169`,  :doc:`../../../../../gene/AGAP008170`,  :doc:`../../../../../gene/AGAP028664`,  :doc:`../../../../../gene/AGAP028663`,  :doc:`../../../../../gene/AGAP028692`,  :doc:`../../../../../gene/AGAP028691`,  :doc:`../../../../../gene/AGAP008173`,  :doc:`../../../../../gene/AGAP013765`,  :doc:`../../../../../gene/AGAP008174`,  :doc:`../../../../../gene/AGAP008175`,  :doc:`../../../../../gene/AGAP008176` (dipeptidyl-peptidase 4),  :doc:`../../../../../gene/AGAP008177`,  :doc:`../../../../../gene/AGAP028550`.



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013774`,  :doc:`../../../../../gene/AGAP008168`,  :doc:`../../../../../gene/AGAP008178`,  :doc:`../../../../../gene/AGAP008179` (SCRBQ3 - Class B Scavenger Receptor (CD36 domain).),  :doc:`../../../../../gene/AGAP008180`,  :doc:`../../../../../gene/AGAP008181` (protein SMG5),  :doc:`../../../../../gene/AGAP008182`:sup:`3`,  :doc:`../../../../../gene/AGAP008183` (CLIPD2 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP008184` (phospholipid-translocating ATPase).


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
    * - :doc:`../../../../../signal/XPEHH/GWA.BFS/3/2/index`
      - XPEHH
      - Guinea Bissau
      - 3R:6,320,000-6,360,000
      - 295
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
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.CMS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 79
        # data points      = 566
        # variables        = 4
        chi-square         = 135.008
        reduced chi-square = 0.240
        Akaike info crit   = -803.227
        Bayesian info crit = -785.872
    [[Variables]]
        center:      0 (fixed)
        amplitude:   4.26876117 +/- 0.224272 (5.25%) (init= 3)
        decay:       0.15000000 +/- 0.003431 (2.29%) (init= 0.5)
        skew:       -0.00748473 +/- 0.099353 (1327.41%) (init= 0)
        baseline:    0.99386349 +/- 0.021549 (2.17%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.636 
        C(decay, baseline)           = -0.210 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 565
        # variables        = 1
        chi-square         = 194.006
        reduced chi-square = 0.344
        Akaike info crit   = -601.949
        Bayesian info crit = -597.613
    [[Variables]]
        c:   1.08608111 +/- 0.024674 (2.27%) (init= 1)



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


