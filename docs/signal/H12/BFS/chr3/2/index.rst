:orphan:

Burkina Faso *An. gambiae* | H12 | Chromosome 3 | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3L between position 26,880,001 and
26,920,000**.




The following 6 genes overlap the focal region: :doc:`/gene/AGAP011532` (septin),  :doc:`/gene/AGAP011533` (tetratricopeptide repeat protein 15),  :doc:`/gene/AGAP011534`,  :doc:`/gene/AGAP011535` (transcription elongation factor B, polypeptide 1),  :doc:`/gene/AGAP011536` (Mini-chromosome maintenance complex-binding protein),  :doc:`/gene/AGAP011537` (Argonaute 3).




The following 7 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP011530`,  :doc:`/gene/AGAP011531` (Selenium-binding protein 2),  :doc:`/gene/AGAP028430`,  :doc:`/gene/AGAP011538`,  :doc:`/gene/AGAP011539` (dynein intermediate chain 2, axonemal),  :doc:`/gene/AGAP011540` (dynein intermediate chain 2, axonemal),  :doc:`/gene/AGAP011541` (Ecto-NOX disulfide-thiol exchanger 1).


.. figure:: peak_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`/signal/H12/CMS/chr3/2/index`,":26880001-26940000",308
    :doc:`/signal/H12/GNS/chr3/3/index`,":26860001-26900000",180
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. figure:: peak_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: peak_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: peak_fit.png

    **Figure 4**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 194
        # variables        = 3
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -2094.293
        Bayesian info crit = -2084.489
    [[Variables]]
        amplitude:   0.07013950 +/- 0.003643 (5.19%) (init= 0.5)
        decay:       0.15000004 +/- 0.010148 (6.77%) (init= 0.5)
        c:           0.01086198 +/- 0.000336 (3.09%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.588 
        C(decay, c)                  = -0.202 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 200
        # variables        = 3
        chi-square         = 0.010
        reduced chi-square = 0.000
        Akaike info crit   = -1983.146
        Bayesian info crit = -1973.251
    [[Variables]]
        amplitude:   0.07177455 +/- 0.008117 (11.31%) (init= 0.5)
        decay:       0.18708188 +/- 0.027466 (14.68%) (init= 0.5)
        c:           0.00980345 +/- 0.000518 (5.29%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.766 
        C(decay, c)                  = -0.222 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 193
        # variables        = 1
        chi-square         = 0.011
        reduced chi-square = 0.000
        Akaike info crit   = -1880.591
        Bayesian info crit = -1877.328
    [[Variables]]
        c:   0.01207599 +/- 0.000549 (4.55%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 199
        # variables        = 1
        chi-square         = 0.012
        reduced chi-square = 0.000
        Akaike info crit   = -1939.360
        Bayesian info crit = -1936.067
    [[Variables]]
        c:   0.01088202 +/- 0.000541 (4.97%) (init= 0.03)


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
