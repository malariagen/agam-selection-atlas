:orphan:

Guinea *An. gambiae* | H12 | Chromosome 2 | Signal #4
================================================================================



This page describes a signal of selection found in the
:doc:`/population/GNS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2L** between positions **25,640,001** and
**25,740,000**.




The following 9 genes overlap the focal region: :doc:`/gene/AGAP006050` (AarF domain containing kinase 5),  :doc:`/gene/AGAP006051` (pentatricopeptide repeat domain 1),  :doc:`/gene/AGAP006052` (protein phosphatase 1, regulatory (inhibitor) subunit 3),  :doc:`/gene/AGAP006053`,  :doc:`/gene/AGAP006054`,  :doc:`/gene/AGAP006055` (NF-kappa-B inhibitor-like protein 2),  :doc:`/gene/AGAP006056`,  :doc:`/gene/AGAP006057` (multiple coagulation factor deficiency 2),  :doc:`/gene/AGAP006058` (heparan sulfate 2-o-sulfotransferase).




The following 5 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP006045` (protein yorkie),  :doc:`/gene/AGAP006046` (Med23 - mediator of RNA polymerase II transcription subunit 23),  :doc:`/gene/AGAP006047` (CYP4J9 - cytochrome P450),  :doc:`/gene/AGAP006048` (CYP4J5 - cytochrome P450),  :doc:`/gene/AGAP006049` (CYP4J10 - cytochrome P450).


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
        # function evals   = 38
        # data points      = 201
        # variables        = 3
        chi-square         = 0.095
        reduced chi-square = 0.000
        Akaike info crit   = -1532.501
        Bayesian info crit = -1522.591
    [[Variables]]
        amplitude:   0.15567044 +/- 0.010343 (6.64%) (init= 0.5)
        decay:       0.63658986 +/- 0.068473 (10.76%) (init= 0.5)
        c:           0.05999994 +/- 0.001871 (3.12%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.607 
        C(decay, c)                  = -0.434 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 200
        # variables        = 3
        chi-square         = 0.334
        reduced chi-square = 0.002
        Akaike info crit   = -1272.952
        Bayesian info crit = -1263.057
    [[Variables]]
        amplitude:   0.14442880 +/- 0.021642 (14.98%) (init= 0.5)
        decay:       0.65625932 +/- 0.150392 (22.92%) (init= 0.5)
        c:           0.04672997 +/- 0.003552 (7.60%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.662 
        C(decay, c)                  = -0.443 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 200
        # variables        = 1
        chi-square         = 0.240
        reduced chi-square = 0.001
        Akaike info crit   = -1343.311
        Bayesian info crit = -1340.013
    [[Variables]]
        c:   0.07223251 +/- 0.002454 (3.40%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 199
        # variables        = 1
        chi-square         = 0.444
        reduced chi-square = 0.002
        Akaike info crit   = -1212.830
        Bayesian info crit = -1209.537
    [[Variables]]
        c:   0.05743894 +/- 0.003357 (5.85%) (init= 0.03)


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
