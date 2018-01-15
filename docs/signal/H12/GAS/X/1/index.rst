:orphan:




H12/GAS/X/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **13,920,000** and
**14,440,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

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




The following 19 genes overlap the focal region: :doc:`../../../../../gene/AGAP000776` (myosin VI),  :doc:`../../../../../gene/AGAP000777`,  :doc:`../../../../../gene/AGAP000778`,  :doc:`../../../../../gene/AGAP000779` (zinc finger homeobox protein 1/2),  :doc:`../../../../../gene/AGAP000780`:sup:`1` (Yippee-like 5),  :doc:`../../../../../gene/AGAP000781` (mitochondrial import inner membrane translocase subunit Tim9),  :doc:`../../../../../gene/AGAP000782`,  :doc:`../../../../../gene/AGAP000783`,  :doc:`../../../../../gene/AGAP000784` (abhydrolase domain containing 4),  :doc:`../../../../../gene/AGAP000785` (Synaptic vesicle protein),  :doc:`../../../../../gene/AGAP000786`,  :doc:`../../../../../gene/AGAP000787` (E3 ubiquitin-protein ligase NEDD4),  :doc:`../../../../../gene/AGAP000788`,  :doc:`../../../../../gene/AGAP013147`,  :doc:`../../../../../gene/AGAP000789`,  :doc:`../../../../../gene/AGAP000790`,  :doc:`../../../../../gene/AGAP000791` (Tango10),  :doc:`../../../../../gene/AGAP000792` (Adenosylhomocysteinase),  :doc:`../../../../../gene/AGAP000793`.




The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000772`,  :doc:`../../../../../gene/AGAP000773` (single-minded),  :doc:`../../../../../gene/AGAP000774` (PH and SEC7 domain-containing protein),  :doc:`../../../../../gene/AGAP000794`:sup:`1` (NADH dehydrogenase (ubiquinone) Fe-S protein 2),  :doc:`../../../../../gene/AGAP013289`,  :doc:`../../../../../gene/AGAP000795`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 390
        # variables        = 4
        chi-square         = 1.314
        reduced chi-square = 0.003
        Akaike info crit   = -2212.348
        Bayesian info crit = -2196.484
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.21889434 +/- 0.012227 (5.59%) (init= 0.5)
        decay:       2.99999755 +/- 2.984731 (99.49%) (init= 0.5)
        skew:       -0.11716133 +/- 0.067429 (57.55%) (init= 0)
        baseline:    0.06593343 +/- 0.013012 (19.74%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           =  0.924 
        C(amplitude, baseline)       = -0.589 
        C(amplitude, decay)          = -0.321 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 389
        # variables        = 1
        chi-square         = 2.450
        reduced chi-square = 0.006
        Akaike info crit   = -1969.317
        Bayesian info crit = -1965.353
    [[Variables]]
        c:   0.14116890 +/- 0.004028 (2.85%) (init= 0.03)



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


