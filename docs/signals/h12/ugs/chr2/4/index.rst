
Uganda *An. gambiae* | H12 | Chromosome 2 | Signal #4
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/ugs` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 2L from
position 8,640,001 to 8,740,000.




The following 8 genes overlap the focal region: :doc:`/genes/AGAP005034` (GPRMGL5 - putative metabotropic glutamate receptor 5),  :doc:`/genes/AGAP005035` (DNA helicase INO80),  :doc:`/genes/AGAP005036`,  :doc:`/genes/AGAP005037` (Coiled-coil domain-containing protein AGAP005037),  :doc:`/genes/AGAP005038`,  :doc:`/genes/AGAP005039`,  :doc:`/genes/AGAP005040` (RILP-like protein-like protein),  :doc:`/genes/AGAP005041`.




The following 5 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP005031` (E3 SUMO-protein ligase PIAS2),  :doc:`/genes/AGAP005032` (calnexin),  :doc:`/genes/AGAP005033` (U3 small nucleolar RNA-associated protein 20),  :doc:`/genes/AGAP005042`,  :doc:`/genes/AGAP005043` (Inactive dipeptidyl peptidase 10).


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
        # function evals   = 68
        # data points      = 157
        # variables        = 3
        chi-square         = 0.518
        reduced chi-square = 0.003
        Akaike info crit   = -891.182
        Bayesian info crit = -882.013
    [[Variables]]
        amplitude:   0.17966474 +/- 0        (0.00%) (init= 0.5)
        decay:       5.20592460 +/- 0        (0.00%) (init= 0.5)
        c:           1.9694e-11 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 51
        # data points      = 148
        # variables        = 3
        chi-square         = 0.058
        reduced chi-square = 0.000
        Akaike info crit   = -1155.591
        Bayesian info crit = -1146.599
    [[Variables]]
        amplitude:   0.11932943 +/- 0.006513 (5.46%) (init= 0.5)
        decay:       1.73539990 +/- 0.266446 (15.35%) (init= 0.5)
        c:           0.07280324 +/- 0.004966 (6.82%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.874 
        C(amplitude, c)              = -0.255 
        C(amplitude, decay)          = -0.113 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 156
        # variables        = 1
        chi-square         = 0.772
        reduced chi-square = 0.005
        Akaike info crit   = -826.205
        Bayesian info crit = -823.155
    [[Variables]]
        c:   0.09691668 +/- 0.005649 (5.83%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 147
        # variables        = 1
        chi-square         = 0.173
        reduced chi-square = 0.001
        Akaike info crit   = -989.364
        Bayesian info crit = -986.374
    [[Variables]]
        c:   0.10443417 +/- 0.002840 (2.72%) (init= 0.04)


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
