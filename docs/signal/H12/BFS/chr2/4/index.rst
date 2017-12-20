:orphan:

Burkina Faso *An. gambiae* | H12 | Chromosome 2 | Signal #4
================================================================================



This page describes a signal of selection found in the
:doc:`/population/BFS` population using the
:doc:`/method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R between position 40,800,001 and
41,020,000**.




The following 17 genes overlap the focal region: :doc:`/gene/AGAP003635`,  :doc:`/gene/AGAP003636` (inositol oxygenase),  :doc:`/gene/AGAP003638`,  :doc:`/gene/AGAP003639` (Prolylcarboxypeptidase),  :doc:`/gene/AGAP003640` (SP8905),  :doc:`/gene/AGAP003641` (SP8907),  :doc:`/gene/AGAP003642` (SP8898),  :doc:`/gene/AGAP003643` (ubiquitin carboxyl-terminal hydrolase 34),  :doc:`/gene/AGAP003644` (mRpS11 - 28S ribosomal protein S11, mitochondrial),  :doc:`/gene/AGAP003645` (kelch-like protein 19),  :doc:`/gene/AGAP013307`,  :doc:`/gene/AGAP003646`,  :doc:`/gene/AGAP003647`,  :doc:`/gene/AGAP003648` (DNA-directed RNA polymerase II subunit RPB2),  :doc:`/gene/AGAP003649`,  :doc:`/gene/AGAP003650` (translation initiation factor eIF-2B subunit alpha),  :doc:`/gene/AGAP003651` (Tyrosine-protein kinase Fes/Fps).




The following 6 genes are within 40 kbp of the focal
region: :doc:`/gene/AGAP003632` (U3 small nucleolar RNA-associated protein 14),  :doc:`/gene/AGAP003633`,  :doc:`/gene/AGAP012992`,  :doc:`/gene/AGAP013502`,  :doc:`/gene/AGAP003652` (aldehyde dehydrogenase (NAD )),  :doc:`/gene/AGAP003654` (GPRCAL3 - putative calcitonin receptor 3).


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

    :doc:`/signal/H12/BFM/chr2/3/index`,":40880001-40980000",512
    :doc:`/signal/H12/CMS/chr2/3/index`,":40620001-41020000",451
    



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
        # data points      = 198
        # variables        = 3
        chi-square         = 0.033
        reduced chi-square = 0.000
        Akaike info crit   = -1717.675
        Bayesian info crit = -1707.810
    [[Variables]]
        amplitude:   0.12861482 +/- 0.005035 (3.92%) (init= 0.5)
        decay:       0.97995076 +/- 0.067365 (6.87%) (init= 0.5)
        c:           0.02248608 +/- 0.001293 (5.75%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.570 
        C(amplitude, decay)          = -0.556 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 197
        # variables        = 3
        chi-square         = 0.078
        reduced chi-square = 0.000
        Akaike info crit   = -1536.954
        Bayesian info crit = -1527.104
    [[Variables]]
        amplitude:   0.11899310 +/- 0.010939 (9.19%) (init= 0.5)
        decay:       0.61819415 +/- 0.086452 (13.98%) (init= 0.5)
        c:           0.04348714 +/- 0.001718 (3.95%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.670 
        C(decay, c)                  = -0.425 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 197
        # variables        = 1
        chi-square         = 0.178
        reduced chi-square = 0.001
        Akaike info crit   = -1379.044
        Bayesian info crit = -1375.760
    [[Variables]]
        c:   0.03812522 +/- 0.002145 (5.63%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 196
        # variables        = 1
        chi-square         = 0.148
        reduced chi-square = 0.001
        Akaike info crit   = -1406.478
        Bayesian info crit = -1403.200
    [[Variables]]
        c:   0.05181048 +/- 0.001970 (3.80%) (init= 0.03)


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
