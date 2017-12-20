:orphan:

Uganda *An. gambiae* | H12 | Chromosome 3 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/UGS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R between position 28,560,001 and
28,620,000**.




The following 15 genes overlap the focal region: :doc:`/gene/AGAP009185`,  :doc:`/gene/AGAP009187` (Indanol dehydrogenase),  :doc:`/gene/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`/gene/AGAP009189`,  :doc:`/gene/AGAP009190` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`/gene/AGAP009191` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`/gene/AGAP009192` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`/gene/AGAP009193` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`/gene/AGAP009194` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`/gene/AGAP009195` (GSTE1 - glutathione S-transferase epsilon class 1),  :doc:`/gene/AGAP009196` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`/gene/AGAP009197` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`/gene/AGAP009198`,  :doc:`/gene/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`/gene/AGAP009200` (collagen type IV alpha).




The following 4 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP009201` (collagen type IV alpha),  :doc:`/gene/AGAP009202` (selenoprotein T),  :doc:`/gene/AGAP028058`,  :doc:`/gene/AGAP009203` (SPRY domain-containing SOCS box protein 3).


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

    :doc:`/signal/H12/CMS/chr3/1/index`,":28540001-28640000",1425
    :doc:`/signal/H12/BFS/chr3/1/index`,":28480001-28620000",1057
    :doc:`/signal/H12/GNS/chr3/1/index`,":28480001-28600000",968
    :doc:`/signal/H12/BFM/chr3/1/index`,":28520001-28620000",730
    



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
        # data points      = 197
        # variables        = 3
        chi-square         = 0.010
        reduced chi-square = 0.000
        Akaike info crit   = -1935.792
        Bayesian info crit = -1925.943
    [[Variables]]
        amplitude:   0.29439897 +/- 0.005428 (1.84%) (init= 0.5)
        decay:       0.19848762 +/- 0.005861 (2.95%) (init= 0.5)
        c:           0.01688617 +/- 0.000548 (3.25%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.608 
        C(decay, c)                  = -0.231 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 166
        # variables        = 3
        chi-square         = 0.023
        reduced chi-square = 0.000
        Akaike info crit   = -1466.922
        Bayesian info crit = -1457.586
    [[Variables]]
        amplitude:   0.31750086 +/- 0.013576 (4.28%) (init= 0.5)
        decay:       0.19309746 +/- 0.010822 (5.60%) (init= 0.5)
        c:           0.02322353 +/- 0.000986 (4.25%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.760 
        C(decay, c)                  = -0.248 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 0.190
        reduced chi-square = 0.001
        Akaike info crit   = -1358.301
        Bayesian info crit = -1355.023
    [[Variables]]
        c:   0.02374043 +/- 0.002227 (9.38%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 165
        # variables        = 1
        chi-square         = 0.142
        reduced chi-square = 0.001
        Akaike info crit   = -1162.825
        Bayesian info crit = -1159.719
    [[Variables]]
        c:   0.02997512 +/- 0.002288 (7.64%) (init= 0.03)


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
