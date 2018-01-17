:orphan:




IHS/BFS/3/7
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **42,540,000** and
**42,980,000**.
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


The following 7 genes overlap the focal region: :doc:`../../../../../gene/AGAP009768` (solute carrier family 6 (neurotransmitter transporter, GABA) member 1),  :doc:`../../../../../gene/AGAP009769`,  :doc:`../../../../../gene/AGAP009770` (GPRCAL1 - putative calcitonin receptor 1),  :doc:`../../../../../gene/AGAP009771`,  :doc:`../../../../../gene/AGAP009772` (Protein PTCD3-like protein, mitochondrial),  :doc:`../../../../../gene/AGAP009773`,  :doc:`../../../../../gene/AGAP009774`.



Gene :doc:`../../../../../gene/AGAP009775` is within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/IHS/CMS/3/2/index`
      - IHS
      - Cameroon *An. gambiae*
      - 3R:42,500,000-42,660,000
      - 191
      - 91.1%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/7/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/7/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/7/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 67
        # data points      = 590
        # variables        = 4
        chi-square         = 99.118
        reduced chi-square = 0.169
        Akaike info crit   = -1044.448
        Bayesian info crit = -1026.928
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.81991859 +/- 0.064905 (7.92%) (init= 3)
        decay:       2.99998008 +/- 0.552444 (18.41%) (init= 0.5)
        skew:       -0.86742314 +/- 0.116352 (13.41%) (init= 0)
        baseline:    2.28226131 +/- 0.046788 (2.05%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.777 
        C(amplitude, baseline)       = -0.465 
        C(amplitude, skew)           =  0.340 
        C(skew, baseline)            = -0.259 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 589
        # variables        = 1
        chi-square         = 126.768
        reduced chi-square = 0.216
        Akaike info crit   = -902.746
        Bayesian info crit = -898.367
    [[Variables]]
        c:   2.57943473 +/- 0.019131 (0.74%) (init= 1)



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


