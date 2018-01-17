:orphan:




H12/UGS/3/4
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **18,780,000** and
**19,000,000**.
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


The following 3 genes overlap the focal region: :doc:`../../../../../gene/AGAP008824`,  :doc:`../../../../../gene/AGAP008825`,  :doc:`../../../../../gene/AGAP008826`.



Gene :doc:`../../../../../gene/AGAP028025` is within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/IHS/UGS/3/2/index`
      - IHS
      - Uganda *An. gambiae*
      - 3R:18,760,000-19,000,000
      - 327
      - 92.9%
      - nan
    * - :doc:`../../../../../signal/IHS/BFS/3/5/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3R:18,760,000-18,920,000
      - 297
      - 90.4%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/3/3/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 3R:18,600,000-19,000,000
      - 215
      - 96.1%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/3/4/peak_finding.png"/>
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

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 38
        # data points      = 387
        # variables        = 4
        chi-square         = 0.005
        reduced chi-square = 0.000
        Akaike info crit   = -4343.911
        Bayesian info crit = -4328.077
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.02499791 +/- 0.002053 (8.22%) (init= 0.5)
        sigma:       0.39923618 +/- 0.026019 (6.52%) (init= 0.5)
        skew:        0.14084752 +/- 0.060100 (42.67%) (init= 0)
        baseline:    0.00867564 +/- 0.000196 (2.25%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.744 
        C(sigma, baseline)           = -0.207 
        C(sigma, skew)               = -0.168 
        C(amplitude, skew)           =  0.152 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 386
        # variables        = 1
        chi-square         = 0.009
        reduced chi-square = 0.000
        Akaike info crit   = -4133.736
        Bayesian info crit = -4129.781
    [[Variables]]
        c:   0.00950227 +/- 0.000240 (2.53%) (init= 0.03)



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


