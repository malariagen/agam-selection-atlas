:orphan:




IHS/BFS/3/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **20,800,000** and
**20,920,000**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area shows the focus of the
    selection signal. The shaded blue area shows the genomic region in linkage with the
    selection event. Use the mouse wheel or the controls at the top right of the plot to zoom
    in, and hover over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP008918` (STIP1 homology and U-box containing protein 1),  :doc:`../../../../../gene/AGAP028004`,  :doc:`../../../../../gene/AGAP008919`.




The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008914`,  :doc:`../../../../../gene/AGAP008915` (gamma-glutamyltranspeptidase),  :doc:`../../../../../gene/AGAP028196`,  :doc:`../../../../../gene/AGAP008916` (RpL7 - 60S ribosomal protein L7),  :doc:`../../../../../gene/AGAP008917` (DNA topoisomerase II),  :doc:`../../../../../gene/AGAP028087`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 532
        # variables        = 4
        chi-square         = 76.657
        reduced chi-square = 0.145
        Akaike info crit   = -1022.645
        Bayesian info crit = -1005.538
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.69820110 +/- 0.121689 (7.17%) (init= 3)
        sigma:       0.21364417 +/- 0.019491 (9.12%) (init= 0.5)
        skew:        0.53569369 +/- 0.109842 (20.50%) (init= 0)
        baseline:    1.74616214 +/- 0.017192 (0.98%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.512 
        C(sigma, skew)               = -0.340 
        C(sigma, baseline)           = -0.151 
        C(amplitude, baseline)       = -0.106 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 531
        # variables        = 1
        chi-square         = 112.183
        reduced chi-square = 0.212
        Akaike info crit   = -823.508
        Bayesian info crit = -819.233
    [[Variables]]
        c:   1.80629060 +/- 0.019965 (1.11%) (init= 1)



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


