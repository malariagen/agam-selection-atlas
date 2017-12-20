:orphan:

Burkina Faso *An. coluzzii* | H12 | Chromosome 3 | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **28,520,001** and
**28,620,000**.




The following 15 genes overlap the focal region: :doc:`/gene/AGAP009185`,  :doc:`/gene/AGAP009187` (Indanol dehydrogenase),  :doc:`/gene/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`/gene/AGAP009189`,  :doc:`/gene/AGAP009190` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`/gene/AGAP009191` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`/gene/AGAP009192` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`/gene/AGAP009193` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`/gene/AGAP009194` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`/gene/AGAP009195` (GSTE1 - glutathione S-transferase epsilon class 1),  :doc:`/gene/AGAP009196` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`/gene/AGAP009197` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`/gene/AGAP009198`,  :doc:`/gene/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`/gene/AGAP009200` (collagen type IV alpha).




The following 5 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP009184`,  :doc:`/gene/AGAP009201` (collagen type IV alpha),  :doc:`/gene/AGAP009202` (selenoprotein T),  :doc:`/gene/AGAP028058`,  :doc:`/gene/AGAP009203` (SPRY domain-containing SOCS box protein 3).


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
    :doc:`/signal/H12/BFS/chr3/1/index`,"3R:28,480,001-28,620,000",1057
    :doc:`/signal/H12/GNS/chr3/1/index`,"3R:28,480,001-28,600,000",968
    :doc:`/signal/H12/UGS/chr3/1/index`,"3R:28,560,001-28,620,000",881
    



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
        chi-square         = 0.037
        reduced chi-square = 0.000
        Akaike info crit   = -1686.548
        Bayesian info crit = -1676.698
    [[Variables]]
        amplitude:   0.25688962 +/- 0.007619 (2.97%) (init= 0.5)
        decay:       0.43490301 +/- 0.020391 (4.69%) (init= 0.5)
        c:           0.01716184 +/- 0.001108 (6.46%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.622 
        C(decay, c)                  = -0.352 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 167
        # variables        = 3
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1361.995
        Bayesian info crit = -1352.641
    [[Variables]]
        amplitude:   0.31010819 +/- 0.014465 (4.66%) (init= 0.5)
        decay:       0.28848770 +/- 0.018583 (6.44%) (init= 0.5)
        c:           0.01825482 +/- 0.001425 (7.81%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.727 
        C(decay, c)                  = -0.300 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 0.334
        reduced chi-square = 0.002
        Akaike info crit   = -1247.686
        Bayesian info crit = -1244.408
    [[Variables]]
        c:   0.03083728 +/- 0.002954 (9.58%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 166
        # variables        = 1
        chi-square         = 0.260
        reduced chi-square = 0.002
        Akaike info crit   = -1070.009
        Bayesian info crit = -1066.897
    [[Variables]]
        c:   0.02923350 +/- 0.003082 (10.55%) (init= 0.03)


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
