:orphan:




H12 / Burkina Faso *An. coluzzii* / Chromosome 2 / #4
=====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,880,001** and
**40,980,000**.
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
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 12 genes overlap the focal region: :doc:`../../../../../gene/AGAP003639` (Prolylcarboxypeptidase),  :doc:`../../../../../gene/AGAP003640`:sup:`1` (SP8905),  :doc:`../../../../../gene/AGAP003641`:sup:`1` (SP8907),  :doc:`../../../../../gene/AGAP003642`:sup:`1` (SP8898),  :doc:`../../../../../gene/AGAP003643` (ubiquitin carboxyl-terminal hydrolase 34),  :doc:`../../../../../gene/AGAP003644` (mRpS11 - 28S ribosomal protein S11, mitochondrial),  :doc:`../../../../../gene/AGAP003645` (kelch-like protein 19),  :doc:`../../../../../gene/AGAP013307`,  :doc:`../../../../../gene/AGAP003646`,  :doc:`../../../../../gene/AGAP003647`,  :doc:`../../../../../gene/AGAP003648` (DNA-directed RNA polymerase II subunit RPB2),  :doc:`../../../../../gene/AGAP003649`.




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003638`,  :doc:`../../../../../gene/AGAP003650` (translation initiation factor eIF-2B subunit alpha),  :doc:`../../../../../gene/AGAP003651` (Tyrosine-protein kinase Fes/Fps).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/BFS/2/6/index`, "2R:40,820,001-41,000,000", 359 (249 | 109)
    :doc:`../../../../../signal/H12/CMS/2/3/index`, "2R:40,600,001-40,980,000", 269 (195 | 74)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 150
        # variables        = 3
        chi-square         = 0.043
        reduced chi-square = 0.000
        Akaike info crit   = -1216.665
        Bayesian info crit = -1207.633
    [[Variables]]
        amplitude:   0.20013693 +/- 0.011838 (5.92%) (init= 0.5)
        decay:       0.24787169 +/- 0.023501 (9.48%) (init= 0.5)
        c:           0.03218181 +/- 0.001533 (4.76%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.607 
        C(decay, c)                  = -0.300 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 147
        # variables        = 3
        chi-square         = 0.021
        reduced chi-square = 0.000
        Akaike info crit   = -1292.035
        Bayesian info crit = -1283.063
    [[Variables]]
        amplitude:   0.17577468 +/- 0.010479 (5.96%) (init= 0.5)
        decay:       0.29058214 +/- 0.024174 (8.32%) (init= 0.5)
        c:           0.02458210 +/- 0.001123 (4.57%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.722 
        C(decay, c)                  = -0.328 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.145
        reduced chi-square = 0.001
        Akaike info crit   = -1030.942
        Bayesian info crit = -1027.938
    [[Variables]]
        c:   0.03995551 +/- 0.002567 (6.43%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 146
        # variables        = 1
        chi-square         = 0.090
        reduced chi-square = 0.001
        Akaike info crit   = -1077.673
        Bayesian info crit = -1074.689
    [[Variables]]
        c:   0.03171602 +/- 0.002058 (6.49%) (init= 0.03)


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


