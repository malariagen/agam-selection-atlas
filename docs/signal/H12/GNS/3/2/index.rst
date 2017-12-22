:orphan:

H12 / Guinea *An. gambiae* / Chromosome 3 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **4,580,001** and
**4,740,000**.
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



Gene :doc:`../../../../../gene/AGAP028427` overlaps the focal region.





The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008028` (voltage-dependent calcium channel beta, invertebrate),  :doc:`../../../../../gene/AGAP008033`,  :doc:`../../../../../gene/AGAP013760`,  :doc:`../../../../../gene/AGAP008034` (solute carrier family 39 (zinc transporter), member 7),  :doc:`../../../../../gene/AGAP008035`,  :doc:`../../../../../gene/AGAP008036`,  :doc:`../../../../../gene/AGAP008037` (KDEL (Lys-Asp-Glu-Leu) containing 1, isoform CRA_a).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/BFS/3/3/index`,"3R:4,580,001-4,760,000",167
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 151
        # variables        = 3
        chi-square         = 0.005
        reduced chi-square = 0.000
        Akaike info crit   = -1557.306
        Bayesian info crit = -1548.255
    [[Variables]]
        amplitude:   0.03225017 +/- 0.002244 (6.96%) (init= 0.5)
        decay:       0.95308210 +/- 0.127737 (13.40%) (init= 0.5)
        c:           0.02107194 +/- 0.000748 (3.55%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.662 
        C(amplitude, decay)          = -0.491 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 75
        # data points      = 150
        # variables        = 3
        chi-square         = 0.008
        reduced chi-square = 0.000
        Akaike info crit   = -1476.633
        Bayesian info crit = -1467.601
    [[Variables]]
        amplitude:   0.02719245 +/- 0.002824 (10.39%) (init= 0.5)
        decay:       1.12208621 +/- 0.236980 (21.12%) (init= 0.5)
        c:           0.02441456 +/- 0.001085 (4.44%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.729 
        C(amplitude, decay)          = -0.484 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.013
        reduced chi-square = 0.000
        Akaike info crit   = -1404.450
        Bayesian info crit = -1401.439
    [[Variables]]
        c:   0.02605272 +/- 0.000754 (2.89%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.013
        reduced chi-square = 0.000
        Akaike info crit   = -1393.695
        Bayesian info crit = -1390.691
    [[Variables]]
        c:   0.02915377 +/- 0.000760 (2.61%) (init= 0.03)


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
