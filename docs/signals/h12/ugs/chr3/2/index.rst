
Uganda *An. gambiae* | H12 | Chromosome 3 | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/ugs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 3R from
position 49,600,001 to 49,820,000.




The following 10 genes overlap the focal region: :doc:`/genes/AGAP010158`,  :doc:`/genes/AGAP010159` (dUTP pyrophosphatase),  :doc:`/genes/AGAP010160` (myosin I),  :doc:`/genes/AGAP010161`,  :doc:`/genes/AGAP010162`,  :doc:`/genes/AGAP010163` (RpL38 - 60S ribosomal protein L38),  :doc:`/genes/AGAP010164` (whd - protein withered, carnitine O-palmitoyltransferase),  :doc:`/genes/AGAP010165` (dynein light intermediate chain 2, cytosolic),  :doc:`/genes/AGAP010166`,  :doc:`/genes/AGAP010167` (numb).




The following 4 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP013762`,  :doc:`/genes/AGAP010157` (Ast2 - allatostatin 2),  :doc:`/genes/AGAP010168`,  :doc:`/genes/AGAP010169`.


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
        # function evals   = 44
        # data points      = 145
        # variables        = 3
        chi-square         = 0.027
        reduced chi-square = 0.000
        Akaike info crit   = -1241.818
        Bayesian info crit = -1232.887
    [[Variables]]
        amplitude:   0.08060342 +/- 0.037502 (46.53%) (init= 0.5)
        decay:       6.82947151 +/- 5.083097 (74.43%) (init= 0.5)
        c:           0.00472933 +/- 0.039794 (841.45%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, c)              = -0.997 
        C(decay, c)                  = -0.993 
        C(amplitude, decay)          =  0.984 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 207
        # variables        = 3
        chi-square         = 0.033
        reduced chi-square = 0.000
        Akaike info crit   = -1803.263
        Bayesian info crit = -1793.265
    [[Variables]]
        amplitude:   0.08404848 +/- 0.009861 (11.73%) (init= 0.5)
        decay:       4.27247803 +/- 1.232280 (28.84%) (init= 0.5)
        c:           0.00431665 +/- 0.011841 (274.32%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.984 
        C(amplitude, c)              = -0.961 
        C(amplitude, decay)          =  0.908 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 10
        # data points      = 144
        # variables        = 1
        chi-square         = 0.051
        reduced chi-square = 0.000
        Akaike info crit   = -1142.902
        Bayesian info crit = -1139.933
    [[Variables]]
        c:   0.05807536 +/- 0.001569 (2.70%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 206
        # variables        = 1
        chi-square         = 0.094
        reduced chi-square = 0.000
        Akaike info crit   = -1581.789
        Bayesian info crit = -1578.461
    [[Variables]]
        c:   0.04296521 +/- 0.001494 (3.48%) (init= 0.04)


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
