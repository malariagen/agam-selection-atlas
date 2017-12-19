
Angola *An. coluzzii* | H12 | Chromosome X | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/aom` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm X from
position 15,320,001 to 15,360,000.




The following 6 genes overlap the focal region: :doc:`/genes/AGAP000822`,  :doc:`/genes/AGAP000823` (CD81 antigen),  :doc:`/genes/AGAP000824` (bone morphogenetic protein 5),  :doc:`/genes/AGAP000825`,  :doc:`/genes/AGAP000826` (cap-specific mRNA (nucleoside-2'-O-)-methyltransferase 1),  :doc:`/genes/AGAP000829` (calpain-15).




The following 6 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP000820` (CPR125 - cuticular protein RR-2 family 125),  :doc:`/genes/AGAP000821`,  :doc:`/genes/AGAP000830` (CASPS7 - short caspase 7),  :doc:`/genes/AGAP000831` (DnaJ homolog subfamily C member 25),  :doc:`/genes/AGAP000832` (Derlin-2/3),  :doc:`/genes/AGAP000833` (MIP - myoinhibitory-like peptide).


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

    :doc:`/signals/h12/bfm/chrX/1/index`,"X:15100001-15380000",955
    :doc:`/signals/h12/ugs/chrX/1/index`,"X:15320001-15460000",384
    

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
        # function evals   = 35
        # data points      = 145
        # variables        = 3
        chi-square         = 0.035
        reduced chi-square = 0.000
        Akaike info crit   = -1201.711
        Bayesian info crit = -1192.780
    [[Variables]]
        amplitude:   0.06894887 +/- 0.010894 (15.80%) (init= 0.5)
        decay:       0.26104509 +/- 0.072378 (27.73%) (init= 0.5)
        c:           0.02791449 +/- 0.001407 (5.04%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.603 
        C(decay, c)                  = -0.273 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 147
        # variables        = 3
        chi-square         = 0.050
        reduced chi-square = 0.000
        Akaike info crit   = -1168.611
        Bayesian info crit = -1159.640
    [[Variables]]
        amplitude:   0.05888290 +/- 0        (0.00%) (init= 0.5)
        decay:       4.72780251 +/- 0        (0.00%) (init= 0.5)
        c:           8.3371e-10 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 144
        # variables        = 1
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1156.607
        Bayesian info crit = -1153.637
    [[Variables]]
        c:   0.03033815 +/- 0.001496 (4.93%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 146
        # variables        = 1
        chi-square         = 0.072
        reduced chi-square = 0.000
        Akaike info crit   = -1109.832
        Bayesian info crit = -1106.848
    [[Variables]]
        c:   0.03263121 +/- 0.001843 (5.65%) (init= 0.04)


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
