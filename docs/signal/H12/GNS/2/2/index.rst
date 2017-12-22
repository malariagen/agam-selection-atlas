:orphan:

H12 / Guinea *An. gambiae* / Chromosome 2 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **28,420,001** and
**28,540,000**.
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




The following 15 genes overlap the focal region: :doc:`../../../../../gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`../../../../../gene/AGAP002862` (CYP6AA1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013128` (CYP6AA2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002863` (COEAE6O - carboxylesterase alpha esterase),  :doc:`../../../../../gene/AGAP002864` (CYP6P15P - cytochrome P450),  :doc:`../../../../../gene/AGAP002865` (CYP6P3 - cytochrome P450),  :doc:`../../../../../gene/AGAP002866` (CYP6P5 - cytochrome P450),  :doc:`../../../../../gene/AGAP002867` (CYP6P4 - cytochrome P450),  :doc:`../../../../../gene/AGAP002868` (CYP6P1 - cytochrome P450),  :doc:`../../../../../gene/AGAP002869` (CYP6P2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002870` (CYP6AD1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013202`,  :doc:`../../../../../gene/AGAP000586`,  :doc:`../../../../../gene/AGAP002872` (lipase),  :doc:`../../../../../gene/AGAP002873`.




The following 10 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`../../../../../gene/AGAP013069`,  :doc:`../../../../../gene/AGAP002874`,  :doc:`../../../../../gene/AGAP002875` (protein HEXIM1/2),  :doc:`../../../../../gene/AGAP013244` (adenosine deaminase, tRNA-specific 2, TAD2 homolog),  :doc:`../../../../../gene/AGAP002876` (single-strand selective monofunctional uracil DNA glycosylase),  :doc:`../../../../../gene/AGAP002877` (Tetratricopeptide repeat protein 30 homolog),  :doc:`../../../../../gene/AGAP002878` (Cystatin-like protein),  :doc:`../../../../../gene/AGAP002879` (cathepsin F),  :doc:`../../../../../gene/AGAP002880` (COP9 signalosome complex subunit 5).


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
    :doc:`../../../../../signal/H12/BFS/2/3/index`,"2R:28,440,001-28,520,000",753
    :doc:`../../../../../signal/H12/BFM/2/3/index`,"2R:28,420,001-28,560,000",557
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/2/peak_fit.png"/>
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
        chi-square         = 0.019
        reduced chi-square = 0.000
        Akaike info crit   = -1348.404
        Bayesian info crit = -1339.352
    [[Variables]]
        amplitude:   0.39757848 +/- 0.007379 (1.86%) (init= 0.5)
        decay:       0.29461693 +/- 0.008746 (2.97%) (init= 0.5)
        c:           0.03188602 +/- 0.001033 (3.24%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.610 
        C(decay, c)                  = -0.329 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 149
        # variables        = 3
        chi-square         = 0.045
        reduced chi-square = 0.000
        Akaike info crit   = -1202.043
        Bayesian info crit = -1193.031
    [[Variables]]
        amplitude:   0.30428469 +/- 0.009436 (3.10%) (init= 0.5)
        decay:       0.62935545 +/- 0.031206 (4.96%) (init= 0.5)
        c:           0.03035989 +/- 0.001888 (6.22%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.638 
        C(decay, c)                  = -0.517 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.497
        reduced chi-square = 0.003
        Akaike info crit   = -854.556
        Bayesian info crit = -851.545
    [[Variables]]
        c:   0.05030176 +/- 0.004714 (9.37%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.477
        reduced chi-square = 0.003
        Akaike info crit   = -847.269
        Bayesian info crit = -844.272
    [[Variables]]
        c:   0.05927454 +/- 0.004680 (7.90%) (init= 0.03)


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
