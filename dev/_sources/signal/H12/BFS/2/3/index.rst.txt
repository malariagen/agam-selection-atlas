:orphan:




H12 / Burkina Faso *An. gambiae* / Chromosome 2 / #3
====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **28,440,001** and
**28,520,000**.
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




The following 12 genes overlap the focal region: :doc:`../../../../../gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`../../../../../gene/AGAP002862`:sup:`1` (CYP6AA1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013128`:sup:`1` (CYP6AA2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002863`:sup:`1` (COEAE6O - carboxylesterase alpha esterase),  :doc:`../../../../../gene/AGAP002864`:sup:`1` (CYP6P15P - cytochrome P450),  :doc:`../../../../../gene/AGAP002865`:sup:`1` (CYP6P3 - cytochrome P450),  :doc:`../../../../../gene/AGAP002866`:sup:`1` (CYP6P5 - cytochrome P450),  :doc:`../../../../../gene/AGAP002867`:sup:`1` (CYP6P4 - cytochrome P450),  :doc:`../../../../../gene/AGAP002868`:sup:`1` (CYP6P1 - cytochrome P450),  :doc:`../../../../../gene/AGAP002869`:sup:`1` (CYP6P2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002870`:sup:`1` (CYP6AD1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013202`.




The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000586`,  :doc:`../../../../../gene/AGAP002872` (lipase),  :doc:`../../../../../gene/AGAP002873`,  :doc:`../../../../../gene/AGAP013069`,  :doc:`../../../../../gene/AGAP002874`,  :doc:`../../../../../gene/AGAP002875` (protein HEXIM1/2).


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
    <img src="../../../../../_static/data/signal/H12/BFS/2/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 151
        # variables        = 3
        chi-square         = 0.031
        reduced chi-square = 0.000
        Akaike info crit   = -1274.992
        Bayesian info crit = -1265.940
    [[Variables]]
        amplitude:   0.38063638 +/- 0.010058 (2.64%) (init= 0.5)
        decay:       0.24559296 +/- 0.010400 (4.23%) (init= 0.5)
        c:           0.02019622 +/- 0.001292 (6.40%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.607 
        C(decay, c)                  = -0.298 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 149
        # variables        = 3
        chi-square         = 0.028
        reduced chi-square = 0.000
        Akaike info crit   = -1273.906
        Bayesian info crit = -1264.894
    [[Variables]]
        amplitude:   0.34898913 +/- 0.010487 (3.01%) (init= 0.5)
        decay:       0.35025840 +/- 0.015079 (4.31%) (init= 0.5)
        c:           0.02480874 +/- 0.001290 (5.20%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.706 
        C(decay, c)                  = -0.365 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.358
        reduced chi-square = 0.002
        Akaike info crit   = -903.690
        Bayesian info crit = -900.679
    [[Variables]]
        c:   0.03437788 +/- 0.004002 (11.64%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.353
        reduced chi-square = 0.002
        Akaike info crit   = -891.818
        Bayesian info crit = -888.821
    [[Variables]]
        c:   0.04210692 +/- 0.004026 (9.56%) (init= 0.03)


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


