:orphan:

H12 / Burkina Faso *An. gambiae* / Chromosome 3 / #6
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **18,600,001** and
**19,100,000**.
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




The following 10 genes overlap the focal region: :doc:`../../../../../gene/AGAP028559`,  :doc:`../../../../../gene/AGAP008823`,  :doc:`../../../../../gene/AGAP008824`,  :doc:`../../../../../gene/AGAP008825`,  :doc:`../../../../../gene/AGAP008826`,  :doc:`../../../../../gene/AGAP028025`,  :doc:`../../../../../gene/AGAP008827`,  :doc:`../../../../../gene/AGAP028123`,  :doc:`../../../../../gene/AGAP008828` (ATP-binding protein involved in chromosome partitioning),  :doc:`../../../../../gene/AGAP008829`.




The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008822` (FK506-binding protein 14),  :doc:`../../../../../gene/AGAP008830` (non-lysosomal glucosylceramidase),  :doc:`../../../../../gene/AGAP008831` (Stress-activated map kinase-interacting protein 1),  :doc:`../../../../../gene/AGAP008832` (cyclic AMP-dependent transcription factor ATF-6 alpha).


Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`../../../../../signal/H12/UGS/3/4/index`,"3R:18,700,001-18,820,000",195
    :doc:`../../../../../signal/H12/GNS/3/4/index`,"3R:18,980,001-19,020,000",88
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/6/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 55
        # data points      = 139
        # variables        = 3
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1569.507
        Bayesian info crit = -1560.704
    [[Variables]]
        amplitude:   0.01779537 +/- 0.002517 (14.15%) (init= 0.5)
        decay:       1.02930732 +/- 0.195671 (19.01%) (init= 0.5)
        c:           0.00789943 +/- 0.000503 (6.37%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.707 
        C(decay, c)                  = -0.686 
        C(amplitude, c)              =  0.183 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 149
        # variables        = 3
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -1628.209
        Bayesian info crit = -1619.197
    [[Variables]]
        amplitude:   0.02507563 +/- 0.005423 (21.63%) (init= 0.5)
        decay:       0.16372860 +/- 0.045421 (27.74%) (init= 0.5)
        c:           0.01171321 +/- 0.000364 (3.10%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.775 
        C(decay, c)                  = -0.234 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 138
        # variables        = 1
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1513.146
        Bayesian info crit = -1510.218
    [[Variables]]
        c:   0.00987886 +/- 0.000353 (3.57%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -1602.465
        Bayesian info crit = -1599.467
    [[Variables]]
        c:   0.01215001 +/- 0.000365 (3.00%) (init= 0.03)


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
