:orphan:

H12 / Angola *An. coluzzii* / Chromosome 3 / #1
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **44,420,001** and
**44,460,000**.
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






The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009859`,  :doc:`../../../../../gene/AGAP009860`.


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 52
        # data points      = 289
        # variables        = 3
        chi-square         = 0.133
        reduced chi-square = 0.000
        Akaike info crit   = -2213.912
        Bayesian info crit = -2202.913
    [[Variables]]
        amplitude:   0.08016603 +/- 0.005724 (7.14%) (init= 0.5)
        decay:       2.99999993 +/- 0.746899 (24.90%) (init= 0.5)
        c:           0.02538219 +/- 0.006361 (25.06%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.950 
        C(amplitude, c)              = -0.530 
        C(amplitude, decay)          =  0.317 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 196
        # variables        = 3
        chi-square         = 0.056
        reduced chi-square = 0.000
        Akaike info crit   = -1594.477
        Bayesian info crit = -1584.642
    [[Variables]]
        amplitude:   0.10623956 +/- 0.023471 (22.09%) (init= 0.5)
        decay:       0.15000001 +/- 0.041611 (27.74%) (init= 0.5)
        c:           0.05658731 +/- 0.001263 (2.23%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.785 
        C(decay, c)                  = -0.200 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 288
        # variables        = 1
        chi-square         = 0.226
        reduced chi-square = 0.001
        Akaike info crit   = -2057.542
        Bayesian info crit = -2053.879
    [[Variables]]
        c:   0.04772280 +/- 0.001652 (3.46%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 195
        # variables        = 1
        chi-square         = 0.063
        reduced chi-square = 0.000
        Akaike info crit   = -1566.036
        Bayesian info crit = -1562.763
    [[Variables]]
        c:   0.05789387 +/- 0.001288 (2.23%) (init= 0.03)


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
