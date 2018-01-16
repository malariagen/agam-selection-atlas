:orphan:




XPEHH/GWA.UGS/2/4
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/UGS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **46,594,895** and
**46,654,895**.
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


The following 14 genes overlap the focal region: :doc:`../../../../../gene/AGAP007439`,  :doc:`../../../../../gene/AGAP007440` (DNA topoisomerase 2-associated protein PAT1),  :doc:`../../../../../gene/AGAP007442`,  :doc:`../../../../../gene/AGAP007443`,  :doc:`../../../../../gene/AGAP007445`,  :doc:`../../../../../gene/AGAP007446`,  :doc:`../../../../../gene/AGAP007450` (hairy and enhancer of split related with YRPW motif),  :doc:`../../../../../gene/AGAP007451`,  :doc:`../../../../../gene/AGAP007452` (neuronal guanine nucleotide exchange factor),  :doc:`../../../../../gene/AGAP007453` (LRIM9 - leucine-rich immune protein (Short)),  :doc:`../../../../../gene/AGAP007454` (LRIM8A - leucine-rich immune protein (Short)),  :doc:`../../../../../gene/AGAP007455` (LRIM10 - leucine-rich immune protein (Short)),  :doc:`../../../../../gene/AGAP007456` (LRIM8B - leucine-rich immune protein (Short)),  :doc:`../../../../../gene/AGAP007457` (LRIM7 - leucine-rich immune protein (Short)).



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007420`:sup:`1` (peptidylglycine monooxygenase),  :doc:`../../../../../gene/AGAP007421` (Similar to mandelate racemase/muconate lactonizing protein),  :doc:`../../../../../gene/AGAP007422`,  :doc:`../../../../../gene/AGAP007423` (chromosome transmission fidelity protein 4),  :doc:`../../../../../gene/AGAP007458`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.UGS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 64
        # data points      = 970
        # variables        = 4
        chi-square         = 59.471
        reduced chi-square = 0.062
        Akaike info crit   = -2700.056
        Bayesian info crit = -2680.547
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.61322625 +/- 0.063154 (10.30%) (init= 3)
        sigma:       0.15371765 +/- 0.020766 (13.51%) (init= 0.5)
        skew:       -0.93512925 +/- 0.164695 (17.61%) (init= 0)
        baseline:    1.14363285 +/- 0.008266 (0.72%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.479 
        C(sigma, skew)               =  0.435 
        C(sigma, baseline)           = -0.143 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 969
        # variables        = 1
        chi-square         = 65.682
        reduced chi-square = 0.068
        Akaike info crit   = -2606.003
        Bayesian info crit = -2601.127
    [[Variables]]
        c:   1.16276141 +/- 0.008368 (0.72%) (init= 1)



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


