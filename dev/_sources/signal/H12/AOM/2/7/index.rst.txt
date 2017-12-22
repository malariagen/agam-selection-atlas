:orphan:

H12 / Angola *An. coluzzii* / Chromosome 2 / #7
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**2R** between positions **48,180,001** and
**48,240,000**.
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



Gene :doc:`../../../../../gene/AGAP013324` (putative G-protein coupled receptor GPCR) overlaps the focal region.





The following 5 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004033`,  :doc:`../../../../../gene/AGAP004034` (GPRNNA4 - putative GPCR class a orphan receptor 4),  :doc:`../../../../../gene/AGAP004035` (GPRFSH - putative glyco-protein hormone fsh-like receptor),  :doc:`../../../../../gene/AGAP004036` (HPX7 - heme peroxidase 7),  :doc:`../../../../../gene/AGAP004038` (HPX8 - heme peroxidase 8).


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/7/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/7/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/7/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 189
        # variables        = 3
        chi-square         = 0.071
        reduced chi-square = 0.000
        Akaike info crit   = -1484.757
        Bayesian info crit = -1475.032
    [[Variables]]
        amplitude:   0.11826571 +/- 0.013634 (11.53%) (init= 0.5)
        decay:       0.24242724 +/- 0.045613 (18.82%) (init= 0.5)
        c:           0.04565794 +/- 0.001517 (3.32%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.616 
        C(decay, c)                  = -0.258 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 195
        # variables        = 3
        chi-square         = 0.107
        reduced chi-square = 0.001
        Akaike info crit   = -1458.453
        Bayesian info crit = -1448.634
    [[Variables]]
        amplitude:   0.06820723 +/- 0.012300 (18.03%) (init= 0.5)
        decay:       0.66659540 +/- 0.184209 (27.63%) (init= 0.5)
        c:           0.05551112 +/- 0.002069 (3.73%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.660 
        C(decay, c)                  = -0.445 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 188
        # variables        = 1
        chi-square         = 0.107
        reduced chi-square = 0.001
        Akaike info crit   = -1403.071
        Bayesian info crit = -1399.834
    [[Variables]]
        c:   0.04910978 +/- 0.001742 (3.55%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 194
        # variables        = 1
        chi-square         = 0.124
        reduced chi-square = 0.001
        Akaike info crit   = -1425.089
        Bayesian info crit = -1421.821
    [[Variables]]
        c:   0.06056056 +/- 0.001819 (3.00%) (init= 0.03)


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
