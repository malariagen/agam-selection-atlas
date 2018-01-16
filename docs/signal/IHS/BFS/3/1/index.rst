:orphan:




IHS/BFS/3/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **27,940,000** and
**28,260,000**.
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




The following 20 genes overlap the focal region: :doc:`../../../../../gene/AGAP009163`,  :doc:`../../../../../gene/AGAP009164`,  :doc:`../../../../../gene/AGAP028161`,  :doc:`../../../../../gene/AGAP009165`,  :doc:`../../../../../gene/AGAP009166` (IKK1 - IMD pathway signalling IKK-beta). (ird5orthologue immune response deficient 5)),  :doc:`../../../../../gene/AGAP009167`,  :doc:`../../../../../gene/AGAP009168`,  :doc:`../../../../../gene/AGAP009170`,  :doc:`../../../../../gene/AGAP009172` (prolyl oligopeptidase),  :doc:`../../../../../gene/AGAP009171`:sup:`1` (tRNA-dihydrouridine synthase 3),  :doc:`../../../../../gene/AGAP009173` (fbp - fructose-1,6-biphosphatase),  :doc:`../../../../../gene/AGAP009174` (vacuolar protein sorting 41 homolog),  :doc:`../../../../../gene/AGAP009175` (galactosylxylosylprotein 3-beta-galactosyltransferase),  :doc:`../../../../../gene/AGAP009176`:sup:`1` (fatty acid synthase, animal type),  :doc:`../../../../../gene/AGAP009177`:sup:`1`,  :doc:`../../../../../gene/AGAP009178`:sup:`1` (Reticulon 4 interacting protein 1),  :doc:`../../../../../gene/AGAP009179` (nucleolar protein 6),  :doc:`../../../../../gene/AGAP009180` (protein son of sevenless),  :doc:`../../../../../gene/AGAP009181`,  :doc:`../../../../../gene/AGAP009182` (protein transport protein SEC61 subunit alpha).




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009160` (Arf-GAP, GTPase, ANK repeat and PH domain-containing protein 1/2/3),  :doc:`../../../../../gene/AGAP009161` (deoxyribose-phosphate aldolase),  :doc:`../../../../../gene/AGAP009162`:sup:`4`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 92
        # data points      = 615
        # variables        = 4
        chi-square         = 207.191
        reduced chi-square = 0.339
        Akaike info crit   = -661.107
        Bayesian info crit = -643.421
    [[Variables]]
        center:      0 (fixed)
        amplitude:   3.10430140 +/- 0.081979 (2.64%) (init= 3)
        decay:       2.50877389 +/- 0.158374 (6.31%) (init= 0.5)
        skew:       -0.99999999 +/- 0.011265 (1.13%) (init= 0)
        baseline:    1.74741223 +/- 0.053236 (3.05%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.733 
        C(amplitude, baseline)       = -0.423 
        C(decay, skew)               = -0.314 
        C(skew, baseline)            =  0.267 
        C(amplitude, skew)           = -0.199 
        C(amplitude, decay)          = -0.113 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 614
        # variables        = 1
        chi-square         = 706.345
        reduced chi-square = 1.152
        Akaike info crit   = 88.026
        Bayesian info crit = 92.446
    [[Variables]]
        c:   2.81962859 +/- 0.043319 (1.54%) (init= 1)



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


