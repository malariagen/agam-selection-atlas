:orphan:




H12/AOM/X/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **4,340,000** and
**4,380,000**.
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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP000232` (regulator of G-protein signaling),  :doc:`../../../../../gene/AGAP000233`.



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000228` (netrin 1),  :doc:`../../../../../gene/AGAP000230`:sup:`3` (Or52 - odorant receptor 52),  :doc:`../../../../../gene/AGAP012975`:sup:`2` (histamine-gated chloride channel subunit),  :doc:`../../../../../gene/AGAP000234`,  :doc:`../../../../../gene/AGAP013530`,  :doc:`../../../../../gene/AGAP000235` (Thymosin).


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
    * - :doc:`../../../../../signal/XPEHH/AOM.GAS/X/1/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:4,340,000-4,420,000
      - 137
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 400
        # variables        = 4
        chi-square         = 0.045
        reduced chi-square = 0.000
        Akaike info crit   = -3628.803
        Bayesian info crit = -3612.837
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.20636852 +/- 0.007841 (3.80%) (init= 0.5)
        decay:       0.15000000 +/- 0.008258 (5.51%) (init= 0.5)
        skew:        0.37504932 +/- 0.055341 (14.76%) (init= 0)
        baseline:    0.02486613 +/- 0.000555 (2.23%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.695 
        C(decay, baseline)           = -0.198 
        C(decay, skew)               = -0.180 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 399
        # variables        = 1
        chi-square         = 0.164
        reduced chi-square = 0.000
        Akaike info crit   = -3108.961
        Bayesian info crit = -3104.972
    [[Variables]]
        c:   0.02836814 +/- 0.001016 (3.58%) (init= 0.03)



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


