:orphan:




H12/CMS/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **26,879,316** and
**26,919,316**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).





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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP011532` (septin),  :doc:`../../../../../gene/AGAP011533` (tetratricopeptide repeat protein 15),  :doc:`../../../../../gene/AGAP011534`,  :doc:`../../../../../gene/AGAP011535` (transcription elongation factor B, polypeptide 1),  :doc:`../../../../../gene/AGAP011536` (Mini-chromosome maintenance complex-binding protein),  :doc:`../../../../../gene/AGAP011537` (Argonaute 3).



The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP011530`,  :doc:`../../../../../gene/AGAP011531` (Selenium-binding protein 2),  :doc:`../../../../../gene/AGAP028430`,  :doc:`../../../../../gene/AGAP011538`,  :doc:`../../../../../gene/AGAP011539` (dynein intermediate chain 2, axonemal),  :doc:`../../../../../gene/AGAP011540` (dynein intermediate chain 2, axonemal),  :doc:`../../../../../gene/AGAP011541` (Ecto-NOX disulfide-thiol exchanger 1).


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
    * - :doc:`../../../../../signal/H12/BFS/3/2/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 3L:26,879,316-26,979,316
      - 291
      - 92.7%
      - nan
    * - :doc:`../../../../../signal/IHS/BFS/3/6/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3L:26,919,316-26,959,316
      - 187
      - 96.6%
      - nan
    * - :doc:`../../../../../signal/IHS/CMS/3/3/index`
      - IHS
      - Cameroon *An. gambiae*
      - 3L:26,919,316-26,959,316
      - 186
      - 93.0%
      - nan
    * - :doc:`../../../../../signal/IHS/GNS/3/3/index`
      - IHS
      - Guinea *An. gambiae*
      - 3L:26,919,316-26,959,316
      - 115
      - 96.8%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 393
        # variables        = 4
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -4298.972
        Bayesian info crit = -4283.077
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.05828341 +/- 0.003134 (5.38%) (init= 0.5)
        decay:       0.15000004 +/- 0.011570 (7.71%) (init= 0.5)
        skew:       -0.00970093 +/- 0.075773 (781.10%) (init= 0)
        baseline:    0.00598710 +/- 0.000220 (3.68%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.706 
        C(decay, baseline)           = -0.200 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 13
        # data points      = 392
        # variables        = 1
        chi-square         = 0.016
        reduced chi-square = 0.000
        Akaike info crit   = -3970.619
        Bayesian info crit = -3966.648
    [[Variables]]
        c:   0.00694796 +/- 0.000319 (4.59%) (init= 0.03)



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


