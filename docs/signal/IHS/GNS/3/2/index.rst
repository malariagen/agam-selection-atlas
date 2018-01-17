:orphan:




IHS/GNS/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **4,400,000** and
**4,960,000**.
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


The following 37 genes overlap the focal region: :doc:`../../../../../gene/AGAP008025` (Homeobox protein engrailed-like),  :doc:`../../../../../gene/AGAP013728`,  :doc:`../../../../../gene/AGAP008026` (enhancer of polycomb-like protein),  :doc:`../../../../../gene/AGAP008027` (Slowmo),  :doc:`../../../../../gene/AGAP008028` (voltage-dependent calcium channel beta, invertebrate),  :doc:`../../../../../gene/AGAP028427`,  :doc:`../../../../../gene/AGAP008033`,  :doc:`../../../../../gene/AGAP013760`,  :doc:`../../../../../gene/AGAP008034` (solute carrier family 39 (zinc transporter), member 7),  :doc:`../../../../../gene/AGAP008035`,  :doc:`../../../../../gene/AGAP008036`,  :doc:`../../../../../gene/AGAP008037` (KDEL (Lys-Asp-Glu-Leu) containing 1, isoform CRA_a),  :doc:`../../../../../gene/AGAP008039` (protein kinase A),  :doc:`../../../../../gene/AGAP008040`,  :doc:`../../../../../gene/AGAP008041` (RING finger protein 121),  :doc:`../../../../../gene/AGAP008042`:sup:`1` (pyridine nucleotide-disulfide oxidoreductase domain 1),  :doc:`../../../../../gene/AGAP008043` (mRpS18B - 28S ribosomal protein S18B, mitochondrial),  :doc:`../../../../../gene/AGAP008044`:sup:`1` (programmed cell death 8 (apoptosis-inducing factor)),  :doc:`../../../../../gene/AGAP008045` (transcription initiation factor TFIID subunit 13),  :doc:`../../../../../gene/AGAP013736`,  :doc:`../../../../../gene/AGAP008046` (protein kinase C and casein kinase substrate in neurons 2 protein),  :doc:`../../../../../gene/AGAP013713`,  :doc:`../../../../../gene/AGAP008047` (integrator complex subunit 1),  :doc:`../../../../../gene/AGAP008048`,  :doc:`../../../../../gene/AGAP008049` (cell division cycle 123 homolog),  :doc:`../../../../../gene/AGAP008050` (phosphorylated adapter RNA export protein),  :doc:`../../../../../gene/AGAP008051` (SAP1 - sensory appendage protein 1),  :doc:`../../../../../gene/AGAP008052` (SAP2 - sensory appendage protein 2),  :doc:`../../../../../gene/AGAP008053` (sphingomyelin phosphodiesterase 2),  :doc:`../../../../../gene/AGAP008054` (SAP3 - sensory appendage protein 3),  :doc:`../../../../../gene/AGAP008055` (CSP3 - chemosensory protein 3),  :doc:`../../../../../gene/AGAP008056`,  :doc:`../../../../../gene/AGAP029127` (CSP5 - chemosensory protein 5),  :doc:`../../../../../gene/AGAP008059` (CSP1 - chemosensory protein 1),  :doc:`../../../../../gene/AGAP008060` (IDGF2 - imaginal disc growth factor 2),  :doc:`../../../../../gene/AGAP008061` (IDGF4 - imaginal disc growth factor 4),  :doc:`../../../../../gene/AGAP008062` (CSP4 - chemosensory protein 4).



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008023` (en - segmentation polarity homeobox protein engrailed),  :doc:`../../../../../gene/AGAP008063` (exosome complex component CSL4),  :doc:`../../../../../gene/AGAP008064` (uroporphyrinogen-III synthase),  :doc:`../../../../../gene/AGAP008065`,  :doc:`../../../../../gene/AGAP013757`.


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
    * - :doc:`../../../../../signal/IHS/BFS/3/2/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3R:4,340,000-4,740,000
      - 504
      - 95.7%
      - nan
    * - :doc:`../../../../../signal/H12/GNS/3/2/index`
      - H12
      - Guinea *An. gambiae*
      - 3R:4,600,000-5,060,000
      - 253
      - 77.2%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GNS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 664
        # variables        = 4
        chi-square         = 121.595
        reduced chi-square = 0.184
        Akaike info crit   = -1119.195
        Bayesian info crit = -1101.202
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.04845614 +/- 0.085612 (4.18%) (init= 3)
        decay:       1.04495854 +/- 0.080020 (7.66%) (init= 0.5)
        skew:       -0.75061850 +/- 0.067250 (8.96%) (init= 0)
        baseline:    1.83033325 +/- 0.024743 (1.35%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.573 
        C(amplitude, decay)          = -0.521 
        C(decay, skew)               =  0.281 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 663
        # variables        = 1
        chi-square         = 262.949
        reduced chi-square = 0.397
        Akaike info crit   = -611.151
        Bayesian info crit = -606.655
    [[Variables]]
        c:   2.14156683 +/- 0.024476 (1.14%) (init= 1)



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


