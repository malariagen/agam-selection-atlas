:orphan:




IHS/CMS/2/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **34,254,895** and
**34,674,895**.
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


The following 29 genes overlap the focal region: :doc:`../../../../../gene/AGAP006579`,  :doc:`../../../../../gene/AGAP006580` (parkin),  :doc:`../../../../../gene/AGAP006581` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006582` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006583` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP028458`,  :doc:`../../../../../gene/AGAP006584` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP028459`,  :doc:`../../../../../gene/AGAP006585` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006586`,  :doc:`../../../../../gene/AGAP006587` (Cysteine-rich venom protein),  :doc:`../../../../../gene/AGAP006588`,  :doc:`../../../../../gene/AGAP028666`,  :doc:`../../../../../gene/AGAP028665`,  :doc:`../../../../../gene/AGAP006590` (T-lymphoma invasion and metastasis-inducing protein 1),  :doc:`../../../../../gene/AGAP006591`,  :doc:`../../../../../gene/AGAP006592`,  :doc:`../../../../../gene/AGAP006593` (dual specificity phosphatase),  :doc:`../../../../../gene/AGAP006594` (solute carrier family 17, member 5),  :doc:`../../../../../gene/AGAP006595` (solute carrier family 17 member 5),  :doc:`../../../../../gene/AGAP006596`,  :doc:`../../../../../gene/AGAP006597`:sup:`4` (CPR72 - cuticular protein RR-2 family 72),  :doc:`../../../../../gene/AGAP006598`,  :doc:`../../../../../gene/AGAP006599` (ATP-dependent RNA helicase A),  :doc:`../../../../../gene/AGAP006600`,  :doc:`../../../../../gene/AGAP006601`,  :doc:`../../../../../gene/AGAP006602`,  :doc:`../../../../../gene/AGAP006603`,  :doc:`../../../../../gene/AGAP006604` (U6 snRNA-associated Sm-like protein LSm5).



The following 11 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006573` (integrin-linked kinase),  :doc:`../../../../../gene/AGAP006574`,  :doc:`../../../../../gene/AGAP006575` (multifunctional methyltransferase subunit TRM112),  :doc:`../../../../../gene/AGAP006576`:sup:`1` (malate/L-lactate dehydrogenase),  :doc:`../../../../../gene/AGAP006577`,  :doc:`../../../../../gene/AGAP006578`,  :doc:`../../../../../gene/AGAP006605`,  :doc:`../../../../../gene/AGAP006606`,  :doc:`../../../../../gene/AGAP006607` (eIF3i - Eukaryotic translation initiation factor 3 subunit I),  :doc:`../../../../../gene/AGAP006608`,  :doc:`../../../../../gene/AGAP006609`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 516
        # variables        = 4
        chi-square         = 94.004
        reduced chi-square = 0.184
        Akaike info crit   = -870.628
        Bayesian info crit = -853.644
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.71788018 +/- 0.051966 (3.03%) (init= 3)
        sigma:       2.55830039 +/- 0.101293 (3.96%) (init= 0.5)
        skew:        0.93413080 +/- 0.038927 (4.17%) (init= 0)
        baseline:    1.77012715 +/- 0.036710 (2.07%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.622 
        C(sigma, baseline)           = -0.576 
        C(sigma, skew)               = -0.256 
        C(amplitude, skew)           = -0.161 
        C(skew, baseline)            =  0.146 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 515
        # variables        = 1
        chi-square         = 295.333
        reduced chi-square = 0.575
        Akaike info crit   = -284.372
        Bayesian info crit = -280.128
    [[Variables]]
        c:   2.54846505 +/- 0.033401 (1.31%) (init= 1)



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


