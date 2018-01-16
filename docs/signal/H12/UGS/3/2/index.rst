:orphan:




H12/UGS/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **49,660,000** and
**49,880,000**.
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


The following 12 genes overlap the focal region: :doc:`../../../../../gene/AGAP010159` (dUTP pyrophosphatase),  :doc:`../../../../../gene/AGAP010160` (myosin I),  :doc:`../../../../../gene/AGAP010161`,  :doc:`../../../../../gene/AGAP010162`,  :doc:`../../../../../gene/AGAP010163` (RpL38 - 60S ribosomal protein L38),  :doc:`../../../../../gene/AGAP010164` (whd - protein withered, carnitine O-palmitoyltransferase),  :doc:`../../../../../gene/AGAP010165` (dynein light intermediate chain 2, cytosolic),  :doc:`../../../../../gene/AGAP010166`,  :doc:`../../../../../gene/AGAP010167` (numb),  :doc:`../../../../../gene/AGAP010168`,  :doc:`../../../../../gene/AGAP010169`:sup:`2`,  :doc:`../../../../../gene/AGAP028032`:sup:`2`.



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010158`,  :doc:`../../../../../gene/AGAP010170`,  :doc:`../../../../../gene/AGAP010171` (papi - TUDOR-domain protein),  :doc:`../../../../../gene/AGAP013768`,  :doc:`../../../../../gene/AGAP010172` (protein phosphatase 2 (formerly 2A), catalytic subunit),  :doc:`../../../../../gene/AGAP010173` (Rack1 - guanine nucleotide-binding protein subunit beta-like protein),  :doc:`../../../../../gene/AGAP010174` (oligosaccharyltransferase complex subunit alpha (ribophorin I)),  :doc:`../../../../../gene/AGAP010175` (adenylyl cyclase-associated protein 1),  :doc:`../../../../../gene/AGAP010176`.


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
    * - :doc:`../../../../../signal/XPEHH/UGS.BFS/3/5/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 3R:49,540,000-49,660,000
      - 93
      - 98.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 473
        # variables        = 4
        chi-square         = 0.078
        reduced chi-square = 0.000
        Akaike info crit   = -4109.529
        Bayesian info crit = -4092.893
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.05891882 +/- 0.002324 (3.94%) (init= 0.5)
        decay:       2.83391207 +/- 0.293192 (10.35%) (init= 0.5)
        skew:        0.63596717 +/- 0.062567 (9.84%) (init= 0)
        baseline:    0.02968130 +/- 0.001665 (5.61%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.842 
        C(skew, baseline)            =  0.395 
        C(amplitude, baseline)       = -0.346 
        C(decay, skew)               = -0.337 
        C(amplitude, skew)           = -0.270 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 472
        # variables        = 1
        chi-square         = 0.192
        reduced chi-square = 0.000
        Akaike info crit   = -3682.247
        Bayesian info crit = -3678.090
    [[Variables]]
        c:   0.04678610 +/- 0.000930 (1.99%) (init= 0.03)



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


