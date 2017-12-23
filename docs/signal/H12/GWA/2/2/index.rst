:orphan:




H12 / Guinea Bissau / Chromosome 2 / #2
=======================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **31,920,001** and
**31,960,000**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP006439` (fringe),  :doc:`../../../../../gene/AGAP006440` (IR136 - ionotropic receptor IR136).




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006436` (Med13 - mediator of RNA polymerase II transcription subunit 13),  :doc:`../../../../../gene/AGAP028457`,  :doc:`../../../../../gene/AGAP006437`,  :doc:`../../../../../gene/AGAP006438` (ribosomal biogenesis protein LAS1).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 144
        # variables        = 3
        chi-square         = 0.050
        reduced chi-square = 0.000
        Akaike info crit   = -1140.069
        Bayesian info crit = -1131.159
    [[Variables]]
        amplitude:   0.13379179 +/- 0.013622 (10.18%) (init= 0.5)
        decay:       0.21866358 +/- 0.035897 (16.42%) (init= 0.5)
        c:           0.04360961 +/- 0.001710 (3.92%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.602 
        C(decay, c)                  = -0.287 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 150
        # variables        = 3
        chi-square         = 0.044
        reduced chi-square = 0.000
        Akaike info crit   = -1213.158
        Bayesian info crit = -1204.126
    [[Variables]]
        amplitude:   0.35749107 +/- 0.023182 (6.48%) (init= 0.5)
        decay:       0.15647095 +/- 0.012930 (8.26%) (init= 0.5)
        c:           0.04577839 +/- 0.001497 (3.27%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.778 
        C(decay, c)                  = -0.235 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 143
        # variables        = 1
        chi-square         = 0.089
        reduced chi-square = 0.001
        Akaike info crit   = -1053.254
        Bayesian info crit = -1050.291
    [[Variables]]
        c:   0.04831156 +/- 0.002096 (4.34%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.168
        reduced chi-square = 0.001
        Akaike info crit   = -1009.194
        Bayesian info crit = -1006.190
    [[Variables]]
        c:   0.05235597 +/- 0.002761 (5.28%) (init= 0.03)


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


