:orphan:




XPEHH/BFM.BFS/2/6
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **43,434,895** and
**43,514,895**.
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


Gene :doc:`../../../../../gene/AGAP007136` (GPR5HT1A - putative serotonin 5HT-1a receptor) overlaps the focal region.



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007137`,  :doc:`../../../../../gene/AGAP007138` (Wurst),  :doc:`../../../../../gene/AGAP007139` (Ser/Thr protein phosphatase/nucleotidase),  :doc:`../../../../../gene/AGAP007140` (Ser/Thr protein phosphatase/nucleotidase),  :doc:`../../../../../gene/AGAP007141` (Serine-type enodpeptidase),  :doc:`../../../../../gene/AGAP007142` (Serine-type enodpeptidase).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/6/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 50
        # data points      = 850
        # variables        = 4
        chi-square         = 134.822
        reduced chi-square = 0.159
        Akaike info crit   = -1557.086
        Bayesian info crit = -1538.105
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.09598093 +/- 0.096479 (8.80%) (init= 3)
        sigma:       0.15000012 +/- 0.016592 (11.06%) (init= 0.5)
        skew:        0.72066609 +/- 0.145206 (20.15%) (init= 0)
        baseline:    1.21877242 +/- 0.014323 (1.18%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          =  0.504 
        C(sigma, skew)               =  0.483 
        C(sigma, baseline)           =  0.148 
        C(amplitude, baseline)       = -0.110 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 849
        # variables        = 1
        chi-square         = 157.816
        reduced chi-square = 0.186
        Akaike info crit   = -1426.552
        Bayesian info crit = -1421.808
    [[Variables]]
        c:   1.26250732 +/- 0.014805 (1.17%) (init= 1)



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


