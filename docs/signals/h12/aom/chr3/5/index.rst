
Angola *An. coluzzii* | H12 | Chromosome 3 | Signal #5
================================================================================



This page describes a signal of selection found in the
:doc:`/populations/aom` population using the
:doc:`/methods/h12` statistic.
The inferred focus of this signal is on chromosome arm 3R from
position 46,220,001 to 46,540,000.




The following 4 genes overlap the focal region: :doc:`/genes/AGAP009954` (ankyrin repeat domain-containing protein 13C),  :doc:`/genes/AGAP009955`,  :doc:`/genes/AGAP009956`,  :doc:`/genes/AGAP009957` (transcription factor SOX1/3/14/21 (SOX group B)).




The following 3 genes are within 40 kbp of the focal
region: :doc:`/genes/AGAP009953` (guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-13),  :doc:`/genes/AGAP009958` (arginine and glutamate-rich protein 1),  :doc:`/genes/AGAP009959` (tubulin monoglycylase TTLL3/8).


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
        # function evals   = 92
        # data points      = 149
        # variables        = 3
        chi-square         = 0.123
        reduced chi-square = 0.001
        Akaike info crit   = -1052.041
        Bayesian info crit = -1043.029
    [[Variables]]
        amplitude:   0.07299790 +/- 0        (0.00%) (init= 0.5)
        decay:       4.82769136 +/- 0        (0.00%) (init= 0.5)
        c:           1.2674e-12 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 144
        # variables        = 3
        chi-square         = 0.064
        reduced chi-square = 0.000
        Akaike info crit   = -1104.879
        Bayesian info crit = -1095.969
    [[Variables]]
        amplitude:   0.09474286 +/- 0        (0.00%) (init= 0.5)
        decay:       1.64716704 +/- 0        (0.00%) (init= 0.5)
        c:           9.1527e-10 +/- 0        (0.00%) (init= 0.04)
        cap:         1 (fixed)


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 7
        # data points      = 148
        # variables        = 1
        chi-square         = 0.158
        reduced chi-square = 0.001
        Akaike info crit   = -1010.331
        Bayesian info crit = -1007.333
    [[Variables]]
        c:   0.04040749 +/- 0.002697 (6.68%) (init= 0.04)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 143
        # variables        = 1
        chi-square         = 0.151
        reduced chi-square = 0.001
        Akaike info crit   = -978.296
        Bayesian info crit = -975.333
    [[Variables]]
        c:   0.02360643 +/- 0.002724 (11.54%) (init= 0.04)


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
