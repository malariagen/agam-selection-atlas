:orphan:

H12 / Gabon *An. gambiae* / Chromosome X / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X** between positions **18,520,001** and
**18,560,000**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).

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




The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP000963`,  :doc:`../../../../../gene/AGAP000964`,  :doc:`../../../../../gene/AGAP000965` (ELAV (embryonic lethal, abnormal vision Drosophila)-like),  :doc:`../../../../../gene/AGAP000966` (beta1 - nicotinic acetylcholine receptor beta 1).




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000967` (estrogen receptor binding site associated antigen 9 variant 1),  :doc:`../../../../../gene/AGAP000968`,  :doc:`../../../../../gene/AGAP000969` (tropomodulin).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/AOM/X/3/index`,"X:18,420,001-18,800,000",115
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 257
        # data points      = 148
        # variables        = 3
        chi-square         = 0.173
        reduced chi-square = 0.001
        Akaike info crit   = -993.659
        Bayesian info crit = -984.668
    [[Variables]]
        amplitude:   0.07222388 +/- 0.010958 (15.17%) (init= 0.5)
        decay:       1.62876977 +/- 0.674864 (41.43%) (init= 0.5)
        c:           0.05999999 +/- 0.006128 (10.21%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.853 
        C(amplitude, c)              =  0.240 
        C(amplitude, decay)          = -0.151 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 41
        # data points      = 243
        # variables        = 3
        chi-square         = 0.106
        reduced chi-square = 0.000
        Akaike info crit   = -1873.495
        Bayesian info crit = -1863.016
    [[Variables]]
        amplitude:   0.05384873 +/- 0.006580 (12.22%) (init= 0.5)
        decay:       2          +/- 1.58e-05 (0.00%) (init= 0.5)
        c:           0.02748427 +/- 0.007149 (26.01%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.954 
        C(amplitude, c)              = -0.447 
        C(amplitude, decay)          = -0.231 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 147
        # variables        = 1
        chi-square         = 0.208
        reduced chi-square = 0.001
        Akaike info crit   = -962.346
        Bayesian info crit = -959.355
    [[Variables]]
        c:   0.08017805 +/- 0.003113 (3.88%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 242
        # variables        = 1
        chi-square         = 0.130
        reduced chi-square = 0.001
        Akaike info crit   = -1819.407
        Bayesian info crit = -1815.918
    [[Variables]]
        c:   0.04109765 +/- 0.001494 (3.64%) (init= 0.03)


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
