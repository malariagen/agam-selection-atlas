:orphan:




IHS/CMS/2/6
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **42,394,895** and
**42,434,895**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).





.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area shows the focus of the
    selection signal. The shaded blue area shows the genomic region in linkage with the
    selection event. Use the mouse wheel or the controls at the top right of the plot to zoom
    in, and hover over genes to see gene names and descriptions.
    </p></div>

Genes
-----


The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP007086`:sup:`2` (Sodium channel protein),  :doc:`../../../../../gene/AGAP007088` (peptidyl-prolyl cis-trans isomerase B (cyclophilin B)),  :doc:`../../../../../gene/AGAP007089`.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007087` (RpL41 - 60s ribosomal protein L41),  :doc:`../../../../../gene/AGAP007090`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping selection signals
-----------------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. list-table::
    :widths: auto
    :header-rows: 1

    * - Signal
      - Statistic
      - Population
      - Focus
      - Peak model :math:`\Delta_{i}`
      - Max. percentile
      - Known locus
    * - :doc:`../../../../../signal/IHS/BFS/2/7/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 2L:42,314,895-42,454,895
      - 222
      - 95.5%
      - nan
    * - :doc:`../../../../../signal/IHS/GNS/2/5/index`
      - IHS
      - Guinea *An. gambiae*
      - 2L:42,274,895-42,414,895
      - 98
      - 87.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/6/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 46
        # data points      = 593
        # variables        = 4
        chi-square         = 58.687
        reduced chi-square = 0.100
        Akaike info crit   = -1363.591
        Bayesian info crit = -1346.050
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.78369435 +/- 0.078754 (10.05%) (init= 3)
        sigma:       0.21943608 +/- 0.031880 (14.53%) (init= 0.5)
        skew:        0.99999786 +/- 0.179797 (17.98%) (init= 0)
        baseline:    1.67656274 +/- 0.013625 (0.81%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.464 
        C(sigma, skew)               = -0.328 
        C(sigma, baseline)           = -0.162 
        C(amplitude, baseline)       = -0.135 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 592
        # variables        = 1
        chi-square         = 68.698
        reduced chi-square = 0.116
        Akaike info crit   = -1273.041
        Bayesian info crit = -1268.658
    [[Variables]]
        c:   1.71410248 +/- 0.014012 (0.82%) (init= 1)



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


