:orphan:




XPEHH/CMS.GAS/3/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population
when compared with the :doc:`../../../../../population/GAS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**3R** between positions **4,300,000** and
**4,380,000**.
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


The following 4 genes overlap the focal region: :doc:`../../../../../gene/AGAP008018`:sup:`1` (CYP12F4 - cytochrome P450),  :doc:`../../../../../gene/AGAP008019`:sup:`1` (CYP12F3 - cytochrome P450),  :doc:`../../../../../gene/AGAP008020`:sup:`1` (CYP12F2 - cytochrome P450),  :doc:`../../../../../gene/AGAP008022`:sup:`1` (CYP12F1 - cytochrome P450).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008017`,  :doc:`../../../../../gene/AGAP008023` (en - segmentation polarity homeobox protein engrailed),  :doc:`../../../../../gene/AGAP008025` (Homeobox protein engrailed-like).


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
    * - :doc:`../../../../../signal/IHS/BFS/3/2/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 3R:4,340,000-4,740,000
      - 504
      - 95.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 47
        # data points      = 582
        # variables        = 4
        chi-square         = 81.388
        reduced chi-square = 0.141
        Akaike info crit   = -1136.934
        Bayesian info crit = -1119.468
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.54764121 +/- 0.049067 (8.96%) (init= 3)
        sigma:       0.67949193 +/- 0.097804 (14.39%) (init= 0.5)
        skew:        0.99999853 +/- 0.168452 (16.85%) (init= 0)
        baseline:    1.18513905 +/- 0.019758 (1.67%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               = -0.405 
        C(amplitude, sigma)          = -0.385 
        C(amplitude, baseline)       = -0.316 
        C(sigma, baseline)           = -0.299 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 581
        # variables        = 1
        chi-square         = 101.968
        reduced chi-square = 0.176
        Akaike info crit   = -1008.996
        Bayesian info crit = -1004.631
    [[Variables]]
        c:   1.30968037 +/- 0.017394 (1.33%) (init= 1)



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


