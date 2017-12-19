
Burkina Faso *An. coluzzii* | H12 | Chromosome 3 | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfm` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 3L from
position 5,600,001 to 5,800,000.




The following 5 genes overlap the focal region: :doc:`/genes/AGAP010519` (kinesin-like protein unc-104),  :doc:`/genes/AGAP010520` (krueppel-like factor, other),  :doc:`/genes/AGAP010530` (CLIPE4 - CLIP-domain serine protease),  :doc:`/genes/AGAP010531` (fibrinogen-related protein 7),  :doc:`/genes/AGAP010534`.




The following 11 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP010514` (activator of 90 kDa heat shock protein ATPase),  :doc:`/genes/AGAP010515` (pre-mRNA-splicing factor SYF2),  :doc:`/genes/AGAP010516`,  :doc:`/genes/AGAP010517` (MnSOD1 - manganese-iron superoxide dismutase 1),  :doc:`/genes/AGAP010518`,  :doc:`/genes/AGAP010535` (3-demethylubiquinone-9 3-methyltransferase 2),  :doc:`/genes/AGAP010536` (nucleolar complex protein 2),  :doc:`/genes/AGAP010537` (hexaprenyldihydroxybenzoate methyltransferase),  :doc:`/genes/AGAP010538` (M-phase phosphoprotein),  :doc:`/genes/AGAP010539` (coiled-coil and C2 domain-containing protein 1-like),  :doc:`/genes/AGAP010540`.


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
        # function evals   = 40
        # data points      = 174
        # variables        = 3
        chi-square         = 0.127
        reduced chi-square = 0.001
        Akaike info crit   = -1250.266
        Bayesian info crit = -1240.789
    [[Variables]]
        amplitude:   0.11663930 +/- 0.010397 (8.91%) (init= 0.5)
        decay:       0.99729952 +/- 0.155475 (15.59%) (init= 0.5)
        c:           5.5169e-12 +/- 0.000109 (1967188876.29%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.693 
        C(amplitude, decay)          = -0.466 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 145
        # variables        = 3
        chi-square         = 0.045
        reduced chi-square = 0.000
        Akaike info crit   = -1164.657
        Bayesian info crit = -1155.727
    [[Variables]]
        amplitude:   0.07278003 +/- 0.019419 (26.68%) (init= 0.5)
        decay:       4.43151465 +/- 2.529048 (57.07%) (init= 0.5)
        c:           0.00330635 +/- 0.022059 (667.18%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.983 
        C(amplitude, c)              = -0.979 
        C(amplitude, decay)          =  0.933 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 173
        # variables        = 1
        chi-square         = 0.238
        reduced chi-square = 0.001
        Akaike info crit   = -1138.033
        Bayesian info crit = -1134.880
    [[Variables]]
        c:   0.01806099 +/- 0.002826 (15.65%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 144
        # variables        = 1
        chi-square         = 0.075
        reduced chi-square = 0.001
        Akaike info crit   = -1087.094
        Bayesian info crit = -1084.124
    [[Variables]]
        c:   0.04280073 +/- 0.001905 (4.45%) (init= 0.04)


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
