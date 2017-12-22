:orphan:




H12 / Guinea Bissau / Chromosome 2 / #4
=======================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **7,880,001** and
**7,920,000**.
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
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----



Gene :doc:`../../../../../gene/AGAP001674` (sidestep) overlaps the focal region.





The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013191`,  :doc:`../../../../../gene/AGAP001675`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 151
        # variables        = 3
        chi-square         = 0.164
        reduced chi-square = 0.001
        Akaike info crit   = -1024.537
        Bayesian info crit = -1015.485
    [[Variables]]
        amplitude:   0.11556255 +/- 0.011473 (9.93%) (init= 0.5)
        decay:       1.28424294 +/- 0.290197 (22.60%) (init= 0.5)
        c:           0.04639043 +/- 0.005644 (12.17%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.777 
        C(amplitude, decay)          = -0.356 
        C(amplitude, c)              = -0.103 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 108
        # data points      = 133
        # variables        = 3
        chi-square         = 0.368
        reduced chi-square = 0.003
        Akaike info crit   = -777.391
        Bayesian info crit = -768.720
    [[Variables]]
        amplitude:   0.70062682 +/- 0.073522 (10.49%) (init= 0.5)
        decay:       0.15000002 +/- 0.008914 (5.94%) (init= 0.5)
        c:           0.05999999 +/- 0.023579 (39.30%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.780 
        C(decay, c)                  =  0.245 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.256
        reduced chi-square = 0.002
        Akaike info crit   = -953.794
        Bayesian info crit = -950.784
    [[Variables]]
        c:   0.06985034 +/- 0.003386 (4.85%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 132
        # variables        = 1
        chi-square         = 0.640
        reduced chi-square = 0.005
        Akaike info crit   = -701.446
        Bayesian info crit = -698.563
    [[Variables]]
        c:   0.09384308 +/- 0.006083 (6.48%) (init= 0.03)


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


