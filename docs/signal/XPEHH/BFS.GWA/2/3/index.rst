:orphan:




XPEHH/BFS.GWA/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **28,420,000** and
**28,500,000**.
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




The following 9 genes overlap the focal region: :doc:`../../../../../gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`../../../../../gene/AGAP002862`:sup:`1` (CYP6AA1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013128`:sup:`1` (CYP6AA2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002863`:sup:`1` (COEAE6O - carboxylesterase alpha esterase),  :doc:`../../../../../gene/AGAP002864`:sup:`1` (CYP6P15P - cytochrome P450),  :doc:`../../../../../gene/AGAP002865`:sup:`1` (CYP6P3 - cytochrome P450),  :doc:`../../../../../gene/AGAP002866`:sup:`1` (CYP6P5 - cytochrome P450),  :doc:`../../../../../gene/AGAP002867`:sup:`1` (CYP6P4 - cytochrome P450),  :doc:`../../../../../gene/AGAP002868`:sup:`1` (CYP6P1 - cytochrome P450).




The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002858` (Sodium/potassium-transporting ATPase subunit alpha),  :doc:`../../../../../gene/AGAP002869`:sup:`1` (CYP6P2 - cytochrome P450),  :doc:`../../../../../gene/AGAP002870`:sup:`1` (CYP6AD1 - cytochrome P450),  :doc:`../../../../../gene/AGAP013202`,  :doc:`../../../../../gene/AGAP000586`,  :doc:`../../../../../gene/AGAP002872` (lipase),  :doc:`../../../../../gene/AGAP002873`,  :doc:`../../../../../gene/AGAP013069`,  :doc:`../../../../../gene/AGAP002874`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

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
    * - :doc:`../../../../../signal/H12/UGS/2/1/index`
      - H12
      - Uganda *An. gambiae*
      - 2R:28,460,000-28,500,000
      - 1,567
      - 99.2%
    * - :doc:`../../../../../signal/H12/CMS/2/1/index`
      - H12
      - Cameroon *An. gambiae*
      - 2R:28,460,000-28,560,000
      - 1,124
      - 100.0%
    * - :doc:`../../../../../signal/H12/GNS/2/2/index`
      - H12
      - Guinea *An. gambiae*
      - 2R:28,420,000-28,460,000
      - 1,073
      - 98.5%
    * - :doc:`../../../../../signal/H12/BFS/2/2/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2R:28,440,000-28,480,000
      - 976
      - 98.4%
    * - :doc:`../../../../../signal/H12/BFM/2/4/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 2R:28,420,000-28,520,000
      - 366
      - 98.5%
    * - :doc:`../../../../../signal/H12/AOM/2/6/index`
      - H12
      - Angola *An. coluzzii*
      - 2R:28,440,000-28,480,000
      - 235
      - 97.8%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.GWA/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 317
        # variables        = 4
        chi-square         = 49.445
        reduced chi-square = 0.158
        Akaike info crit   = -581.002
        Bayesian info crit = -565.966
    [[Variables]]
        center:      0 (fixed)
        amplitude:   4.61124488 +/- 0.106044 (2.30%) (init= 3)
        sigma:       0.24513600 +/- 0.007188 (2.93%) (init= 0.5)
        skew:       -0.11919071 +/- 0.032780 (27.50%) (init= 0)
        baseline:    1.41122948 +/- 0.024466 (1.73%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.556 
        C(amplitude, baseline)       = -0.198 
        C(sigma, baseline)           = -0.186 
        C(sigma, skew)               =  0.112 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 316
        # variables        = 1
        chi-square         = 453.874
        reduced chi-square = 1.441
        Akaike info crit   = 116.416
        Bayesian info crit = 120.172
    [[Variables]]
        c:   1.86022957 +/- 0.067525 (3.63%) (init= 1)



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


