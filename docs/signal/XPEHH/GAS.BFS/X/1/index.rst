:orphan:




XPEHH/GAS.BFS/X/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**X** between positions **14,040,000** and
**14,400,000**.
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


The following 12 genes overlap the focal region: :doc:`../../../../../gene/AGAP000780`:sup:`1` (Yippee-like 5),  :doc:`../../../../../gene/AGAP000781` (mitochondrial import inner membrane translocase subunit Tim9),  :doc:`../../../../../gene/AGAP000782`,  :doc:`../../../../../gene/AGAP000783`,  :doc:`../../../../../gene/AGAP000784` (abhydrolase domain containing 4),  :doc:`../../../../../gene/AGAP000785` (Synaptic vesicle protein),  :doc:`../../../../../gene/AGAP000786`,  :doc:`../../../../../gene/AGAP000787` (E3 ubiquitin-protein ligase NEDD4),  :doc:`../../../../../gene/AGAP000788`,  :doc:`../../../../../gene/AGAP013147`,  :doc:`../../../../../gene/AGAP000789`,  :doc:`../../../../../gene/AGAP000790`.



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000791` (Tango10),  :doc:`../../../../../gene/AGAP000792` (Adenosylhomocysteinase),  :doc:`../../../../../gene/AGAP000793`,  :doc:`../../../../../gene/AGAP000794`:sup:`1` (NADH dehydrogenase (ubiquinone) Fe-S protein 2),  :doc:`../../../../../gene/AGAP013289`.


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
    * - :doc:`../../../../../signal/H12/GAS/X/1/index`
      - H12
      - Gabon *An. gambiae*
      - X:13,920,000-14,440,000
      - 243
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 67
        # data points      = 477
        # variables        = 4
        chi-square         = 139.154
        reduced chi-square = 0.294
        Akaike info crit   = -579.632
        Bayesian info crit = -562.962
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.59608159 +/- 0.095935 (6.01%) (init= 3)
        decay:       2.99999930 +/- 0.908656 (30.29%) (init= 0.5)
        skew:        0.91481929 +/- 0.118422 (12.94%) (init= 0)
        baseline:    1.45568187 +/- 0.093149 (6.40%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           =  0.860 
        C(amplitude, baseline)       = -0.711 
        C(decay, skew)               =  0.597 
        C(skew, baseline)            =  0.496 
        C(amplitude, skew)           = -0.412 
        C(amplitude, decay)          = -0.380 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 476
        # variables        = 1
        chi-square         = 237.347
        reduced chi-square = 0.500
        Akaike info crit   = -329.246
        Bayesian info crit = -325.080
    [[Variables]]
        c:   2.20281308 +/- 0.032399 (1.47%) (init= 1)



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


