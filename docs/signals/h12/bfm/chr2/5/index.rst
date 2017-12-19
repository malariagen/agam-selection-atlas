
Burkina Faso *An. coluzzii* | H12 | Chromosome 2 | Signal #5
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfm` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2R from
position 24,820,001 to 24,860,000.




The following 6 genes overlap the focal region: :doc:`/genes/AGAP002636`,  :doc:`/genes/AGAP002637`,  :doc:`/genes/AGAP013045`,  :doc:`/genes/AGAP002638` (ABCH1 - ATP-binding cassette transporter (ABC transporter) family H member 1),  :doc:`/genes/AGAP002639` (Or39 - odorant receptor 39),  :doc:`/genes/AGAP002640` (Or38 - odorant receptor 38).




The following 14 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP002634` (membrane dipeptidase),  :doc:`/genes/AGAP002635` (Gr13 - gustatory receptor 13),  :doc:`/genes/AGAP013517`,  :doc:`/genes/AGAP013086`,  :doc:`/genes/AGAP013456`,  :doc:`/genes/AGAP013225`,  :doc:`/genes/AGAP013322`,  :doc:`/genes/AGAP013353`,  :doc:`/genes/AGAP013110`,  :doc:`/genes/AGAP013484`,  :doc:`/genes/AGAP013247`,  :doc:`/genes/AGAP013316`,  :doc:`/genes/AGAP002641`,  :doc:`/genes/AGAP002642` (DNA mismatch repair protein MSH5).


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
        # function evals   = 47
        # data points      = 151
        # variables        = 3
        chi-square         = 0.117
        reduced chi-square = 0.001
        Akaike info crit   = -1075.643
        Bayesian info crit = -1066.591
    [[Variables]]
        amplitude:   0.17417516 +/- 0.016473 (9.46%) (init= 0.5)
        decay:       0.38089152 +/- 0.057954 (15.22%) (init= 0.5)
        c:           0.04395785 +/- 0.002645 (6.02%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.607 
        C(decay, c)                  = -0.380 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 59
        # data points      = 150
        # variables        = 3
        chi-square         = 0.098
        reduced chi-square = 0.001
        Akaike info crit   = -1094.746
        Bayesian info crit = -1085.714
    [[Variables]]
        amplitude:   0.43959931 +/- 0        (0.00%) (init= 0.5)
        decay:       0.15000000 +/- 0        (0.00%) (init= 0.5)
        c:           0.04447738 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 150
        # variables        = 1
        chi-square         = 0.227
        reduced chi-square = 0.002
        Akaike info crit   = -971.912
        Bayesian info crit = -968.902
    [[Variables]]
        c:   0.05438283 +/- 0.003187 (5.86%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 149
        # variables        = 1
        chi-square         = 0.222
        reduced chi-square = 0.002
        Akaike info crit   = -967.764
        Bayesian info crit = -964.760
    [[Variables]]
        c:   0.05160145 +/- 0.003173 (6.15%) (init= 0.04)


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
