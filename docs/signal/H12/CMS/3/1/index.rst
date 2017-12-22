:orphan:

H12 / Cameroon *An. gambiae* / Chromosome 3 / #1
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **28,540,001** and
**28,640,000**.
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




The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009184`,  :doc:`../../../../../gene/AGAP009201` (collagen type IV alpha),  :doc:`../../../../../gene/AGAP009202` (selenoprotein T),  :doc:`../../../../../gene/AGAP028058`,  :doc:`../../../../../gene/AGAP009203` (SPRY domain-containing SOCS box protein 3),  :doc:`../../../../../gene/AGAP009204` (eIF3h - Eukaryotic translation initiation factor 3 subunit H),  :doc:`../../../../../gene/AGAP009205` (ankyrin repeat domain 39),  :doc:`../../../../../gene/AGAP009206`.


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/BFS/3/1/index`,"3R:28,480,001-28,620,000",818
    :doc:`../../../../../signal/H12/GNS/3/1/index`,"3R:28,480,001-28,600,000",755
    :doc:`../../../../../signal/H12/UGS/3/1/index`,"3R:28,560,001-28,620,000",750
    :doc:`../../../../../signal/H12/BFM/3/1/index`,"3R:28,520,001-28,620,000",676
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 19
        # data points      = 151
        # variables        = 3
        chi-square         = 0.011
        reduced chi-square = 0.000
        Akaike info crit   = -1433.243
        Bayesian info crit = -1424.191
    [[Variables]]
        amplitude:   0.46391822 +/- 0.004632 (1.00%) (init= 0.5)
        decay:       0.46764246 +/- 0.007619 (1.63%) (init= 0.5)
        c:           0.01531472 +/- 0.000843 (5.50%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.599 
        C(decay, c)                  = -0.428 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 19
        # data points      = 128
        # variables        = 3
        chi-square         = 0.027
        reduced chi-square = 0.000
        Akaike info crit   = -1077.244
        Bayesian info crit = -1068.687
    [[Variables]]
        amplitude:   0.51297639 +/- 0.011116 (2.17%) (init= 0.5)
        decay:       0.35470785 +/- 0.011089 (3.13%) (init= 0.5)
        c:           0.01430139 +/- 0.001509 (10.56%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.698 
        C(decay, c)                  = -0.375 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.980
        reduced chi-square = 0.007
        Akaike info crit   = -752.657
        Bayesian info crit = -749.646
    [[Variables]]
        c:   0.04991149 +/- 0.006621 (13.27%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 127
        # variables        = 1
        chi-square         = 0.756
        reduced chi-square = 0.006
        Akaike info crit   = -648.816
        Bayesian info crit = -645.972
    [[Variables]]
        c:   0.04442964 +/- 0.006871 (15.47%) (init= 0.03)


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
