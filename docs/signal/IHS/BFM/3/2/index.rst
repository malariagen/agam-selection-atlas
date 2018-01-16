:orphan:




IHS/BFM/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **10,040,000** and
**10,100,000**.
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


The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP008360` (SPZ3 - spaetzle-like cytokine 3),  :doc:`../../../../../gene/AGAP008362` (kelch-like protein 2/3),  :doc:`../../../../../gene/AGAP008363` (cytochrome b5 outer mitochondrial membrane isoform),  :doc:`../../../../../gene/AGAP008364` (TEP15 - thioester-containing protein 15),  :doc:`../../../../../gene/AGAP008366` (TEP2 - thioester-containing protein 2),  :doc:`../../../../../gene/AGAP008368` (TEP14 - thioester-containing protein 14),  :doc:`../../../../../gene/AGAP008369`,  :doc:`../../../../../gene/AGAP008370` (carboxypeptidase A),  :doc:`../../../../../gene/AGAP008371`,  :doc:`../../../../../gene/AGAP008372`,  :doc:`../../../../../gene/AGAP008373`.



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008359` (sodium-coupled monocarboxylate transporter 1),  :doc:`../../../../../gene/AGAP028115`,  :doc:`../../../../../gene/AGAP008374` (Inosine triphosphate pyrophosphatase),  :doc:`../../../../../gene/AGAP008375` (mannose-P-dolichol utilization defect 1),  :doc:`../../../../../gene/AGAP008376` (mRpL28 - 39S ribosomal protein L28, mitochondrial),  :doc:`../../../../../gene/AGAP008377` (TBC1 domain family member 19),  :doc:`../../../../../gene/AGAP008378` (amiloride-sensitive sodium channel, other),  :doc:`../../../../../gene/AGAP008379`,  :doc:`../../../../../gene/AGAP008380`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 647
        # variables        = 4
        chi-square         = 86.464
        reduced chi-square = 0.134
        Akaike info crit   = -1294.167
        Bayesian info crit = -1276.278
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.02496695 +/- 0.153960 (7.60%) (init= 3)
        decay:       0.15878621 +/- 0.021083 (13.28%) (init= 0.5)
        skew:       -0.88929568 +/- 0.148644 (16.71%) (init= 0)
        baseline:    1.97328548 +/- 0.015308 (0.78%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.593 
        C(decay, skew)               =  0.469 
        C(decay, baseline)           = -0.210 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 646
        # variables        = 1
        chi-square         = 122.171
        reduced chi-square = 0.189
        Akaike info crit   = -1073.836
        Bayesian info crit = -1069.365
    [[Variables]]
        c:   2.03331204 +/- 0.017123 (0.84%) (init= 1)



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


