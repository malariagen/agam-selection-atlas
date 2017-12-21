:orphan:

H12 / Burkina Faso *An. gambiae* / Chromosome 3 / #7
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **20,800,001** and
**20,860,000**.
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




The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP008918` (STIP1 homology and U-box containing protein 1),  :doc:`../../../../../gene/AGAP028004`,  :doc:`../../../../../gene/AGAP008919`.




The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008914`,  :doc:`../../../../../gene/AGAP008915` (gamma-glutamyltranspeptidase),  :doc:`../../../../../gene/AGAP028196`,  :doc:`../../../../../gene/AGAP008916` (RpL7 - 60S ribosomal protein L7),  :doc:`../../../../../gene/AGAP008917` (DNA topoisomerase II),  :doc:`../../../../../gene/AGAP028087`.


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/7/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/7/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/7/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 138
        # variables        = 3
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1545.168
        Bayesian info crit = -1536.386
    [[Variables]]
        amplitude:   0.01689683 +/- 0.002795 (16.54%) (init= 0.5)
        decay:       0.18398611 +/- 0.049570 (26.94%) (init= 0.5)
        c:           0.01049728 +/- 0.000335 (3.19%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.592 
        C(decay, c)                  = -0.268 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 44
        # data points      = 147
        # variables        = 3
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1755.148
        Bayesian info crit = -1746.176
    [[Variables]]
        amplitude:   0.02703459 +/- 0.003494 (12.93%) (init= 0.5)
        decay:       0.15000001 +/- 0.024495 (16.33%) (init= 0.5)
        c:           0.01062669 +/- 0.000220 (2.07%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.782 
        C(decay, c)                  = -0.233 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 137
        # variables        = 1
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1504.748
        Bayesian info crit = -1501.828
    [[Variables]]
        c:   0.01100318 +/- 0.000351 (3.19%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 146
        # variables        = 1
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1676.927
        Bayesian info crit = -1673.943
    [[Variables]]
        c:   0.01108772 +/- 0.000264 (2.38%) (init= 0.03)


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
