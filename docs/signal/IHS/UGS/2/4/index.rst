:orphan:




IHS/UGS/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **42,794,895** and
**42,834,895**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP007105`,  :doc:`../../../../../gene/AGAP007106` (ubiquitin carboxyl-terminal hydrolase 47),  :doc:`../../../../../gene/AGAP007107` (DnaJ homolog subfamily B member 4),  :doc:`../../../../../gene/AGAP007108` (multiple PDZ domain protein).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007103` (calsyntenin-1),  :doc:`../../../../../gene/AGAP007104` (farnesyl diphosphate synthase),  :doc:`../../../../../gene/AGAP007109`.


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
    * - :doc:`../../../../../signal/H12/UGS/2/5/index`
      - H12
      - Uganda *An. gambiae*
      - 2L:42,774,895-42,814,895
      - 98
      - 94.4%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/UGS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 624
        # variables        = 4
        chi-square         = 128.889
        reduced chi-square = 0.208
        Akaike info crit   = -976.170
        Bayesian info crit = -958.426
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.71898589 +/- 0.169023 (9.83%) (init= 3)
        decay:       0.28313090 +/- 0.044603 (15.75%) (init= 0.5)
        skew:        0.85203494 +/- 0.164780 (19.34%) (init= 0)
        baseline:    1.96110348 +/- 0.020175 (1.03%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.628 
        C(decay, skew)               = -0.414 
        C(decay, baseline)           = -0.276 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 623
        # variables        = 1
        chi-square         = 166.251
        reduced chi-square = 0.267
        Akaike info crit   = -821.013
        Bayesian info crit = -816.579
    [[Variables]]
        c:   2.04655189 +/- 0.020712 (1.01%) (init= 1)



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


