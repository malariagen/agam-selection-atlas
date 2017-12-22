:orphan:




H12 / Gabon *An. gambiae* / Chromosome 3 / #3
=============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GAS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **41,840,001** and
**41,960,000**.
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




The following 7 genes overlap the focal region: :doc:`../../../../../gene/AGAP009728` (ficolin),  :doc:`../../../../../gene/AGAP009729` (CCAP - cardioacceleratory peptide),  :doc:`../../../../../gene/AGAP009730` (myosin III),  :doc:`../../../../../gene/AGAP009731` (wingless-type MMTV integration site family, member 10A),  :doc:`../../../../../gene/AGAP009732` (Protein Wnt),  :doc:`../../../../../gene/AGAP009733` (wingless-type MMTV integration site family, member 6),  :doc:`../../../../../gene/AGAP009734` (wingless-type MMTV integration site family, member 1).



Gene :doc:`../../../../../gene/AGAP009727` (RhoGAP92B) is within 50 kbp of the focal region.



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

    :doc:`../../../../../signal/H12/AOM/3/2/index`, "3R:41,920,001-42,180,000", 182 (161 | 21)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/3/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GAS/3/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 31
        # data points      = 244
        # variables        = 3
        chi-square         = 0.043
        reduced chi-square = 0.000
        Akaike info crit   = -2104.728
        Bayesian info crit = -2094.237
    [[Variables]]
        amplitude:   0.04189601 +/- 0.009280 (22.15%) (init= 0.5)
        decay:       0.16138955 +/- 0.043012 (26.65%) (init= 0.5)
        c:           0.03166275 +/- 0.000979 (3.09%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.716 
        C(decay, c)                  = -0.370 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 144
        # variables        = 3
        chi-square         = 0.009
        reduced chi-square = 0.000
        Akaike info crit   = -1383.937
        Bayesian info crit = -1375.028
    [[Variables]]
        amplitude:   0.04111554 +/- 0.003107 (7.56%) (init= 0.5)
        decay:       1.18465454 +/- 0.189826 (16.02%) (init= 0.5)
        c:           0.02070269 +/- 0.001292 (6.24%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.743 
        C(amplitude, decay)          = -0.464 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 243
        # variables        = 1
        chi-square         = 0.047
        reduced chi-square = 0.000
        Akaike info crit   = -2074.546
        Bayesian info crit = -2071.053
    [[Variables]]
        c:   0.03348870 +/- 0.000896 (2.68%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 143
        # variables        = 1
        chi-square         = 0.022
        reduced chi-square = 0.000
        Akaike info crit   = -1255.683
        Bayesian info crit = -1252.720
    [[Variables]]
        c:   0.02845591 +/- 0.001032 (3.63%) (init= 0.03)


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


