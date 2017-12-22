:orphan:




H12 / Uganda *An. gambiae* / Chromosome 3 / #4
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **18,700,001** and
**18,820,000**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).

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



Gene :doc:`../../../../../gene/AGAP008824` overlaps the focal region.





The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP028559`,  :doc:`../../../../../gene/AGAP008823`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have an focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/BFS/3/6/index`, "3R:18,600,001-19,100,000", 82 (56 | 25)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 147
        # variables        = 3
        chi-square         = 0.001
        reduced chi-square = 0.000
        Akaike info crit   = -1687.150
        Bayesian info crit = -1678.178
    [[Variables]]
        amplitude:   0.02422037 +/- 0.003543 (14.63%) (init= 0.5)
        decay:       0.45026961 +/- 0.075475 (16.76%) (init= 0.5)
        c:           0.00783937 +/- 0.000316 (4.03%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.827 
        C(decay, c)                  = -0.425 
        C(amplitude, c)              =  0.152 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 91
        # data points      = 141
        # variables        = 3
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1579.580
        Bayesian info crit = -1570.734
    [[Variables]]
        amplitude:   0.08308106 +/- 0.019175 (23.08%) (init= 0.5)
        decay:       0.31291897 +/- 0.045147 (14.43%) (init= 0.5)
        c:           0.00873089 +/- 0.000347 (3.98%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.953 
        C(decay, c)                  = -0.347 
        C(amplitude, c)              =  0.237 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 146
        # variables        = 1
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -1598.672
        Bayesian info crit = -1595.689
    [[Variables]]
        c:   0.00905602 +/- 0.000346 (3.82%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 140
        # variables        = 1
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1472.391
        Bayesian info crit = -1469.449
    [[Variables]]
        c:   0.01005278 +/- 0.000438 (4.36%) (init= 0.03)


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


