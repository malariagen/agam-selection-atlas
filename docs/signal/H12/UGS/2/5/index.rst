:orphan:




H12/UGS/2/5
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **42,774,895** and
**42,814,895**.
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




The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP007103` (calsyntenin-1),  :doc:`../../../../../gene/AGAP007104` (farnesyl diphosphate synthase),  :doc:`../../../../../gene/AGAP007105`,  :doc:`../../../../../gene/AGAP007106` (ubiquitin carboxyl-terminal hydrolase 47).




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007107` (DnaJ homolog subfamily B member 4),  :doc:`../../../../../gene/AGAP007108` (multiple PDZ domain protein),  :doc:`../../../../../gene/AGAP007109`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 78
        # data points      = 400
        # variables        = 4
        chi-square         = 0.053
        reduced chi-square = 0.000
        Akaike info crit   = -3562.424
        Bayesian info crit = -3546.458
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.08939596 +/- 0.008482 (9.49%) (init= 0.5)
        decay:       0.15000000 +/- 0.020637 (13.76%) (init= 0.5)
        skew:        0.12634992 +/- 0.136781 (108.26%) (init= 0)
        baseline:    0.01783358 +/- 0.000602 (3.38%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.694 
        C(decay, baseline)           =  0.198 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 399
        # variables        = 1
        chi-square         = 0.067
        reduced chi-square = 0.000
        Akaike info crit   = -3463.637
        Bayesian info crit = -3459.648
    [[Variables]]
        c:   0.01921253 +/- 0.000652 (3.39%) (init= 0.03)



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


