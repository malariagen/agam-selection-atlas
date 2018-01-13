:orphan:




XPEHH (versus GWA) / Burkina Faso *An. gambiae* / Chromosome X / #1
===================================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**X** between positions **15,060,000** and
**15,220,000**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP013424`,  :doc:`../../../../../gene/AGAP012997`.




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013474`,  :doc:`../../../../../gene/AGAP013173`,  :doc:`../../../../../gene/AGAP000818`:sup:`1` (CYP9K1 - cytochrome P450),  :doc:`../../../../../gene/AGAP000819` (nuclear receptor subfamily 2 group E member (Tailless)).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Peak Model Fit (:math:`\Delta_{i}`)

    :doc:`../../../../../signal/H12/BFS/X/1/index`, "X:15,100,000-15,240,000", 815
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS/X/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 328
        # variables        = 4
        chi-square         = 69.975
        reduced chi-square = 0.216
        Akaike info crit   = -498.721
        Bayesian info crit = -483.549
    [[Variables]]
        center:      0 (fixed)
        amplitude:   7.32335607 +/- 0.137024 (1.87%) (init= 3)
        sigma:       0.53309185 +/- 0.009638 (1.81%) (init= 0.5)
        skew:        0.00617080 +/- 0.018153 (294.19%) (init= 0)
        baseline:    1.32519043 +/- 0.030086 (2.27%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.605 
        C(sigma, baseline)           = -0.317 
        C(sigma, skew)               = -0.260 
        C(amplitude, baseline)       = -0.127 
        C(amplitude, skew)           =  0.124 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 327
        # variables        = 1
        chi-square         = 1000.103
        reduced chi-square = 3.068
        Akaike info crit   = 367.553
        Bayesian info crit = 371.343
    [[Variables]]
        c:   2.12240358 +/- 0.096858 (4.56%) (init= 1)



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


