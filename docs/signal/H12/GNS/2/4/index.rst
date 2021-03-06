:orphan:




H12/GNS/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **25,534,895** and
**25,814,895**.
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


The following 21 genes overlap the focal region: :doc:`../../../../../gene/AGAP006038` (serine/arginine repetitive matrix protein 2),  :doc:`../../../../../gene/AGAP006040` (peroxisomal membrane protein 2),  :doc:`../../../../../gene/AGAP006041` (E3 ubiquitin-protein ligase RNF5),  :doc:`../../../../../gene/AGAP006042`,  :doc:`../../../../../gene/AGAP029130`,  :doc:`../../../../../gene/AGAP029102`,  :doc:`../../../../../gene/AGAP006045` (protein yorkie),  :doc:`../../../../../gene/AGAP006046` (Med23 - mediator of RNA polymerase II transcription subunit 23),  :doc:`../../../../../gene/AGAP006047`:sup:`1` (CYP4J9 - cytochrome P450),  :doc:`../../../../../gene/AGAP006048`:sup:`1` (CYP4J5 - cytochrome P450),  :doc:`../../../../../gene/AGAP006049`:sup:`1` (CYP4J10 - cytochrome P450),  :doc:`../../../../../gene/AGAP006050` (AarF domain containing kinase 5),  :doc:`../../../../../gene/AGAP006051` (pentatricopeptide repeat domain 1),  :doc:`../../../../../gene/AGAP006052` (protein phosphatase 1, regulatory (inhibitor) subunit 3),  :doc:`../../../../../gene/AGAP006053`,  :doc:`../../../../../gene/AGAP006054`,  :doc:`../../../../../gene/AGAP006055` (NF-kappa-B inhibitor-like protein 2),  :doc:`../../../../../gene/AGAP006056`,  :doc:`../../../../../gene/AGAP006057` (multiple coagulation factor deficiency 2),  :doc:`../../../../../gene/AGAP006058` (heparan sulfate 2-o-sulfotransferase),  :doc:`../../../../../gene/AGAP006059`.



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006035` (Ras-related protein Rab-36),  :doc:`../../../../../gene/AGAP006036` (axonemal dynein intermediate chain inner arm i1),  :doc:`../../../../../gene/AGAP006037` (RpL24 - 60S ribosomal protein L24),  :doc:`../../../../../gene/AGAP006039`.


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
    * - :doc:`../../../../../signal/XPEHH/BFM.BFS/2/1/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - 2L:25,454,895-25,554,895
      - 468
      - 99.3%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/GAS.GWA/2/1/index`
      - XPEHH
      - Gabon *An. gambiae*
      - 2L:25,474,895-25,634,895
      - 423
      - 100.0%
      - Rdl
    * - :doc:`../../../../../signal/H12/BFS/2/5/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2L:25,454,895-25,534,895
      - 375
      - 96.1%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/GAS.BFS/2/2/index`
      - XPEHH
      - Gabon *An. gambiae*
      - 2L:25,614,895-25,894,895
      - 284
      - 99.9%
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
    <img src="../../../../../_static/data/signal/H12/GNS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 400
        # variables        = 4
        chi-square         = 0.335
        reduced chi-square = 0.001
        Akaike info crit   = -2826.355
        Bayesian info crit = -2810.389
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.16175841 +/- 0.008569 (5.30%) (init= 0.5)
        decay:       0.91354877 +/- 0.081832 (8.96%) (init= 0.5)
        skew:       -0.18634269 +/- 0.077054 (41.35%) (init= 0)
        baseline:    0.05805465 +/- 0.001975 (3.40%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.590 
        C(decay, baseline)           = -0.543 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 399
        # variables        = 1
        chi-square         = 0.765
        reduced chi-square = 0.002
        Akaike info crit   = -2494.266
        Bayesian info crit = -2490.277
    [[Variables]]
        c:   0.07621936 +/- 0.002195 (2.88%) (init= 0.03)



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


