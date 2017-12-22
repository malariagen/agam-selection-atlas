:orphan:




H12 / Uganda *An. gambiae* / Chromosome 3 / #5
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **36,240,001** and
**36,300,000**.
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




The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP012010` (6-phosphofructo-2-kinase / fructose-2,6-bisphosphatase),  :doc:`../../../../../gene/AGAP012011`,  :doc:`../../../../../gene/AGAP012012`.




The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP028185`,  :doc:`../../../../../gene/AGAP012007`,  :doc:`../../../../../gene/AGAP012008`,  :doc:`../../../../../gene/AGAP028012` (DNA-directed RNA polymerase subunit),  :doc:`../../../../../gene/AGAP012009` (chromodomain-helicase-DNA-binding protein 4),  :doc:`../../../../../gene/AGAP012013`,  :doc:`../../../../../gene/AGAP012014` (Arf1 - ADP-ribosylation factor 1),  :doc:`../../../../../gene/AGAP012015`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/5/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 149
        # variables        = 3
        chi-square         = 0.000
        reduced chi-square = 0.000
        Akaike info crit   = -1918.287
        Bayesian info crit = -1909.275
    [[Variables]]
        amplitude:   0.00830763 +/- 0.001061 (12.78%) (init= 0.5)
        decay:       0.43185443 +/- 0.081710 (18.92%) (init= 0.5)
        c:           0.00633743 +/- 0.000154 (2.43%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.685 
        C(decay, c)                  = -0.412 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 51
        # data points      = 144
        # variables        = 3
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1781.845
        Bayesian info crit = -1772.936
    [[Variables]]
        amplitude:   0.01515244 +/- 0.002877 (18.99%) (init= 0.5)
        decay:       0.15000011 +/- 0.036921 (24.61%) (init= 0.5)
        c:           0.00672071 +/- 0.000178 (2.65%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.792 
        C(decay, c)                  = -0.213 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1838.931
        Bayesian info crit = -1835.934
    [[Variables]]
        c:   0.00685547 +/- 0.000164 (2.39%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 143
        # variables        = 1
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1760.533
        Bayesian info crit = -1757.571
    [[Variables]]
        c:   0.00694027 +/- 0.000177 (2.55%) (init= 0.03)


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


