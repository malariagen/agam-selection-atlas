
Guinea-Bissau | H12 | Chromosome 3 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/gwa` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 3R from
position 45,080,001 to 45,160,000.



Gene :doc:`/genes/AGAP009899` overlaps the focal region.





The following 10 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP009901` (diphosphoinositol-polyphosphate diphosphatase),  :doc:`/genes/AGAP009902` (E3 ubiquitin-protein ligase RNF146),  :doc:`/genes/AGAP009903` (tRNA pseudouridine synthase (Fragment)),  :doc:`/genes/AGAP009904` (tRNA (adenine-N(1)-)-methyltransferase non-catalytic subunit),  :doc:`/genes/AGAP009905` (PHD finger-like domain-containing protein 5A),  :doc:`/genes/AGAP009906`,  :doc:`/genes/AGAP009907` (leukotriene-A4 hydrolase),  :doc:`/genes/AGAP009908` (mRpL13 - 39S ribosomal protein L13, mitochondrial),  :doc:`/genes/AGAP009909`,  :doc:`/genes/AGAP009910` (ATP-dependent DNA helicase 2 subunit 2).


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
        # function evals   = 71
        # data points      = 145
        # variables        = 3
        chi-square         = 0.025
        reduced chi-square = 0.000
        Akaike info crit   = -1252.378
        Bayesian info crit = -1243.448
    [[Variables]]
        amplitude:   0.06016655 +/- 0.008356 (13.89%) (init= 0.5)
        decay:       0.31174847 +/- 0.069513 (22.30%) (init= 0.5)
        c:           0.04148278 +/- 0.001236 (2.98%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.607 
        C(decay, c)                  = -0.347 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 146
        # variables        = 3
        chi-square         = 0.028
        reduced chi-square = 0.000
        Akaike info crit   = -1243.216
        Bayesian info crit = -1234.265
    [[Variables]]
        amplitude:   0.05102982 +/- 0.012583 (24.66%) (init= 0.5)
        decay:       3.99317103 +/- 2.256846 (56.52%) (init= 0.5)
        c:           0.02518721 +/- 0.014732 (58.49%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.979 
        C(amplitude, c)              = -0.967 
        C(amplitude, decay)          =  0.907 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 144
        # variables        = 1
        chi-square         = 0.036
        reduced chi-square = 0.000
        Akaike info crit   = -1193.151
        Bayesian info crit = -1190.181
    [[Variables]]
        c:   0.04453994 +/- 0.001318 (2.96%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 145
        # variables        = 1
        chi-square         = 0.043
        reduced chi-square = 0.000
        Akaike info crit   = -1175.152
        Bayesian info crit = -1172.176
    [[Variables]]
        c:   0.05129455 +/- 0.001438 (2.80%) (init= 0.04)


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
