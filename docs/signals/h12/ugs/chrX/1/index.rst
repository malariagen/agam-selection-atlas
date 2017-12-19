
Uganda *An. gambiae* | H12 | Chromosome X | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/ugs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm X from
position 15,320,001 to 15,460,000.




The following 13 genes overlap the focal region: :doc:`/genes/AGAP000822`,  :doc:`/genes/AGAP000823` (CD81 antigen),  :doc:`/genes/AGAP000824` (bone morphogenetic protein 5),  :doc:`/genes/AGAP000825`,  :doc:`/genes/AGAP000826` (cap-specific mRNA (nucleoside-2'-O-)-methyltransferase 1),  :doc:`/genes/AGAP000829` (calpain-15),  :doc:`/genes/AGAP000830` (CASPS7 - short caspase 7),  :doc:`/genes/AGAP000831` (DnaJ homolog subfamily C member 25),  :doc:`/genes/AGAP000832` (Derlin-2/3),  :doc:`/genes/AGAP000833` (MIP - myoinhibitory-like peptide),  :doc:`/genes/AGAP000834`,  :doc:`/genes/AGAP000835`,  :doc:`/genes/AGAP028655`.




The following 3 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP000820` (CPR125 - cuticular protein RR-2 family 125),  :doc:`/genes/AGAP000821`,  :doc:`/genes/AGAP013506`.


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
        # function evals   = 27
        # data points      = 145
        # variables        = 3
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1443.489
        Bayesian info crit = -1434.559
    [[Variables]]
        amplitude:   0.07164179 +/- 0.002367 (3.30%) (init= 0.5)
        decay:       1.37779028 +/- 0.106060 (7.70%) (init= 0.5)
        c:           0.00688232 +/- 0.001257 (18.27%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.805 
        C(amplitude, decay)          = -0.276 
        C(amplitude, c)              = -0.150 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 147
        # variables        = 3
        chi-square         = 0.029
        reduced chi-square = 0.000
        Akaike info crit   = -1245.669
        Bayesian info crit = -1236.698
    [[Variables]]
        amplitude:   0.08728581 +/- 0.008517 (9.76%) (init= 0.5)
        decay:       0.52782252 +/- 0.079196 (15.00%) (init= 0.5)
        c:           0.02245157 +/- 0.001472 (6.56%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.661 
        C(decay, c)                  = -0.467 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 144
        # variables        = 1
        chi-square         = 0.048
        reduced chi-square = 0.000
        Akaike info crit   = -1150.027
        Bayesian info crit = -1147.057
    [[Variables]]
        c:   0.02172094 +/- 0.001531 (7.05%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 146
        # variables        = 1
        chi-square         = 0.053
        reduced chi-square = 0.000
        Akaike info crit   = -1154.942
        Bayesian info crit = -1151.959
    [[Variables]]
        c:   0.02916075 +/- 0.001579 (5.42%) (init= 0.04)


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
