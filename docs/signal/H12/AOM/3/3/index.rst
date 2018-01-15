:orphan:




H12/AOM/3/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3L** between positions **17,719,316** and
**17,759,316**.
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



Gene :doc:`../../../../../gene/AGAP011134` (LIM homeobox protein 5) overlaps the focal region.





The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP011130`:sup:`1` (NADH dehydrogenase (ubiquinone) 1 alpha subcomplex 10),  :doc:`../../../../../gene/AGAP028410`,  :doc:`../../../../../gene/AGAP011131` (F-type H -transporting ATPase subunit d),  :doc:`../../../../../gene/AGAP011132` (GINS complex subunit 3),  :doc:`../../../../../gene/AGAP011133`:sup:`1` (Inosine-5'-monophosphate dehydrogenase),  :doc:`../../../../../gene/AGAP011135` (synaptosomal-associated protein, 29kDa),  :doc:`../../../../../gene/AGAP011136`,  :doc:`../../../../../gene/AGAP011137` (Thiomorpholine-carboxylate dehydrogenase),  :doc:`../../../../../gene/AGAP011138` (myosin XVIII).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 63
        # data points      = 393
        # variables        = 4
        chi-square         = 0.022
        reduced chi-square = 0.000
        Akaike info crit   = -3846.736
        Bayesian info crit = -3830.840
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.05408939 +/- 0.005216 (9.64%) (init= 0.5)
        decay:       0.15065810 +/- 0.020939 (13.90%) (init= 0.5)
        skew:       -0.74385199 +/- 0.154284 (20.74%) (init= 0)
        baseline:    0.02372787 +/- 0.000394 (1.66%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.663 
        C(decay, skew)               =  0.350 
        C(decay, baseline)           = -0.201 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 392
        # variables        = 1
        chi-square         = 0.030
        reduced chi-square = 0.000
        Akaike info crit   = -3710.811
        Bayesian info crit = -3706.840
    [[Variables]]
        c:   0.02475691 +/- 0.000444 (1.79%) (init= 0.03)



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


