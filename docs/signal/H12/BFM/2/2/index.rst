:orphan:

H12 / Burkina Faso *An. coluzzii* / Chromosome 2 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **25,400,001** and
**25,520,000**.
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
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>




The following 9 genes overlap the focal region: :doc:`../../../../../gene/AGAP006028` (Rdl - GABA-gated chloride channel subunit),  :doc:`../../../../../gene/AGAP006029`,  :doc:`../../../../../gene/AGAP006030` (mfrn - mitoferrin),  :doc:`../../../../../gene/AGAP006031` (nuclear pore complex protein Nup54),  :doc:`../../../../../gene/AGAP006032`,  :doc:`../../../../../gene/AGAP006033`,  :doc:`../../../../../gene/AGAP006034`,  :doc:`../../../../../gene/AGAP006035` (Ras-related protein Rab-36),  :doc:`../../../../../gene/AGAP006036` (axonemal dynein intermediate chain inner arm i1).




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006037` (RpL24 - 60S ribosomal protein L24),  :doc:`../../../../../gene/AGAP006038` (serine/arginine repetitive matrix protein 2),  :doc:`../../../../../gene/AGAP006039`,  :doc:`../../../../../gene/AGAP006040` (peroxisomal membrane protein 2),  :doc:`../../../../../gene/AGAP006041` (E3 ubiquitin-protein ligase RNF5),  :doc:`../../../../../gene/AGAP006042`,  :doc:`../../../../../gene/AGAP029130`.


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/GAS/2/1/index`,"2L:25,460,001-25,520,000",496
    :doc:`../../../../../signal/H12/BFS/2/5/index`,"2L:25,380,001-25,420,000",409
    :doc:`../../../../../signal/H12/AOM/2/3/index`,"2L:25,380,001-25,460,000",392
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 19
        # data points      = 151
        # variables        = 3
        chi-square         = 0.041
        reduced chi-square = 0.000
        Akaike info crit   = -1235.742
        Bayesian info crit = -1226.690
    [[Variables]]
        amplitude:   0.32833369 +/- 0.007646 (2.33%) (init= 0.5)
        decay:       0.66634871 +/- 0.026671 (4.00%) (init= 0.5)
        c:           0.01406966 +/- 0.001799 (12.79%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.566 
        C(decay, c)                  = -0.531 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 150
        # variables        = 3
        chi-square         = 0.013
        reduced chi-square = 0.000
        Akaike info crit   = -1396.621
        Bayesian info crit = -1387.589
    [[Variables]]
        amplitude:   0.38089750 +/- 0.008128 (2.13%) (init= 0.5)
        decay:       0.28760767 +/- 0.008545 (2.97%) (init= 0.5)
        c:           0.01709534 +/- 0.000855 (5.00%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.724 
        C(decay, c)                  = -0.326 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.672
        reduced chi-square = 0.005
        Akaike info crit   = -809.246
        Bayesian info crit = -806.235
    [[Variables]]
        c:   0.04916964 +/- 0.005482 (11.15%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.341
        reduced chi-square = 0.002
        Akaike info crit   = -903.795
        Bayesian info crit = -900.791
    [[Variables]]
        c:   0.03221222 +/- 0.003933 (12.21%) (init= 0.03)


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
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
