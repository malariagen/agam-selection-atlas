:orphan:

H12 / Guinea *An. gambiae* / Chromosome 2 / #5
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **3,400,001** and
**3,460,000**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).

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




The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP001344`,  :doc:`../../../../../gene/AGAP001345` (hexamerin),  :doc:`../../../../../gene/AGAP001346`,  :doc:`../../../../../gene/AGAP001347`,  :doc:`../../../../../gene/AGAP001348`,  :doc:`../../../../../gene/AGAP001349` (chronic lymphocytic leukemia deletion region gene 6 protein-like protein),  :doc:`../../../../../gene/AGAP001356` (ACE1 - Acetylcholinesterase),  :doc:`../../../../../gene/AGAP001357` (beta-catenin-like protein 1).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/BFS/2/4/index`,"2R:3,400,001-3,480,000",413
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/5/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 148
        # variables        = 3
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1469.294
        Bayesian info crit = -1460.303
    [[Variables]]
        amplitude:   0.04488942 +/- 0.003221 (7.18%) (init= 0.5)
        decay:       0.67661741 +/- 0.082846 (12.24%) (init= 0.5)
        c:           0.02319049 +/- 0.000762 (3.29%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.542 
        C(decay, c)                  = -0.540 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 49
        # data points      = 150
        # variables        = 3
        chi-square         = 0.009
        reduced chi-square = 0.000
        Akaike info crit   = -1453.117
        Bayesian info crit = -1444.085
    [[Variables]]
        amplitude:   0.02029685 +/- 0.003112 (15.34%) (init= 0.5)
        decay:       1.08425632 +/- 0.330364 (30.47%) (init= 0.5)
        c:           0.02374280 +/- 0.001138 (4.79%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.716 
        C(amplitude, decay)          = -0.500 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.017
        reduced chi-square = 0.000
        Akaike info crit   = -1326.525
        Bayesian info crit = -1323.535
    [[Variables]]
        c:   0.02778072 +/- 0.000902 (3.25%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.011
        reduced chi-square = 0.000
        Akaike info crit   = -1416.061
        Bayesian info crit = -1413.057
    [[Variables]]
        c:   0.02707610 +/- 0.000705 (2.60%) (init= 0.03)


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
