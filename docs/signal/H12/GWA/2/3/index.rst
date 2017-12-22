:orphan:

H12 / Guinea-Bissau / Chromosome 2 / #3
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **11,260,001** and
**11,320,000**.
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
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP005169`,  :doc:`../../../../../gene/AGAP005170`.




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP005165`,  :doc:`../../../../../gene/AGAP005171` (Tctex1 domain-containing protein 4),  :doc:`../../../../../gene/AGAP005172`,  :doc:`../../../../../gene/AGAP005173` (Px serine/threonine kinase).


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 142
        # variables        = 3
        chi-square         = 0.041
        reduced chi-square = 0.000
        Akaike info crit   = -1149.788
        Bayesian info crit = -1140.920
    [[Variables]]
        amplitude:   0.19911473 +/- 0.011957 (6.01%) (init= 0.5)
        decay:       0.24547305 +/- 0.023704 (9.66%) (init= 0.5)
        c:           0.04729228 +/- 0.001593 (3.37%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.604 
        C(decay, c)                  = -0.308 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 148
        # variables        = 3
        chi-square         = 0.088
        reduced chi-square = 0.001
        Akaike info crit   = -1092.727
        Bayesian info crit = -1083.735
    [[Variables]]
        amplitude:   0.15999437 +/- 0.018432 (11.52%) (init= 0.5)
        decay:       0.36123172 +/- 0.059938 (16.59%) (init= 0.5)
        c:           0.05999999 +/- 0.005852 (9.75%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.703 
        C(decay, c)                  =  0.373 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 141
        # variables        = 1
        chi-square         = 0.141
        reduced chi-square = 0.001
        Akaike info crit   = -971.598
        Bayesian info crit = -968.649
    [[Variables]]
        c:   0.05538852 +/- 0.002676 (4.83%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.145
        reduced chi-square = 0.001
        Akaike info crit   = -1015.132
        Bayesian info crit = -1012.141
    [[Variables]]
        c:   0.07105564 +/- 0.002602 (3.66%) (init= 0.03)


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
