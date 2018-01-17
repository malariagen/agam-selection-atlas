:orphan:




H12/BFM/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **11,159,316** and
**11,199,316**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).




This signal occurs within 50 kbp of the :doc:`../../../../../known-locus/tep1`,
a genome region with prior evidence of an association with insecticide resistance and/or recent positive
selection in *Anopheles* mosquitoes.


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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP010813` (TEP18 - thioester-containing protein 18),  :doc:`../../../../../gene/AGAP010814` (TEP6 - thioester-containing protein 6).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010815` (TEP1 - thioester-containing protein 1),  :doc:`../../../../../gene/AGAP010816` (TEP3 - thioester-containing protein 3),  :doc:`../../../../../gene/AGAP010817`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 388
        # variables        = 4
        chi-square         = 1.717
        reduced chi-square = 0.004
        Akaike info crit   = -2095.045
        Bayesian info crit = -2079.201
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.55345846 +/- 0.033617 (6.07%) (init= 0.5)
        decay:       0.26082150 +/- 0.026389 (10.12%) (init= 0.5)
        skew:       -0.98603104 +/- 0.107950 (10.95%) (init= 0)
        baseline:    0.02473373 +/- 0.003710 (15.00%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.614 
        C(decay, skew)               =  0.421 
        C(decay, baseline)           = -0.271 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 387
        # variables        = 1
        chi-square         = 3.425
        reduced chi-square = 0.009
        Akaike info crit   = -1827.429
        Bayesian info crit = -1823.470
    [[Variables]]
        c:   0.04534636 +/- 0.004787 (10.56%) (init= 0.03)



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


