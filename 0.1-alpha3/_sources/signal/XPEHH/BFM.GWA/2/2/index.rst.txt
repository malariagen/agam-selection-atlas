:orphan:




XPEHH/BFM.GWA/2/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **25,474,895** and
**25,514,895**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).




This signal occurs within 50 kbp of the :doc:`../../../../../known-locus/rdl`,
a genome region with prior evidence of an association with insecticide resistance and/or recent positive
selection in *Anopheles* mosquitoes.


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


Gene :doc:`../../../../../gene/AGAP006035` (Ras-related protein Rab-36) overlaps the focal region.



The following 14 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006028`:sup:`2` (Rdl - GABA-gated chloride channel subunit),  :doc:`../../../../../gene/AGAP006029`,  :doc:`../../../../../gene/AGAP006030` (mfrn - mitoferrin),  :doc:`../../../../../gene/AGAP006031` (nuclear pore complex protein Nup54),  :doc:`../../../../../gene/AGAP006032`,  :doc:`../../../../../gene/AGAP006033`,  :doc:`../../../../../gene/AGAP006034`,  :doc:`../../../../../gene/AGAP006036` (axonemal dynein intermediate chain inner arm i1),  :doc:`../../../../../gene/AGAP006037` (RpL24 - 60S ribosomal protein L24),  :doc:`../../../../../gene/AGAP006038` (serine/arginine repetitive matrix protein 2),  :doc:`../../../../../gene/AGAP006039`,  :doc:`../../../../../gene/AGAP006040` (peroxisomal membrane protein 2),  :doc:`../../../../../gene/AGAP006041` (E3 ubiquitin-protein ligase RNF5),  :doc:`../../../../../gene/AGAP006042`.


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
    * - :doc:`../../../../../signal/H12/BFM/2/2/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 2L:25,434,895-25,494,895
      - 1,172
      - 98.4%
      - Rdl
    * - :doc:`../../../../../signal/H12/GAS/2/1/index`
      - H12
      - Gabon *An. gambiae*
      - 2L:25,454,895-25,514,895
      - 529
      - 100.0%
      - Rdl
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
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/2/4/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2L:25,434,895-25,474,895
      - 388
      - 98.3%
      - Rdl
    * - :doc:`../../../../../signal/H12/BFS/2/5/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2L:25,454,895-25,534,895
      - 375
      - 96.1%
      - Rdl
    * - :doc:`../../../../../signal/IHS/BFS/2/5/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 2L:25,434,895-25,614,895
      - 256
      - 99.8%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/2/6/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2L:25,434,895-25,474,895
      - 138
      - 95.3%
      - Rdl
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.GWA/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.GWA/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.GWA/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 405
        # variables        = 4
        chi-square         = 62.639
        reduced chi-square = 0.156
        Akaike info crit   = -747.935
        Bayesian info crit = -731.919
    [[Variables]]
        center:      0 (fixed)
        amplitude:   5.51702474 +/- 0.169988 (3.08%) (init= 3)
        decay:       0.29634725 +/- 0.014757 (4.98%) (init= 0.5)
        skew:        0.66242393 +/- 0.052663 (7.95%) (init= 0)
        baseline:    2.37027100 +/- 0.021599 (0.91%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.604 
        C(decay, baseline)           = -0.298 
        C(decay, skew)               = -0.241 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 404
        # variables        = 1
        chi-square         = 296.697
        reduced chi-square = 0.736
        Akaike info crit   = -122.716
        Bayesian info crit = -118.715
    [[Variables]]
        c:   2.60140764 +/- 0.042688 (1.64%) (init= 1)



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


