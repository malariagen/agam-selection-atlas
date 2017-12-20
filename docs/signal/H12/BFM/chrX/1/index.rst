:orphan:

Burkina Faso *An. coluzzii* | H12 | Chromosome X | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFM` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X** between positions **15,100,001** and
**15,380,000**.




The following 14 genes overlap the focal region: :doc:`/gene/AGAP012997`,  :doc:`/gene/AGAP000818` (CYP9K1 - cytochrome P450),  :doc:`/gene/AGAP000819` (nuclear receptor subfamily 2 group E member (Tailless)),  :doc:`/gene/AGAP000820` (CPR125 - cuticular protein RR-2 family 125),  :doc:`/gene/AGAP000821`,  :doc:`/gene/AGAP000822`,  :doc:`/gene/AGAP000823` (CD81 antigen),  :doc:`/gene/AGAP000824` (bone morphogenetic protein 5),  :doc:`/gene/AGAP000825`,  :doc:`/gene/AGAP000826` (cap-specific mRNA (nucleoside-2'-O-)-methyltransferase 1),  :doc:`/gene/AGAP000829` (calpain-15),  :doc:`/gene/AGAP000830` (CASPS7 - short caspase 7),  :doc:`/gene/AGAP000831` (DnaJ homolog subfamily C member 25),  :doc:`/gene/AGAP000832` (Derlin-2/3).




The following 4 genes are within 50 kbp of the focal
region: :doc:`/gene/AGAP013173`,  :doc:`/gene/AGAP013424`,  :doc:`/gene/AGAP000833` (MIP - myoinhibitory-like peptide),  :doc:`/gene/AGAP000834`.


.. figure:: peak_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Overlapping signals
-------------------



The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    :doc:`/signal/H12/BFS/chrX/1/index`,"X:15,120,001-15,260,000",1073
    :doc:`/signal/H12/GNS/chrX/1/index`,"X:15,100,001-15,220,000",595
    :doc:`/signal/H12/UGS/chrX/1/index`,"X:15,320,001-15,460,000",510
    



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
        # data points      = 194
        # variables        = 3
        chi-square         = 0.163
        reduced chi-square = 0.001
        Akaike info crit   = -1367.938
        Bayesian info crit = -1358.134
    [[Variables]]
        amplitude:   1.24396992 +/- 0.024252 (1.95%) (init= 0.5)
        decay:       0.63994517 +/- 0.014822 (2.32%) (init= 0.5)
        c:           0.01947099 +/- 0.002544 (13.07%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.750 
        C(decay, c)                  = -0.440 
        C(amplitude, c)              =  0.105 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 197
        # variables        = 3
        chi-square         = 0.511
        reduced chi-square = 0.003
        Akaike info crit   = -1167.232
        Bayesian info crit = -1157.383
    [[Variables]]
        amplitude:   1.07943882 +/- 0.028028 (2.60%) (init= 0.5)
        decay:       0.86021191 +/- 0.032967 (3.83%) (init= 0.5)
        c:           0.05999999 +/- 0.001942 (3.24%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.704 
        C(decay, c)                  = -0.526 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 193
        # variables        = 1
        chi-square         = 6.598
        reduced chi-square = 0.034
        Akaike info crit   = -649.559
        Bayesian info crit = -646.297
    [[Variables]]
        c:   0.09521558 +/- 0.013343 (14.01%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 8.517
        reduced chi-square = 0.044
        Akaike info crit   = -612.676
        Bayesian info crit = -609.398
    [[Variables]]
        c:   0.17528017 +/- 0.014927 (8.52%) (init= 0.03)


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
