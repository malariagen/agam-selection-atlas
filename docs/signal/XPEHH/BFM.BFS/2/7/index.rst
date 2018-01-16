:orphan:




XPEHH/BFM.BFS/2/7
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **41,094,895** and
**41,154,895**.
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


Gene :doc:`../../../../../gene/AGAP028463` overlaps the focal region.



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP007028` (glucosyl/glucuronosyl transferases),  :doc:`../../../../../gene/AGAP007029` (glucosyl/glucuronosyl transferases),  :doc:`../../../../../gene/AGAP028734`,  :doc:`../../../../../gene/AGAP028733`,  :doc:`../../../../../gene/AGAP028735`,  :doc:`../../../../../gene/AGAP007031` (Scabrous protein).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/7/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/7/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/BFM.BFS/2/7/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 820
        # variables        = 4
        chi-square         = 119.057
        reduced chi-square = 0.146
        Akaike info crit   = -1574.355
        Bayesian info crit = -1555.518
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.98874289 +/- 0.094614 (9.57%) (init= 3)
        sigma:       0.27460608 +/- 0.035901 (13.07%) (init= 0.5)
        skew:       -0.99999547 +/- 0.167141 (16.71%) (init= 0)
        baseline:    1.24808211 +/- 0.014002 (1.12%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.558 
        C(amplitude, sigma)          = -0.420 
        C(sigma, baseline)           = -0.156 
        C(amplitude, baseline)       = -0.106 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 819
        # variables        = 1
        chi-square         = 134.741
        reduced chi-square = 0.165
        Akaike info crit   = -1476.075
        Bayesian info crit = -1471.367
    [[Variables]]
        c:   1.28664618 +/- 0.014181 (1.10%) (init= 1)



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


