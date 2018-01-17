:orphan:




IHS/UGS/3/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **43,800,000** and
**43,920,000**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).





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


The following 8 genes overlap the focal region: :doc:`../../../../../gene/AGAP009820`,  :doc:`../../../../../gene/AGAP009821`,  :doc:`../../../../../gene/AGAP009822` (DNA-binding protein rfxank),  :doc:`../../../../../gene/AGAP009823`,  :doc:`../../../../../gene/AGAP009824` (NADH dehydrogenase (ubiquinone) Fe-S protein 5),  :doc:`../../../../../gene/AGAP009825`,  :doc:`../../../../../gene/AGAP009826`,  :doc:`../../../../../gene/AGAP009827` (CCR4-NOT transcription complex subunit 4).



The following 10 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009810` (peptidyl-prolyl isomerase E (cyclophilin E)),  :doc:`../../../../../gene/AGAP009811` (Cdk5rap3),  :doc:`../../../../../gene/AGAP009812`,  :doc:`../../../../../gene/AGAP028647`,  :doc:`../../../../../gene/AGAP009815`,  :doc:`../../../../../gene/AGAP009816` (anterior pharynx defective 1),  :doc:`../../../../../gene/AGAP009817`,  :doc:`../../../../../gene/AGAP009818` (methyltransferase-like protein 6),  :doc:`../../../../../gene/AGAP009819`,  :doc:`../../../../../gene/AGAP009828`.


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
    * - :doc:`../../../../../signal/XPEHH/AOM.GAS/3/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 3R:43,460,000-44,120,000
      - 605
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/CMS.GAS/3/1/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 3R:43,920,000-44,560,000
      - 538
      - 99.5%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/3/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 3R:43,860,000-44,500,000
      - 314
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/3/2/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:43,920,000-43,980,000
      - 214
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/IHS/AOM/3/1/index`
      - IHS
      - Angola *An. coluzzii*
      - 3R:43,740,000-44,560,000
      - 112
      - 99.2%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 558
        # variables        = 4
        chi-square         = 80.696
        reduced chi-square = 0.146
        Akaike info crit   = -1070.990
        Bayesian info crit = -1053.693
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.45503995 +/- 0.164116 (11.28%) (init= 3)
        decay:       0.46872353 +/- 0.072374 (15.44%) (init= 0.5)
        skew:       -0.75455185 +/- 0.135020 (17.89%) (init= 0)
        baseline:    2.61377518 +/- 0.018655 (0.71%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.735 
        C(decay, baseline)           = -0.339 
        C(decay, skew)               =  0.240 
        C(amplitude, skew)           =  0.104 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 557
        # variables        = 1
        chi-square         = 108.245
        reduced chi-square = 0.195
        Akaike info crit   = -910.462
        Bayesian info crit = -906.139
    [[Variables]]
        c:   2.70908950 +/- 0.018695 (0.69%) (init= 1)



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


