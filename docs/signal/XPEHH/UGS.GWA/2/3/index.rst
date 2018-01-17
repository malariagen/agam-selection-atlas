:orphan:




XPEHH/UGS.GWA/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **50,960,000** and
**51,100,000**.
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


The following 9 genes overlap the focal region: :doc:`../../../../../gene/AGAP004160`,  :doc:`../../../../../gene/AGAP004161` (myofilin variant C),  :doc:`../../../../../gene/AGAP004162` (myosin, light polypeptide 9, regulatory),  :doc:`../../../../../gene/AGAP004163`:sup:`1` (GSTD7 - glutathione S-transferase delta class 7),  :doc:`../../../../../gene/AGAP004164`:sup:`1` (GSTD1-4 - glutathione S-transferase delta class 1),  :doc:`../../../../../gene/AGAP004165`:sup:`1` (GSTD2 - glutathione S-transferase delta class 2),  :doc:`../../../../../gene/AGAP004166`,  :doc:`../../../../../gene/AGAP004167`,  :doc:`../../../../../gene/AGAP004169`.



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004156` (synaptic vesicle protein),  :doc:`../../../../../gene/AGAP004157` (synaptic vesicle protein),  :doc:`../../../../../gene/AGAP004158` (UDP-sugar diphosphatase),  :doc:`../../../../../gene/AGAP004159`:sup:`1` (malate dehydrogenase (oxaloacetate-decarboxylating)(NADP )).


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
    * - :doc:`../../../../../signal/H12/UGS/2/4/index`
      - H12
      - Uganda *An. gambiae*
      - 2R:51,020,000-51,120,000
      - 117
      - 94.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.GWA/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.GWA/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.GWA/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 57
        # data points      = 524
        # variables        = 4
        chi-square         = 89.369
        reduced chi-square = 0.172
        Akaike info crit   = -918.809
        Bayesian info crit = -901.763
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.20958408 +/- 0.074710 (6.18%) (init= 3)
        decay:       2.99999999 +/- 0.063550 (2.12%) (init= 0.5)
        skew:       -0.16782621 +/- 0.074996 (44.69%) (init= 0)
        baseline:    1.48598747 +/- 0.079161 (5.33%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           =  0.918 
        C(amplitude, baseline)       = -0.649 
        C(amplitude, decay)          = -0.379 
        C(skew, baseline)            = -0.135 
        C(decay, skew)               = -0.128 
        C(amplitude, skew)           =  0.109 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 523
        # variables        = 1
        chi-square         = 138.371
        reduced chi-square = 0.265
        Akaike info crit   = -693.403
        Bayesian info crit = -689.143
    [[Variables]]
        c:   1.93302799 +/- 0.022513 (1.16%) (init= 1)



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


