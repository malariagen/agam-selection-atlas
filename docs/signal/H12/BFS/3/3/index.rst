:orphan:




H12 / Burkina Faso *An. gambiae* / Chromosome 3 / #3
====================================================

This page describes a signal of selection found in the
:doc:`../../../../../population/BFS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **4,580,001** and
**4,760,000**.
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



Gene :doc:`../../../../../gene/AGAP028427` overlaps the focal region.





The following 14 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP008028` (voltage-dependent calcium channel beta, invertebrate),  :doc:`../../../../../gene/AGAP008033`,  :doc:`../../../../../gene/AGAP013760`,  :doc:`../../../../../gene/AGAP008034` (solute carrier family 39 (zinc transporter), member 7),  :doc:`../../../../../gene/AGAP008035`,  :doc:`../../../../../gene/AGAP008036`,  :doc:`../../../../../gene/AGAP008037` (KDEL (Lys-Asp-Glu-Leu) containing 1, isoform CRA_a),  :doc:`../../../../../gene/AGAP008039` (protein kinase A),  :doc:`../../../../../gene/AGAP008040`,  :doc:`../../../../../gene/AGAP008041` (RING finger protein 121),  :doc:`../../../../../gene/AGAP008042`:sup:`1` (pyridine nucleotide-disulfide oxidoreductase domain 1),  :doc:`../../../../../gene/AGAP008043` (mRpS18B - 28S ribosomal protein S18B, mitochondrial),  :doc:`../../../../../gene/AGAP008044`:sup:`1` (programmed cell death 8 (apoptosis-inducing factor)),  :doc:`../../../../../gene/AGAP008045` (transcription initiation factor TFIID subunit 13).


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

    :doc:`../../../../../signal/H12/GNS/3/2/index`, "3R:4,580,001-4,740,000", 235 (152 | 82)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 151
        # variables        = 3
        chi-square         = 0.002
        reduced chi-square = 0.000
        Akaike info crit   = -1730.904
        Bayesian info crit = -1721.853
    [[Variables]]
        amplitude:   0.01636842 +/- 0.001007 (6.15%) (init= 0.5)
        decay:       1.74159251 +/- 0.303912 (17.45%) (init= 0.5)
        c:           0.00736559 +/- 0.000791 (10.74%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.873 
        C(amplitude, c)              = -0.304 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 150
        # variables        = 3
        chi-square         = 0.003
        reduced chi-square = 0.000
        Akaike info crit   = -1594.470
        Bayesian info crit = -1585.438
    [[Variables]]
        amplitude:   0.00970744 +/- 0.001852 (19.08%) (init= 0.5)
        decay:       1.18732565 +/- 0.476336 (40.12%) (init= 0.5)
        c:           0.01285424 +/- 0.000770 (5.99%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.750 
        C(amplitude, decay)          = -0.458 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1585.386
        Bayesian info crit = -1582.376
    [[Variables]]
        c:   0.01184931 +/- 0.000413 (3.48%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.004
        reduced chi-square = 0.000
        Akaike info crit   = -1572.816
        Bayesian info crit = -1569.812
    [[Variables]]
        c:   0.01458435 +/- 0.000417 (2.86%) (init= 0.03)


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


