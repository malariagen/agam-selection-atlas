:orphan:




H12 / Guinea *An. gambiae* / Chromosome X / #1
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **14,960,001** and
**15,100,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 5 genes overlap the focal region: :doc:`../../../../../gene/AGAP000817`,  :doc:`../../../../../gene/AGAP000816`,  :doc:`../../../../../gene/AGAP013474`,  :doc:`../../../../../gene/AGAP013173`,  :doc:`../../../../../gene/AGAP013424`.




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000813`:sup:`1` (Frataxin homolog, mitochondrial),  :doc:`../../../../../gene/AGAP000814`,  :doc:`../../../../../gene/AGAP000815` (INTB - integrin beta subunit).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/X/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 151
        # variables        = 3
        chi-square         = 0.020
        reduced chi-square = 0.000
        Akaike info crit   = -1339.007
        Bayesian info crit = -1329.955
    [[Variables]]
        amplitude:   0.21349827 +/- 0.007163 (3.36%) (init= 0.5)
        decay:       0.34493837 +/- 0.018557 (5.38%) (init= 0.5)
        c:           0.03004693 +/- 0.001089 (3.62%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.609 
        C(decay, c)                  = -0.359 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 51
        # data points      = 141
        # variables        = 3
        chi-square         = 0.140
        reduced chi-square = 0.001
        Akaike info crit   = -969.005
        Bayesian info crit = -960.159
    [[Variables]]
        amplitude:   0.34281200 +/- 0.031560 (9.21%) (init= 0.5)
        decay:       0.65126682 +/- 0.070882 (10.88%) (init= 0.5)
        c:           0.05973670 +/- 0.003588 (6.01%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.816 
        C(decay, c)                  = -0.543 
        C(amplitude, c)              =  0.213 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.169
        reduced chi-square = 0.001
        Akaike info crit   = -1016.570
        Bayesian info crit = -1013.559
    [[Variables]]
        c:   0.04152271 +/- 0.002747 (6.62%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 140
        # variables        = 1
        chi-square         = 0.468
        reduced chi-square = 0.003
        Akaike info crit   = -796.144
        Bayesian info crit = -793.202
    [[Variables]]
        c:   0.08561394 +/- 0.004903 (5.73%) (init= 0.03)


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
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments.</a></noscript>


