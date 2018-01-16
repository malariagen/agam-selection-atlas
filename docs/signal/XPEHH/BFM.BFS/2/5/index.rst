:orphan:




XPEHH/BFM.BFS/2/5
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **28,200,000** and
**28,240,000**.
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


The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP002836` (endoribonuclease Dicer),  :doc:`../../../../../gene/AGAP002837`,  :doc:`../../../../../gene/AGAP013054`,  :doc:`../../../../../gene/AGAP002838`,  :doc:`../../../../../gene/AGAP013404`,  :doc:`../../../../../gene/AGAP002839` (WD repeat-containing protein 85),  :doc:`../../../../../gene/AGAP002840`,  :doc:`../../../../../gene/AGAP013351`,  :doc:`../../../../../gene/AGAP002841` (pyridoxal phosphate phosphatase PHOSPHO2),  :doc:`../../../../../gene/AGAP002842` (CLIPD1 protein).



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002835` (alpha-tocopherol transfer protein-like protein),  :doc:`../../../../../gene/AGAP002845`.


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
    * - :doc:`../../../../../signal/IHS/CMS/2/1/index`
      - IHS
      - Cameroon *An. gambiae*
      - 2R:28,240,000-28,560,000
      - 1,249
      - 100.0%
      - Cyp6p
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/2/1/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2R:27,980,000-28,280,000
      - 753
      - 99.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 741
        # variables        = 4
        chi-square         = 368.646
        reduced chi-square = 0.500
        Akaike info crit   = -509.339
        Bayesian info crit = -490.907
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.15973926 +/- 0.197464 (9.14%) (init= 3)
        sigma:       0.15000000 +/- 0.001384 (0.92%) (init= 0.5)
        skew:        0.99999862 +/- 0.110442 (11.04%) (init= 0)
        baseline:    2.57643528 +/- 0.027023 (1.05%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.498 
        C(amplitude, sigma)          =  0.495 
        C(sigma, baseline)           =  0.135 
        C(amplitude, baseline)       = -0.100 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 740
        # variables        = 1
        chi-square         = 447.941
        reduced chi-square = 0.606
        Akaike info crit   = -369.471
        Bayesian info crit = -364.865
    [[Variables]]
        c:   2.65349952 +/- 0.028619 (1.08%) (init= 1)



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


