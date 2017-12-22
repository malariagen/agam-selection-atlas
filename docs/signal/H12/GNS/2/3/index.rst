:orphan:

H12 / Guinea *An. gambiae* / Chromosome 2 / #3
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **28,760,001** and
**28,920,000**.
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




The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP006263` (ARR2 - arrestin Arr2-like),  :doc:`../../../../../gene/AGAP006264` (Peroxisomal targeting signal 2 receptor),  :doc:`../../../../../gene/AGAP006265`,  :doc:`../../../../../gene/AGAP006266` (HIV Tat-specific factor 1),  :doc:`../../../../../gene/AGAP006267` (CTL6 - C-type lectin (CTL)),  :doc:`../../../../../gene/AGAP006268`.




The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006260` (Z band alternatively spliced PDZ-motif protein 66),  :doc:`../../../../../gene/AGAP006261` (CPR135 - cuticular protein RR-2 family 135),  :doc:`../../../../../gene/AGAP006262`,  :doc:`../../../../../gene/AGAP006269` (phosphatidylinositol glycan, class O),  :doc:`../../../../../gene/AGAP006270` (fyn-related kinase),  :doc:`../../../../../gene/AGAP006271`.


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 113
        # data points      = 151
        # variables        = 3
        chi-square         = 0.454
        reduced chi-square = 0.003
        Akaike info crit   = -870.751
        Bayesian info crit = -861.699
    [[Variables]]
        amplitude:   0.22994979 +/- 0.017427 (7.58%) (init= 0.5)
        decay:       1.93212802 +/- 0.442237 (22.89%) (init= 0.5)
        c:           0.05999999 +/- 0.000365 (0.61%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.897 
        C(amplitude, c)              =  0.416 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 143
        # variables        = 3
        chi-square         = 0.026
        reduced chi-square = 0.000
        Akaike info crit   = -1227.100
        Bayesian info crit = -1218.212
    [[Variables]]
        amplitude:   0.27867877 +/- 0.012445 (4.47%) (init= 0.5)
        decay:       0.26192087 +/- 0.016120 (6.15%) (init= 0.5)
        c:           0.03534786 +/- 0.001254 (3.55%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.730 
        C(decay, c)                  = -0.317 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.867
        reduced chi-square = 0.006
        Akaike info crit   = -770.975
        Bayesian info crit = -767.964
    [[Variables]]
        c:   0.13332639 +/- 0.006228 (4.67%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 142
        # variables        = 1
        chi-square         = 0.184
        reduced chi-square = 0.001
        Akaike info crit   = -942.140
        Bayesian info crit = -939.184
    [[Variables]]
        c:   0.04576732 +/- 0.003031 (6.62%) (init= 0.03)


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
