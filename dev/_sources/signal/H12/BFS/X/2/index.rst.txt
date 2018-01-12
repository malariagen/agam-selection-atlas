:orphan:




H12 / Burkina Faso *An. gambiae* / Chromosome X / #2
====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **9,180,000** and
**9,240,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

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



Gene :doc:`../../../../../gene/AGAP000519` (diacylglycerol kinase (ATP dependent)) overlaps the focal region.




No genes are within 50 kbp of the focal region.




Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 64
        # data points      = 299
        # variables        = 4
        chi-square         = 0.072
        reduced chi-square = 0.000
        Akaike info crit   = -2482.241
        Bayesian info crit = -2467.439
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.22175740 +/- 0.007461 (3.36%) (init= 0.5)
        sigma:       0.15000000 +/- 9.09e-07 (0.00%) (init= 0.5)
        skew:        0.00975591 +/- 0.045589 (467.30%) (init= 0)
        baseline:    0.02186443 +/- 0.000937 (4.28%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.555 
        C(sigma, baseline)           = -0.153 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 8
        # data points      = 298
        # variables        = 1
        chi-square         = 0.317
        reduced chi-square = 0.001
        Akaike info crit   = -2037.924
        Bayesian info crit = -2034.227
    [[Variables]]
        c:   0.02796658 +/- 0.001893 (6.77%) (init= 0.03)



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


