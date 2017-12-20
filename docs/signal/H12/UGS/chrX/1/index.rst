:orphan:

Uganda *An. gambiae* | H12 | Chromosome X | Signal #1
================================================================================



This page describes a signal of selection found in the
:doc:`/population/UGS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**X between position 15,320,001 and
15,460,000**.




The following 13 genes overlap the focal region: :doc:`/gene/AGAP000822`,  :doc:`/gene/AGAP000823` (CD81 antigen),  :doc:`/gene/AGAP000824` (bone morphogenetic protein 5),  :doc:`/gene/AGAP000825`,  :doc:`/gene/AGAP000826` (cap-specific mRNA (nucleoside-2'-O-)-methyltransferase 1),  :doc:`/gene/AGAP000829` (calpain-15),  :doc:`/gene/AGAP000830` (CASPS7 - short caspase 7),  :doc:`/gene/AGAP000831` (DnaJ homolog subfamily C member 25),  :doc:`/gene/AGAP000832` (Derlin-2/3),  :doc:`/gene/AGAP000833` (MIP - myoinhibitory-like peptide),  :doc:`/gene/AGAP000834`,  :doc:`/gene/AGAP000835`,  :doc:`/gene/AGAP028655`.




The following 3 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP000820` (CPR125 - cuticular protein RR-2 family 125),  :doc:`/gene/AGAP000821`,  :doc:`/gene/AGAP013506`.


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

    :doc:`/signal/H12/BFM/chrX/1/index`,":15100001-15380000",1272
    



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
        # function evals   = 31
        # data points      = 195
        # variables        = 3
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1983.989
        Bayesian info crit = -1974.170
    [[Variables]]
        amplitude:   0.07090687 +/- 0.002173 (3.07%) (init= 0.5)
        decay:       1.27030162 +/- 0.073143 (5.76%) (init= 0.5)
        c:           0.00865943 +/- 0.000700 (8.09%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.666 
        C(amplitude, decay)          = -0.467 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 35
        # data points      = 197
        # variables        = 3
        chi-square         = 0.034
        reduced chi-square = 0.000
        Akaike info crit   = -1703.044
        Bayesian info crit = -1693.195
    [[Variables]]
        amplitude:   0.08740090 +/- 0.007863 (9.00%) (init= 0.5)
        decay:       0.52500371 +/- 0.069794 (13.29%) (init= 0.5)
        c:           0.02251743 +/- 0.001094 (4.86%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.684 
        C(decay, c)                  = -0.391 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 194
        # variables        = 1
        chi-square         = 0.054
        reduced chi-square = 0.000
        Akaike info crit   = -1587.894
        Bayesian info crit = -1584.626
    [[Variables]]
        c:   0.01877733 +/- 0.001195 (6.37%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 0.059
        reduced chi-square = 0.000
        Akaike info crit   = -1588.602
        Bayesian info crit = -1585.324
    [[Variables]]
        c:   0.02749157 +/- 0.001238 (4.50%) (init= 0.03)


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
