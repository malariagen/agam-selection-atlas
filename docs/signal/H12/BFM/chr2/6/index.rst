:orphan:

Burkina Faso *An. coluzzii* | H12 | Chromosome 2 | Signal #6
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R between position 24,820,001 and
24,860,000**.




The following 6 genes overlap the focal region: :doc:`/gene/AGAP002636`,  :doc:`/gene/AGAP002637`,  :doc:`/gene/AGAP013045`,  :doc:`/gene/AGAP002638` (ABCH1 - ATP-binding cassette transporter (ABC transporter) family H member 1),  :doc:`/gene/AGAP002639` (Or39 - odorant receptor 39),  :doc:`/gene/AGAP002640` (Or38 - odorant receptor 38).




The following 15 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP002634` (membrane dipeptidase),  :doc:`/gene/AGAP002635` (Gr13 - gustatory receptor 13),  :doc:`/gene/AGAP013517`,  :doc:`/gene/AGAP013086`,  :doc:`/gene/AGAP013456`,  :doc:`/gene/AGAP013225`,  :doc:`/gene/AGAP013322`,  :doc:`/gene/AGAP013353`,  :doc:`/gene/AGAP013110`,  :doc:`/gene/AGAP013484`,  :doc:`/gene/AGAP013247`,  :doc:`/gene/AGAP013316`,  :doc:`/gene/AGAP002641`,  :doc:`/gene/AGAP002642` (DNA mismatch repair protein MSH5),  :doc:`/gene/AGAP002643`.


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
        # function evals   = 35
        # data points      = 201
        # variables        = 3
        chi-square         = 0.129
        reduced chi-square = 0.001
        Akaike info crit   = -1471.941
        Bayesian info crit = -1462.031
    [[Variables]]
        amplitude:   0.17627985 +/- 0.014666 (8.32%) (init= 0.5)
        decay:       0.39866475 +/- 0.052235 (13.10%) (init= 0.5)
        c:           0.04095901 +/- 0.002009 (4.91%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.624 
        C(decay, c)                  = -0.332 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 56
        # data points      = 200
        # variables        = 3
        chi-square         = 0.164
        reduced chi-square = 0.001
        Akaike info crit   = -1415.125
        Bayesian info crit = -1405.230
    [[Variables]]
        amplitude:   0.42649816 +/- 0.039878 (9.35%) (init= 0.5)
        decay:       0.15000000 +/- 0.004741 (3.16%) (init= 0.5)
        c:           0.05018155 +/- 0.002122 (4.23%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.785 
        C(decay, c)                  = -0.198 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.251
        reduced chi-square = 0.001
        Akaike info crit   = -1333.993
        Bayesian info crit = -1330.695
    [[Variables]]
        c:   0.04925960 +/- 0.002512 (5.10%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 199
        # variables        = 1
        chi-square         = 0.279
        reduced chi-square = 0.001
        Akaike info crit   = -1305.340
        Bayesian info crit = -1302.047
    [[Variables]]
        c:   0.05532940 +/- 0.002661 (4.81%) (init= 0.03)


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
