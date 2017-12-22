:orphan:




H12 / Angola *An. coluzzii* / Chromosome 2 / #6
===============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **34,480,001** and
**34,540,000**.
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




The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP003252` (CLIPB6 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP013184` (CLIPB36 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003253` (Gr15 - gustatory receptor 15),  :doc:`../../../../../gene/AGAP003254` (Gr16 - gustatory receptor 16),  :doc:`../../../../../gene/AGAP003255` (Gr17 - gustatory receptor 17),  :doc:`../../../../../gene/AGAP003256` (Gr18 - gustatory receptor 18),  :doc:`../../../../../gene/AGAP003257`:sup:`1` (GSTU2 - glutathione S-transferase unclassified 2),  :doc:`../../../../../gene/AGAP003258` (Gustatory receptor),  :doc:`../../../../../gene/AGAP003259` (Gr20 - gustatory receptor 20),  :doc:`../../../../../gene/AGAP003260` (Gr21 - gustatory receptor 21).




The following 11 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003245` (CLIPA19 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003246` (CLIPB2 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003247` (CLIPB19 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003248`,  :doc:`../../../../../gene/AGAP013487`,  :doc:`../../../../../gene/AGAP003249` (CLIPB3 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003250` (CLIPB4 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003251` (CLIPB1 - CLIP-domain serine protease),  :doc:`../../../../../gene/AGAP003261`,  :doc:`../../../../../gene/AGAP003262` (integrator complex subunit 10),  :doc:`../../../../../gene/AGAP003263` (CDC42 small effector protein-like protein).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/6/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 199
        # variables        = 3
        chi-square         = 0.025
        reduced chi-square = 0.000
        Akaike info crit   = -1777.553
        Bayesian info crit = -1767.673
    [[Variables]]
        amplitude:   0.07763714 +/- 0.004808 (6.19%) (init= 0.5)
        decay:       0.81772820 +/- 0.085183 (10.42%) (init= 0.5)
        c:           0.02084834 +/- 0.001052 (5.05%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.583 
        C(decay, c)                  = -0.508 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 197
        # variables        = 3
        chi-square         = 0.035
        reduced chi-square = 0.000
        Akaike info crit   = -1697.217
        Bayesian info crit = -1687.367
    [[Variables]]
        amplitude:   0.02350933 +/- 0.003920 (16.68%) (init= 0.5)
        decay:       2.95317617 +/- 1.575570 (53.35%) (init= 0.5)
        c:           0.02501477 +/- 0.004211 (16.84%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.924 
        C(amplitude, c)              = -0.561 
        C(amplitude, decay)          =  0.289 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 198
        # variables        = 1
        chi-square         = 0.066
        reduced chi-square = 0.000
        Akaike info crit   = -1584.311
        Bayesian info crit = -1581.023
    [[Variables]]
        c:   0.02848625 +/- 0.001297 (4.55%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 0.039
        reduced chi-square = 0.000
        Akaike info crit   = -1669.465
        Bayesian info crit = -1666.186
    [[Variables]]
        c:   0.03286989 +/- 0.001007 (3.06%) (init= 0.03)


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


