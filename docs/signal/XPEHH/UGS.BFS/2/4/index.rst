:orphan:




XPEHH/UGS.BFS/2/4
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **14,374,895** and
**14,554,895**.
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


The following 9 genes overlap the focal region: :doc:`../../../../../gene/AGAP005347` (alpha-1,3-mannosyl-glycoprotein beta-1,2-N-acetylglucosaminyltransferase),  :doc:`../../../../../gene/AGAP005348`,  :doc:`../../../../../gene/AGAP005349`,  :doc:`../../../../../gene/AGAP005350`,  :doc:`../../../../../gene/AGAP005351` (DEAD box polypeptide 5),  :doc:`../../../../../gene/AGAP005352` (tyrosine-protein phosphatase non-receptor type 1),  :doc:`../../../../../gene/AGAP005353` (biogenesis of lysosome-related organelles complex 1 subunit 2),  :doc:`../../../../../gene/AGAP005354`,  :doc:`../../../../../gene/AGAP005355`.



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP005345`,  :doc:`../../../../../gene/AGAP005346`,  :doc:`../../../../../gene/AGAP005356` (predicted G-protein coupled receptor GPCR).


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
    * - :doc:`../../../../../signal/XPEHH/UGS.CMS/2/4/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2L:14,374,895-14,554,895
      - 92
      - 91.4%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/2/4/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 33
        # data points      = 569
        # variables        = 4
        chi-square         = 185.509
        reduced chi-square = 0.328
        Akaike info crit   = -629.723
        Bayesian info crit = -612.347
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.48577310 +/- 0.124166 (8.36%) (init= 3)
        sigma:       0.28782456 +/- 0.029290 (10.18%) (init= 0.5)
        skew:        0.16571507 +/- 0.115266 (69.56%) (init= 0)
        baseline:    1.16421414 +/- 0.026259 (2.26%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.532 
        C(sigma, baseline)           = -0.234 
        C(amplitude, baseline)       = -0.154 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 568
        # variables        = 1
        chi-square         = 244.294
        reduced chi-square = 0.431
        Akaike info crit   = -477.250
        Bayesian info crit = -472.908
    [[Variables]]
        c:   1.28186027 +/- 0.027540 (2.15%) (init= 1)



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


