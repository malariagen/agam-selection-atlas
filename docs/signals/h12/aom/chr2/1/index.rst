
Angola *An. coluzzii* | H12 | Chromosome 2 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/aom` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2R from
position 28,060,001 to 28,100,000.




The following 6 genes overlap the focal region: :doc:`/genes/AGAP002828`,  :doc:`/genes/AGAP002829` (SPN-E - ATP-dependent RNA helicase spindle-E),  :doc:`/genes/AGAP002830` (C-1-tetrahydrofolate synthase, mitochondrial precursor),  :doc:`/genes/AGAP002831` (ribosomal RNA small subunit methyltransferase H),  :doc:`/genes/AGAP013130`,  :doc:`/genes/AGAP002832` (protein-tyrosine phosphatase).




The following 2 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP002824` (GPRTAK1 - putative tachykinin receptor 1),  :doc:`/genes/AGAP002826`.


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
        # function evals   = 31
        # data points      = 151
        # variables        = 3
        chi-square         = 0.047
        reduced chi-square = 0.000
        Akaike info crit   = -1212.229
        Bayesian info crit = -1203.177
    [[Variables]]
        amplitude:   0.51269599 +/- 0.012721 (2.48%) (init= 0.5)
        decay:       0.22732478 +/- 0.009060 (3.99%) (init= 0.5)
        c:           0.02192831 +/- 0.001579 (7.20%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.605 
        C(decay, c)                  = -0.286 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 149
        # variables        = 3
        chi-square         = 0.110
        reduced chi-square = 0.001
        Akaike info crit   = -1068.476
        Bayesian info crit = -1059.464
    [[Variables]]
        amplitude:   0.10952242 +/- 0.008905 (8.13%) (init= 0.5)
        decay:       2.00888266 +/- 0.509040 (25.34%) (init= 0.5)
        c:           0.00837007 +/- 0.008559 (102.26%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.908 
        C(amplitude, c)              = -0.427 
        C(amplitude, decay)          =  0.112 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 149
        # variables        = 1
        chi-square         = 0.456
        reduced chi-square = 0.003
        Akaike info crit   = -860.451
        Bayesian info crit = -857.447
    [[Variables]]
        c:   0.03693419 +/- 0.004549 (12.32%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 8
        # data points      = 148
        # variables        = 1
        chi-square         = 0.192
        reduced chi-square = 0.001
        Akaike info crit   = -981.581
        Bayesian info crit = -978.584
    [[Variables]]
        c:   0.04181212 +/- 0.002973 (7.11%) (init= 0.04)


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
