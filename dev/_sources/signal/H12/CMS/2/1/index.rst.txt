:orphan:




H12 / Cameroon *An. gambiae* / Chromosome 2 / #1
================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **28,400,001** and
**28,440,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----



Gene :doc:`../../../../../gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)) overlaps the focal region.





The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`../../../../../gene/AGAP002862`:sup:`1` (CYP6AA1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013128`:sup:`1` (CYP6AA2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002863`:sup:`1` (COEAE6O - carboxylesterase alpha esterase),  :doc:`../../../../../gene/AGAP002864`:sup:`1` (CYP6P15P - cytochrome P450).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have an focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/UGS/2/1/index`, "2R:28,420,001-28,520,000", 1230 (582 | 647)
    :doc:`../../../../../signal/H12/GNS/2/2/index`, "2R:28,420,001-28,540,000", 848 (493 | 354)
    :doc:`../../../../../signal/H12/BFM/2/3/index`, "2R:28,420,001-28,560,000", 557 (369 | 188)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 151
        # variables        = 3
        chi-square         = 0.016
        reduced chi-square = 0.000
        Akaike info crit   = -1375.354
        Bayesian info crit = -1366.302
    [[Variables]]
        amplitude:   0.20374244 +/- 0.003987 (1.96%) (init= 0.5)
        decay:       1.01323923 +/- 0.039297 (3.88%) (init= 0.5)
        c:           0.01031565 +/- 0.001428 (13.85%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.686 
        C(amplitude, decay)          = -0.471 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 149
        # variables        = 3
        chi-square         = 0.052
        reduced chi-square = 0.000
        Akaike info crit   = -1179.627
        Bayesian info crit = -1170.615
    [[Variables]]
        amplitude:   0.37900901 +/- 0.008649 (2.28%) (init= 0.5)
        decay:       0.84199286 +/- 0.033781 (4.01%) (init= 0.5)
        c:           0.01961050 +/- 0.002327 (11.87%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.619 
        C(amplitude, decay)          = -0.580 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.353
        reduced chi-square = 0.002
        Akaike info crit   = -905.800
        Bayesian info crit = -902.790
    [[Variables]]
        c:   0.04398483 +/- 0.003974 (9.04%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.994
        reduced chi-square = 0.007
        Akaike info crit   = -738.440
        Bayesian info crit = -735.442
    [[Variables]]
        c:   0.06979709 +/- 0.006760 (9.69%) (init= 0.03)


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


