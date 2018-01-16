:orphan:




H12/AOM/2/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **28,040,000** and
**28,080,000**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP002826`,  :doc:`../../../../../gene/AGAP002828`,  :doc:`../../../../../gene/AGAP002829` (SPN-E - ATP-dependent RNA helicase spindle-E),  :doc:`../../../../../gene/AGAP002830`:sup:`1` (C-1-tetrahydrofolate synthase, mitochondrial precursor).



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002824` (GPRTAK1 - putative tachykinin receptor 1),  :doc:`../../../../../gene/AGAP002825`:sup:`1` (PPO1 - prophenoloxidase 1),  :doc:`../../../../../gene/AGAP002831` (ribosomal RNA small subunit methyltransferase H),  :doc:`../../../../../gene/AGAP013130`,  :doc:`../../../../../gene/AGAP002832` (protein-tyrosine phosphatase).


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
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/2/1/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2R:27,980,000-28,280,000
      - 753
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/IHS/AOM/2/1/index`
      - IHS
      - Angola *An. coluzzii*
      - 2R:27,980,000-28,040,000
      - 324
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/2/3/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2R:28,000,000-28,060,000
      - 295
      - 99.4%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/2/5/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2R:27,980,000-28,040,000
      - 96
      - 95.2%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 57
        # data points      = 399
        # variables        = 4
        chi-square         = 0.278
        reduced chi-square = 0.001
        Akaike info crit   = -2892.383
        Bayesian info crit = -2876.428
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.47033668 +/- 0.019105 (4.06%) (init= 0.5)
        decay:       0.15000001 +/- 0.008766 (5.84%) (init= 0.5)
        skew:        0.56526965 +/- 0.061665 (10.91%) (init= 0)
        baseline:    0.03000975 +/- 0.001385 (4.62%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          =  0.681 
        C(decay, skew)               =  0.269 
        C(decay, baseline)           =  0.199 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 398
        # variables        = 1
        chi-square         = 0.920
        reduced chi-square = 0.002
        Akaike info crit   = -2413.961
        Bayesian info crit = -2409.975
    [[Variables]]
        c:   0.03837102 +/- 0.002412 (6.29%) (init= 0.03)



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


