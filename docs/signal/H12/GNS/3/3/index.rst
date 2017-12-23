:orphan:




H12 / Guinea *An. gambiae* / Chromosome 3 / #3
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **26,860,001** and
**26,900,000**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP011530`,  :doc:`../../../../../gene/AGAP011531` (Selenium-binding protein 2),  :doc:`../../../../../gene/AGAP011532` (septin),  :doc:`../../../../../gene/AGAP011533` (tetratricopeptide repeat protein 15),  :doc:`../../../../../gene/AGAP011534`.




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP011535` (transcription elongation factor B, polypeptide 1),  :doc:`../../../../../gene/AGAP011536` (Mini-chromosome maintenance complex-binding protein),  :doc:`../../../../../gene/AGAP011537` (Argonaute 3),  :doc:`../../../../../gene/AGAP028430`,  :doc:`../../../../../gene/AGAP011538`,  :doc:`../../../../../gene/AGAP011539` (dynein intermediate chain 2, axonemal),  :doc:`../../../../../gene/AGAP011540` (dynein intermediate chain 2, axonemal).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/CMS/3/2/index`, "3L:26,880,001-26,940,000", 294 (265 | 29)
    :doc:`../../../../../signal/H12/BFS/3/2/index`, "3L:26,880,001-26,920,000", 252 (210 | 41)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 42
        # data points      = 149
        # variables        = 3
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1550.224
        Bayesian info crit = -1541.212
    [[Variables]]
        amplitude:   0.05152194 +/- 0.004418 (8.58%) (init= 0.5)
        decay:       0.15000016 +/- 0.027017 (18.01%) (init= 0.5)
        c:           0.02298342 +/- 0.000471 (2.05%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.581 
        C(decay, c)                  =  0.231 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 150
        # variables        = 3
        chi-square         = 0.018
        reduced chi-square = 0.000
        Akaike info crit   = -1345.577
        Bayesian info crit = -1336.545
    [[Variables]]
        amplitude:   0.13107556 +/- 0.013084 (9.98%) (init= 0.5)
        decay:       0.18525118 +/- 0.024177 (13.05%) (init= 0.5)
        c:           0.02152857 +/- 0.000974 (4.52%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.762 
        C(decay, c)                  = -0.257 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1472.898
        Bayesian info crit = -1469.901
    [[Variables]]
        c:   0.02406347 +/- 0.000565 (2.35%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.033
        reduced chi-square = 0.000
        Akaike info crit   = -1251.761
        Bayesian info crit = -1248.757
    [[Variables]]
        c:   0.02433147 +/- 0.001223 (5.03%) (init= 0.03)


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
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments.</a></noscript>


