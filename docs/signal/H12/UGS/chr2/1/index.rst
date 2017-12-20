:orphan:

Uganda *An. gambiae* | H12 | Chromosome 2 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/UGS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **28,420,001** and
**28,520,000**.




The following 12 genes overlap the focal region: :doc:`/gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`/gene/AGAP002862` (CYP6AA1 - cytochrome P450),  :doc:`/gene/AGAP013128` (CYP6AA2 - cytochrome P450),  :doc:`/gene/AGAP002863` (COEAE6O - carboxylesterase alpha esterase),  :doc:`/gene/AGAP002864` (CYP6P15P - cytochrome P450),  :doc:`/gene/AGAP002865` (CYP6P3 - cytochrome P450),  :doc:`/gene/AGAP002866` (CYP6P5 - cytochrome P450),  :doc:`/gene/AGAP002867` (CYP6P4 - cytochrome P450),  :doc:`/gene/AGAP002868` (CYP6P1 - cytochrome P450),  :doc:`/gene/AGAP002869` (CYP6P2 - cytochrome P450),  :doc:`/gene/AGAP002870` (CYP6AD1 - cytochrome P450),  :doc:`/gene/AGAP013202`.




The following 7 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`/gene/AGAP000586`,  :doc:`/gene/AGAP002872` (lipase),  :doc:`/gene/AGAP002873`,  :doc:`/gene/AGAP013069`,  :doc:`/gene/AGAP002874`,  :doc:`/gene/AGAP002875` (protein HEXIM1/2).


.. figure:: peak_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`/signal/H12/CMS/chr2/1/index`,"2R:28,400,001-28,460,000",1231
    :doc:`/signal/H12/GNS/chr2/2/index`,"2R:28,420,001-28,540,000",1069
    :doc:`/signal/H12/BFS/chr2/3/index`,"2R:28,440,001-28,520,000",965
    :doc:`/signal/H12/BFM/chr2/4/index`,"2R:28,380,001-28,500,000",442
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. figure:: peak_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: peak_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: peak_fit.png

    **Figure 4**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 201
        # variables        = 3
        chi-square         = 0.043
        reduced chi-square = 0.000
        Akaike info crit   = -1693.260
        Bayesian info crit = -1683.350
    [[Variables]]
        amplitude:   0.52949660 +/- 0.007260 (1.37%) (init= 0.5)
        decay:       0.57294174 +/- 0.012592 (2.20%) (init= 0.5)
        c:           0.02217734 +/- 0.001226 (5.53%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.614 
        C(decay, c)                  = -0.408 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 199
        # variables        = 3
        chi-square         = 0.035
        reduced chi-square = 0.000
        Akaike info crit   = -1714.791
        Bayesian info crit = -1704.911
    [[Variables]]
        amplitude:   0.75896349 +/- 0.007803 (1.03%) (init= 0.5)
        decay:       0.54484312 +/- 0.008319 (1.53%) (init= 0.5)
        c:           0.01418251 +/- 0.001110 (7.83%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.681 
        C(decay, c)                  = -0.398 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 1.613
        reduced chi-square = 0.008
        Akaike info crit   = -962.048
        Bayesian info crit = -958.750
    [[Variables]]
        c:   0.05862946 +/- 0.006366 (10.86%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 2.762
        reduced chi-square = 0.014
        Akaike info crit   = -843.915
        Bayesian info crit = -840.627
    [[Variables]]
        c:   0.06099785 +/- 0.008414 (13.80%) (init= 0.03)


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
