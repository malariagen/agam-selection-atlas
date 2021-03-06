:orphan:




IHS/BFM/3/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3L** between positions **19,819,316** and
**19,899,316**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).





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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP011230`,  :doc:`../../../../../gene/AGAP011231` (fibrinogen),  :doc:`../../../../../gene/AGAP011232`,  :doc:`../../../../../gene/AGAP011233`,  :doc:`../../../../../gene/AGAP011234`,  :doc:`../../../../../gene/AGAP028622`.



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP011229` (Tartan),  :doc:`../../../../../gene/AGAP011237`,  :doc:`../../../../../gene/AGAP011238`,  :doc:`../../../../../gene/AGAP011239`,  :doc:`../../../../../gene/AGAP028623`,  :doc:`../../../../../gene/AGAP011242` (E3 ubiquitin ligase SMURF1/2).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 614
        # variables        = 4
        chi-square         = 126.421
        reduced chi-square = 0.207
        Akaike info crit   = -962.352
        Bayesian info crit = -944.672
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.71111109 +/- 0.241296 (8.90%) (init= 3)
        decay:       0.20990504 +/- 0.025580 (12.19%) (init= 0.5)
        skew:       -0.20785586 +/- 0.116061 (55.84%) (init= 0)
        baseline:    2.10831775 +/- 0.019435 (0.92%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.716 
        C(decay, baseline)           = -0.232 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 613
        # variables        = 1
        chi-square         = 172.951
        reduced chi-square = 0.283
        Akaike info crit   = -773.665
        Bayesian info crit = -769.246
    [[Variables]]
        c:   2.17579119 +/- 0.021471 (0.99%) (init= 1)



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


