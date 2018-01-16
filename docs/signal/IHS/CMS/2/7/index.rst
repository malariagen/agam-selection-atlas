:orphan:




IHS/CMS/2/7
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **46,054,895** and
**46,094,895**.
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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP007361` (translocation protein SEC63),  :doc:`../../../../../gene/AGAP007362` (SH3 domain-binding glutamic acid-rich-like protein 3),  :doc:`../../../../../gene/AGAP007363`,  :doc:`../../../../../gene/AGAP007364`,  :doc:`../../../../../gene/AGAP007365`,  :doc:`../../../../../gene/AGAP007366`.



The following 14 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007353` (phosphatidylinositol transfer protein SEC14),  :doc:`../../../../../gene/AGAP007354` (phosphatidylinositol transfer protein SEC14),  :doc:`../../../../../gene/AGAP007355` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP007356` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP007357` (retinaldehyde-binding protein 1-like protein 1),  :doc:`../../../../../gene/AGAP007358` (cellular retinaldehyde binding protein),  :doc:`../../../../../gene/AGAP007359`,  :doc:`../../../../../gene/AGAP007367` (solute carrier family 6 (neurotransmitter transporter, dopamine) member 3),  :doc:`../../../../../gene/AGAP007368`,  :doc:`../../../../../gene/AGAP007369` (Ras-related protein Rap-1b precursor),  :doc:`../../../../../gene/AGAP007370`,  :doc:`../../../../../gene/AGAP007371`,  :doc:`../../../../../gene/AGAP007372`,  :doc:`../../../../../gene/AGAP007373` (Tetraspanin).


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
    * - :doc:`../../../../../signal/IHS/BFS/2/6/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 2L:46,034,895-46,214,895
      - 221
      - 96.2%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/7/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/7/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/2/7/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 70
        # data points      = 661
        # variables        = 4
        chi-square         = 49.013
        reduced chi-square = 0.075
        Akaike info crit   = -1711.707
        Bayesian info crit = -1693.732
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.12085747 +/- 0.139081 (12.41%) (init= 3)
        decay:       0.15000040 +/- 0.013910 (9.27%) (init= 0.5)
        skew:        0.50836283 +/- 0.182545 (35.91%) (init= 0)
        baseline:    1.60522644 +/- 0.011168 (0.70%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.690 
        C(decay, baseline)           =  0.220 
        C(decay, skew)               =  0.146 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 660
        # variables        = 1
        chi-square         = 57.114
        reduced chi-square = 0.087
        Akaike info crit   = -1613.145
        Bayesian info crit = -1608.652
    [[Variables]]
        c:   1.63033405 +/- 0.011459 (0.70%) (init= 1)



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


