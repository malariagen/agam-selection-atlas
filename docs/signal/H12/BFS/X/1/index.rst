:orphan:




H12 / Burkina Faso *An. gambiae* / Chromosome X / #1
====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **15,120,001** and
**15,260,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP012997`,  :doc:`../../../../../gene/AGAP000818`:sup:`1` (CYP9K1 - cytochrome P450),  :doc:`../../../../../gene/AGAP000819` (nuclear receptor subfamily 2 group E member (Tailless)).




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013424`,  :doc:`../../../../../gene/AGAP000820`:sup:`4` (CPR125 - cuticular protein RR-2 family 125),  :doc:`../../../../../gene/AGAP000821`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have an focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/BFM/X/1/index`, "X:15,100,001-15,380,000", 954 (534 | 420)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 19
        # data points      = 146
        # variables        = 3
        chi-square         = 0.034
        reduced chi-square = 0.000
        Akaike info crit   = -1216.298
        Bayesian info crit = -1207.348
    [[Variables]]
        amplitude:   0.44556414 +/- 0.007692 (1.73%) (init= 0.5)
        decay:       0.65192407 +/- 0.018025 (2.76%) (init= 0.5)
        c:           0.01449774 +/- 0.001661 (11.46%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.525 
        C(amplitude, decay)          = -0.520 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 19
        # data points      = 146
        # variables        = 3
        chi-square         = 0.082
        reduced chi-square = 0.001
        Akaike info crit   = -1087.426
        Bayesian info crit = -1078.475
    [[Variables]]
        amplitude:   0.49155334 +/- 0.017368 (3.53%) (init= 0.5)
        decay:       0.45628987 +/- 0.022483 (4.93%) (init= 0.5)
        c:           0.05582530 +/- 0.002376 (4.26%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.710 
        C(decay, c)                  = -0.427 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 145
        # variables        = 1
        chi-square         = 0.984
        reduced chi-square = 0.007
        Akaike info crit   = -721.895
        Bayesian info crit = -718.918
    [[Variables]]
        c:   0.05387687 +/- 0.006866 (12.74%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 145
        # variables        = 1
        chi-square         = 0.839
        reduced chi-square = 0.006
        Akaike info crit   = -744.996
        Bayesian info crit = -742.019
    [[Variables]]
        c:   0.08695567 +/- 0.006340 (7.29%) (init= 0.03)


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


