:orphan:

H12 / Cameroon *An. gambiae* / Chromosome 3 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3L** between positions **26,880,001** and
**26,940,000**.
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




The following 7 genes overlap the focal region: :doc:`../../../../../gene/AGAP011532` (septin),  :doc:`../../../../../gene/AGAP011533` (tetratricopeptide repeat protein 15),  :doc:`../../../../../gene/AGAP011534`,  :doc:`../../../../../gene/AGAP011535` (transcription elongation factor B, polypeptide 1),  :doc:`../../../../../gene/AGAP011536` (Mini-chromosome maintenance complex-binding protein),  :doc:`../../../../../gene/AGAP011537` (Argonaute 3),  :doc:`../../../../../gene/AGAP028430`.




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP011530`,  :doc:`../../../../../gene/AGAP011531` (Selenium-binding protein 2),  :doc:`../../../../../gene/AGAP011538`,  :doc:`../../../../../gene/AGAP011539` (dynein intermediate chain 2, axonemal),  :doc:`../../../../../gene/AGAP011540` (dynein intermediate chain 2, axonemal),  :doc:`../../../../../gene/AGAP011541` (Ecto-NOX disulfide-thiol exchanger 1),  :doc:`../../../../../gene/AGAP011542`.


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/BFS/3/2/index`,"3L:26,880,001-26,920,000",252
    :doc:`../../../../../signal/H12/GNS/3/3/index`,"3L:26,860,001-26,900,000",171
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 149
        # variables        = 3
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1726.081
        Bayesian info crit = -1717.069
    [[Variables]]
        amplitude:   0.06372860 +/- 0.002430 (3.81%) (init= 0.5)
        decay:       0.15402663 +/- 0.009687 (6.29%) (init= 0.5)
        c:           0.00606772 +/- 0.000261 (4.31%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.583 
        C(decay, c)                  = -0.234 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 150
        # variables        = 3
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1574.960
        Bayesian info crit = -1565.928
    [[Variables]]
        amplitude:   0.03578199 +/- 0.005358 (14.97%) (init= 0.5)
        decay:       0.22111070 +/- 0.044439 (20.10%) (init= 0.5)
        c:           0.00500729 +/- 0.000459 (9.18%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.747 
        C(decay, c)                  = -0.283 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.008
        reduced chi-square = 0.000
        Akaike info crit   = -1461.012
        Bayesian info crit = -1458.014
    [[Variables]]
        c:   0.00755094 +/- 0.000589 (7.79%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.005
        reduced chi-square = 0.000
        Akaike info crit   = -1545.222
        Bayesian info crit = -1542.218
    [[Variables]]
        c:   0.00590501 +/- 0.000457 (7.74%) (init= 0.03)


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
