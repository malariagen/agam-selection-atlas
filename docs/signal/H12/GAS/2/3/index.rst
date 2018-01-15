:orphan:




H12/GAS/2/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **14,694,895** and
**14,814,895**.
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




The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP005369`,  :doc:`../../../../../gene/AGAP005370` (COEBE4C - carboxylesterase beta esterase),  :doc:`../../../../../gene/AGAP005371`:sup:`1` (COEBE2C - carboxylesterase beta esterase),  :doc:`../../../../../gene/AGAP005372`:sup:`1` (COEBE3C - carboxylesterase beta esterase),  :doc:`../../../../../gene/AGAP005373`:sup:`1` (COEBE1C - carboxylesterase beta esterase),  :doc:`../../../../../gene/AGAP005374`,  :doc:`../../../../../gene/AGAP005375` (nonsense-mediated mRNA decay protein),  :doc:`../../../../../gene/AGAP005376`,  :doc:`../../../../../gene/AGAP005377`,  :doc:`../../../../../gene/AGAP005378`.




The following 20 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP005360` (PQ loop repeat-containing protein 3),  :doc:`../../../../../gene/AGAP005361`,  :doc:`../../../../../gene/AGAP005362` (NF-X1-type zinc finger protein NFXL1),  :doc:`../../../../../gene/AGAP005363`,  :doc:`../../../../../gene/AGAP005364` (protein BAT5),  :doc:`../../../../../gene/AGAP005365` (ribosome biogenesis protein BRX1),  :doc:`../../../../../gene/AGAP005366` (serine/arginine repetitive matrix protein 1),  :doc:`../../../../../gene/AGAP005368`,  :doc:`../../../../../gene/AGAP005379`,  :doc:`../../../../../gene/AGAP005380`,  :doc:`../../../../../gene/AGAP005381` (hexosaminidase),  :doc:`../../../../../gene/AGAP005382` (transcription initiation factor TFIIE subunit beta),  :doc:`../../../../../gene/AGAP005383` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP005384` (phosphatidylinositol transfer protein SEC14),  :doc:`../../../../../gene/AGAP005385` (phosphatidylinositol transfer protein SEC14),  :doc:`../../../../../gene/AGAP005386`,  :doc:`../../../../../gene/AGAP005387` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP005388` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP005389`,  :doc:`../../../../../gene/AGAP005390`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 73
        # data points      = 397
        # variables        = 4
        chi-square         = 0.233
        reduced chi-square = 0.001
        Akaike info crit   = -2945.657
        Bayesian info crit = -2929.722
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.04424056 +/- 0.003435 (7.77%) (init= 0.5)
        sigma:       1.86856880 +/- 0.199881 (10.70%) (init= 0.5)
        skew:       -0.95677923 +/- 0.113354 (11.85%) (init= 0)
        baseline:    0.04054460 +/- 0.002052 (5.06%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.525 
        C(amplitude, baseline)       = -0.490 
        C(sigma, skew)               =  0.430 
        C(amplitude, sigma)          = -0.122 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 396
        # variables        = 1
        chi-square         = 0.315
        reduced chi-square = 0.001
        Akaike info crit   = -2823.719
        Bayesian info crit = -2819.738
    [[Variables]]
        c:   0.05578867 +/- 0.001419 (2.54%) (init= 0.03)



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


