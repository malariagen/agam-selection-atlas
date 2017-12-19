
Uganda *An. gambiae* | H12 | Chromosome 3 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/ugs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 3R from
position 28,560,001 to 28,620,000.




The following 15 genes overlap the focal region: :doc:`/genes/AGAP009185`,  :doc:`/genes/AGAP009187` (Indanol dehydrogenase),  :doc:`/genes/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`/genes/AGAP009189`,  :doc:`/genes/AGAP009190` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`/genes/AGAP009191` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`/genes/AGAP009192` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`/genes/AGAP009193` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`/genes/AGAP009194` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`/genes/AGAP009195` (GSTE1 - glutathione S-transferase epsilon class 1),  :doc:`/genes/AGAP009196` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`/genes/AGAP009197` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`/genes/AGAP009198`,  :doc:`/genes/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`/genes/AGAP009200` (collagen type IV alpha).




The following 4 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP009201` (collagen type IV alpha),  :doc:`/genes/AGAP009202` (selenoprotein T),  :doc:`/genes/AGAP028058`,  :doc:`/genes/AGAP009203` (SPRY domain-containing SOCS box protein 3).


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

    :doc:`/signals/h12/bfs/chr3/1/index`,"3R:28480001-28620000",818
    :doc:`/signals/h12/bfm/chr3/1/index`,"3R:28520001-28620000",676
    

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
        # data points      = 151
        # variables        = 3
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1497.293
        Bayesian info crit = -1488.241
    [[Variables]]
        amplitude:   0.26111748 +/- 0.005388 (2.06%) (init= 0.5)
        decay:       0.17530508 +/- 0.005890 (3.36%) (init= 0.5)
        c:           0.01840311 +/- 0.000603 (3.27%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.592 
        C(decay, c)                  = -0.249 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 128
        # variables        = 3
        chi-square         = 0.016
        reduced chi-square = 0.000
        Akaike info crit   = -1144.356
        Bayesian info crit = -1135.800
    [[Variables]]
        amplitude:   0.34255756 +/- 0.011732 (3.43%) (init= 0.5)
        decay:       0.21937578 +/- 0.010149 (4.63%) (init= 0.5)
        c:           0.02258692 +/- 0.001098 (4.86%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.743 
        C(decay, c)                  = -0.305 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 10
        # data points      = 150
        # variables        = 1
        chi-square         = 0.117
        reduced chi-square = 0.001
        Akaike info crit   = -1071.074
        Bayesian info crit = -1068.063
    [[Variables]]
        c:   0.02518365 +/- 0.002290 (9.10%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 127
        # variables        = 1
        chi-square         = 0.196
        reduced chi-square = 0.002
        Akaike info crit   = -820.499
        Bayesian info crit = -817.655
    [[Variables]]
        c:   0.03397464 +/- 0.003495 (10.29%) (init= 0.04)


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
