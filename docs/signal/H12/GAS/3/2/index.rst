:orphan:




H12/GAS/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **41,680,000** and
**41,980,000**.
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




The following 9 genes overlap the focal region: :doc:`../../../../../gene/AGAP009726`,  :doc:`../../../../../gene/AGAP009727` (RhoGAP92B),  :doc:`../../../../../gene/AGAP009728` (ficolin),  :doc:`../../../../../gene/AGAP009729` (CCAP - cardioacceleratory peptide),  :doc:`../../../../../gene/AGAP009730` (myosin III),  :doc:`../../../../../gene/AGAP009731` (wingless-type MMTV integration site family, member 10A),  :doc:`../../../../../gene/AGAP009732` (Protein Wnt),  :doc:`../../../../../gene/AGAP009733` (wingless-type MMTV integration site family, member 6),  :doc:`../../../../../gene/AGAP009734` (wingless-type MMTV integration site family, member 1).




The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009725` (cadherin),  :doc:`../../../../../gene/AGAP009735` (wingless-type MMTV integration site family, member 16).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 489
        # variables        = 4
        chi-square         = 0.066
        reduced chi-square = 0.000
        Akaike info crit   = -4346.352
        Bayesian info crit = -4329.583
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.02668243 +/- 0.002665 (9.99%) (init= 0.5)
        sigma:       0.45318301 +/- 0.049391 (10.90%) (init= 0.5)
        skew:       -0.65948632 +/- 0.116949 (17.73%) (init= 0)
        baseline:    0.02830380 +/- 0.000605 (2.14%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.547 
        C(sigma, baseline)           = -0.303 
        C(sigma, skew)               = -0.180 
        C(amplitude, baseline)       = -0.140 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 8
        # data points      = 488
        # variables        = 1
        chi-square         = 0.083
        reduced chi-square = 0.000
        Akaike info crit   = -4233.482
        Bayesian info crit = -4229.292
    [[Variables]]
        c:   0.03089682 +/- 0.000591 (1.91%) (init= 0.03)



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


