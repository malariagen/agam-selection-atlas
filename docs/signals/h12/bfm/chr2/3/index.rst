
Burkina Faso *An. coluzzii* | H12 | Chromosome 2 | Signal #3
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfm` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2R from
position 28,420,001 to 28,560,000.




The following 17 genes overlap the focal region: :doc:`/genes/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`/genes/AGAP002862` (CYP6AA1 - cytochrome P450),  :doc:`/genes/AGAP013128` (CYP6AA2 - cytochrome P450),  :doc:`/genes/AGAP002863` (COEAE6O - carboxylesterase alpha esterase),  :doc:`/genes/AGAP002864` (CYP6P15P - cytochrome P450),  :doc:`/genes/AGAP002865` (CYP6P3 - cytochrome P450),  :doc:`/genes/AGAP002866` (CYP6P5 - cytochrome P450),  :doc:`/genes/AGAP002867` (CYP6P4 - cytochrome P450),  :doc:`/genes/AGAP002868` (CYP6P1 - cytochrome P450),  :doc:`/genes/AGAP002869` (CYP6P2 - cytochrome P450),  :doc:`/genes/AGAP002870` (CYP6AD1 - cytochrome P450),  :doc:`/genes/AGAP013202`,  :doc:`/genes/AGAP000586`,  :doc:`/genes/AGAP002872` (lipase),  :doc:`/genes/AGAP002873`,  :doc:`/genes/AGAP013069`,  :doc:`/genes/AGAP002874`.




The following 8 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`/genes/AGAP002875` (protein HEXIM1/2),  :doc:`/genes/AGAP013244` (adenosine deaminase, tRNA-specific 2, TAD2 homolog),  :doc:`/genes/AGAP002876` (single-strand selective monofunctional uracil DNA glycosylase),  :doc:`/genes/AGAP002877` (Tetratricopeptide repeat protein 30 homolog),  :doc:`/genes/AGAP002878` (Cystatin-like protein),  :doc:`/genes/AGAP002879` (cathepsin F),  :doc:`/genes/AGAP002880` (COP9 signalosome complex subunit 5).


.. figure:: signal_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Related signals
---------------

Overlapping signals
~~~~~~~~~~~~~~~~~~~

The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`/signals/h12/ugs/chr2/1/index`,"2R:28420001-28520000",1230
    :doc:`/signals/h12/bfs/chr2/3/index`,"2R:28440001-28520000",753
    

Adjacent signals
~~~~~~~~~~~~~~~~

The following selection signals have an inferred focus that is immediately
adjacent to the focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Nearby signals
~~~~~~~~~~~~~~

The following signals affect a genome region that overlaps with the genome region
affected by this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/methods/peak_modelling` procedure.

.. figure:: signal_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: signal_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: signal_fit.png

    **Figure 4**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

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
        amplitude:   0.38458587 +/- 0.011342 (2.95%) (init= 0.5)
        decay:       0.57207681 +/- 0.028198 (4.93%) (init= 0.5)
        c:           0.04941991 +/- 0.002369 (4.80%) (init= 0.04)
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
        decay:       0.91145906 +/- 0.095539 (10.48%) (init= 0.5)
        c:           0.04042973 +/- 0.003116 (7.71%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.649 
        C(amplitude, decay)          = -0.559 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 150
        # variables        = 1
        chi-square         = 0.889
        reduced chi-square = 0.006
        Akaike info crit   = -767.277
        Bayesian info crit = -764.266
    [[Variables]]
        c:   0.08495204 +/- 0.006306 (7.42%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 148
        # variables        = 1
        chi-square         = 0.294
        reduced chi-square = 0.002
        Akaike info crit   = -918.904
        Bayesian info crit = -915.907
    [[Variables]]
        c:   0.06637828 +/- 0.003674 (5.54%) (init= 0.04)


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
