:orphan:




H12/BFM/3/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **52,600,000** and
**53,080,000**.
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


The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP010297`,  :doc:`../../../../../gene/AGAP010298` (V-type H -transporting ATPase subunit D),  :doc:`../../../../../gene/AGAP010299`,  :doc:`../../../../../gene/AGAP010300`,  :doc:`../../../../../gene/AGAP010301`,  :doc:`../../../../../gene/AGAP010302`,  :doc:`../../../../../gene/AGAP010303` (autophagy-related protein 7),  :doc:`../../../../../gene/AGAP010304`,  :doc:`../../../../../gene/AGAP010305` (WD repeat and SOF domain-containing protein 1),  :doc:`../../../../../gene/AGAP010306`,  :doc:`../../../../../gene/AGAP010307` (Pleckstrin homology domain containing, family F (with FYVE domain) member 2).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010295`,  :doc:`../../../../../gene/AGAP010308` (nucleolar complex protein 3),  :doc:`../../../../../gene/AGAP010309`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 161
        # data points      = 500
        # variables        = 4
        chi-square         = 0.408
        reduced chi-square = 0.001
        Akaike info crit   = -3547.255
        Bayesian info crit = -3530.396
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.05517604 +/- 0.003950 (7.16%) (init= 0.5)
        decay:       1.90468398 +/- 0.376353 (19.76%) (init= 0.5)
        skew:       -0.99999999 +/- 0.320147 (32.01%) (init= 0)
        baseline:    0.03687997 +/- 0.002714 (7.36%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.697 
        C(amplitude, baseline)       = -0.481 
        C(decay, skew)               = -0.436 
        C(skew, baseline)            =  0.175 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 499
        # variables        = 1
        chi-square         = 0.553
        reduced chi-square = 0.001
        Akaike info crit   = -3393.531
        Bayesian info crit = -3389.318
    [[Variables]]
        c:   0.05644559 +/- 0.001492 (2.64%) (init= 0.03)



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


