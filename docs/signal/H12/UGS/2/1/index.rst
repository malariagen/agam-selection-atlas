:orphan:

H12 / Uganda *An. gambiae* / Chromosome 2 / #1
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **28,420,001** and
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
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>




The following 12 genes overlap the focal region: :doc:`../../../../../gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`../../../../../gene/AGAP002862` (CYP6AA1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013128` (CYP6AA2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002863` (COEAE6O - carboxylesterase alpha esterase),  :doc:`../../../../../gene/AGAP002864` (CYP6P15P - cytochrome P450),  :doc:`../../../../../gene/AGAP002865` (CYP6P3 - cytochrome P450),  :doc:`../../../../../gene/AGAP002866` (CYP6P5 - cytochrome P450),  :doc:`../../../../../gene/AGAP002867` (CYP6P4 - cytochrome P450),  :doc:`../../../../../gene/AGAP002868` (CYP6P1 - cytochrome P450),  :doc:`../../../../../gene/AGAP002869` (CYP6P2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002870` (CYP6AD1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013202`.




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`../../../../../gene/AGAP000586`,  :doc:`../../../../../gene/AGAP002872` (lipase),  :doc:`../../../../../gene/AGAP002873`,  :doc:`../../../../../gene/AGAP013069`,  :doc:`../../../../../gene/AGAP002874`,  :doc:`../../../../../gene/AGAP002875` (protein HEXIM1/2).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/CMS/2/1/index`,"2R:28,400,001-28,440,000",910
    :doc:`../../../../../signal/H12/GNS/2/2/index`,"2R:28,420,001-28,540,000",848
    :doc:`../../../../../signal/H12/BFS/2/3/index`,"2R:28,440,001-28,520,000",753
    :doc:`../../../../../signal/H12/BFM/2/3/index`,"2R:28,420,001-28,560,000",557
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/1/peak_fit.png"/>
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
        chi-square         = 0.032
        reduced chi-square = 0.000
        Akaike info crit   = -1269.823
        Bayesian info crit = -1260.771
    [[Variables]]
        amplitude:   0.52948475 +/- 0.007296 (1.38%) (init= 0.5)
        decay:       0.57330194 +/- 0.013208 (2.30%) (init= 0.5)
        c:           0.02210332 +/- 0.001526 (6.91%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.583 
        C(decay, c)                  = -0.484 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 149
        # variables        = 3
        chi-square         = 0.034
        reduced chi-square = 0.000
        Akaike info crit   = -1244.401
        Bayesian info crit = -1235.389
    [[Variables]]
        amplitude:   0.75940105 +/- 0.008942 (1.18%) (init= 0.5)
        decay:       0.53929390 +/- 0.009795 (1.82%) (init= 0.5)
        c:           0.01598470 +/- 0.001559 (9.76%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.660 
        C(decay, c)                  = -0.470 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 1.515
        reduced chi-square = 0.010
        Akaike info crit   = -687.328
        Bayesian info crit = -684.317
    [[Variables]]
        c:   0.07073491 +/- 0.008231 (11.64%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 2.593
        reduced chi-square = 0.018
        Akaike info crit   = -596.558
        Bayesian info crit = -593.560
    [[Variables]]
        c:   0.07795459 +/- 0.010917 (14.01%) (init= 0.03)


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
