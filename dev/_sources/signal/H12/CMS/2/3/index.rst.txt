:orphan:




H12 / Cameroon *An. gambiae* / Chromosome 2 / #3
================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,600,001** and
**40,980,000**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 27 genes overlap the focal region: :doc:`../../../../../gene/AGAP003623` (long-chain acyl-CoA synthetase),  :doc:`../../../../../gene/AGAP003624`,  :doc:`../../../../../gene/AGAP029110`,  :doc:`../../../../../gene/AGAP003626`,  :doc:`../../../../../gene/AGAP013221`,  :doc:`../../../../../gene/AGAP012946`,  :doc:`../../../../../gene/AGAP003627`,  :doc:`../../../../../gene/AGAP003629`,  :doc:`../../../../../gene/AGAP003630`,  :doc:`../../../../../gene/AGAP003631` (GPRGRP2 - putative gastrin/bombesin receptor 2),  :doc:`../../../../../gene/AGAP003632` (U3 small nucleolar RNA-associated protein 14),  :doc:`../../../../../gene/AGAP003633`,  :doc:`../../../../../gene/AGAP003635`,  :doc:`../../../../../gene/AGAP003636`:sup:`1` (inositol oxygenase),  :doc:`../../../../../gene/AGAP003638`,  :doc:`../../../../../gene/AGAP003639` (Prolylcarboxypeptidase),  :doc:`../../../../../gene/AGAP003640`:sup:`1` (SP8905),  :doc:`../../../../../gene/AGAP003641`:sup:`1` (SP8907),  :doc:`../../../../../gene/AGAP003642`:sup:`1` (SP8898),  :doc:`../../../../../gene/AGAP003643` (ubiquitin carboxyl-terminal hydrolase 34),  :doc:`../../../../../gene/AGAP003644` (mRpS11 - 28S ribosomal protein S11, mitochondrial),  :doc:`../../../../../gene/AGAP003645` (kelch-like protein 19),  :doc:`../../../../../gene/AGAP013307`,  :doc:`../../../../../gene/AGAP003646`,  :doc:`../../../../../gene/AGAP003647`,  :doc:`../../../../../gene/AGAP003648` (DNA-directed RNA polymerase II subunit RPB2),  :doc:`../../../../../gene/AGAP003649`.




The following 10 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP029083`,  :doc:`../../../../../gene/AGAP003615` (toll-interacting protein),  :doc:`../../../../../gene/AGAP003616`,  :doc:`../../../../../gene/AGAP003618` (serine/threonine-protein kinase LATS1/2),  :doc:`../../../../../gene/AGAP003619` (transcription elongation factor SPT6),  :doc:`../../../../../gene/AGAP003620`,  :doc:`../../../../../gene/AGAP003621` (coiled-coil domain-containing protein 25),  :doc:`../../../../../gene/AGAP003622` (Queuine tRNA-ribosyltransferase catalytic subunit 1),  :doc:`../../../../../gene/AGAP003650` (translation initiation factor eIF-2B subunit alpha),  :doc:`../../../../../gene/AGAP003651` (Tyrosine-protein kinase Fes/Fps).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have an focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/BFM/2/4/index`, "2R:40,880,001-40,980,000", 400 (185 | 214)
    :doc:`../../../../../signal/H12/BFS/2/6/index`, "2R:40,820,001-41,000,000", 359 (249 | 109)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 150
        # variables        = 3
        chi-square         = 0.027
        reduced chi-square = 0.000
        Akaike info crit   = -1285.215
        Bayesian info crit = -1276.183
    [[Variables]]
        amplitude:   0.09174235 +/- 0.004350 (4.74%) (init= 0.5)
        decay:       1.99999998 +/- 0.291781 (14.59%) (init= 0.5)
        c:           0.01941933 +/- 0.004175 (21.50%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.906 
        C(amplitude, c)              = -0.466 
        C(amplitude, decay)          =  0.155 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 45
        # data points      = 147
        # variables        = 3
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1181.198
        Bayesian info crit = -1172.227
    [[Variables]]
        amplitude:   0.05634944 +/- 0.005782 (10.26%) (init= 0.5)
        decay:       1.99999849 +/- 0.641559 (32.08%) (init= 0.5)
        c:           0.05197010 +/- 0.005541 (10.66%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.907 
        C(amplitude, c)              = -0.422 
        C(amplitude, decay)          =  0.107 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.098
        reduced chi-square = 0.001
        Akaike info crit   = -1089.847
        Bayesian info crit = -1086.843
    [[Variables]]
        c:   0.04796618 +/- 0.002106 (4.39%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 146
        # variables        = 1
        chi-square         = 0.074
        reduced chi-square = 0.001
        Akaike info crit   = -1106.733
        Bayesian info crit = -1103.750
    [[Variables]]
        c:   0.06940894 +/- 0.001863 (2.68%) (init= 0.03)


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


