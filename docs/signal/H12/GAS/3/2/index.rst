:orphan:

H12 / Gabon *An. gambiae* / Chromosome 3 / #2
================================================================================



This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The inferred focus of this signal is on chromosome arm
**3R** between positions **80,001** and
**180,000**.
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




The following 8 genes overlap the focal region: :doc:`../../../../../gene/AGAP007735`,  :doc:`../../../../../gene/AGAP007736`,  :doc:`../../../../../gene/AGAP007737`,  :doc:`../../../../../gene/AGAP007738`,  :doc:`../../../../../gene/AGAP007739` (transducin (beta)-like 1),  :doc:`../../../../../gene/AGAP007740` (RpLP1 - 60S ribosomal protein LP1),  :doc:`../../../../../gene/AGAP007741` (ribonuclease H2 subunit A),  :doc:`../../../../../gene/AGAP007742` (E3 UFM1-protein ligase 1 homolog).




The following 13 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007732` (solute carrier family 17, member 5),  :doc:`../../../../../gene/AGAP007733` (Sialin),  :doc:`../../../../../gene/AGAP007734`,  :doc:`../../../../../gene/AGAP007743` (solute carrier family 16 (monocarboxylic acid transporters), member 10),  :doc:`../../../../../gene/AGAP007744`,  :doc:`../../../../../gene/AGAP007746`,  :doc:`../../../../../gene/AGAP007745`,  :doc:`../../../../../gene/AGAP007747`,  :doc:`../../../../../gene/AGAP013766`,  :doc:`../../../../../gene/AGAP007748`,  :doc:`../../../../../gene/AGAP007749`,  :doc:`../../../../../gene/AGAP007750`,  :doc:`../../../../../gene/AGAP007751`.


Overlapping signals
-------------------


No overlapping signals.


Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 7
        # variables        = 3
        chi-square         = 0.000
        reduced chi-square = 0.000
        Akaike info crit   = -60.949
        Bayesian info crit = -61.112
    [[Variables]]
        amplitude:   0.21411571 +/- 0.095583 (44.64%) (init= 0.5)
        decay:       0.25358981 +/- 0.183585 (72.39%) (init= 0.5)
        c:           2.0761e-12 +/- 0.002020 (97315315354.63%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, c)              =  0.996 
        C(decay, c)                  =  0.990 
        C(amplitude, decay)          =  0.977 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 149
        # variables        = 3
        chi-square         = 0.094
        reduced chi-square = 0.001
        Akaike info crit   = -1092.678
        Bayesian info crit = -1083.667
    [[Variables]]
        amplitude:   0.12667533 +/- 0.008266 (6.53%) (init= 0.5)
        decay:       1.68756125 +/- 0.306421 (18.16%) (init= 0.5)
        c:           0.01807777 +/- 0.006122 (33.87%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.868 
        C(amplitude, c)              = -0.228 
        C(amplitude, decay)          = -0.150 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 6
        # variables        = 1
        chi-square         = 0.009
        reduced chi-square = 0.002
        Akaike info crit   = -36.967
        Bayesian info crit = -37.175
    [[Variables]]
        c:   0.12906569 +/- 0.017388 (13.47%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 148
        # variables        = 1
        chi-square         = 0.229
        reduced chi-square = 0.002
        Akaike info crit   = -956.021
        Bayesian info crit = -953.023
    [[Variables]]
        c:   0.05156228 +/- 0.003241 (6.29%) (init= 0.03)


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
