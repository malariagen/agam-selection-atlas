:orphan:




H12/BFM/X/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **15,100,000** and
**15,300,000**.
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




The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP012997`,  :doc:`../../../../../gene/AGAP000818`:sup:`1` (CYP9K1 - cytochrome P450),  :doc:`../../../../../gene/AGAP000819` (nuclear receptor subfamily 2 group E member (Tailless)),  :doc:`../../../../../gene/AGAP000820`:sup:`4` (CPR125 - cuticular protein RR-2 family 125).




The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013173`,  :doc:`../../../../../gene/AGAP013424`,  :doc:`../../../../../gene/AGAP000821`,  :doc:`../../../../../gene/AGAP000822`,  :doc:`../../../../../gene/AGAP000823` (CD81 antigen),  :doc:`../../../../../gene/AGAP000824` (bone morphogenetic protein 5),  :doc:`../../../../../gene/AGAP000825`,  :doc:`../../../../../gene/AGAP000826` (cap-specific mRNA (nucleoside-2'-O-)-methyltransferase 1).


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
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/X/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - X:15,060,000-15,220,000
      - 866
      - 99.6%
    * - :doc:`../../../../../signal/H12/BFS/X/1/index`
      - H12
      - Burkina Faso *An. gambiae*
      - X:15,100,000-15,240,000
      - 815
      - 98.5%
    * - :doc:`../../../../../signal/H12/GNS/X/1/index`
      - H12
      - Guinea *An. gambiae*
      - X:14,960,000-15,160,000
      - 419
      - 97.8%
    * - :doc:`../../../../../signal/H12/UGS/X/1/index`
      - H12
      - Uganda *An. gambiae*
      - X:15,160,000-15,480,000
      - 348
      - 94.9%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 390
        # variables        = 4
        chi-square         = 0.632
        reduced chi-square = 0.002
        Akaike info crit   = -2497.987
        Bayesian info crit = -2482.122
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.84016747 +/- 0.009655 (1.15%) (init= 0.5)
        sigma:       0.69281907 +/- 0.009071 (1.31%) (init= 0.5)
        skew:       -0.34433495 +/- 0.014997 (4.36%) (init= 0)
        baseline:    0.05407297 +/- 0.002331 (4.31%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.471 
        C(sigma, baseline)           = -0.302 
        C(sigma, skew)               =  0.178 
        C(amplitude, baseline)       = -0.168 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 389
        # variables        = 1
        chi-square         = 16.379
        reduced chi-square = 0.042
        Akaike info crit   = -1230.190
        Bayesian info crit = -1226.226
    [[Variables]]
        c:   0.13726598 +/- 0.010415 (7.59%) (init= 0.03)



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


