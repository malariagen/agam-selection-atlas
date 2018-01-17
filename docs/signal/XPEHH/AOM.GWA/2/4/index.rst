:orphan:




XPEHH/AOM.GWA/2/4
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **8,120,000** and
**8,320,000**.
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


The following 6 genes overlap the focal region: :doc:`../../../../../gene/AGAP013310`,  :doc:`../../../../../gene/AGAP001679`,  :doc:`../../../../../gene/AGAP001680`,  :doc:`../../../../../gene/AGAP001681` (ubiquitin conjugation factor E4 A),  :doc:`../../../../../gene/AGAP001682` (Mitochondrial inner membrane protease subunit 1),  :doc:`../../../../../gene/AGAP001683` (calcium/calmodulin-dependent serine protein kinase).



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP001678`,  :doc:`../../../../../gene/AGAP001684` (Alkaline phosphatase).


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
    * - :doc:`../../../../../signal/H12/AOM/2/1/index`
      - H12
      - Angola *An. coluzzii*
      - 2R:8,280,000-8,340,000
      - 479
      - 97.0%
      - nan
    * - :doc:`../../../../../signal/IHS/AOM/2/2/index`
      - IHS
      - Angola *An. coluzzii*
      - 2R:8,160,000-8,280,000
      - 230
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.BFM/2/5/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2R:8,140,000-8,240,000
      - 168
      - 89.0%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 161
        # variables        = 4
        chi-square         = 14.696
        reduced chi-square = 0.094
        Akaike info crit   = -377.407
        Bayesian info crit = -365.081
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.04413636 +/- 0.089480 (8.57%) (init= 3)
        sigma:       0.23229447 +/- 0.036642 (15.77%) (init= 0.5)
        skew:       -0.58900568 +/- 0.189400 (32.16%) (init= 0)
        baseline:    1.18031973 +/- 0.027791 (2.35%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.590 
        C(amplitude, sigma)          = -0.471 
        C(amplitude, baseline)       = -0.256 
        C(sigma, baseline)           = -0.192 
        C(amplitude, skew)           = -0.165 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 160
        # variables        = 1
        chi-square         = 29.175
        reduced chi-square = 0.183
        Akaike info crit   = -270.299
        Bayesian info crit = -267.224
    [[Variables]]
        c:   1.32914129 +/- 0.033862 (2.55%) (init= 1)



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


