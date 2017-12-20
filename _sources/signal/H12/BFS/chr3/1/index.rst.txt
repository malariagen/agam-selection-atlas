:orphan:

Burkina Faso *An. gambiae* | H12 | Chromosome 3 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **28,480,001** and
**28,620,000**.




The following 16 genes overlap the focal region: :doc:`/gene/AGAP009184`,  :doc:`/gene/AGAP009185`,  :doc:`/gene/AGAP009187` (Indanol dehydrogenase),  :doc:`/gene/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`/gene/AGAP009189`,  :doc:`/gene/AGAP009190` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`/gene/AGAP009191` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`/gene/AGAP009192` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`/gene/AGAP009193` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`/gene/AGAP009194` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`/gene/AGAP009195` (GSTE1 - glutathione S-transferase epsilon class 1),  :doc:`/gene/AGAP009196` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`/gene/AGAP009197` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`/gene/AGAP009198`,  :doc:`/gene/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`/gene/AGAP009200` (collagen type IV alpha).




The following 4 genes are within 50 kbp of the focal
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

    :doc:`/signal/H12/CMS/chr3/1/index`,"3R:28,540,001-28,640,000",1425
    :doc:`/signal/H12/GNS/chr3/1/index`,"3R:28,480,001-28,600,000",968
    :doc:`/signal/H12/UGS/chr3/1/index`,"3R:28,560,001-28,620,000",881
    :doc:`/signal/H12/BFM/chr3/1/index`,"3R:28,520,001-28,620,000",730
    



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
        # data points      = 197
        # variables        = 3
        chi-square         = 0.023
        reduced chi-square = 0.000
        Akaike info crit   = -1775.523
        Bayesian info crit = -1765.673
    [[Variables]]
        amplitude:   0.37241717 +/- 0.006179 (1.66%) (init= 0.5)
        decay:       0.41811606 +/- 0.010952 (2.62%) (init= 0.5)
        c:           0.01678305 +/- 0.000879 (5.24%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.623 
        C(decay, c)                  = -0.345 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 19
        # data points      = 169
        # variables        = 3
        chi-square         = 0.066
        reduced chi-square = 0.000
        Akaike info crit   = -1319.407
        Bayesian info crit = -1310.017
    [[Variables]]
        amplitude:   0.42844945 +/- 0.013466 (3.14%) (init= 0.5)
        decay:       0.42963945 +/- 0.019489 (4.54%) (init= 0.5)
        c:           0.02596609 +/- 0.001752 (6.75%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.696 
        C(decay, c)                  = -0.347 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 0.630
        reduced chi-square = 0.003
        Akaike info crit   = -1122.960
        Bayesian info crit = -1119.682
    [[Variables]]
        c:   0.03585659 +/- 0.004061 (11.33%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 168
        # variables        = 1
        chi-square         = 0.717
        reduced chi-square = 0.004
        Akaike info crit   = -914.625
        Bayesian info crit = -911.501
    [[Variables]]
        c:   0.04949294 +/- 0.005056 (10.22%) (init= 0.03)


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
