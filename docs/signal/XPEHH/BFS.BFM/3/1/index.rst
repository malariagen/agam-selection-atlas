:orphan:




XPEHH/BFS.BFM/3/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population
when compared with the :doc:`../../../../../population/BFM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **28,360,000** and
**28,460,000**.
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


Gene :doc:`../../../../../gene/AGAP009183` (defective proboscis extension response) overlaps the focal region.



Gene :doc:`../../../../../gene/AGAP009184` is within 50 kbp of the focal region.


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
    * - :doc:`../../../../../signal/XPEHH/CMS.UGS/3/1/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 3R:28,240,000-28,380,000
      - 1,234
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/3/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 3R:28,320,000-28,360,000
      - 1,209
      - 100.0%
      - nan
    * - :doc:`../../../../../signal/IHS/CMS/3/1/index`
      - IHS
      - Cameroon *An. gambiae*
      - 3R:28,320,000-28,700,000
      - 1,106
      - 100.0%
      - Gste
    * - :doc:`../../../../../signal/IHS/BFM/3/1/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 3R:28,260,000-28,620,000
      - 1,058
      - 100.0%
      - Gste
    * - :doc:`../../../../../signal/IHS/GNS/3/1/index`
      - IHS
      - Guinea *An. gambiae*
      - 3R:28,240,000-28,420,000
      - 791
      - 99.9%
      - nan
    * - :doc:`../../../../../signal/IHS/UGS/3/1/index`
      - IHS
      - Uganda *An. gambiae*
      - 3R:28,440,000-28,640,000
      - 493
      - 99.7%
      - Gste
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.BFM/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.BFM/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFS.BFM/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 57
        # data points      = 463
        # variables        = 4
        chi-square         = 823.126
        reduced chi-square = 1.793
        Akaike info crit   = 274.402
        Bayesian info crit = 290.953
    [[Variables]]
        center:      0 (fixed)
        amplitude:   4.79898758 +/- 0.282637 (5.89%) (init= 3)
        decay:       0.77819409 +/- 0.109841 (14.11%) (init= 0.5)
        skew:       -0.99999985 +/- 1.943232 (194.32%) (init= 0)
        baseline:    1.96526906 +/- 0.085522 (4.35%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.532 
        C(amplitude, decay)          = -0.465 
        C(decay, skew)               = -0.335 
        C(amplitude, skew)           = -0.107 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 462
        # variables        = 1
        chi-square         = 1454.188
        reduced chi-square = 3.154
        Akaike info crit   = 531.747
        Bayesian info crit = 535.882
    [[Variables]]
        c:   2.65289275 +/- 0.082628 (3.11%) (init= 1)



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


