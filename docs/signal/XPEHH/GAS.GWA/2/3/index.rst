:orphan:




XPEHH/GAS.GWA/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **15,254,895** and
**15,554,895**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).





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


The following 34 genes overlap the focal region: :doc:`../../../../../gene/AGAP005411`,  :doc:`../../../../../gene/AGAP005412`,  :doc:`../../../../../gene/AGAP005413` (survival of motor neuron protein-interacting protein 1),  :doc:`../../../../../gene/AGAP005414` (misexpression suppressor of ras 6),  :doc:`../../../../../gene/AGAP005415` (FtsJ methyltransferase domain-containing protein 1),  :doc:`../../../../../gene/AGAP005416` (DEF4 - defensin anti-microbial peptide),  :doc:`../../../../../gene/AGAP005417` (protein singed wings 2),  :doc:`../../../../../gene/AGAP005418` (aminoacyl tRNA synthase complex-interacting multifunctional protein 2),  :doc:`../../../../../gene/AGAP005419`:sup:`1` (Adrenodoxin_red - NADPH:adrenodoxin oxidoreductase, mitochondrial),  :doc:`../../../../../gene/AGAP005420`,  :doc:`../../../../../gene/AGAP005421` (mitochondrial inner membrane protein OXA1L),  :doc:`../../../../../gene/AGAP005422`,  :doc:`../../../../../gene/AGAP005423` (Prosalpha4 - 26S proteasome alpha 4 subunit),  :doc:`../../../../../gene/AGAP005424`,  :doc:`../../../../../gene/AGAP013197`,  :doc:`../../../../../gene/AGAP005425` (actin-binding LIM protein),  :doc:`../../../../../gene/AGAP005427` (RpL28 - 60S ribosomal protein L28),  :doc:`../../../../../gene/AGAP005428` (transcription elongation factor SPT4 1),  :doc:`../../../../../gene/AGAP005429` (Thoc6 - THO complex subunit 6),  :doc:`../../../../../gene/AGAP005430`,  :doc:`../../../../../gene/AGAP005431` (thioredoxin domain-containing protein),  :doc:`../../../../../gene/AGAP005432` (programmed cell death protein 5),  :doc:`../../../../../gene/AGAP005433`,  :doc:`../../../../../gene/AGAP005434` (vitellogenic carboxypeptidase-like protein),  :doc:`../../../../../gene/AGAP028445`,  :doc:`../../../../../gene/AGAP005435`:sup:`1` (Iodotyrosine dehalogenase),  :doc:`../../../../../gene/AGAP005437`,  :doc:`../../../../../gene/AGAP005438` (ribosome biogenesis protein MAK21),  :doc:`../../../../../gene/AGAP005440`,  :doc:`../../../../../gene/AGAP005444`,  :doc:`../../../../../gene/AGAP005445` (Ras-related C3 botulinum toxin substrate),  :doc:`../../../../../gene/AGAP005446`,  :doc:`../../../../../gene/AGAP005447`:sup:`1` (trimethyllysine dioxygenase),  :doc:`../../../../../gene/AGAP005448` (B9 domain-containing protein 2).



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP005408`,  :doc:`../../../../../gene/AGAP005409`,  :doc:`../../../../../gene/AGAP005410` (peptide alpha-N-acetyltransferase),  :doc:`../../../../../gene/AGAP005449` (E3 ubiquitin-protein ligase CBL).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping selection signals
-----------------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. list-table::
    :widths: auto
    :header-rows: 1

    * - Signal
      - Statistic
      - Population
      - Focus
      - Peak model :math:`\Delta_{i}`
      - Max. percentile
      - Known locus
    * - :doc:`../../../../../signal/XPEHH/GAS.BFS/2/1/index`
      - XPEHH
      - Gabon *An. gambiae*
      - 2L:15,294,895-15,694,895
      - 380
      - 98.1%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.GWA/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.GWA/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.GWA/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 51
        # data points      = 400
        # variables        = 4
        chi-square         = 73.970
        reduced chi-square = 0.187
        Akaike info crit   = -667.121
        Bayesian info crit = -651.155
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.29576236 +/- 0.102105 (7.88%) (init= 3)
        decay:       2.99999997 +/- 0.017556 (0.59%) (init= 0.5)
        skew:       -0.35128180 +/- 0.086065 (24.50%) (init= 0)
        baseline:    1.23280731 +/- 0.112633 (9.14%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.911 
        C(amplitude, baseline)       = -0.829 
        C(amplitude, decay)          =  0.589 
        C(decay, skew)               =  0.124 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 399
        # variables        = 1
        chi-square         = 118.162
        reduced chi-square = 0.297
        Akaike info crit   = -483.543
        Bayesian info crit = -479.554
    [[Variables]]
        c:   1.86199786 +/- 0.027277 (1.46%) (init= 1)



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


