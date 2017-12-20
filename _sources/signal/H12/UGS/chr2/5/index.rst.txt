:orphan:

Uganda *An. gambiae* | H12 | Chromosome 2 | Signal #5
================================================================================



This page describes a signal of selection found in the
:doc:`/population/UGS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **50,420,001** and
**50,820,000**.




The following 36 genes overlap the focal region: :doc:`/gene/AGAP004126` (Osi3 - osiris 3),  :doc:`/gene/AGAP004127` (Osi4 - osiris 4),  :doc:`/gene/AGAP004128` (Osi8 - osiris 8),  :doc:`/gene/AGAP004129` (Osi6 - osiris 6),  :doc:`/gene/AGAP004130` (Osi7 - osiris 7),  :doc:`/gene/AGAP004131` (Osi9 - osiris 9),  :doc:`/gene/AGAP004132` (Osi10 - protein osiris 10),  :doc:`/gene/AGAP004133`,  :doc:`/gene/AGAP004134` (Osi11 - osiris 11),  :doc:`/gene/AGAP013195` (Osi12 - osiris 12),  :doc:`/gene/AGAP004135` (Yellow-e),  :doc:`/gene/AGAP004136`,  :doc:`/gene/AGAP012972`,  :doc:`/gene/AGAP004137`,  :doc:`/gene/AGAP004138`,  :doc:`/gene/AGAP013023`,  :doc:`/gene/AGAP004139`,  :doc:`/gene/AGAP004140` (disp - protein dispatched (segment polarity protein)),  :doc:`/gene/AGAP013524`,  :doc:`/gene/AGAP004141`,  :doc:`/gene/AGAP004142` (aspartate aminotransferase, cytoplasmic),  :doc:`/gene/AGAP004143`,  :doc:`/gene/AGAP013209`,  :doc:`/gene/AGAP004144`,  :doc:`/gene/AGAP004145` (RNA-binding protein PNO1),  :doc:`/gene/AGAP012989`,  :doc:`/gene/AGAP004146` (Ras-related protein Rab-1A),  :doc:`/gene/AGAP004147` (Exo5 - exocyst complex component 5),  :doc:`/gene/AGAP004148` (CLIPB5 - CLIP-domain serine protease),  :doc:`/gene/AGAP004149`,  :doc:`/gene/AGAP004150`,  :doc:`/gene/AGAP004151` (protein phosphatase 5),  :doc:`/gene/AGAP004152`,  :doc:`/gene/AGAP004153` (serine palmitoyltransferase small subunit A),  :doc:`/gene/AGAP012977`,  :doc:`/gene/AGAP004154` (jagged).




The following 2 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP004124` (Osi24 - osiris 24),  :doc:`/gene/AGAP004125` (Osi2 - osiris 2).


.. figure:: peak_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. figure:: peak_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: peak_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: peak_fit.png

    **Figure 4**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 195
        # variables        = 3
        chi-square         = 0.089
        reduced chi-square = 0.000
        Akaike info crit   = -1493.299
        Bayesian info crit = -1483.480
    [[Variables]]
        amplitude:   0.04565543 +/- 0.007413 (16.24%) (init= 0.5)
        decay:       1.28122963 +/- 0.410150 (32.01%) (init= 0.5)
        c:           0.05732916 +/- 0.002498 (4.36%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.667 
        C(amplitude, decay)          = -0.495 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 59
        # data points      = 194
        # variables        = 3
        chi-square         = 0.042
        reduced chi-square = 0.000
        Akaike info crit   = -1630.675
        Bayesian info crit = -1620.871
    [[Variables]]
        amplitude:   0.04557364 +/- 0.004509 (9.90%) (init= 0.5)
        decay:       2.99999972 +/- 0.955547 (31.85%) (init= 0.5)
        c:           0.04980079 +/- 0.005009 (10.06%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.930 
        C(amplitude, c)              = -0.607 
        C(amplitude, decay)          =  0.352 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 194
        # variables        = 1
        chi-square         = 0.107
        reduced chi-square = 0.001
        Akaike info crit   = -1452.720
        Bayesian info crit = -1449.453
    [[Variables]]
        c:   0.06434674 +/- 0.001694 (2.63%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 193
        # variables        = 1
        chi-square         = 0.061
        reduced chi-square = 0.000
        Akaike info crit   = -1553.288
        Bayesian info crit = -1550.026
    [[Variables]]
        c:   0.06554973 +/- 0.001283 (1.96%) (init= 0.03)


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
