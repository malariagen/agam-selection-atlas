:orphan:

H12 / Uganda *An. gambiae* / Chromosome 3 / #1
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **28,560,001** and
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
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>




The following 15 genes overlap the focal region: :doc:`../../../../../gene/AGAP009185`,  :doc:`../../../../../gene/AGAP009187` (Indanol dehydrogenase),  :doc:`../../../../../gene/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`../../../../../gene/AGAP009189`,  :doc:`../../../../../gene/AGAP009190` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`../../../../../gene/AGAP009191` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`../../../../../gene/AGAP009192` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`../../../../../gene/AGAP009193` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`../../../../../gene/AGAP009194` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`../../../../../gene/AGAP009195` (GSTE1 - glutathione S-transferase epsilon class 1),  :doc:`../../../../../gene/AGAP009196` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`../../../../../gene/AGAP009197` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`../../../../../gene/AGAP009198`,  :doc:`../../../../../gene/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`../../../../../gene/AGAP009200` (collagen type IV alpha).




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009201` (collagen type IV alpha),  :doc:`../../../../../gene/AGAP009202` (selenoprotein T),  :doc:`../../../../../gene/AGAP028058`,  :doc:`../../../../../gene/AGAP009203` (SPRY domain-containing SOCS box protein 3).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/CMS/3/1/index`,"3R:28,540,001-28,640,000",1109
    :doc:`../../../../../signal/H12/BFS/3/1/index`,"3R:28,480,001-28,620,000",818
    :doc:`../../../../../signal/H12/GNS/3/1/index`,"3R:28,480,001-28,600,000",755
    :doc:`../../../../../signal/H12/BFM/3/1/index`,"3R:28,520,001-28,620,000",676
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/1/peak_fit.png"/>
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
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1497.293
        Bayesian info crit = -1488.241
    [[Variables]]
        amplitude:   0.26111748 +/- 0.005388 (2.06%) (init= 0.5)
        decay:       0.17530508 +/- 0.005890 (3.36%) (init= 0.5)
        c:           0.01840311 +/- 0.000603 (3.27%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.592 
        C(decay, c)                  = -0.249 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 128
        # variables        = 3
        chi-square         = 0.016
        reduced chi-square = 0.000
        Akaike info crit   = -1144.356
        Bayesian info crit = -1135.800
    [[Variables]]
        amplitude:   0.34255741 +/- 0.011732 (3.43%) (init= 0.5)
        decay:       0.21937595 +/- 0.010149 (4.63%) (init= 0.5)
        c:           0.02258691 +/- 0.001098 (4.86%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.743 
        C(decay, c)                  = -0.305 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.117
        reduced chi-square = 0.001
        Akaike info crit   = -1071.074
        Bayesian info crit = -1068.063
    [[Variables]]
        c:   0.02518364 +/- 0.002290 (9.10%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 127
        # variables        = 1
        chi-square         = 0.196
        reduced chi-square = 0.002
        Akaike info crit   = -820.499
        Bayesian info crit = -817.655
    [[Variables]]
        c:   0.03397464 +/- 0.003495 (10.29%) (init= 0.03)


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
