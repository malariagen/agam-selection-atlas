:orphan:




H12 / Angola *An. coluzzii* / Chromosome 2 / #5
===============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **59,700,001** and
**60,240,000**.
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




The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP004659` (Homeotic antennapedia protein),  :doc:`../../../../../gene/AGAP013157` (Antp family),  :doc:`../../../../../gene/AGAP004660` (Antennapedia homeotic protein),  :doc:`../../../../../gene/AGAP004661` (Antp family, other),  :doc:`../../../../../gene/AGAP004662` (homeobox protein abdominal-A homolog).



No genes are within 50 kbp of the focal region.




Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/5/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 82
        # data points      = 235
        # variables        = 3
        chi-square         = 0.833
        reduced chi-square = 0.004
        Akaike info crit   = -1319.942
        Bayesian info crit = -1309.564
    [[Variables]]
        amplitude:   0.33070797 +/- 0.016384 (4.95%) (init= 0.5)
        decay:       2.99999974 +/- 0.317671 (10.59%) (init= 0.5)
        c:           0.05999999 +/- 0.037655 (62.76%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.927 
        C(amplitude, c)              =  0.833 
        C(amplitude, decay)          =  0.647 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 113
        # data points      = 329
        # variables        = 3
        chi-square         = 2.752
        reduced chi-square = 0.008
        Akaike info crit   = -1567.850
        Bayesian info crit = -1556.461
    [[Variables]]
        amplitude:   0.27637999 +/- 0.020414 (7.39%) (init= 0.5)
        decay:       3          +/- 0.065861 (2.20%) (init= 0.5)
        c:           0.05999999 +/- 0.193846 (323.08%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.909 
        C(amplitude, c)              =  0.752 
        C(amplitude, decay)          =  0.487 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 233
        # variables        = 1
        chi-square         = 2.793
        reduced chi-square = 0.012
        Akaike info crit   = -1028.740
        Bayesian info crit = -1025.289
    [[Variables]]
        c:   0.21034692 +/- 0.007188 (3.42%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 328
        # variables        = 1
        chi-square         = 3.053
        reduced chi-square = 0.009
        Akaike info crit   = -1532.009
        Bayesian info crit = -1528.216
    [[Variables]]
        c:   0.20468030 +/- 0.005335 (2.61%) (init= 0.03)


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


