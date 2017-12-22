:orphan:

H12 / Burkina Faso *An. gambiae* / Chromosome 3 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3L** between positions **26,880,001** and
**26,920,000**.
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




The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP011532` (septin),  :doc:`../../../../../gene/AGAP011533` (tetratricopeptide repeat protein 15),  :doc:`../../../../../gene/AGAP011534`,  :doc:`../../../../../gene/AGAP011535` (transcription elongation factor B, polypeptide 1),  :doc:`../../../../../gene/AGAP011536` (Mini-chromosome maintenance complex-binding protein),  :doc:`../../../../../gene/AGAP011537` (Argonaute 3).




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP011530`,  :doc:`../../../../../gene/AGAP011531` (Selenium-binding protein 2),  :doc:`../../../../../gene/AGAP028430`,  :doc:`../../../../../gene/AGAP011538`,  :doc:`../../../../../gene/AGAP011539` (dynein intermediate chain 2, axonemal),  :doc:`../../../../../gene/AGAP011540` (dynein intermediate chain 2, axonemal),  :doc:`../../../../../gene/AGAP011541` (Ecto-NOX disulfide-thiol exchanger 1).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/CMS/3/2/index`,"3L:26,880,001-26,940,000",294
    :doc:`../../../../../signal/H12/GNS/3/3/index`,"3L:26,860,001-26,900,000",171
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 44
        # data points      = 149
        # variables        = 3
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -1627.698
        Bayesian info crit = -1618.687
    [[Variables]]
        amplitude:   0.07138020 +/- 0.003405 (4.77%) (init= 0.5)
        decay:       0.15000000 +/- 0.012084 (8.06%) (init= 0.5)
        c:           0.01015940 +/- 0.000363 (3.57%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.581 
        C(decay, c)                  = -0.231 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 150
        # variables        = 3
        chi-square         = 0.008
        reduced chi-square = 0.000
        Akaike info crit   = -1473.916
        Bayesian info crit = -1464.884
    [[Variables]]
        amplitude:   0.07182790 +/- 0.008340 (11.61%) (init= 0.5)
        decay:       0.19100194 +/- 0.029139 (15.26%) (init= 0.5)
        c:           0.00937114 +/- 0.000636 (6.79%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.759 
        C(decay, c)                  = -0.261 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.010
        reduced chi-square = 0.000
        Akaike info crit   = -1416.847
        Bayesian info crit = -1413.850
    [[Variables]]
        c:   0.01177360 +/- 0.000683 (5.80%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.010
        reduced chi-square = 0.000
        Akaike info crit   = -1432.369
        Bayesian info crit = -1429.365
    [[Variables]]
        c:   0.01085732 +/- 0.000668 (6.15%) (init= 0.03)


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
