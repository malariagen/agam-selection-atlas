:orphan:




IHS/GAS/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3L** between positions **10,399,316** and
**10,559,316**.
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


The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP010790` (dynein heavy chain 2, cytosolic),  :doc:`../../../../../gene/AGAP010791` (polyribonucleotide nucleotidyltransferase),  :doc:`../../../../../gene/AGAP010792` (NADH dehydrogenase (ubiquinone) 1 alpha subcomplex 9),  :doc:`../../../../../gene/AGAP010793` (synembryn-A),  :doc:`../../../../../gene/AGAP010794`,  :doc:`../../../../../gene/AGAP010795`,  :doc:`../../../../../gene/AGAP010796`,  :doc:`../../../../../gene/AGAP010797`,  :doc:`../../../../../gene/AGAP010798` (female reproductive tract protease),  :doc:`../../../../../gene/AGAP029080`.



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010786`,  :doc:`../../../../../gene/AGAP010787` (timeless),  :doc:`../../../../../gene/AGAP010788` (fatty acyl-CoA reductase 1),  :doc:`../../../../../gene/AGAP010789`,  :doc:`../../../../../gene/AGAP010799`,  :doc:`../../../../../gene/AGAP010800` (nuclear protein NHN1),  :doc:`../../../../../gene/AGAP010801` (phosphatidylinositol 4-kinase),  :doc:`../../../../../gene/AGAP010802`,  :doc:`../../../../../gene/AGAP010803`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GAS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GAS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GAS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 265
        # variables        = 4
        chi-square         = 49.356
        reduced chi-square = 0.189
        Akaike info crit   = -437.375
        Bayesian info crit = -423.056
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.95268047 +/- 0.094017 (9.87%) (init= 3)
        sigma:       3          +/- 0.000148 (0.00%) (init= 0.5)
        skew:       -0.35550336 +/- 0.108373 (30.48%) (init= 0)
        baseline:    2.45610149 +/- 0.085933 (3.50%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           =  0.793 
        C(amplitude, baseline)       = -0.746 
        C(sigma, skew)               = -0.466 
        C(amplitude, sigma)          = -0.410 
        C(amplitude, skew)           =  0.176 
        C(skew, baseline)            = -0.143 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 264
        # variables        = 1
        chi-square         = 70.965
        reduced chi-square = 0.270
        Akaike info crit   = -344.835
        Bayesian info crit = -341.259
    [[Variables]]
        c:   2.88731293 +/- 0.031969 (1.11%) (init= 1)



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


