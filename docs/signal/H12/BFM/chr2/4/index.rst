:orphan:

Burkina Faso *An. coluzzii* | H12 | Chromosome 2 | Signal #4
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R between position 28,380,001 and
28,500,000**.




The following 10 genes overlap the focal region: :doc:`/gene/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`/gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`/gene/AGAP002862` (CYP6AA1 - cytochrome P450),  :doc:`/gene/AGAP013128` (CYP6AA2 - cytochrome P450),  :doc:`/gene/AGAP002863` (COEAE6O - carboxylesterase alpha esterase),  :doc:`/gene/AGAP002864` (CYP6P15P - cytochrome P450),  :doc:`/gene/AGAP002865` (CYP6P3 - cytochrome P450),  :doc:`/gene/AGAP002866` (CYP6P5 - cytochrome P450),  :doc:`/gene/AGAP002867` (CYP6P4 - cytochrome P450),  :doc:`/gene/AGAP002868` (CYP6P1 - cytochrome P450).




The following 8 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP002869` (CYP6P2 - cytochrome P450),  :doc:`/gene/AGAP002870` (CYP6AD1 - cytochrome P450),  :doc:`/gene/AGAP013202`,  :doc:`/gene/AGAP000586`,  :doc:`/gene/AGAP002872` (lipase),  :doc:`/gene/AGAP002873`,  :doc:`/gene/AGAP013069`,  :doc:`/gene/AGAP002874`.


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
    :doc:`/signal/H12/CMS/chr2/1/index`,":28400001-28460000",1231
    :doc:`/signal/H12/GNS/chr2/2/index`,":28420001-28540000",1069
    :doc:`/signal/H12/BFS/chr2/3/index`,":28440001-28520000",965
    



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
        # function evals   = 41
        # data points      = 201
        # variables        = 3
        chi-square         = 0.535
        reduced chi-square = 0.003
        Akaike info crit   = -1185.807
        Bayesian info crit = -1175.897
    [[Variables]]
        amplitude:   0.27395897 +/- 0.027747 (10.13%) (init= 0.5)
        decay:       0.47697730 +/- 0.076537 (16.05%) (init= 0.5)
        c:           0.05999999 +/- 0.083879 (139.80%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.621 
        C(decay, c)                  =  0.367 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 199
        # variables        = 3
        chi-square         = 0.130
        reduced chi-square = 0.001
        Akaike info crit   = -1452.957
        Bayesian info crit = -1443.077
    [[Variables]]
        amplitude:   0.37840260 +/- 0.015405 (4.07%) (init= 0.5)
        decay:       0.52432420 +/- 0.031522 (6.01%) (init= 0.5)
        c:           0.04703120 +/- 0.002129 (4.53%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.684 
        C(decay, c)                  = -0.390 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.816
        reduced chi-square = 0.004
        Akaike info crit   = -1098.389
        Bayesian info crit = -1095.091
    [[Variables]]
        c:   0.07927903 +/- 0.004527 (5.71%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.766
        reduced chi-square = 0.004
        Akaike info crit   = -1097.852
        Bayesian info crit = -1094.563
    [[Variables]]
        c:   0.06928399 +/- 0.004431 (6.40%) (init= 0.03)


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
