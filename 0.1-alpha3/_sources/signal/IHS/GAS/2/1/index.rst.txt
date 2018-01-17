:orphan:




IHS/GAS/2/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **13,880,000** and
**14,040,000**.
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


The following 25 genes overlap the focal region: :doc:`../../../../../gene/AGAP002009` (dynein heavy chain, axonemal),  :doc:`../../../../../gene/AGAP002010`,  :doc:`../../../../../gene/AGAP002011` (ammonium transporter Rh),  :doc:`../../../../../gene/AGAP002012`,  :doc:`../../../../../gene/AGAP012959`,  :doc:`../../../../../gene/AGAP013169`,  :doc:`../../../../../gene/AGAP013098`,  :doc:`../../../../../gene/AGAP013325`,  :doc:`../../../../../gene/AGAP013295`,  :doc:`../../../../../gene/AGAP013531`,  :doc:`../../../../../gene/AGAP013438`,  :doc:`../../../../../gene/AGAP013072`,  :doc:`../../../../../gene/AGAP013483`,  :doc:`../../../../../gene/AGAP002013` (leucine-rich repeat-containing protein 49),  :doc:`../../../../../gene/AGAP002014` (leucyl-tRNA synthetase),  :doc:`../../../../../gene/AGAP002015` (dynein heavy chain 1, cytosolic),  :doc:`../../../../../gene/AGAP002016` (iron/zinc purple acid phosphatase-like protein precursor),  :doc:`../../../../../gene/AGAP002017` (Hexosyltransferase),  :doc:`../../../../../gene/AGAP002018` (histone-lysine N-methyltransferase setd3),  :doc:`../../../../../gene/AGAP013249`,  :doc:`../../../../../gene/AGAP002019` (COMPASS component SWD3),  :doc:`../../../../../gene/AGAP002020` (NADH dehydrogenase (ubiquinone) 1 beta subcomplex 8),  :doc:`../../../../../gene/AGAP002021` (lysophosphatidate acyltransferase),  :doc:`../../../../../gene/AGAP002022` (Protein maelstrom),  :doc:`../../../../../gene/AGAP013079`.



The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002008`,  :doc:`../../../../../gene/AGAP002023`,  :doc:`../../../../../gene/AGAP002024`,  :doc:`../../../../../gene/AGAP002025` (OBP11 - odorant-binding protein 11),  :doc:`../../../../../gene/AGAP002026` (Ditrans,polycis-polyprenyl diphosphate synthase ((2E,6E)-farnesyl diphosphate specific)),  :doc:`../../../../../gene/AGAP002028` (E3 ubiquitin-protein ligase RNF13),  :doc:`../../../../../gene/AGAP002030` (bromodomain and WD repeat domain containing protein 1/3).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GAS/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GAS/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GAS/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 113
        # data points      = 635
        # variables        = 4
        chi-square         = 300.323
        reduced chi-square = 0.476
        Akaike info crit   = -467.468
        Bayesian info crit = -449.653
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.99285303 +/- 0.089953 (9.06%) (init= 3)
        sigma:       1.56883425 +/- 0.175104 (11.16%) (init= 0.5)
        skew:       -0.20047559 +/- 0.107214 (53.48%) (init= 0)
        baseline:    2.31709136 +/- 0.040571 (1.75%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.541 
        C(amplitude, sigma)          = -0.339 
        C(amplitude, baseline)       = -0.285 
        C(sigma, skew)               =  0.109 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 634
        # variables        = 1
        chi-square         = 357.188
        reduced chi-square = 0.564
        Akaike info crit   = -361.780
        Bayesian info crit = -357.328
    [[Variables]]
        c:   2.55064351 +/- 0.029832 (1.17%) (init= 1)



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


