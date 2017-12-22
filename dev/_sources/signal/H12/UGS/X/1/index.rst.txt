:orphan:




H12 / Uganda *An. gambiae* / Chromosome X / #1
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **15,320,001** and
**15,460,000**.
The evidence supporting this signal is
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks).

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




The following 13 genes overlap the focal region: :doc:`../../../../../gene/AGAP000822`,  :doc:`../../../../../gene/AGAP000823` (CD81 antigen),  :doc:`../../../../../gene/AGAP000824` (bone morphogenetic protein 5),  :doc:`../../../../../gene/AGAP000825`,  :doc:`../../../../../gene/AGAP000826` (cap-specific mRNA (nucleoside-2'-O-)-methyltransferase 1),  :doc:`../../../../../gene/AGAP000829` (calpain-15),  :doc:`../../../../../gene/AGAP000830` (CASPS7 - short caspase 7),  :doc:`../../../../../gene/AGAP000831` (DnaJ homolog subfamily C member 25),  :doc:`../../../../../gene/AGAP000832` (Derlin-2/3),  :doc:`../../../../../gene/AGAP000833` (MIP - myoinhibitory-like peptide),  :doc:`../../../../../gene/AGAP000834`,  :doc:`../../../../../gene/AGAP000835`,  :doc:`../../../../../gene/AGAP028655`.




The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP000820`:sup:`4` (CPR125 - cuticular protein RR-2 family 125),  :doc:`../../../../../gene/AGAP000821`,  :doc:`../../../../../gene/AGAP013506`.


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

    :doc:`../../../../../signal/H12/BFM/X/1/index`, "X:15,100,001-15,380,000", 954 (534 | 420)
    



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/X/1/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/X/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/UGS/X/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 27
        # data points      = 145
        # variables        = 3
        chi-square         = 0.007
        reduced chi-square = 0.000
        Akaike info crit   = -1443.489
        Bayesian info crit = -1434.559
    [[Variables]]
        amplitude:   0.07164169 +/- 0.002367 (3.31%) (init= 0.5)
        decay:       1.37780655 +/- 0.106032 (7.70%) (init= 0.5)
        c:           0.00688216 +/- 0.001256 (18.26%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.805 
        C(amplitude, decay)          = -0.276 
        C(amplitude, c)              = -0.150 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 39
        # data points      = 147
        # variables        = 3
        chi-square         = 0.029
        reduced chi-square = 0.000
        Akaike info crit   = -1245.669
        Bayesian info crit = -1236.698
    [[Variables]]
        amplitude:   0.08728579 +/- 0.008517 (9.76%) (init= 0.5)
        decay:       0.52782288 +/- 0.079199 (15.00%) (init= 0.5)
        c:           0.02245157 +/- 0.001472 (6.56%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.661 
        C(decay, c)                  = -0.467 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 144
        # variables        = 1
        chi-square         = 0.048
        reduced chi-square = 0.000
        Akaike info crit   = -1150.027
        Bayesian info crit = -1147.057
    [[Variables]]
        c:   0.02172094 +/- 0.001531 (7.05%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 146
        # variables        = 1
        chi-square         = 0.053
        reduced chi-square = 0.000
        Akaike info crit   = -1154.942
        Bayesian info crit = -1151.959
    [[Variables]]
        c:   0.02916075 +/- 0.001579 (5.42%) (init= 0.03)


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


