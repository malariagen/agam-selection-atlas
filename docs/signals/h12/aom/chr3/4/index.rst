
Angola *An. coluzzii* | H12 | Chromosome 3 | Signal #4
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/aom` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 3L from
position 8,080,001 to 8,180,000.




The following 9 genes overlap the focal region: :doc:`/genes/AGAP010655`,  :doc:`/genes/AGAP010656` (ATP-dependent RNA helicase DDX46/PRP5),  :doc:`/genes/AGAP010657`,  :doc:`/genes/AGAP010658`,  :doc:`/genes/AGAP010659`,  :doc:`/genes/AGAP010661` (eupolytin),  :doc:`/genes/AGAP010662`,  :doc:`/genes/AGAP010663` (female reproductive tract protease GLEANR_2575),  :doc:`/genes/AGAP010669` (TOLL5B - TOLL-like receptor 5B).




The following 4 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP010670` (ATP-dependent RNA helicase DDX31/DBP7),  :doc:`/genes/AGAP010671` (actin-related protein 8),  :doc:`/genes/AGAP010672` (succinate dehydrogenase (ubiquinone) cytochrome b560 subunit),  :doc:`/genes/AGAP010673`.


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
        # function evals   = 54
        # data points      = 146
        # variables        = 3
        chi-square         = 0.040
        reduced chi-square = 0.000
        Akaike info crit   = -1192.536
        Bayesian info crit = -1183.586
    [[Variables]]
        amplitude:   0.05346192 +/- 0        (0.00%) (init= 0.5)
        decay:       1.70155409 +/- 0        (0.00%) (init= 0.5)
        c:           1.5636e-09 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 51
        # data points      = 146
        # variables        = 3
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1440.098
        Bayesian info crit = -1431.147
    [[Variables]]
        amplitude:   0.03429708 +/- 0.005102 (14.88%) (init= 0.5)
        decay:       0.38800220 +/- 0.084177 (21.70%) (init= 0.5)
        c:           0.02912586 +/- 0.000689 (2.37%) (init= 0.04)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.695 
        C(decay, c)                  = -0.392 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 145
        # variables        = 1
        chi-square         = 0.071
        reduced chi-square = 0.000
        Akaike info crit   = -1103.732
        Bayesian info crit = -1100.755
    [[Variables]]
        c:   0.01300748 +/- 0.001840 (14.15%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 145
        # variables        = 1
        chi-square         = 0.010
        reduced chi-square = 0.000
        Akaike info crit   = -1384.307
        Bayesian info crit = -1381.331
    [[Variables]]
        c:   0.03102011 +/- 0.000699 (2.25%) (init= 0.04)


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
