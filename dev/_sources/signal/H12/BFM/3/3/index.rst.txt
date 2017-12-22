:orphan:




H12 / Burkina Faso *An. coluzzii* / Chromosome 3 / #3
=====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **52,980,001** and
**53,020,000**.
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




The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP010304`,  :doc:`../../../../../gene/AGAP010305` (WD repeat and SOF domain-containing protein 1),  :doc:`../../../../../gene/AGAP010306`.



Gene :doc:`../../../../../gene/AGAP010303` (autophagy-related protein 7) is within 50 kbp of the focal region.



Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 176
        # variables        = 3
        chi-square         = 0.090
        reduced chi-square = 0.001
        Akaike info crit   = -1327.403
        Bayesian info crit = -1317.891
    [[Variables]]
        amplitude:   0.14064486 +/- 0.010168 (7.23%) (init= 0.5)
        decay:       0.20298812 +/- 0.025612 (12.62%) (init= 0.5)
        c:           0.03699927 +/- 0.001990 (5.38%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.622 
        C(decay, c)                  = -0.319 
        C(amplitude, c)              = -0.105 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 209
        # variables        = 3
        chi-square         = 0.166
        reduced chi-square = 0.001
        Akaike info crit   = -1486.300
        Bayesian info crit = -1476.273
    [[Variables]]
        amplitude:   0.03386475 +/- 0.006865 (20.27%) (init= 0.5)
        decay:       1.99999843 +/- 1.402688 (70.13%) (init= 0.5)
        c:           0.05091042 +/- 0.007581 (14.89%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.896 
        C(amplitude, c)              = -0.627 
        C(amplitude, decay)          =  0.317 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 175
        # variables        = 1
        chi-square         = 0.233
        reduced chi-square = 0.001
        Akaike info crit   = -1156.462
        Bayesian info crit = -1153.297
    [[Variables]]
        c:   0.04984307 +/- 0.002768 (5.55%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 208
        # variables        = 1
        chi-square         = 0.180
        reduced chi-square = 0.001
        Akaike info crit   = -1465.179
        Bayesian info crit = -1461.841
    [[Variables]]
        c:   0.06475994 +/- 0.002043 (3.16%) (init= 0.03)


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


