:orphan:




XPEHH/BFS.UGS/2/4
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/UGS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **25,434,895** and
**25,474,895**.
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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP006029`,  :doc:`../../../../../gene/AGAP006030` (mfrn - mitoferrin),  :doc:`../../../../../gene/AGAP006031` (nuclear pore complex protein Nup54),  :doc:`../../../../../gene/AGAP006032`,  :doc:`../../../../../gene/AGAP006033`,  :doc:`../../../../../gene/AGAP006034`.



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006028`:sup:`2` (Rdl - GABA-gated chloride channel subunit),  :doc:`../../../../../gene/AGAP006035` (Ras-related protein Rab-36),  :doc:`../../../../../gene/AGAP006036` (axonemal dynein intermediate chain inner arm i1),  :doc:`../../../../../gene/AGAP006037` (RpL24 - 60S ribosomal protein L24),  :doc:`../../../../../gene/AGAP006038` (serine/arginine repetitive matrix protein 2).


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
    * - :doc:`../../../../../signal/XPEHH/BFM.GWA/2/2/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - 2L:25,474,895-25,514,895
      - 625
      - 99.4%
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
    * - :doc:`../../../../../signal/H12/BFS/2/5/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2L:25,454,895-25,534,895
      - 375
      - 96.1%
      - Rdl
    * - :doc:`../../../../../signal/IHS/BFM/2/3/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 2L:24,754,895-25,434,895
      - 304
      - 99.9%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/CMS.UGS/2/2/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 2L:25,414,895-25,454,895
      - 291
      - 90.3%
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
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.UGS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 59
        # data points      = 793
        # variables        = 4
        chi-square         = 69.301
        reduced chi-square = 0.088
        Akaike info crit   = -1924.826
        Bayesian info crit = -1906.123
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.93195232 +/- 0.155802 (5.31%) (init= 3)
        decay:       0.15000001 +/- 0.014567 (9.71%) (init= 0.5)
        skew:        0.16229811 +/- 0.087574 (53.96%) (init= 0)
        baseline:    0.94752560 +/- 0.010864 (1.15%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.665 
        C(decay, baseline)           = -0.179 
        C(decay, skew)               =  0.146 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 7
        # data points      = 792
        # variables        = 1
        chi-square         = 113.500
        reduced chi-square = 0.143
        Akaike info crit   = -1536.665
        Bayesian info crit = -1531.990
    [[Variables]]
        c:   0.99054599 +/- 0.013459 (1.36%) (init= 1)



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


