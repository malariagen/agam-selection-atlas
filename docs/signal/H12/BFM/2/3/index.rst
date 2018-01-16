:orphan:




H12/BFM/2/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,920,000** and
**40,960,000**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).





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


The following 7 genes overlap the focal region: :doc:`../../../../../gene/AGAP003643` (ubiquitin carboxyl-terminal hydrolase 34),  :doc:`../../../../../gene/AGAP003644` (mRpS11 - 28S ribosomal protein S11, mitochondrial),  :doc:`../../../../../gene/AGAP003645` (kelch-like protein 19),  :doc:`../../../../../gene/AGAP013307`,  :doc:`../../../../../gene/AGAP003646`,  :doc:`../../../../../gene/AGAP003647`,  :doc:`../../../../../gene/AGAP003648` (DNA-directed RNA polymerase II subunit RPB2).



The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003638`,  :doc:`../../../../../gene/AGAP003639` (Prolylcarboxypeptidase),  :doc:`../../../../../gene/AGAP003640`:sup:`1` (SP8905),  :doc:`../../../../../gene/AGAP003641`:sup:`1` (SP8907),  :doc:`../../../../../gene/AGAP003642`:sup:`1` (SP8898),  :doc:`../../../../../gene/AGAP003649`,  :doc:`../../../../../gene/AGAP003650` (translation initiation factor eIF-2B subunit alpha),  :doc:`../../../../../gene/AGAP003651` (Tyrosine-protein kinase Fes/Fps).


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
      - Peak Model :math:`\Delta_{i}`
      - Max Percentile
      - Known Loci
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/2/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2R:40,880,000-40,940,000
      - 1,181
      - 99.6%
      - nan
    * - :doc:`../../../../../signal/H12/BFS/2/4/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2R:40,640,000-41,060,000
      - 384
      - 95.9%
      - nan
    * - :doc:`../../../../../signal/IHS/BFM/2/2/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 2R:40,880,000-41,160,000
      - 312
      - 99.7%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/BFM/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 28
        # data points      = 396
        # variables        = 4
        chi-square         = 0.075
        reduced chi-square = 0.000
        Akaike info crit   = -3389.000
        Bayesian info crit = -3373.075
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.19691717 +/- 0.007808 (3.97%) (init= 0.5)
        decay:       0.25357434 +/- 0.014701 (5.80%) (init= 0.5)
        skew:       -0.02286927 +/- 0.056741 (248.11%) (init= 0)
        baseline:    0.02845731 +/- 0.000742 (2.61%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.687 
        C(decay, baseline)           = -0.261 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 395
        # variables        = 1
        chi-square         = 0.270
        reduced chi-square = 0.001
        Akaike info crit   = -2876.279
        Bayesian info crit = -2872.300
    [[Variables]]
        c:   0.03429287 +/- 0.001318 (3.84%) (init= 0.03)



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


