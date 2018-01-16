:orphan:




XPEHH/UGS.BFS/3/4
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/BFS` population
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
    * - :doc:`../../../../../signal/XPEHH/UGS.CMS/3/3/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:6,360,000-6,400,000
      - 201
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
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 82
        # data points      = 559
        # variables        = 4
        chi-square         = 158.883
        reduced chi-square = 0.286
        Akaike info crit   = -695.211
        Bayesian info crit = -677.907
    [[Variables]]
        center:      0 (fixed)
        amplitude:   4.16680483 +/- 0.247838 (5.95%) (init= 3)
        decay:       0.15000000 +/- 0.017940 (11.96%) (init= 0.5)
        skew:        0.14781293 +/- 0.114111 (77.20%) (init= 0)
        baseline:    1.11683764 +/- 0.023656 (2.12%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.642 
        C(decay, baseline)           =  0.206 
        C(decay, skew)               =  0.140 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 558
        # variables        = 1
        chi-square         = 204.472
        reduced chi-square = 0.367
        Akaike info crit   = -558.193
        Bayesian info crit = -553.868
    [[Variables]]
        c:   1.20632212 +/- 0.025648 (2.13%) (init= 1)



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


