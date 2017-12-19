
Uganda *An. gambiae* | H12 | Chromosome 2 | Signal #5
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/ugs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2R from
position 51,200,001 to 51,380,000.




The following 12 genes overlap the focal region: :doc:`/genes/AGAP004170`,  :doc:`/genes/AGAP004171` (GSTD8 - glutathione S-transferase delta class 8),  :doc:`/genes/AGAP004172` (GSTD9 - glutathione S-transferase delta class 9),  :doc:`/genes/AGAP004173` (GSTD5 - glutathione S-transferase delta class 5),  :doc:`/genes/AGAP004174`,  :doc:`/genes/AGAP004175` (uridine monophosphate synthetase),  :doc:`/genes/AGAP004176` (serine/threonine-protein kinase/endoribonuclease IRE1),  :doc:`/genes/AGAP013223` (ribosomal RNA large subunit methyltransferase E),  :doc:`/genes/AGAP004177` (23S rRNA (uridine2552-2'-O)-methyltransferase),  :doc:`/genes/AGAP004178`,  :doc:`/genes/AGAP004179` (EF-hand domain family, member A1),  :doc:`/genes/AGAP004181` (Fibroblast growth factor).




The following 3 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP004182`,  :doc:`/genes/AGAP004183`,  :doc:`/genes/AGAP004186`.


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
        # function evals   = 79
        # data points      = 146
        # variables        = 3
        chi-square         = 0.051
        reduced chi-square = 0.000
        Akaike info crit   = -1156.488
        Bayesian info crit = -1147.537
    [[Variables]]
        amplitude:   0.10083065 +/- 0        (0.00%) (init= 0.5)
        decay:       7.35857849 +/- 0        (0.00%) (init= 0.5)
        c:           2.7864e-10 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 76
        # data points      = 148
        # variables        = 3
        chi-square         = 0.074
        reduced chi-square = 0.001
        Akaike info crit   = -1118.904
        Bayesian info crit = -1109.912
    [[Variables]]
        amplitude:   0.09107452 +/- 0        (0.00%) (init= 0.5)
        decay:       5.29993298 +/- 0        (0.00%) (init= 0.5)
        c:           4.9179e-09 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 145
        # variables        = 1
        chi-square         = 0.087
        reduced chi-square = 0.001
        Akaike info crit   = -1073.112
        Bayesian info crit = -1070.135
    [[Variables]]
        c:   0.06849356 +/- 0.002045 (2.99%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 147
        # variables        = 1
        chi-square         = 0.121
        reduced chi-square = 0.001
        Akaike info crit   = -1042.323
        Bayesian info crit = -1039.332
    [[Variables]]
        c:   0.05335807 +/- 0.002372 (4.45%) (init= 0.04)


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
