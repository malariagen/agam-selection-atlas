:orphan:

Gabon *An. gambiae* | H12 | Chromosome 3 | Signal #2
================================================================================



This page describes a signal of selection found in the
:doc:`/population/GAS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
3R between position 41,760,001 and
41,960,000.




The following 9 genes overlap the focal region: :doc:`/gene/AGAP009726`,  :doc:`/gene/AGAP009727` (RhoGAP92B),  :doc:`/gene/AGAP009728` (ficolin),  :doc:`/gene/AGAP009729` (CCAP - cardioacceleratory peptide),  :doc:`/gene/AGAP009730` (myosin III),  :doc:`/gene/AGAP009731` (wingless-type MMTV integration site family, member 10A),  :doc:`/gene/AGAP009732` (Protein Wnt),  :doc:`/gene/AGAP009733` (wingless-type MMTV integration site family, member 6),  :doc:`/gene/AGAP009734` (wingless-type MMTV integration site family, member 1).



No genes are within 50 kbp of the focal region.




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
        # function evals   = 63
        # data points      = 294
        # variables        = 3
        chi-square         = 0.048
        reduced chi-square = 0.000
        Akaike info crit   = -2558.614
        Bayesian info crit = -2547.564
    [[Variables]]
        amplitude:   0.05005996 +/- 0.009018 (18.02%) (init= 0.5)
        decay:       0.19189376 +/- 0.038562 (20.10%) (init= 0.5)
        c:           0.03194687 +/- 0.000848 (2.65%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.688 
        C(decay, c)                  = -0.361 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 194
        # variables        = 3
        chi-square         = 0.010
        reduced chi-square = 0.000
        Akaike info crit   = -1913.167
        Bayesian info crit = -1903.363
    [[Variables]]
        amplitude:   0.03525603 +/- 0.002710 (7.69%) (init= 0.5)
        decay:       1.21181590 +/- 0.172466 (14.23%) (init= 0.5)
        c:           0.02136549 +/- 0.000799 (3.74%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.640 
        C(amplitude, decay)          = -0.561 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 293
        # variables        = 1
        chi-square         = 0.055
        reduced chi-square = 0.000
        Akaike info crit   = -2514.120
        Bayesian info crit = -2510.440
    [[Variables]]
        c:   0.03372919 +/- 0.000799 (2.37%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 193
        # variables        = 1
        chi-square         = 0.020
        reduced chi-square = 0.000
        Akaike info crit   = -1768.386
        Bayesian info crit = -1765.123
    [[Variables]]
        c:   0.02639166 +/- 0.000735 (2.79%) (init= 0.03)


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
