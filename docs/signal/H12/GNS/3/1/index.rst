:orphan:




H12 / Guinea *An. gambiae* / Chromosome 3 / #1
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **28,480,001** and
**28,600,000**.
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




The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP009184`,  :doc:`../../../../../gene/AGAP009185`,  :doc:`../../../../../gene/AGAP009187`:sup:`1` (Indanol dehydrogenase),  :doc:`../../../../../gene/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`../../../../../gene/AGAP009189`,  :doc:`../../../../../gene/AGAP009190`:sup:`1` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`../../../../../gene/AGAP009191`:sup:`1` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`../../../../../gene/AGAP009192`:sup:`1` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`../../../../../gene/AGAP009193`:sup:`1` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`../../../../../gene/AGAP009194`:sup:`1` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`../../../../../gene/AGAP009195`:sup:`1` (GSTE1 - glutathione S-transferase epsilon class 1).




The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009196`:sup:`1` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`../../../../../gene/AGAP009197`:sup:`1` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`../../../../../gene/AGAP009198`,  :doc:`../../../../../gene/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`../../../../../gene/AGAP009200` (collagen type IV alpha),  :doc:`../../../../../gene/AGAP009201` (collagen type IV alpha).


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
    :doc:`../../../../../signal/H12/UGS/3/1/index`, "3R:28,560,001-28,620,000", 750 (426 | 323)
    :doc:`../../../../../signal/H12/BFM/3/1/index`, "3R:28,520,001-28,620,000", 676 (393 | 283)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 151
        # variables        = 3
        chi-square         = 0.016
        reduced chi-square = 0.000
        Akaike info crit   = -1378.525
        Bayesian info crit = -1369.473
    [[Variables]]
        amplitude:   0.28332466 +/- 0.005967 (2.11%) (init= 0.5)
        decay:       0.39268236 +/- 0.013330 (3.39%) (init= 0.5)
        c:           0.03069796 +/- 0.000976 (3.18%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.606 
        C(decay, c)                  = -0.387 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 128
        # variables        = 3
        chi-square         = 0.035
        reduced chi-square = 0.000
        Akaike info crit   = -1042.569
        Bayesian info crit = -1034.013
    [[Variables]]
        amplitude:   0.28690892 +/- 0.010571 (3.68%) (init= 0.5)
        decay:       0.48543795 +/- 0.027009 (5.56%) (init= 0.5)
        c:           0.03659054 +/- 0.001821 (4.98%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.666 
        C(decay, c)                  = -0.427 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.327
        reduced chi-square = 0.002
        Akaike info crit   = -917.487
        Bayesian info crit = -914.476
    [[Variables]]
        c:   0.04833853 +/- 0.003822 (7.91%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 127
        # variables        = 1
        chi-square         = 0.345
        reduced chi-square = 0.003
        Akaike info crit   = -748.382
        Bayesian info crit = -745.538
    [[Variables]]
        c:   0.06027186 +/- 0.004642 (7.70%) (init= 0.03)


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


