:orphan:




XPEHH/GAS.AOM/2/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/AOM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **14,654,895** and
**14,834,895**.
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


The following 17 genes overlap the focal region: :doc:`../../../../../gene/AGAP005364` (protein BAT5),  :doc:`../../../../../gene/AGAP005365` (ribosome biogenesis protein BRX1),  :doc:`../../../../../gene/AGAP005366` (serine/arginine repetitive matrix protein 1),  :doc:`../../../../../gene/AGAP005368`,  :doc:`../../../../../gene/AGAP005369`,  :doc:`../../../../../gene/AGAP005370` (COEBE4C - carboxylesterase beta esterase),  :doc:`../../../../../gene/AGAP005371`:sup:`1` (COEBE2C - carboxylesterase beta esterase),  :doc:`../../../../../gene/AGAP005372`:sup:`1` (COEBE3C - carboxylesterase beta esterase),  :doc:`../../../../../gene/AGAP005373`:sup:`1` (COEBE1C - carboxylesterase beta esterase),  :doc:`../../../../../gene/AGAP005374`,  :doc:`../../../../../gene/AGAP005375` (nonsense-mediated mRNA decay protein),  :doc:`../../../../../gene/AGAP005376`,  :doc:`../../../../../gene/AGAP005377`,  :doc:`../../../../../gene/AGAP005378`,  :doc:`../../../../../gene/AGAP005379`,  :doc:`../../../../../gene/AGAP005380`,  :doc:`../../../../../gene/AGAP005381` (hexosaminidase).



The following 15 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP005356` (predicted G-protein coupled receptor GPCR),  :doc:`../../../../../gene/AGAP005359` (F-box and WD-40 domain protein 7),  :doc:`../../../../../gene/AGAP005360` (PQ loop repeat-containing protein 3),  :doc:`../../../../../gene/AGAP005361`,  :doc:`../../../../../gene/AGAP005362` (NF-X1-type zinc finger protein NFXL1),  :doc:`../../../../../gene/AGAP005363`,  :doc:`../../../../../gene/AGAP005382` (transcription initiation factor TFIIE subunit beta),  :doc:`../../../../../gene/AGAP005383` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP005384` (phosphatidylinositol transfer protein SEC14),  :doc:`../../../../../gene/AGAP005385` (phosphatidylinositol transfer protein SEC14),  :doc:`../../../../../gene/AGAP005386`,  :doc:`../../../../../gene/AGAP005387` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP005388` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP005389`,  :doc:`../../../../../gene/AGAP005390`.


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
    * - :doc:`../../../../../signal/H12/GAS/2/3/index`
      - H12
      - Gabon *An. gambiae*
      - 2L:14,694,895-14,814,895
      - 121
      - 98.8%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.AOM/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.AOM/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.AOM/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 298
        # variables        = 4
        chi-square         = 77.494
        reduced chi-square = 0.264
        Akaike info crit   = -393.374
        Bayesian info crit = -378.586
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.19477016 +/- 0.088756 (7.43%) (init= 3)
        sigma:       2.35799535 +/- 0.235591 (9.99%) (init= 0.5)
        skew:       -1          +/- 0.005332 (0.53%) (init= 0)
        baseline:    1.15691003 +/- 0.074084 (6.40%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.774 
        C(sigma, baseline)           = -0.560 
        C(sigma, skew)               = -0.451 
        C(amplitude, sigma)          =  0.151 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 297
        # variables        = 1
        chi-square         = 123.264
        reduced chi-square = 0.416
        Akaike info crit   = -259.184
        Bayesian info crit = -255.490
    [[Variables]]
        c:   1.85404759 +/- 0.037444 (2.02%) (init= 1)



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


