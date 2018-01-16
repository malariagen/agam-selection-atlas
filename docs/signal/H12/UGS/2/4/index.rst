:orphan:




H12/UGS/2/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **51,020,000** and
**51,120,000**.
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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP004167`,  :doc:`../../../../../gene/AGAP004169`.



The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004162` (myosin, light polypeptide 9, regulatory),  :doc:`../../../../../gene/AGAP004163`:sup:`1` (GSTD7 - glutathione S-transferase delta class 7),  :doc:`../../../../../gene/AGAP004164`:sup:`1` (GSTD1-4 - glutathione S-transferase delta class 1),  :doc:`../../../../../gene/AGAP004165`:sup:`1` (GSTD2 - glutathione S-transferase delta class 2),  :doc:`../../../../../gene/AGAP004166`.


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
    * - :doc:`../../../../../signal/XPEHH/UGS.GWA/2/3/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2R:50,960,000-51,100,000
      - 225
      - 90.2%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 390
        # variables        = 4
        chi-square         = 0.127
        reduced chi-square = 0.000
        Akaike info crit   = -3123.708
        Bayesian info crit = -3107.843
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.03200985 +/- 0.002601 (8.13%) (init= 0.5)
        sigma:       2.07031739 +/- 0.231140 (11.16%) (init= 0.5)
        skew:        0.11051085 +/- 0.099992 (90.48%) (init= 0)
        baseline:    0.05402677 +/- 0.001656 (3.07%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.654 
        C(amplitude, baseline)       = -0.455 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 389
        # variables        = 1
        chi-square         = 0.170
        reduced chi-square = 0.000
        Akaike info crit   = -3006.533
        Bayesian info crit = -3002.570
    [[Variables]]
        c:   0.06433156 +/- 0.001062 (1.65%) (init= 0.03)



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


