:orphan:

H12 / Angola *An. coluzzii* / Chromosome 2 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **8,320,001** and
**8,380,000**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP001683` (calcium/calmodulin-dependent serine protein kinase),  :doc:`../../../../../gene/AGAP001684` (Alkaline phosphatase).



No genes are within 50 kbp of the focal region.




Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 201
        # variables        = 3
        chi-square         = 0.024
        reduced chi-square = 0.000
        Akaike info crit   = -1811.098
        Bayesian info crit = -1801.188
    [[Variables]]
        amplitude:   0.12271763 +/- 0.005721 (4.66%) (init= 0.5)
        decay:       0.50434916 +/- 0.037351 (7.41%) (init= 0.5)
        c:           0.02548073 +/- 0.000894 (3.51%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.619 
        C(decay, c)                  = -0.379 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 183
        # variables        = 3
        chi-square         = 0.020
        reduced chi-square = 0.000
        Akaike info crit   = -1667.761
        Bayesian info crit = -1658.133
    [[Variables]]
        amplitude:   0.08589147 +/- 0.005816 (6.77%) (init= 0.5)
        decay:       0.59029047 +/- 0.060171 (10.19%) (init= 0.5)
        c:           0.02682090 +/- 0.000924 (3.44%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.668 
        C(decay, c)                  = -0.417 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.095
        reduced chi-square = 0.000
        Akaike info crit   = -1527.895
        Bayesian info crit = -1524.597
    [[Variables]]
        c:   0.03281250 +/- 0.001547 (4.71%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 182
        # variables        = 1
        chi-square         = 0.057
        reduced chi-square = 0.000
        Akaike info crit   = -1466.435
        Bayesian info crit = -1463.231
    [[Variables]]
        c:   0.03308379 +/- 0.001315 (3.98%) (init= 0.03)


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
