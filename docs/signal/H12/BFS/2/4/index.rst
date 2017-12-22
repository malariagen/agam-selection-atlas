:orphan:

H12 / Burkina Faso *An. gambiae* / Chromosome 2 / #4
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **3,400,001** and
**3,480,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>




The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP001350`,  :doc:`../../../../../gene/AGAP001351`,  :doc:`../../../../../gene/AGAP001352`,  :doc:`../../../../../gene/AGAP001353`,  :doc:`../../../../../gene/AGAP001354`,  :doc:`../../../../../gene/AGAP001355`.




The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP001344`,  :doc:`../../../../../gene/AGAP001345` (hexamerin),  :doc:`../../../../../gene/AGAP001346`,  :doc:`../../../../../gene/AGAP001347`,  :doc:`../../../../../gene/AGAP001348`,  :doc:`../../../../../gene/AGAP001349` (chronic lymphocytic leukemia deletion region gene 6 protein-like protein),  :doc:`../../../../../gene/AGAP001356` (ACE1 - Acetylcholinesterase),  :doc:`../../../../../gene/AGAP001357` (beta-catenin-like protein 1),  :doc:`../../../../../gene/AGAP001358`.


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/GNS/2/5/index`,"2R:3,400,001-3,460,000",179
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 148
        # variables        = 3
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -1590.501
        Bayesian info crit = -1581.510
    [[Variables]]
        amplitude:   0.05691908 +/- 0.002520 (4.43%) (init= 0.5)
        decay:       0.44727876 +/- 0.033086 (7.40%) (init= 0.5)
        c:           0.01265460 +/- 0.000449 (3.55%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.579 
        C(decay, c)                  = -0.422 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 83
        # data points      = 150
        # variables        = 3
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1571.773
        Bayesian info crit = -1562.741
    [[Variables]]
        amplitude:   0.03350765 +/- 0.002187 (6.53%) (init= 0.5)
        decay:       1.00065551 +/- 0.124233 (12.42%) (init= 0.5)
        c:           0.01081279 +/- 0.000719 (6.66%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.684 
        C(amplitude, decay)          = -0.531 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.015
        reduced chi-square = 0.000
        Akaike info crit   = -1346.308
        Bayesian info crit = -1343.317
    [[Variables]]
        c:   0.01642202 +/- 0.000844 (5.14%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.012
        reduced chi-square = 0.000
        Akaike info crit   = -1402.859
        Bayesian info crit = -1399.855
    [[Variables]]
        c:   0.01605582 +/- 0.000737 (4.59%) (init= 0.03)


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
