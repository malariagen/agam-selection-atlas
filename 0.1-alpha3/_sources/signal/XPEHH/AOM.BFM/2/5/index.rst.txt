:orphan:




XPEHH/AOM.BFM/2/5
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/BFM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **8,140,000** and
**8,240,000**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP001679`,  :doc:`../../../../../gene/AGAP001680`,  :doc:`../../../../../gene/AGAP001681` (ubiquitin conjugation factor E4 A),  :doc:`../../../../../gene/AGAP001682` (Mitochondrial inner membrane protease subunit 1).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP001678`,  :doc:`../../../../../gene/AGAP013310`,  :doc:`../../../../../gene/AGAP001683` (calcium/calmodulin-dependent serine protein kinase).


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
    * - :doc:`../../../../../signal/IHS/AOM/2/2/index`
      - IHS
      - Angola *An. coluzzii*
      - 2R:8,160,000-8,280,000
      - 230
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/2/4/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2R:8,120,000-8,320,000
      - 107
      - 78.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/5/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/5/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/5/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 62
        # data points      = 217
        # variables        = 4
        chi-square         = 29.301
        reduced chi-square = 0.138
        Akaike info crit   = -426.492
        Bayesian info crit = -412.972
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.29288586 +/- 0.085702 (6.63%) (init= 3)
        sigma:       0.26378668 +/- 0.029455 (11.17%) (init= 0.5)
        skew:       -0.99999997 +/- 0.136206 (13.62%) (init= 0)
        baseline:    1.40347689 +/- 0.030670 (2.19%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.612 
        C(amplitude, sigma)          = -0.382 
        C(amplitude, baseline)       = -0.293 
        C(sigma, baseline)           = -0.249 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 216
        # variables        = 1
        chi-square         = 64.696
        reduced chi-square = 0.301
        Akaike info crit   = -258.406
        Bayesian info crit = -255.030
    [[Variables]]
        c:   1.63883778 +/- 0.037324 (2.28%) (init= 1)



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


