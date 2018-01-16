:orphan:




XPEHH/GAS.BFS/2/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **25,614,895** and
**25,894,895**.
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


The following 15 genes overlap the focal region: :doc:`../../../../../gene/AGAP006045` (protein yorkie),  :doc:`../../../../../gene/AGAP006046` (Med23 - mediator of RNA polymerase II transcription subunit 23),  :doc:`../../../../../gene/AGAP006047`:sup:`1` (CYP4J9 - cytochrome P450),  :doc:`../../../../../gene/AGAP006048`:sup:`1` (CYP4J5 - cytochrome P450),  :doc:`../../../../../gene/AGAP006049`:sup:`1` (CYP4J10 - cytochrome P450),  :doc:`../../../../../gene/AGAP006050` (AarF domain containing kinase 5),  :doc:`../../../../../gene/AGAP006051` (pentatricopeptide repeat domain 1),  :doc:`../../../../../gene/AGAP006052` (protein phosphatase 1, regulatory (inhibitor) subunit 3),  :doc:`../../../../../gene/AGAP006053`,  :doc:`../../../../../gene/AGAP006054`,  :doc:`../../../../../gene/AGAP006055` (NF-kappa-B inhibitor-like protein 2),  :doc:`../../../../../gene/AGAP006056`,  :doc:`../../../../../gene/AGAP006057` (multiple coagulation factor deficiency 2),  :doc:`../../../../../gene/AGAP006058` (heparan sulfate 2-o-sulfotransferase),  :doc:`../../../../../gene/AGAP006059`.



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006042`,  :doc:`../../../../../gene/AGAP029130`,  :doc:`../../../../../gene/AGAP029102`,  :doc:`../../../../../gene/AGAP006060`,  :doc:`../../../../../gene/AGAP006061`,  :doc:`../../../../../gene/AGAP006062`.


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
      - Peak Model :math:`\Delta_{i}`
      - Max Percentile
      - Known Loci
    * - :doc:`../../../../../signal/XPEHH/GAS.GWA/2/1/index`
      - XPEHH
      - Gabon *An. gambiae*
      - 2L:25,474,895-25,634,895
      - 423
      - 100.0%
      - Rdl
    * - :doc:`../../../../../signal/H12/GNS/2/4/index`
      - H12
      - Guinea *An. gambiae*
      - 2L:25,534,895-25,814,895
      - 332
      - 97.8%
      - nan
    * - :doc:`../../../../../signal/IHS/BFS/2/5/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 2L:25,434,895-25,614,895
      - 256
      - 99.8%
      - Rdl
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GAS.BFS/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 85
        # data points      = 336
        # variables        = 4
        chi-square         = 86.495
        reduced chi-square = 0.261
        Akaike info crit   = -447.961
        Bayesian info crit = -432.693
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.38799462 +/- 0.116245 (4.87%) (init= 3)
        decay:       1.04439260 +/- 0.113503 (10.87%) (init= 0.5)
        skew:        0.99999998 +/- 0.045031 (4.50%) (init= 0)
        baseline:    1.68971839 +/- 0.058294 (3.45%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.723 
        C(decay, skew)               =  0.319 
        C(amplitude, decay)          = -0.318 
        C(amplitude, baseline)       = -0.173 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 335
        # variables        = 1
        chi-square         = 204.530
        reduced chi-square = 0.612
        Akaike info crit   = -163.295
        Bayesian info crit = -159.480
    [[Variables]]
        c:   2.25546530 +/- 0.042754 (1.90%) (init= 1)



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


