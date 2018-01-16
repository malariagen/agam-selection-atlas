:orphan:




XPEHH/AOM.BFM/2/6
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/BFM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **48,280,000** and
**48,360,000**.
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


Gene :doc:`../../../../../gene/AGAP004039` (afadin) overlaps the focal region.



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013324` (putative G-protein coupled receptor GPCR),  :doc:`../../../../../gene/AGAP004035` (GPRFSH - putative glyco-protein hormone fsh-like receptor),  :doc:`../../../../../gene/AGAP004036`:sup:`1` (HPX7 - heme peroxidase 7),  :doc:`../../../../../gene/AGAP004038`:sup:`1` (HPX8 - heme peroxidase 8).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/6/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 481
        # variables        = 4
        chi-square         = 115.201
        reduced chi-square = 0.242
        Akaike info crit   = -679.442
        Bayesian info crit = -662.738
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.82161126 +/- 0.156707 (8.60%) (init= 3)
        sigma:       0.19121515 +/- 0.021848 (11.43%) (init= 0.5)
        skew:        0.87263898 +/- 0.138672 (15.89%) (init= 0)
        baseline:    1.91848492 +/- 0.023426 (1.22%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.501 
        C(sigma, skew)               = -0.396 
        C(sigma, baseline)           = -0.153 
        C(amplitude, baseline)       = -0.110 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 480
        # variables        = 1
        chi-square         = 157.483
        reduced chi-square = 0.329
        Akaike info crit   = -532.945
        Bayesian info crit = -528.771
    [[Variables]]
        c:   1.99157979 +/- 0.026171 (1.31%) (init= 1)



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


