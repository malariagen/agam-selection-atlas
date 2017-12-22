:orphan:




H12 / Guinea Bissau / Chromosome 2 / #5
=======================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **11,080,001** and
**11,160,000**.
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
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----



Gene :doc:`../../../../../gene/AGAP001826` (Lp - lipophorin) overlaps the focal region.




Gene :doc:`../../../../../gene/AGAP001824` is within 50 kbp of the focal region.



Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/5/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 67
        # data points      = 134
        # variables        = 3
        chi-square         = 0.331
        reduced chi-square = 0.003
        Akaike info crit   = -798.645
        Bayesian info crit = -789.952
    [[Variables]]
        amplitude:   0.21307692 +/- 0.027688 (12.99%) (init= 0.5)
        decay:       0.44514281 +/- 0.094004 (21.12%) (init= 0.5)
        c:           0.05999999 +/- 0.005207 (8.68%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.594 
        C(decay, c)                  = -0.412 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 42
        # data points      = 150
        # variables        = 3
        chi-square         = 0.266
        reduced chi-square = 0.002
        Akaike info crit   = -944.248
        Bayesian info crit = -935.216
    [[Variables]]
        amplitude:   0.30774365 +/- 0.032260 (10.48%) (init= 0.5)
        decay:       0.35236581 +/- 0.052943 (15.03%) (init= 0.5)
        c:           0.05999999 +/- 0.011020 (18.37%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.706 
        C(decay, c)                  =  0.365 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 133
        # variables        = 1
        chi-square         = 0.415
        reduced chi-square = 0.003
        Akaike info crit   = -765.541
        Bayesian info crit = -762.650
    [[Variables]]
        c:   0.09145652 +/- 0.004859 (5.31%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.411
        reduced chi-square = 0.003
        Akaike info crit   = -876.144
        Bayesian info crit = -873.140
    [[Variables]]
        c:   0.08426371 +/- 0.004316 (5.12%) (init= 0.03)


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


