:orphan:

Angola *An. coluzzii* | H12 | Chromosome 2 | Signal #6
================================================================================



This page describes a signal of selection found in the
:doc:`/population/AOM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
2R between position 34,440,001 and
34,540,000.




The following 18 genes overlap the focal region: :doc:`/gene/AGAP003245` (CLIPA19 - CLIP-domain serine protease),  :doc:`/gene/AGAP003246` (CLIPB2 - CLIP-domain serine protease),  :doc:`/gene/AGAP003247` (CLIPB19 - CLIP-domain serine protease),  :doc:`/gene/AGAP003248`,  :doc:`/gene/AGAP013487`,  :doc:`/gene/AGAP003249` (CLIPB3 - CLIP-domain serine protease),  :doc:`/gene/AGAP003250` (CLIPB4 - CLIP-domain serine protease),  :doc:`/gene/AGAP003251` (CLIPB1 - CLIP-domain serine protease),  :doc:`/gene/AGAP003252` (CLIPB6 - CLIP-domain serine protease),  :doc:`/gene/AGAP013184` (CLIPB36 - CLIP-domain serine protease),  :doc:`/gene/AGAP003253` (Gr15 - gustatory receptor 15),  :doc:`/gene/AGAP003254` (Gr16 - gustatory receptor 16),  :doc:`/gene/AGAP003255` (Gr17 - gustatory receptor 17),  :doc:`/gene/AGAP003256` (Gr18 - gustatory receptor 18),  :doc:`/gene/AGAP003257` (GSTU2 - glutathione S-transferase unclassified 2),  :doc:`/gene/AGAP003258` (Gustatory receptor),  :doc:`/gene/AGAP003259` (Gr20 - gustatory receptor 20),  :doc:`/gene/AGAP003260` (Gr21 - gustatory receptor 21).




The following 6 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP003242` (RNA polymerase-associated protein LEO1),  :doc:`/gene/AGAP003243`,  :doc:`/gene/AGAP003244` (GPRGHP2 - putative growth hormone releasing hormone receptor 2),  :doc:`/gene/AGAP003261`,  :doc:`/gene/AGAP003262` (integrator complex subunit 10),  :doc:`/gene/AGAP003263` (CDC42 small effector protein-like protein).


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

    :doc:`/signal/H12/BFS/chr2/11/index`,"2R:34,420,001-34,540,000",90
    



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
        # function evals   = 23
        # data points      = 199
        # variables        = 3
        chi-square         = 0.025
        reduced chi-square = 0.000
        Akaike info crit   = -1780.870
        Bayesian info crit = -1770.990
    [[Variables]]
        amplitude:   0.07252747 +/- 0.004988 (6.88%) (init= 0.5)
        decay:       0.74018622 +/- 0.084144 (11.37%) (init= 0.5)
        c:           0.02110043 +/- 0.001011 (4.79%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.594 
        C(decay, c)                  = -0.478 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 197
        # variables        = 3
        chi-square         = 0.038
        reduced chi-square = 0.000
        Akaike info crit   = -1677.249
        Bayesian info crit = -1667.399
    [[Variables]]
        amplitude:   0.03040894 +/- 0.003955 (13.01%) (init= 0.5)
        decay:       2.28368146 +/- 0.834649 (36.55%) (init= 0.5)
        c:           0.02554836 +/- 0.003015 (11.80%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.871 
        C(amplitude, c)              = -0.254 
        C(amplitude, decay)          = -0.120 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.055
        reduced chi-square = 0.000
        Akaike info crit   = -1617.825
        Bayesian info crit = -1614.536
    [[Variables]]
        c:   0.02748947 +/- 0.001192 (4.34%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1634.388
        Bayesian info crit = -1631.110
    [[Variables]]
        c:   0.03367984 +/- 0.001101 (3.27%) (init= 0.03)


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
