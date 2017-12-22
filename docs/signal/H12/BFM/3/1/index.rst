:orphan:




H12 / Burkina Faso *An. coluzzii* / Chromosome 3 / #1
=====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **28,520,001** and
**28,620,000**.
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
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 15 genes overlap the focal region: :doc:`../../../../../gene/AGAP009185`,  :doc:`../../../../../gene/AGAP009187`:sup:`1` (Indanol dehydrogenase),  :doc:`../../../../../gene/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`../../../../../gene/AGAP009189`,  :doc:`../../../../../gene/AGAP009190`:sup:`1` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`../../../../../gene/AGAP009191`:sup:`1` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`../../../../../gene/AGAP009192`:sup:`1` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`../../../../../gene/AGAP009193`:sup:`1` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`../../../../../gene/AGAP009194`:sup:`1` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`../../../../../gene/AGAP009195`:sup:`1` (GSTE1 - glutathione S-transferase epsilon class 1),  :doc:`../../../../../gene/AGAP009196`:sup:`1` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`../../../../../gene/AGAP009197`:sup:`1` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`../../../../../gene/AGAP009198`,  :doc:`../../../../../gene/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`../../../../../gene/AGAP009200` (collagen type IV alpha).




The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009184`,  :doc:`../../../../../gene/AGAP009201` (collagen type IV alpha),  :doc:`../../../../../gene/AGAP009202` (selenoprotein T),  :doc:`../../../../../gene/AGAP028058`,  :doc:`../../../../../gene/AGAP009203` (SPRY domain-containing SOCS box protein 3).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have an focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/CMS/3/1/index`, "3R:28,540,001-28,640,000", 1109 (680 | 428)
    :doc:`../../../../../signal/H12/BFS/3/1/index`, "3R:28,480,001-28,620,000", 818 (500 | 318)
    :doc:`../../../../../signal/H12/GNS/3/1/index`, "3R:28,480,001-28,600,000", 755 (461 | 294)
    :doc:`../../../../../signal/H12/UGS/3/1/index`, "3R:28,560,001-28,620,000", 750 (426 | 323)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 151
        # variables        = 3
        chi-square         = 0.024
        reduced chi-square = 0.000
        Akaike info crit   = -1317.399
        Bayesian info crit = -1308.347
    [[Variables]]
        amplitude:   0.25718106 +/- 0.006981 (2.71%) (init= 0.5)
        decay:       0.43876681 +/- 0.019332 (4.41%) (init= 0.5)
        c:           0.01646784 +/- 0.001219 (7.41%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.602 
        C(decay, c)                  = -0.412 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 128
        # variables        = 3
        chi-square         = 0.026
        reduced chi-square = 0.000
        Akaike info crit   = -1079.781
        Bayesian info crit = -1071.225
    [[Variables]]
        amplitude:   0.30925549 +/- 0.012424 (4.02%) (init= 0.5)
        decay:       0.29276550 +/- 0.016555 (5.65%) (init= 0.5)
        c:           0.01743621 +/- 0.001459 (8.37%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.716 
        C(decay, c)                  = -0.350 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.312
        reduced chi-square = 0.002
        Akaike info crit   = -924.250
        Bayesian info crit = -921.240
    [[Variables]]
        c:   0.03452005 +/- 0.003736 (10.83%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 127
        # variables        = 1
        chi-square         = 0.237
        reduced chi-square = 0.002
        Akaike info crit   = -796.236
        Bayesian info crit = -793.392
    [[Variables]]
        c:   0.03199139 +/- 0.003845 (12.02%) (init= 0.03)


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


