:orphan:




IHS/BFS/2/8
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **37,274,895** and
**37,594,895**.
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




The following 16 genes overlap the focal region: :doc:`../../../../../gene/AGAP006723`:sup:`1` (COEAE2G - carboxylesterase),  :doc:`../../../../../gene/AGAP006724` (COEAE3G - carboxylesterase),  :doc:`../../../../../gene/AGAP006725`:sup:`1` (COEAE3H - carboxylesterase alpha esterase),  :doc:`../../../../../gene/AGAP006726` (COEAE5G - carboxylesterase),  :doc:`../../../../../gene/AGAP006727`:sup:`1` (COEAE6G - carboxylesterase),  :doc:`../../../../../gene/AGAP006728` (COEAE7G - carboxylesterase),  :doc:`../../../../../gene/AGAP006729` (Ester hydrolase C11orf54),  :doc:`../../../../../gene/AGAP006730`,  :doc:`../../../../../gene/AGAP006731`,  :doc:`../../../../../gene/AGAP006732`,  :doc:`../../../../../gene/AGAP006733` (Thoc4 - THO complex subunit 4),  :doc:`../../../../../gene/AGAP006734` (DNA-repair protein XRCC2),  :doc:`../../../../../gene/AGAP006735`,  :doc:`../../../../../gene/AGAP006736` (zinc finger protein GLIS2),  :doc:`../../../../../gene/AGAP028461`,  :doc:`../../../../../gene/AGAP006737`.




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006721`,  :doc:`../../../../../gene/AGAP006722` (CEC4 - cecropin anti-microbial peptide),  :doc:`../../../../../gene/AGAP006738`,  :doc:`../../../../../gene/AGAP006739`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/8/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/8/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/8/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 79
        # data points      = 424
        # variables        = 4
        chi-square         = 47.288
        reduced chi-square = 0.113
        Akaike info crit   = -922.035
        Bayesian info crit = -905.836
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.95590686 +/- 0.085201 (8.91%) (init= 3)
        decay:       1.32106245 +/- 0.209733 (15.88%) (init= 0.5)
        skew:       -1          +/- 0.002535 (0.25%) (init= 0)
        baseline:    1.71717194 +/- 0.025482 (1.48%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.583 
        C(amplitude, decay)          = -0.528 
        C(decay, skew)               =  0.357 
        C(skew, baseline)            = -0.100 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 423
        # variables        = 1
        chi-square         = 64.206
        reduced chi-square = 0.152
        Akaike info crit   = -795.474
        Bayesian info crit = -791.427
    [[Variables]]
        c:   1.88330114 +/- 0.018965 (1.01%) (init= 1)



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


