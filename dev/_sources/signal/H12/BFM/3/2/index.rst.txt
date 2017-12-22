:orphan:

H12 / Burkina Faso *An. coluzzii* / Chromosome 3 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3L** between positions **11,200,001** and
**11,240,000**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP010815` (TEP1 - thioester-containing protein 1),  :doc:`../../../../../gene/AGAP010816` (TEP3 - thioester-containing protein 3).




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010813` (TEP18 - thioester-containing protein 18),  :doc:`../../../../../gene/AGAP010814` (TEP6 - thioester-containing protein 6),  :doc:`../../../../../gene/AGAP010817`,  :doc:`../../../../../gene/AGAP010818` (TEP11 - thioester-containing protein 11).


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 44
        # data points      = 147
        # variables        = 3
        chi-square         = 0.124
        reduced chi-square = 0.001
        Akaike info crit   = -1034.049
        Bayesian info crit = -1025.078
    [[Variables]]
        amplitude:   0.80070447 +/- 0.023821 (2.98%) (init= 0.5)
        decay:       0.15000000 +/- 0.007370 (4.91%) (init= 0.5)
        c:           0.02783632 +/- 0.002558 (9.19%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.581 
        C(decay, c)                  = -0.233 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 147
        # variables        = 3
        chi-square         = 1.380
        reduced chi-square = 0.010
        Akaike info crit   = -680.288
        Bayesian info crit = -671.317
    [[Variables]]
        amplitude:   0.34675102 +/- 0.042677 (12.31%) (init= 0.5)
        decay:       0.92197787 +/- 0.209281 (22.70%) (init= 0.5)
        c:           0.00792414 +/- 0.012780 (161.29%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.657 
        C(amplitude, decay)          = -0.543 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 146
        # variables        = 1
        chi-square         = 1.057
        reduced chi-square = 0.007
        Akaike info crit   = -717.511
        Bayesian info crit = -714.527
    [[Variables]]
        c:   0.04609656 +/- 0.007066 (15.33%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 146
        # variables        = 1
        chi-square         = 1.785
        reduced chi-square = 0.012
        Akaike info crit   = -641.007
        Bayesian info crit = -638.023
    [[Variables]]
        c:   0.05418022 +/- 0.009182 (16.95%) (init= 0.03)


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
