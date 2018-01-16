:orphan:




XPEHH/GWA.BFM/2/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` population
when compared with the :doc:`../../../../../population/BFM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **47,760,000** and
**47,800,000**.
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


Gene :doc:`../../../../../gene/AGAP004000` (myosin IX) overlaps the focal region.



The following 11 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003997` (casein kinase 1, gamma),  :doc:`../../../../../gene/AGAP003999`,  :doc:`../../../../../gene/AGAP004002` (60 kDa heat shock protein, mitochondrial precursor),  :doc:`../../../../../gene/AGAP013015` (p53 and DNA damage-regulated protein),  :doc:`../../../../../gene/AGAP004003`,  :doc:`../../../../../gene/AGAP004004`,  :doc:`../../../../../gene/AGAP004005`,  :doc:`../../../../../gene/AGAP013019`,  :doc:`../../../../../gene/AGAP004006`,  :doc:`../../../../../gene/AGAP004007`,  :doc:`../../../../../gene/AGAP004008`.


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
    * - :doc:`../../../../../signal/XPEHH/GWA.BFS/2/3/index`
      - XPEHH
      - Guinea Bissau
      - 2R:47,760,000-47,800,000
      - 167
      - 98.6%
      - nan
    * - :doc:`../../../../../signal/IHS/GWA/2/1/index`
      - IHS
      - Guinea Bissau
      - 2R:47,780,000-47,940,000
      - 117
      - 99.9%
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
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFM/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFM/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/GWA.BFM/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 249
        # variables        = 4
        chi-square         = 52.671
        reduced chi-square = 0.215
        Akaike info crit   = -378.792
        Bayesian info crit = -364.723
    [[Variables]]
        center:      0 (fixed)
        amplitude:   3.66812880 +/- 0.181246 (4.94%) (init= 3)
        decay:       0.28208406 +/- 0.025464 (9.03%) (init= 0.5)
        skew:       -0.68072724 +/- 0.092392 (13.57%) (init= 0)
        baseline:    1.84411420 +/- 0.034346 (1.86%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.596 
        C(decay, skew)               =  0.341 
        C(decay, baseline)           = -0.331 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 248
        # variables        = 1
        chi-square         = 181.822
        reduced chi-square = 0.736
        Akaike info crit   = -74.980
        Bayesian info crit = -71.466
    [[Variables]]
        c:   2.16657681 +/- 0.054481 (2.51%) (init= 1)



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


