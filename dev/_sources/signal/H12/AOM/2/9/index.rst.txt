:orphan:




H12 / Angola *An. coluzzii* / Chromosome 2 / #9
===============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **44,900,001** and
**45,360,000**.
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




The following 8 genes overlap the focal region: :doc:`../../../../../gene/AGAP003874` (uridine kinase),  :doc:`../../../../../gene/AGAP003875`,  :doc:`../../../../../gene/AGAP003876` (bHLH factor, other),  :doc:`../../../../../gene/AGAP003877`,  :doc:`../../../../../gene/AGAP013059`,  :doc:`../../../../../gene/AGAP003878`,  :doc:`../../../../../gene/AGAP003879` (VhaAC45 - vacuolar H  ATPase AC45 accessory subunit),  :doc:`../../../../../gene/AGAP003880`.




The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003872`,  :doc:`../../../../../gene/AGAP003873` (protein crumbs).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/9/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/9/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/9/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 198
        # variables        = 3
        chi-square         = 0.031
        reduced chi-square = 0.000
        Akaike info crit   = -1730.388
        Bayesian info crit = -1720.523
    [[Variables]]
        amplitude:   0.03830485 +/- 0.003442 (8.99%) (init= 0.5)
        decay:       2.50648268 +/- 0.673698 (26.88%) (init= 0.5)
        c:           0.02747964 +/- 0.003049 (11.10%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.892 
        C(amplitude, c)              = -0.391 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 188
        # variables        = 3
        chi-square         = 0.078
        reduced chi-square = 0.000
        Akaike info crit   = -1458.484
        Bayesian info crit = -1448.775
    [[Variables]]
        amplitude:   0.06146088 +/- 0.013989 (22.76%) (init= 0.5)
        decay:       0.42199836 +/- 0.138147 (32.74%) (init= 0.5)
        c:           0.04290625 +/- 0.001677 (3.91%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.704 
        C(decay, c)                  = -0.328 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 197
        # variables        = 1
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1646.732
        Bayesian info crit = -1643.449
    [[Variables]]
        c:   0.03881133 +/- 0.001087 (2.80%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 187
        # variables        = 1
        chi-square         = 0.087
        reduced chi-square = 0.000
        Akaike info crit   = -1433.421
        Bayesian info crit = -1430.190
    [[Variables]]
        c:   0.04569771 +/- 0.001579 (3.46%) (init= 0.03)


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


