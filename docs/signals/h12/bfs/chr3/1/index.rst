
Burkina Faso *An. gambiae* | H12 | Chromosome 3 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/bfs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 3R from
position 28,480,001 to 28,620,000.




The following 16 genes overlap the focal region: :doc:`/genes/AGAP009184`,  :doc:`/genes/AGAP009185`,  :doc:`/genes/AGAP009187` (Indanol dehydrogenase),  :doc:`/genes/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`/genes/AGAP009189`,  :doc:`/genes/AGAP009190` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`/genes/AGAP009191` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`/genes/AGAP009192` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`/genes/AGAP009193` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`/genes/AGAP009194` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`/genes/AGAP009195` (GSTE1 - glutathione S-transferase epsilon class 1),  :doc:`/genes/AGAP009196` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`/genes/AGAP009197` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`/genes/AGAP009198`,  :doc:`/genes/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`/genes/AGAP009200` (collagen type IV alpha).




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

    :doc:`/signals/h12/ugs/chr3/1/index`,"3R:28560001-28620000",750
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
        # function evals   = 19
        # data points      = 151
        # variables        = 3
        chi-square         = 0.022
        reduced chi-square = 0.000
        Akaike info crit   = -1326.625
        Bayesian info crit = -1317.573
    [[Variables]]
        amplitude:   0.37227263 +/- 0.006946 (1.87%) (init= 0.5)
        decay:       0.41247699 +/- 0.012439 (3.02%) (init= 0.5)
        c:           0.01806011 +/- 0.001169 (6.47%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.604 
        C(decay, c)                  = -0.398 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 19
        # data points      = 128
        # variables        = 3
        chi-square         = 0.059
        reduced chi-square = 0.000
        Akaike info crit   = -977.538
        Bayesian info crit = -968.982
    [[Variables]]
        amplitude:   0.42850612 +/- 0.014404 (3.36%) (init= 0.5)
        decay:       0.44088855 +/- 0.022049 (5.00%) (init= 0.5)
        c:           0.02301842 +/- 0.002307 (10.03%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.676 
        C(decay, c)                  = -0.411 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 150
        # variables        = 1
        chi-square         = 0.601
        reduced chi-square = 0.004
        Akaike info crit   = -826.088
        Bayesian info crit = -823.078
    [[Variables]]
        c:   0.04263120 +/- 0.005183 (12.16%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 127
        # variables        = 1
        chi-square         = 0.697
        reduced chi-square = 0.006
        Akaike info crit   = -659.144
        Bayesian info crit = -656.300
    [[Variables]]
        c:   0.05501850 +/- 0.006597 (11.99%) (init= 0.04)


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
