:orphan:




H12 / Gabon *An. gambiae* / Chromosome X / #1
=============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **14,480,001** and
**14,720,000**.
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
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP000795`,  :doc:`../../../../../gene/AGAP000797` (E3 ubiquitin-protein ligase HECW2),  :doc:`../../../../../gene/AGAP000798`:sup:`2` (GLURIIc - ionotropic receptor GLURIIc),  :doc:`../../../../../gene/AGAP000801`:sup:`2` (GLURIIb - ionotropic receptor GLURIIb).




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000792` (Adenosylhomocysteinase),  :doc:`../../../../../gene/AGAP000793`,  :doc:`../../../../../gene/AGAP000794`:sup:`1` (NADH dehydrogenase (ubiquinone) Fe-S protein 2),  :doc:`../../../../../gene/AGAP013289`,  :doc:`../../../../../gene/AGAP000803`:sup:`2` (GLURIIa - ionotropic receptor GLURIIa),  :doc:`../../../../../gene/AGAP000804`:sup:`1` (GPXH2 - glutathione peroxidase 2),  :doc:`../../../../../gene/AGAP000805` (BTB/POZ domain-containing protein KCTD16).


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

    :doc:`../../../../../signal/H12/AOM/X/2/index`, "X:14,660,001-14,720,000", 262 (204 | 58)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 124
        # data points      = 151
        # variables        = 3
        chi-square         = 0.899
        reduced chi-square = 0.006
        Akaike info crit   = -767.687
        Bayesian info crit = -758.635
    [[Variables]]
        amplitude:   0.29296462 +/- 0.024707 (8.43%) (init= 0.5)
        decay:       1.99999978 +/- 0.395854 (19.79%) (init= 0.5)
        c:           0.05999999 +/- 0.029358 (48.93%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  =  0.904 
        C(amplitude, c)              =  0.457 
        C(amplitude, decay)          =  0.144 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 80
        # data points      = 141
        # variables        = 3
        chi-square         = 0.457
        reduced chi-square = 0.003
        Akaike info crit   = -802.329
        Bayesian info crit = -793.482
    [[Variables]]
        amplitude:   0.25113155 +/- 0.019553 (7.79%) (init= 0.5)
        decay:       2          +/- 0.460004 (23.00%) (init= 0.5)
        c:           0.05999999 +/- 0.018011 (30.02%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.906 
        C(amplitude, c)              = -0.444 
        C(amplitude, decay)          =  0.132 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 1.018
        reduced chi-square = 0.007
        Akaike info crit   = -746.919
        Bayesian info crit = -743.908
    [[Variables]]
        c:   0.17340774 +/- 0.006748 (3.89%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 140
        # variables        = 1
        chi-square         = 0.759
        reduced chi-square = 0.005
        Akaike info crit   = -728.376
        Bayesian info crit = -725.434
    [[Variables]]
        c:   0.14301316 +/- 0.006246 (4.37%) (init= 0.03)


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


