
Burkina Faso *An. gambiae* | H12 | Chromosome 2 | Signal #6
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2R from
position 40,760,001 to 40,800,000.




The following 3 genes overlap the focal region: :doc:`/genes/AGAP003632` (U3 small nucleolar RNA-associated protein 14),  :doc:`/genes/AGAP003633`,  :doc:`/genes/AGAP003635`.



No genes overlap the windows immediately adjacent to the focal region.




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
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

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

.. figure:: signal_fit.png

    **Figure 3**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 150
        # variables        = 3
        chi-square         = 0.030
        reduced chi-square = 0.000
        Akaike info crit   = -1272.812
        Bayesian info crit = -1263.780
    [[Variables]]
        amplitude:   0.09354209 +/- 0.005882 (6.29%) (init= 0.5)
        decay:       0.85442450 +/- 0.099336 (11.63%) (init= 0.2)
        c:           0.02644573 +/- 0.001754 (6.63%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.623 
        C(amplitude, decay)          = -0.519 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 40
        # data points      = 147
        # variables        = 3
        chi-square         = 0.070
        reduced chi-square = 0.000
        Akaike info crit   = -1119.414
        Bayesian info crit = -1110.442
    [[Variables]]
        amplitude:   0.12834965 +/- 0.009869 (7.69%) (init= 0.5)
        decay:       0.87523068 +/- 0.120664 (13.79%) (init= 0.2)
        c:           0.04130276 +/- 0.002778 (6.73%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.631 
        C(amplitude, decay)          = -0.572 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 7
        # data points      = 149
        # variables        = 1
        chi-square         = 0.091
        reduced chi-square = 0.001
        Akaike info crit   = -1100.688
        Bayesian info crit = -1097.684
    [[Variables]]
        c:   0.03944142 +/- 0.002031 (5.15%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 10
        # data points      = 146
        # variables        = 1
        chi-square         = 0.177
        reduced chi-square = 0.001
        Akaike info crit   = -978.808
        Bayesian info crit = -975.825
    [[Variables]]
        c:   0.05898856 +/- 0.002887 (4.90%) (init= 0.04)


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
