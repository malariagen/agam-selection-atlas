
Burkina Faso *An. coluzzii* | H12 | Chromosome 2 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfm` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2L from
position 2,520,001 to 2,900,000.




The following 20 genes overlap the focal region: :doc:`/genes/AGAP004713`,  :doc:`/genes/AGAP004714`,  :doc:`/genes/AGAP004715` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`/genes/AGAP004716` (Gr57 - gustatory receptor 57),  :doc:`/genes/AGAP004717`,  :doc:`/genes/AGAP004718`,  :doc:`/genes/AGAP004719` (CLIPC9 - CLIP-domain serine protease),  :doc:`/genes/AGAP004720`,  :doc:`/genes/AGAP004721` (N-acetylglucosamine-6-sulfatase),  :doc:`/genes/AGAP004722`,  :doc:`/genes/AGAP004723` (chromobox protein homolog 1),  :doc:`/genes/AGAP004724` (Intraflagellar transport 74 homolog),  :doc:`/genes/AGAP004725` (eIF3c - Eukaryotic translation initiation factor 3 subunit C),  :doc:`/genes/AGAP004726` (Uncharacterized protein CG3556),  :doc:`/genes/AGAP004727` (Gr25 - gustatory receptor 25),  :doc:`/genes/AGAP004728`,  :doc:`/genes/AGAP004729`,  :doc:`/genes/AGAP004730` (phospholipase A2, venom),  :doc:`/genes/AGAP004731` (secretory phospholipase A2),  :doc:`/genes/AGAP029113`.




The following 5 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP004709` (mRpL18 - 39S ribosomal protein L18, mitochondrial),  :doc:`/genes/AGAP004710` (ubiquinol-cytochrome c reductase subunit 9),  :doc:`/genes/AGAP004711` (ATP-dependent RNA helicase DDX41),  :doc:`/genes/AGAP004712`,  :doc:`/genes/AGAP004733`.


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

    :doc:`/signals/h12/bfs/chr2/1/index`,"2L:2420001-2720000",1365
    :doc:`/signals/h12/ugs/chr2/2/index`,"2L:2000001-3100000",1003
    

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
        # function evals   = 42
        # data points      = 325
        # variables        = 3
        chi-square         = 1.799
        reduced chi-square = 0.006
        Akaike info crit   = -1682.821
        Bayesian info crit = -1671.470
    [[Variables]]
        amplitude:   0.89089278 +/- 0        (0.00%) (init= 0.5)
        decay:       1.30548171 +/- 0        (0.00%) (init= 0.5)
        c:           1.1213e-10 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 164
        # variables        = 3
        chi-square         = 0.076
        reduced chi-square = 0.000
        Akaike info crit   = -1253.243
        Bayesian info crit = -1243.944
    [[Variables]]
        amplitude:   0.96587637 +/- 0.016018 (1.66%) (init= 0.5)
        decay:       0.36840226 +/- 0.008741 (2.37%) (init= 0.5)
        c:           0.02685048 +/- 0.001924 (7.17%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.706 
        C(decay, c)                  = -0.355 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 323
        # variables        = 1
        chi-square         = 20.902
        reduced chi-square = 0.065
        Akaike info crit   = -882.305
        Bayesian info crit = -878.528
    [[Variables]]
        c:   0.29555443 +/- 0.014176 (4.80%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 163
        # variables        = 1
        chi-square         = 2.915
        reduced chi-square = 0.018
        Akaike info crit   = -653.909
        Bayesian info crit = -650.815
    [[Variables]]
        c:   0.07354618 +/- 0.010506 (14.29%) (init= 0.04)


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
