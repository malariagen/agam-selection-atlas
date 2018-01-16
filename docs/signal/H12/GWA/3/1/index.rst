:orphan:




H12/GWA/3/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/GWA` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **49,480,000** and
**49,620,000**.
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


The following 12 genes overlap the focal region: :doc:`../../../../../gene/AGAP010147` (myosin heavy chain),  :doc:`../../../../../gene/AGAP010148`,  :doc:`../../../../../gene/AGAP010149` (cytochrome b5-related),  :doc:`../../../../../gene/AGAP010150`:sup:`1` (cytochrome b5-related),  :doc:`../../../../../gene/AGAP010151`,  :doc:`../../../../../gene/AGAP010152` (gem associated protein 5),  :doc:`../../../../../gene/AGAP010155`,  :doc:`../../../../../gene/AGAP013739`,  :doc:`../../../../../gene/AGAP010156` (ATP citrate lyase),  :doc:`../../../../../gene/AGAP013762`,  :doc:`../../../../../gene/AGAP010157` (Ast2 - allatostatin 2),  :doc:`../../../../../gene/AGAP010158`.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010145` (yellow),  :doc:`../../../../../gene/AGAP010146`.


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
    <img src="../../../../../_static/data/signal/H12/GWA/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GWA/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 473
        # variables        = 4
        chi-square         = 0.152
        reduced chi-square = 0.000
        Akaike info crit   = -3794.902
        Bayesian info crit = -3778.266
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.05697042 +/- 0.004509 (7.91%) (init= 0.5)
        sigma:       0.44493708 +/- 0.048596 (10.92%) (init= 0.5)
        skew:        0.99999999 +/- 0.017545 (1.75%) (init= 0)
        baseline:    0.04713326 +/- 0.000899 (1.91%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.482 
        C(amplitude, sigma)          = -0.450 
        C(sigma, baseline)           = -0.206 
        C(amplitude, baseline)       = -0.141 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 472
        # variables        = 1
        chi-square         = 0.215
        reduced chi-square = 0.000
        Akaike info crit   = -3629.080
        Bayesian info crit = -3624.923
    [[Variables]]
        c:   0.05102718 +/- 0.000984 (1.93%) (init= 0.03)



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


