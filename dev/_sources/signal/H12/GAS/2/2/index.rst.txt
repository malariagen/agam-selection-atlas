:orphan:

H12 / Gabon *An. gambiae* / Chromosome 2 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **2,600,001** and
**2,640,000**.
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




The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP004715` (Pyruvate dehydrogenase phosphatase regulatory subunit, mitochondrial),  :doc:`../../../../../gene/AGAP004716` (Gr57 - gustatory receptor 57).




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004713`,  :doc:`../../../../../gene/AGAP004714`,  :doc:`../../../../../gene/AGAP004717`,  :doc:`../../../../../gene/AGAP004718`.


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/BFM/2/1/index`,"2L:2,520,001-2,900,000",1399
    :doc:`../../../../../signal/H12/BFS/2/1/index`,"2L:2,420,001-2,720,000",1365
    :doc:`../../../../../signal/H12/GNS/2/1/index`,"2L:1,760,001-2,700,000",1256
    :doc:`../../../../../signal/H12/UGS/2/2/index`,"2L:2,520,001-3,120,000",982
    :doc:`../../../../../signal/H12/CMS/2/2/index`,"2L:2,420,001-2,920,000",566
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 74
        # data points      = 284
        # variables        = 3
        chi-square         = 0.251
        reduced chi-square = 0.001
        Akaike info crit   = -1990.661
        Bayesian info crit = -1979.714
    [[Variables]]
        amplitude:   0.20891149 +/- 0.013626 (6.52%) (init= 0.5)
        decay:       0.17281169 +/- 0.017814 (10.31%) (init= 0.5)
        c:           0.05941395 +/- 0.002023 (3.41%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.630 
        C(decay, c)                  = -0.353 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 172
        # variables        = 3
        chi-square         = 0.412
        reduced chi-square = 0.002
        Akaike info crit   = -1032.073
        Bayesian info crit = -1022.631
    [[Variables]]
        amplitude:   0.12068563 +/- 0.013853 (11.48%) (init= 0.5)
        decay:       1.99999952 +/- 0.712570 (35.63%) (init= 0.5)
        c:           0.05999999 +/- 0.013504 (22.51%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.905 
        C(amplitude, c)              = -0.584 
        C(amplitude, decay)          =  0.309 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 283
        # variables        = 1
        chi-square         = 0.545
        reduced chi-square = 0.002
        Akaike info crit   = -1767.301
        Bayesian info crit = -1763.655
    [[Variables]]
        c:   0.07132321 +/- 0.002613 (3.66%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 171
        # variables        = 1
        chi-square         = 0.546
        reduced chi-square = 0.003
        Akaike info crit   = -980.589
        Bayesian info crit = -977.447
    [[Variables]]
        c:   0.09940401 +/- 0.004335 (4.36%) (init= 0.03)


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
