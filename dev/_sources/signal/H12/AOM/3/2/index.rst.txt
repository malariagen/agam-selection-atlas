:orphan:




H12 / Angola *An. coluzzii* / Chromosome 3 / #2
===============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **41,920,001** and
**42,180,000**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the top right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

Genes
-----




The following 16 genes overlap the focal region: :doc:`../../../../../gene/AGAP009733` (wingless-type MMTV integration site family, member 6),  :doc:`../../../../../gene/AGAP009734` (wingless-type MMTV integration site family, member 1),  :doc:`../../../../../gene/AGAP009735` (wingless-type MMTV integration site family, member 16),  :doc:`../../../../../gene/AGAP009736` (solute carrier family 4 member 10),  :doc:`../../../../../gene/AGAP009737` (Elongation factor G, mitochondrial),  :doc:`../../../../../gene/AGAP009738`:sup:`1` (GRX3 - glutaredoxin),  :doc:`../../../../../gene/AGAP009739` (vacuolar protein sorting 52 homolog),  :doc:`../../../../../gene/AGAP009740` (tRNA (guanine26-N2/guanine27-N2)-dimethyltransferase),  :doc:`../../../../../gene/AGAP009741`,  :doc:`../../../../../gene/AGAP009742` (splicing factor, arginine/serine-rich 2),  :doc:`../../../../../gene/AGAP009743` (ribonuclease Z),  :doc:`../../../../../gene/AGAP009744`,  :doc:`../../../../../gene/AGAP009745` (Sugar transporter ERD6-like 4),  :doc:`../../../../../gene/AGAP009746` (RuvB-like protein 2),  :doc:`../../../../../gene/AGAP009747` (gamma-interferon-inducible lysosomal thiol reductase precursor),  :doc:`../../../../../gene/AGAP028645` (aryl hydrocarbon receptor nuclear translocator).



Gene :doc:`../../../../../gene/AGAP009732` (Protein Wnt) is within 50 kbp of the focal region.



Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

The following selection signals have an focus which overlaps with the
focus of this signal.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    :doc:`../../../../../signal/H12/GAS/3/3/index`, "3R:41,840,001-41,960,000", 158 (30 | 128)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/2/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/3/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 67
        # data points      = 294
        # variables        = 3
        chi-square         = 0.046
        reduced chi-square = 0.000
        Akaike info crit   = -2569.190
        Bayesian info crit = -2558.139
    [[Variables]]
        amplitude:   0.07692110 +/- 0.007298 (9.49%) (init= 0.5)
        decay:       0.28398721 +/- 0.032060 (11.29%) (init= 0.5)
        c:           0.02463415 +/- 0.000892 (3.62%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.723 
        C(decay, c)                  = -0.426 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 37
        # data points      = 194
        # variables        = 3
        chi-square         = 0.071
        reduced chi-square = 0.000
        Akaike info crit   = -1530.141
        Bayesian info crit = -1520.337
    [[Variables]]
        amplitude:   0.06427053 +/- 0.017452 (27.16%) (init= 0.5)
        decay:       0.26670192 +/- 0.098347 (36.88%) (init= 0.5)
        c:           0.05399816 +/- 0.001486 (2.75%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.737 
        C(decay, c)                  = -0.271 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 293
        # variables        = 1
        chi-square         = 0.078
        reduced chi-square = 0.000
        Akaike info crit   = -2407.899
        Bayesian info crit = -2404.218
    [[Variables]]
        c:   0.02949232 +/- 0.000958 (3.25%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 193
        # variables        = 1
        chi-square         = 0.077
        reduced chi-square = 0.000
        Akaike info crit   = -1508.435
        Bayesian info crit = -1505.172
    [[Variables]]
        c:   0.05569574 +/- 0.001441 (2.59%) (init= 0.03)


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


