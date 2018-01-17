:orphan:




IHS/BFM/2/3
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2L** between positions **24,754,895** and
**25,434,895**.
The evidence supporting this signal is
**strong** (:math:`\Delta_{i}` >= 100 on both flanks).


This signal overlaps the :doc:`../../../../../known-locus/rdl`, a genome
region with prior evidence of an association with insecticide resistance and/or recent positive selection in
*Anopheles* mosquitoes.




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


The following 11 genes overlap the focal region: :doc:`../../../../../gene/AGAP006018`,  :doc:`../../../../../gene/AGAP006019` (maltase),  :doc:`../../../../../gene/AGAP006020`:sup:`1` (tryptophan 5-monooxygenase),  :doc:`../../../../../gene/AGAP006021` (JNK-interacting protein 1),  :doc:`../../../../../gene/AGAP006022` (Bhlh_PAS),  :doc:`../../../../../gene/AGAP006023`:sup:`1` (tyrosine 3-monooxygenase),  :doc:`../../../../../gene/AGAP006024`,  :doc:`../../../../../gene/AGAP006025` (Ras-like protein family member),  :doc:`../../../../../gene/AGAP006026`:sup:`2`,  :doc:`../../../../../gene/AGAP006027`:sup:`2` (glutamate receptor, ionotropic , AMPA),  :doc:`../../../../../gene/AGAP006028`:sup:`2` (Rdl - GABA-gated chloride channel subunit).



The following 6 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006029`,  :doc:`../../../../../gene/AGAP006030` (mfrn - mitoferrin),  :doc:`../../../../../gene/AGAP006031` (nuclear pore complex protein Nup54),  :doc:`../../../../../gene/AGAP006032`,  :doc:`../../../../../gene/AGAP006033`,  :doc:`../../../../../gene/AGAP006034`.


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
    * - :doc:`../../../../../signal/H12/BFM/2/2/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 2L:25,434,895-25,494,895
      - 1,172
      - 98.4%
      - Rdl
    * - :doc:`../../../../../signal/H12/AOM/2/3/index`
      - H12
      - Angola *An. coluzzii*
      - 2L:25,214,895-25,334,895
      - 398
      - 95.7%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/2/4/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2L:25,434,895-25,474,895
      - 388
      - 98.3%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/CMS.UGS/2/2/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 2L:25,414,895-25,454,895
      - 291
      - 90.3%
      - Rdl
    * - :doc:`../../../../../signal/IHS/BFS/2/5/index`
      - IHS
      - Burkina Faso *An. gambiae*
      - 2L:25,434,895-25,614,895
      - 256
      - 99.8%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/2/6/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2L:25,434,895-25,474,895
      - 138
      - 95.3%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/2/6/index`
      - XPEHH
      - Angola *An. coluzzii*
      - 2L:25,254,895-25,414,895
      - 92
      - 83.9%
      - Rdl
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 53
        # data points      = 349
        # variables        = 4
        chi-square         = 137.951
        reduced chi-square = 0.400
        Akaike info crit   = -315.933
        Bayesian info crit = -300.513
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.67582524 +/- 0.128281 (4.79%) (init= 3)
        sigma:       1.44113319 +/- 0.079125 (5.49%) (init= 0.5)
        skew:       -0.41309249 +/- 0.053281 (12.90%) (init= 0)
        baseline:    2.22028202 +/- 0.046991 (2.12%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, baseline)           = -0.482 
        C(amplitude, sigma)          = -0.454 
        C(sigma, skew)               =  0.241 
        C(amplitude, baseline)       = -0.204 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 348
        # variables        = 1
        chi-square         = 334.758
        reduced chi-square = 0.965
        Akaike info crit   = -11.500
        Bayesian info crit = -7.648
    [[Variables]]
        c:   2.73605201 +/- 0.052650 (1.92%) (init= 1)



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


