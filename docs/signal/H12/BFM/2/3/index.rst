:orphan:

H12 / Burkina Faso *An. coluzzii* / Chromosome 2 / #3
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **28,420,001** and
**28,560,000**.
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




The following 17 genes overlap the focal region: :doc:`../../../../../gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`../../../../../gene/AGAP002862` (CYP6AA1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013128` (CYP6AA2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002863` (COEAE6O - carboxylesterase alpha esterase),  :doc:`../../../../../gene/AGAP002864` (CYP6P15P - cytochrome P450),  :doc:`../../../../../gene/AGAP002865` (CYP6P3 - cytochrome P450),  :doc:`../../../../../gene/AGAP002866` (CYP6P5 - cytochrome P450),  :doc:`../../../../../gene/AGAP002867` (CYP6P4 - cytochrome P450),  :doc:`../../../../../gene/AGAP002868` (CYP6P1 - cytochrome P450),  :doc:`../../../../../gene/AGAP002869` (CYP6P2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002870` (CYP6AD1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013202`,  :doc:`../../../../../gene/AGAP000586`,  :doc:`../../../../../gene/AGAP002872` (lipase),  :doc:`../../../../../gene/AGAP002873`,  :doc:`../../../../../gene/AGAP013069`,  :doc:`../../../../../gene/AGAP002874`.




The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`../../../../../gene/AGAP002875` (protein HEXIM1/2),  :doc:`../../../../../gene/AGAP013244` (adenosine deaminase, tRNA-specific 2, TAD2 homolog),  :doc:`../../../../../gene/AGAP002876` (single-strand selective monofunctional uracil DNA glycosylase),  :doc:`../../../../../gene/AGAP002877` (Tetratricopeptide repeat protein 30 homolog),  :doc:`../../../../../gene/AGAP002878` (Cystatin-like protein),  :doc:`../../../../../gene/AGAP002879` (cathepsin F),  :doc:`../../../../../gene/AGAP002880` (COP9 signalosome complex subunit 5).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/UGS/2/1/index`,"2R:28,420,001-28,520,000",1230
    :doc:`../../../../../signal/H12/CMS/2/1/index`,"2R:28,400,001-28,440,000",910
    :doc:`../../../../../signal/H12/GNS/2/2/index`,"2R:28,420,001-28,540,000",848
    :doc:`../../../../../signal/H12/BFS/2/3/index`,"2R:28,440,001-28,520,000",753
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/3/peak_fit.png"/>
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
        chi-square         = 0.078
        reduced chi-square = 0.001
        Akaike info crit   = -1136.862
        Bayesian info crit = -1127.811
    [[Variables]]
        amplitude:   0.38458588 +/- 0.011342 (2.95%) (init= 0.5)
        decay:       0.57207676 +/- 0.028199 (4.93%) (init= 0.5)
        c:           0.04941991 +/- 0.002370 (4.80%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.584 
        C(decay, c)                  = -0.483 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 149
        # variables        = 3
        chi-square         = 0.085
        reduced chi-square = 0.001
        Akaike info crit   = -1106.972
        Bayesian info crit = -1097.960
    [[Variables]]
        amplitude:   0.18340593 +/- 0.010569 (5.76%) (init= 0.5)
        decay:       0.91145911 +/- 0.095539 (10.48%) (init= 0.5)
        c:           0.04042973 +/- 0.003116 (7.71%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.649 
        C(amplitude, decay)          = -0.559 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.889
        reduced chi-square = 0.006
        Akaike info crit   = -767.277
        Bayesian info crit = -764.266
    [[Variables]]
        c:   0.08495204 +/- 0.006306 (7.42%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.294
        reduced chi-square = 0.002
        Akaike info crit   = -918.904
        Bayesian info crit = -915.907
    [[Variables]]
        c:   0.06637828 +/- 0.003674 (5.54%) (init= 0.03)


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
