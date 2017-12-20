:orphan:

Burkina Faso *An. coluzzii* | H12 | Chromosome 2 | Signal #3
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **40,880,001** and
**40,980,000**.




The following 12 genes overlap the focal region: :doc:`/gene/AGAP003639` (Prolylcarboxypeptidase),  :doc:`/gene/AGAP003640` (SP8905),  :doc:`/gene/AGAP003641` (SP8907),  :doc:`/gene/AGAP003642` (SP8898),  :doc:`/gene/AGAP003643` (ubiquitin carboxyl-terminal hydrolase 34),  :doc:`/gene/AGAP003644` (mRpS11 - 28S ribosomal protein S11, mitochondrial),  :doc:`/gene/AGAP003645` (kelch-like protein 19),  :doc:`/gene/AGAP013307`,  :doc:`/gene/AGAP003646`,  :doc:`/gene/AGAP003647`,  :doc:`/gene/AGAP003648` (DNA-directed RNA polymerase II subunit RPB2),  :doc:`/gene/AGAP003649`.




The following 3 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP003638`,  :doc:`/gene/AGAP003650` (translation initiation factor eIF-2B subunit alpha),  :doc:`/gene/AGAP003651` (Tyrosine-protein kinase Fes/Fps).


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

    :doc:`/signal/H12/BFS/chr2/4/index`,"2R:40,800,001-41,020,000",469
    :doc:`/signal/H12/CMS/chr2/3/index`,"2R:40,620,001-41,020,000",451
    



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
        # function evals   = 27
        # data points      = 198
        # variables        = 3
        chi-square         = 0.044
        reduced chi-square = 0.000
        Akaike info crit   = -1661.066
        Bayesian info crit = -1651.201
    [[Variables]]
        amplitude:   0.11987102 +/- 0.010382 (8.66%) (init= 0.5)
        decay:       0.24401091 +/- 0.033478 (13.72%) (init= 0.5)
        c:           0.03221502 +/- 0.001135 (3.53%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.617 
        C(decay, c)                  = -0.256 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 197
        # variables        = 3
        chi-square         = 0.025
        reduced chi-square = 0.000
        Akaike info crit   = -1759.052
        Bayesian info crit = -1749.202
    [[Variables]]
        amplitude:   0.24024117 +/- 0.009245 (3.85%) (init= 0.5)
        decay:       0.31785537 +/- 0.016975 (5.34%) (init= 0.5)
        c:           0.02427600 +/- 0.000888 (3.66%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.725 
        C(decay, c)                  = -0.294 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 197
        # variables        = 1
        chi-square         = 0.080
        reduced chi-square = 0.000
        Akaike info crit   = -1535.817
        Bayesian info crit = -1532.534
    [[Variables]]
        c:   0.03567213 +/- 0.001441 (4.04%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 0.177
        reduced chi-square = 0.001
        Akaike info crit   = -1372.039
        Bayesian info crit = -1368.761
    [[Variables]]
        c:   0.03242169 +/- 0.002151 (6.64%) (init= 0.03)


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
