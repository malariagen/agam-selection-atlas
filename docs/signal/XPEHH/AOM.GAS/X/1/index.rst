:orphan:




XPEHH/AOM.GAS/X/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/GAS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**X** between positions **4,340,000** and
**4,420,000**.
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


The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP000232` (regulator of G-protein signaling),  :doc:`../../../../../gene/AGAP000233`,  :doc:`../../../../../gene/AGAP000234`,  :doc:`../../../../../gene/AGAP013530`,  :doc:`../../../../../gene/AGAP000235` (Thymosin).



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000228` (netrin 1),  :doc:`../../../../../gene/AGAP000230`:sup:`3` (Or52 - odorant receptor 52),  :doc:`../../../../../gene/AGAP012975`:sup:`2` (histamine-gated chloride channel subunit),  :doc:`../../../../../gene/AGAP000236` (3',5'-cyclic-nucleotide phosphodiesterase),  :doc:`../../../../../gene/AGAP000237` (cAMP response element-binding protein (CREB)).


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
    * - :doc:`../../../../../signal/H12/AOM/X/1/index`
      - H12
      - Angola *An. coluzzii*
      - X:4,340,000-4,380,000
      - 519
      - 97.8%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/X/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:4,320,000-4,360,000
      - 292
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/X/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:4,340,000-4,380,000
      - 242
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/IHS/AOM/X/1/index`
      - IHS
      - Angola *An. coluzzii*
      - X:4,280,000-4,360,000
      - 178
      - 99.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GAS/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GAS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GAS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 229
        # variables        = 4
        chi-square         = 39.761
        reduced chi-square = 0.177
        Akaike info crit   = -392.942
        Bayesian info crit = -379.207
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.73039694 +/- 0.209598 (7.68%) (init= 3)
        sigma:       0.15196857 +/- 0.013782 (9.07%) (init= 0.5)
        skew:        0.19614771 +/- 0.108566 (55.35%) (init= 0)
        baseline:    1.55915182 +/- 0.028909 (1.85%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.526 
        C(sigma, baseline)           = -0.164 
        C(sigma, skew)               = -0.134 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 228
        # variables        = 1
        chi-square         = 73.816
        reduced chi-square = 0.325
        Akaike info crit   = -255.131
        Bayesian info crit = -251.702
    [[Variables]]
        c:   1.64597310 +/- 0.037765 (2.29%) (init= 1)



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


