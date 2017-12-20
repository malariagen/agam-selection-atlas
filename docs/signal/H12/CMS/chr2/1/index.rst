:orphan:

Cameroon *An. gambiae* | H12 | Chromosome 2 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/CMS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R between position 28,400,001 and
28,460,000**.



Gene :doc:`/gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)) overlaps the focal region.





The following 11 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`/gene/AGAP002862` (CYP6AA1 - cytochrome P450),  :doc:`/gene/AGAP013128` (CYP6AA2 - cytochrome P450),  :doc:`/gene/AGAP002863` (COEAE6O - carboxylesterase alpha esterase),  :doc:`/gene/AGAP002864` (CYP6P15P - cytochrome P450),  :doc:`/gene/AGAP002865` (CYP6P3 - cytochrome P450),  :doc:`/gene/AGAP002866` (CYP6P5 - cytochrome P450),  :doc:`/gene/AGAP002867` (CYP6P4 - cytochrome P450),  :doc:`/gene/AGAP002868` (CYP6P1 - cytochrome P450),  :doc:`/gene/AGAP002869` (CYP6P2 - cytochrome P450),  :doc:`/gene/AGAP002870` (CYP6AD1 - cytochrome P450).


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

    :doc:`/signal/H12/UGS/chr2/1/index`,":28420001-28520000",1602
    :doc:`/signal/H12/GNS/chr2/2/index`,":28420001-28540000",1069
    :doc:`/signal/H12/BFS/chr2/3/index`,":28440001-28520000",965
    :doc:`/signal/H12/BFM/chr2/4/index`,":28380001-28500000",442
    



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
        chi-square         = 0.017
        reduced chi-square = 0.000
        Akaike info crit   = -1873.454
        Bayesian info crit = -1863.544
    [[Variables]]
        amplitude:   0.20360574 +/- 0.003614 (1.78%) (init= 0.5)
        decay:       0.99930145 +/- 0.031188 (3.12%) (init= 0.5)
        c:           0.01107805 +/- 0.000932 (8.41%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.572 
        C(amplitude, decay)          = -0.555 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 199
        # variables        = 3
        chi-square         = 0.054
        reduced chi-square = 0.000
        Akaike info crit   = -1628.472
        Bayesian info crit = -1618.592
    [[Variables]]
        amplitude:   0.37902174 +/- 0.007521 (1.98%) (init= 0.5)
        decay:       0.85605990 +/- 0.027505 (3.21%) (init= 0.5)
        c:           0.01799454 +/- 0.001556 (8.65%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.627 
        C(decay, c)                  = -0.522 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.392
        reduced chi-square = 0.002
        Akaike info crit   = -1244.788
        Bayesian info crit = -1241.490
    [[Variables]]
        c:   0.03602092 +/- 0.003139 (8.72%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 1.104
        reduced chi-square = 0.006
        Akaike info crit   = -1025.499
        Bayesian info crit = -1022.210
    [[Variables]]
        c:   0.05620172 +/- 0.005319 (9.47%) (init= 0.03)


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
