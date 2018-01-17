:orphan:




IHS/CMS/3/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**3R** between positions **42,500,000** and
**42,660,000**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).





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


Gene :doc:`../../../../../gene/AGAP009768` (solute carrier family 6 (neurotransmitter transporter, GABA) member 1) overlaps the focal region.



The following 10 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009757` (ANCE7 - angiotensin-converting enzyme 7),  :doc:`../../../../../gene/AGAP029049`,  :doc:`../../../../../gene/AGAP029054` (NimB2 - nimrod B2),  :doc:`../../../../../gene/AGAP029055`,  :doc:`../../../../../gene/AGAP009763`,  :doc:`../../../../../gene/AGAP009764`,  :doc:`../../../../../gene/AGAP009765` (dymeclin),  :doc:`../../../../../gene/AGAP009766`,  :doc:`../../../../../gene/AGAP009769`,  :doc:`../../../../../gene/AGAP009770` (GPRCAL1 - putative calcitonin receptor 1).


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
      - Peak model :math:`\Delta_{i}`
      - Max. percentile
      - Known locus
    * - :doc:`../../../../../signal/IHS/BFS/3/7/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3R:42,540,000-42,980,000
      - 141
      - 96.4%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/CMS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 620
        # variables        = 4
        chi-square         = 75.817
        reduced chi-square = 0.123
        Akaike info crit   = -1294.868
        Bayesian info crit = -1277.149
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.60876542 +/- 0.039611 (6.51%) (init= 3)
        sigma:       2.99999904 +/- 0.249057 (8.30%) (init= 0.5)
        skew:       -0.94946405 +/- 0.083738 (8.82%) (init= 0)
        baseline:    1.75588485 +/- 0.030711 (1.75%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.689 
        C(sigma, baseline)           =  0.555 
        C(amplitude, skew)           =  0.233 
        C(skew, baseline)            = -0.137 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 619
        # variables        = 1
        chi-square         = 103.720
        reduced chi-square = 0.168
        Akaike info crit   = -1103.785
        Bayesian info crit = -1099.357
    [[Variables]]
        c:   2.07745427 +/- 0.016466 (0.79%) (init= 1)



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


