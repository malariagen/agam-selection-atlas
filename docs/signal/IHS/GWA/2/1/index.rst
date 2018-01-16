:orphan:




IHS/GWA/2/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **47,780,000** and
**47,940,000**.
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


The following 24 genes overlap the focal region: :doc:`../../../../../gene/AGAP004002` (60 kDa heat shock protein, mitochondrial precursor),  :doc:`../../../../../gene/AGAP013015` (p53 and DNA damage-regulated protein),  :doc:`../../../../../gene/AGAP004003`,  :doc:`../../../../../gene/AGAP004004`,  :doc:`../../../../../gene/AGAP004005`,  :doc:`../../../../../gene/AGAP013019`,  :doc:`../../../../../gene/AGAP004006`,  :doc:`../../../../../gene/AGAP004007`,  :doc:`../../../../../gene/AGAP004008`,  :doc:`../../../../../gene/AGAP004011` (survival motor neuron protein),  :doc:`../../../../../gene/AGAP004012` (katanin p60 ATPase-containing subunit),  :doc:`../../../../../gene/AGAP004013`:sup:`1` (SP11838),  :doc:`../../../../../gene/AGAP004014`:sup:`1` (SP11706),  :doc:`../../../../../gene/AGAP004015`:sup:`1` (SP21408),  :doc:`../../../../../gene/AGAP013186`,  :doc:`../../../../../gene/AGAP004017`,  :doc:`../../../../../gene/AGAP004016`,  :doc:`../../../../../gene/AGAP004018`,  :doc:`../../../../../gene/AGAP004020` (alpha-mannosidase II),  :doc:`../../../../../gene/AGAP004021`:sup:`2` (IR40a - ionotropic receptor IR40a),  :doc:`../../../../../gene/AGAP004022`,  :doc:`../../../../../gene/AGAP004023` (APG4A - autophagy related gene),  :doc:`../../../../../gene/AGAP004028` (intron-binding protein aquarius),  :doc:`../../../../../gene/AGAP004025` (GPRMTH5 - methuselah receptor 5).



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003997` (casein kinase 1, gamma),  :doc:`../../../../../gene/AGAP004000` (myosin IX),  :doc:`../../../../../gene/AGAP004026` (GPRMTH6 - methuselah receptor 6),  :doc:`../../../../../gene/AGAP004029` (DNA excision repair protein ERCC-1),  :doc:`../../../../../gene/AGAP004030` (dynein light intermediate chain, axonemal),  :doc:`../../../../../gene/AGAP004031`:sup:`1` (mitochondrial electron transfer flavoprotein subunit alpha).


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
    * - :doc:`../../../../../signal/H12/GWA/2/2/index`
      - H12
      - Guinea Bissau
      - 2R:47,740,000-47,800,000
      - 380
      - 98.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GWA.BFM/2/2/index`
      - XPEHH
      - Guinea Bissau
      - 2R:47,760,000-47,800,000
      - 303
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GWA.BFS/2/3/index`
      - XPEHH
      - Guinea Bissau
      - 2R:47,760,000-47,800,000
      - 167
      - 98.6%
      - nan
    * - :doc:`../../../../../signal/XPEHH/GWA.UGS/2/2/index`
      - XPEHH
      - Guinea Bissau
      - 2R:47,740,000-47,800,000
      - 113
      - 95.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GWA/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GWA/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/GWA/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 73
        # data points      = 627
        # variables        = 4
        chi-square         = 125.249
        reduced chi-square = 0.201
        Akaike info crit   = -1001.871
        Bayesian info crit = -984.107
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.53392061 +/- 0.146643 (9.56%) (init= 3)
        sigma:       0.23358693 +/- 0.026595 (11.39%) (init= 0.5)
        skew:       -0.69812739 +/- 0.135442 (19.40%) (init= 0)
        baseline:    2.62652769 +/- 0.018580 (0.71%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.529 
        C(sigma, skew)               =  0.214 
        C(sigma, baseline)           = -0.157 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 626
        # variables        = 1
        chi-square         = 151.868
        reduced chi-square = 0.243
        Akaike info crit   = -884.628
        Bayesian info crit = -880.189
    [[Variables]]
        c:   2.67141259 +/- 0.019701 (0.74%) (init= 1)



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


