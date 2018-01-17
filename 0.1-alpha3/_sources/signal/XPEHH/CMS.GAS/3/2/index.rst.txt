:orphan:




XPEHH/CMS.GAS/3/2
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population
when compared with the :doc:`../../../../../population/GAS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **28,260,000** and
**28,320,000**.
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


No genes overlap the focal region.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009182` (protein transport protein SEC61 subunit alpha),  :doc:`../../../../../gene/AGAP009183` (defective proboscis extension response).


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
    * - :doc:`../../../../../signal/IHS/BFS/3/1/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3R:27,940,000-28,260,000
      - 749
      - 100.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/3/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 42
        # data points      = 395
        # variables        = 4
        chi-square         = 99.686
        reduced chi-square = 0.255
        Akaike info crit   = -535.861
        Bayesian info crit = -519.945
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.92222475 +/- 0.118189 (6.15%) (init= 3)
        sigma:       0.29532617 +/- 0.026319 (8.91%) (init= 0.5)
        skew:       -0.99999999 +/- 0.014662 (1.47%) (init= 0)
        baseline:    1.43485157 +/- 0.027965 (1.95%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               = -0.519 
        C(amplitude, sigma)          = -0.418 
        C(amplitude, baseline)       = -0.196 
        C(sigma, baseline)           = -0.194 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 394
        # variables        = 1
        chi-square         = 181.692
        reduced chi-square = 0.462
        Akaike info crit   = -302.972
        Bayesian info crit = -298.996
    [[Variables]]
        c:   1.61384785 +/- 0.034254 (2.12%) (init= 1)



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


