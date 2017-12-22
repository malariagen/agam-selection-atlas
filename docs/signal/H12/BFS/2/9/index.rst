:orphan:

H12 / Burkina Faso *An. gambiae* / Chromosome 2 / #9
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **27,480,001** and
**27,520,000**.
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


No genes overlap the focal region.





Gene :doc:`../../../../../gene/AGAP002793` (slit homolog 1 protein precursor) is within 50 kbp of the focal region.



Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/9/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/9/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/2/9/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 151
        # variables        = 3
        chi-square         = 0.005
        reduced chi-square = 0.000
        Akaike info crit   = -1550.380
        Bayesian info crit = -1541.329
    [[Variables]]
        amplitude:   0.02652676 +/- 0.002497 (9.42%) (init= 0.5)
        decay:       0.79168154 +/- 0.134035 (16.93%) (init= 0.5)
        c:           0.01064923 +/- 0.000686 (6.44%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.591 
        C(amplitude, decay)          = -0.538 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 150
        # variables        = 3
        chi-square         = 0.028
        reduced chi-square = 0.000
        Akaike info crit   = -1283.444
        Bayesian info crit = -1274.412
    [[Variables]]
        amplitude:   0.06919180 +/- 0.018974 (27.42%) (init= 0.5)
        decay:       0.15000007 +/- 0.051954 (34.64%) (init= 0.5)
        c:           0.02848198 +/- 0.001182 (4.15%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.782 
        C(decay, c)                  = -0.230 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.009
        reduced chi-square = 0.000
        Akaike info crit   = -1458.803
        Bayesian info crit = -1455.792
    [[Variables]]
        c:   0.01394706 +/- 0.000629 (4.51%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.031
        reduced chi-square = 0.000
        Akaike info crit   = -1261.013
        Bayesian info crit = -1258.009
    [[Variables]]
        c:   0.02961675 +/- 0.001186 (4.01%) (init= 0.03)


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
