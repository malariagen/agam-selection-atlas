:orphan:

H12 / Angola *An. coluzzii* / Chromosome X / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X** between positions **14,660,001** and
**14,720,000**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>



Gene :doc:`../../../../../gene/AGAP000801` (GLURIIb - ionotropic receptor GLURIIb) overlaps the focal region.





The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000798` (GLURIIc - ionotropic receptor GLURIIc),  :doc:`../../../../../gene/AGAP000803` (GLURIIa - ionotropic receptor GLURIIa),  :doc:`../../../../../gene/AGAP000804` (GPXH2 - glutathione peroxidase 2),  :doc:`../../../../../gene/AGAP000805` (BTB/POZ domain-containing protein KCTD16).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/GAS/X/1/index`,"X:14,480,001-14,720,000",94
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 200
        # variables        = 3
        chi-square         = 0.017
        reduced chi-square = 0.000
        Akaike info crit   = -1866.759
        Bayesian info crit = -1856.864
    [[Variables]]
        amplitude:   0.05884861 +/- 0.003577 (6.08%) (init= 0.5)
        decay:       1.00738723 +/- 0.108062 (10.73%) (init= 0.5)
        c:           0.02546942 +/- 0.000934 (3.67%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.576 
        C(amplitude, decay)          = -0.553 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 191
        # variables        = 3
        chi-square         = 0.084
        reduced chi-square = 0.000
        Akaike info crit   = -1469.975
        Bayesian info crit = -1460.218
    [[Variables]]
        amplitude:   0.07606479 +/- 0.010894 (14.32%) (init= 0.5)
        decay:       0.68355152 +/- 0.159877 (23.39%) (init= 0.5)
        c:           0.05089292 +/- 0.001875 (3.68%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.627 
        C(decay, c)                  = -0.464 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 199
        # variables        = 1
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -1661.964
        Bayesian info crit = -1658.671
    [[Variables]]
        c:   0.03268495 +/- 0.001086 (3.32%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 190
        # variables        = 1
        chi-square         = 0.111
        reduced chi-square = 0.001
        Akaike info crit   = -1411.949
        Bayesian info crit = -1408.702
    [[Variables]]
        c:   0.05619005 +/- 0.001761 (3.13%) (init= 0.03)


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
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
