:orphan:




IHS/BFS/2/6
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **46,034,895** and
**46,214,895**.
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


The following 26 genes overlap the focal region: :doc:`../../../../../gene/AGAP007358` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP007359`,  :doc:`../../../../../gene/AGAP007361` (translocation protein SEC63),  :doc:`../../../../../gene/AGAP007362` (SH3 domain-binding glutamic acid-rich-like protein 3),  :doc:`../../../../../gene/AGAP007363`,  :doc:`../../../../../gene/AGAP007364`,  :doc:`../../../../../gene/AGAP007365`,  :doc:`../../../../../gene/AGAP007366`,  :doc:`../../../../../gene/AGAP007367` (solute carrier family 6 (neurotransmitter transporter, dopamine) member 3),  :doc:`../../../../../gene/AGAP007368`,  :doc:`../../../../../gene/AGAP007369` (Ras-related protein Rap-1b precursor),  :doc:`../../../../../gene/AGAP007370`,  :doc:`../../../../../gene/AGAP007371`,  :doc:`../../../../../gene/AGAP007372`,  :doc:`../../../../../gene/AGAP007373` (Tetraspanin),  :doc:`../../../../../gene/AGAP007374` (glucuronosyltransferase),  :doc:`../../../../../gene/AGAP007375`,  :doc:`../../../../../gene/AGAP013291` (Trafficking protein particle complex 3),  :doc:`../../../../../gene/AGAP007376` (nuclear transcription factor Y, alpha),  :doc:`../../../../../gene/AGAP007377`,  :doc:`../../../../../gene/AGAP007378` (N-acetyltransferase 9),  :doc:`../../../../../gene/AGAP013544`:sup:`1` (L-gulonate 3-dehydrogenase),  :doc:`../../../../../gene/AGAP007379` (ArfGAP with dual PH domains 2),  :doc:`../../../../../gene/AGAP007380` (NADH dehydrogenase (ubiquinone) 1 beta subcomplex 11),  :doc:`../../../../../gene/AGAP007381`,  :doc:`../../../../../gene/AGAP007382` (Fem-1 homolog b).



The following 13 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007348` (coiled-coil domain-containing protein 102A),  :doc:`../../../../../gene/AGAP007349`,  :doc:`../../../../../gene/AGAP007353` (phosphatidylinositol transfer protein SEC14),  :doc:`../../../../../gene/AGAP007354` (phosphatidylinositol transfer protein SEC14),  :doc:`../../../../../gene/AGAP007355` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP007356` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP007357` (retinaldehyde-binding protein 1-like protein 1),  :doc:`../../../../../gene/AGAP007383`,  :doc:`../../../../../gene/AGAP007384`,  :doc:`../../../../../gene/AGAP007385` (LYSC4 - C-type lysozyme),  :doc:`../../../../../gene/AGAP007386` (LYSC7 - C-type lysozyme),  :doc:`../../../../../gene/AGAP007387` (DNA methyltransferase 1-associated protein 1),  :doc:`../../../../../gene/AGAP007388` (midasin).


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
    * - :doc:`../../../../../signal/IHS/CMS/2/7/index`
      - IHS
      - Cameroon *An. gambiae*
      - 2L:46,054,895-46,094,895
      - 98
      - 77.4%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/6/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFS/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 646
        # variables        = 4
        chi-square         = 128.543
        reduced chi-square = 0.200
        Akaike info crit   = -1034.990
        Bayesian info crit = -1017.107
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.71009409 +/- 0.130024 (7.60%) (init= 3)
        decay:       0.45634361 +/- 0.055327 (12.12%) (init= 0.5)
        skew:        0.44358587 +/- 0.115898 (26.13%) (init= 0)
        baseline:    1.78814605 +/- 0.020610 (1.15%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.640 
        C(decay, baseline)           = -0.383 
        C(decay, skew)               = -0.172 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 645
        # variables        = 1
        chi-square         = 182.161
        reduced chi-square = 0.283
        Akaike info crit   = -813.512
        Bayesian info crit = -809.043
    [[Variables]]
        c:   1.90660454 +/- 0.020941 (1.10%) (init= 1)



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


