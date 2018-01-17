:orphan:




H12/AOM/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **58,660,000** and
**59,200,000**.
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


The following 20 genes overlap the focal region: :doc:`../../../../../gene/AGAP004630` (Erg28-domain containing protein),  :doc:`../../../../../gene/AGAP004631`,  :doc:`../../../../../gene/AGAP004632` (DEF2 - defensin anti-microbial peptide),  :doc:`../../../../../gene/AGAP004633` (sodium-independent sulfate anion transporter),  :doc:`../../../../../gene/AGAP004634`,  :doc:`../../../../../gene/AGAP004635` (sodium-independent sulfate anion transporter),  :doc:`../../../../../gene/AGAP013218` (sodium-independent sulfate anion transporter),  :doc:`../../../../../gene/AGAP004636` (sodium-independent sulfate anion transporter),  :doc:`../../../../../gene/AGAP004637` (transcriptional activator cubitus interruptus),  :doc:`../../../../../gene/AGAP013117`,  :doc:`../../../../../gene/AGAP004638`,  :doc:`../../../../../gene/AGAP004639`,  :doc:`../../../../../gene/AGAP004640`,  :doc:`../../../../../gene/AGAP013302`,  :doc:`../../../../../gene/AGAP004641` (ATP synthase mitochondrial F1 complex assembly factor 1),  :doc:`../../../../../gene/AGAP004642` (NPF - Neuropeptide F),  :doc:`../../../../../gene/AGAP013063` (Synaptic vesicle protein),  :doc:`../../../../../gene/AGAP004643` (SCRB6 - Class B Scavenger Receptor (CD36 domain).),  :doc:`../../../../../gene/AGAP004644`,  :doc:`../../../../../gene/AGAP004645` (juvenile hormone diol kinase).



The following 12 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004619`,  :doc:`../../../../../gene/AGAP004620` (Envelysin),  :doc:`../../../../../gene/AGAP004621`,  :doc:`../../../../../gene/AGAP004622`:sup:`1` (glutamate dehydrogenase (NAD(P) )),  :doc:`../../../../../gene/AGAP004623` (anaphase-promoting complex subunit 6),  :doc:`../../../../../gene/AGAP004624`,  :doc:`../../../../../gene/AGAP004625` (cortactin),  :doc:`../../../../../gene/AGAP004626`,  :doc:`../../../../../gene/AGAP004627`,  :doc:`../../../../../gene/AGAP004628` (scaffold protein salvador),  :doc:`../../../../../gene/AGAP004629`,  :doc:`../../../../../gene/AGAP004646` (homeobox protein HoxA/B/C/D4).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 72
        # data points      = 564
        # variables        = 4
        chi-square         = 3.051
        reduced chi-square = 0.005
        Akaike info crit   = -2935.818
        Bayesian info crit = -2918.478
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.21263410 +/- 0.010066 (4.73%) (init= 0.5)
        sigma:       2.99999788 +/- 0.201409 (6.71%) (init= 0.5)
        skew:       -0.43426841 +/- 0.052185 (12.02%) (init= 0)
        baseline:    0.08373883 +/- 0.009670 (11.55%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.831 
        C(sigma, baseline)           = -0.785 
        C(amplitude, sigma)          =  0.472 
        C(sigma, skew)               =  0.257 
        C(amplitude, skew)           =  0.209 
        C(skew, baseline)            = -0.171 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 563
        # variables        = 1
        chi-square         = 6.152
        reduced chi-square = 0.011
        Akaike info crit   = -2540.760
        Bayesian info crit = -2536.427
    [[Variables]]
        c:   0.20629218 +/- 0.004409 (2.14%) (init= 0.03)



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


