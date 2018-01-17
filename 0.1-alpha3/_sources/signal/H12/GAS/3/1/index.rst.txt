:orphan:




H12/GAS/3/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **9,639,316** and
**10,199,316**.
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


The following 32 genes overlap the focal region: :doc:`../../../../../gene/AGAP010744`,  :doc:`../../../../../gene/AGAP010745`,  :doc:`../../../../../gene/AGAP010746`,  :doc:`../../../../../gene/AGAP010748`,  :doc:`../../../../../gene/AGAP010750` (ryanodine receptor 2),  :doc:`../../../../../gene/AGAP010751`,  :doc:`../../../../../gene/AGAP010752`,  :doc:`../../../../../gene/AGAP010753`,  :doc:`../../../../../gene/AGAP010754`,  :doc:`../../../../../gene/AGAP010755` (protein mago nashi),  :doc:`../../../../../gene/AGAP010756`,  :doc:`../../../../../gene/AGAP010757`,  :doc:`../../../../../gene/AGAP010758` (Metalloendopeptidase (Fragment)),  :doc:`../../../../../gene/AGAP010759`,  :doc:`../../../../../gene/AGAP010760`,  :doc:`../../../../../gene/AGAP010761`,  :doc:`../../../../../gene/AGAP010762`,  :doc:`../../../../../gene/AGAP010763`,  :doc:`../../../../../gene/AGAP010764` (Metalloendopeptidase),  :doc:`../../../../../gene/AGAP010765`,  :doc:`../../../../../gene/AGAP010766`,  :doc:`../../../../../gene/AGAP010767`,  :doc:`../../../../../gene/AGAP010768` (NEFA-interacting nuclear protein NIP30),  :doc:`../../../../../gene/AGAP010769` (glucosamine-phosphate N-acetyltransferase),  :doc:`../../../../../gene/AGAP010770`,  :doc:`../../../../../gene/AGAP010771`,  :doc:`../../../../../gene/AGAP010772`,  :doc:`../../../../../gene/AGAP010773`,  :doc:`../../../../../gene/AGAP010774`,  :doc:`../../../../../gene/AGAP010775`,  :doc:`../../../../../gene/AGAP010776`,  :doc:`../../../../../gene/AGAP010777` (hunchback).



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010778`,  :doc:`../../../../../gene/AGAP010779`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 56
        # data points      = 388
        # variables        = 4
        chi-square         = 0.051
        reduced chi-square = 0.000
        Akaike info crit   = -3457.238
        Bayesian info crit = -3441.394
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.04179434 +/- 0.002559 (6.12%) (init= 0.5)
        sigma:       0.66179714 +/- 0.053230 (8.04%) (init= 0.5)
        skew:        0.99999760 +/- 0.094250 (9.43%) (init= 0)
        baseline:    0.03321885 +/- 0.000688 (2.07%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               = -0.491 
        C(amplitude, sigma)          = -0.434 
        C(sigma, baseline)           = -0.294 
        C(amplitude, baseline)       = -0.180 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 387
        # variables        = 1
        chi-square         = 0.096
        reduced chi-square = 0.000
        Akaike info crit   = -3212.286
        Bayesian info crit = -3208.328
    [[Variables]]
        c:   0.03824965 +/- 0.000800 (2.09%) (init= 0.03)



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


