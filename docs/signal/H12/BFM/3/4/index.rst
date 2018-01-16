:orphan:




H12/BFM/3/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **11,619,316** and
**11,659,316**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).





.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area shows the focus of the
    selection signal. The shaded blue area shows the genomic region in linkage with the
    selection event. Use the mouse wheel or the controls at the top right of the plot to zoom
    in, and hover over genes to see gene names and descriptions.
    </p></div>

Genes
-----


Gene :doc:`../../../../../gene/AGAP010833` (CLIPB14 - CLIP-domain serine protease) overlaps the focal region.



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP010830` (TEP9 - thioester-containing protein 9),  :doc:`../../../../../gene/AGAP010831` (TEP8 - thioester-containing protein 8),  :doc:`../../../../../gene/AGAP010832` (TEP19 - thioester-containing protein 19).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping selection signals
-----------------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. list-table::
    :widths: auto
    :header-rows: 1

    * - Signal
      - Statistic
      - Population
      - Focus
      - Peak Model :math:`\Delta_{i}`
      - Max Percentile
      - Known Loci
    * - :doc:`../../../../../signal/XPEHH/BFM.BFS/3/1/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - 3L:11,579,316-11,659,316
      - 251
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFM.GWA/3/2/index`
      - XPEHH
      - Burkina Faso *An. coluzzii*
      - 3L:11,599,316-11,659,316
      - 230
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/3/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 64
        # data points      = 389
        # variables        = 4
        chi-square         = 0.689
        reduced chi-square = 0.002
        Akaike info crit   = -2456.871
        Bayesian info crit = -2441.017
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.44316448 +/- 0.034081 (7.69%) (init= 0.5)
        decay:       0.15000000 +/- 0.014623 (9.75%) (init= 0.5)
        skew:        0.46143464 +/- 0.105992 (22.97%) (init= 0)
        baseline:    0.02209699 +/- 0.002232 (10.10%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.688 
        C(decay, skew)               = -0.229 
        C(decay, baseline)           = -0.199 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 388
        # variables        = 1
        chi-square         = 0.877
        reduced chi-square = 0.002
        Akaike info crit   = -2361.788
        Bayesian info crit = -2357.827
    [[Variables]]
        c:   0.02800293 +/- 0.002416 (8.63%) (init= 0.03)



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


