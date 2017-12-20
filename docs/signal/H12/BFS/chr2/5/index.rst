:orphan:

Burkina Faso *An. gambiae* | H12 | Chromosome 2 | Signal #5
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **25,380,001** and
**25,440,000**.



Gene :doc:`/gene/AGAP006028` (Rdl - GABA-gated chloride channel subunit) overlaps the focal region.





The following 6 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP006029`,  :doc:`/gene/AGAP006030` (mfrn - mitoferrin),  :doc:`/gene/AGAP006031` (nuclear pore complex protein Nup54),  :doc:`/gene/AGAP006032`,  :doc:`/gene/AGAP006033`,  :doc:`/gene/AGAP006034`.


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

    :doc:`/signal/H12/BFM/chr2/2/index`,"2L:25,400,001-25,500,000",1180
    :doc:`/signal/H12/AOM/chr2/3/index`,"2L:25,380,001-25,460,000",392
    



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
        # function evals   = 39
        # data points      = 201
        # variables        = 3
        chi-square         = 0.020
        reduced chi-square = 0.000
        Akaike info crit   = -1849.903
        Bayesian info crit = -1839.993
    [[Variables]]
        amplitude:   0.05969693 +/- 0.003291 (5.51%) (init= 0.5)
        decay:       1.38775652 +/- 0.153043 (11.03%) (init= 0.5)
        c:           0.01225030 +/- 0.001209 (9.87%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.698 
        C(amplitude, decay)          = -0.468 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 200
        # variables        = 3
        chi-square         = 0.062
        reduced chi-square = 0.000
        Akaike info crit   = -1608.950
        Bayesian info crit = -1599.055
    [[Variables]]
        amplitude:   0.15531884 +/- 0.014097 (9.08%) (init= 0.5)
        decay:       0.32824113 +/- 0.041469 (12.63%) (init= 0.5)
        c:           0.03661769 +/- 0.001375 (3.76%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.722 
        C(decay, c)                  = -0.299 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.056
        reduced chi-square = 0.000
        Akaike info crit   = -1632.367
        Bayesian info crit = -1629.069
    [[Variables]]
        c:   0.02232150 +/- 0.001191 (5.34%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 199
        # variables        = 1
        chi-square         = 0.127
        reduced chi-square = 0.001
        Akaike info crit   = -1461.308
        Bayesian info crit = -1458.015
    [[Variables]]
        c:   0.04199544 +/- 0.001798 (4.28%) (init= 0.03)


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
