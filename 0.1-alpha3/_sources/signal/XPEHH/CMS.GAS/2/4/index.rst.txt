:orphan:




XPEHH/CMS.GAS/2/4
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population
when compared with the :doc:`../../../../../population/GAS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **15,980,000** and
**16,140,000**.
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


The following 16 genes overlap the focal region: :doc:`../../../../../gene/AGAP002118` (zinc finger protein 622),  :doc:`../../../../../gene/AGAP002119` (dual-specificity tyrosine-(Y)-phosphorylation regulated kinase),  :doc:`../../../../../gene/AGAP002120` (RUN and TBC1 domain-containing protein 3),  :doc:`../../../../../gene/AGAP002121` (DNA-directed RNA polymerase II subunit RPB7),  :doc:`../../../../../gene/AGAP002122` (RpL32 - 60S ribosomal protein L32),  :doc:`../../../../../gene/AGAP002123` (Axn - axin),  :doc:`../../../../../gene/AGAP002124`,  :doc:`../../../../../gene/AGAP002125`:sup:`3` (Or34 - odorant receptor 34),  :doc:`../../../../../gene/AGAP002126`:sup:`3` (Or37 - odorant receptor 37),  :doc:`../../../../../gene/AGAP002127` (alpha-centractin),  :doc:`../../../../../gene/AGAP002128` (BRCA1-associated protein),  :doc:`../../../../../gene/AGAP002129` (deoxyhypusine monooxygenase),  :doc:`../../../../../gene/AGAP002130` (tubulin-specific chaperone A),  :doc:`../../../../../gene/AGAP002131`,  :doc:`../../../../../gene/AGAP002132` (YEATS domain-containing protein 1/3),  :doc:`../../../../../gene/AGAP002133` (tRNA modification GTPase).



Gene :doc:`../../../../../gene/AGAP002117` is within 50 kbp of the focal region.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 62
        # data points      = 505
        # variables        = 4
        chi-square         = 111.629
        reduced chi-square = 0.223
        Akaike info crit   = -754.237
        Bayesian info crit = -737.339
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.68920177 +/- 0.058090 (8.43%) (init= 3)
        sigma:       1.06905084 +/- 0.131726 (12.32%) (init= 0.5)
        skew:       -0.99999965 +/- 0.131113 (13.11%) (init= 0)
        baseline:    1.30253024 +/- 0.034057 (2.61%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.478 
        C(amplitude, baseline)       = -0.463 
        C(sigma, skew)               =  0.364 
        C(amplitude, sigma)          = -0.203 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 504
        # variables        = 1
        chi-square         = 142.391
        reduced chi-square = 0.283
        Akaike info crit   = -635.055
        Bayesian info crit = -630.832
    [[Variables]]
        c:   1.54669208 +/- 0.023699 (1.53%) (init= 1)



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


