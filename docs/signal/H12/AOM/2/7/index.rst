:orphan:




H12/AOM/2/7
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2R** between positions **34,040,000** and
**34,220,000**.
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


The following 9 genes overlap the focal region: :doc:`../../../../../gene/AGAP003226` (dynein heavy chain 2),  :doc:`../../../../../gene/AGAP003227` (nucleoside-diphosphate kinase),  :doc:`../../../../../gene/AGAP003228` (histone acetyltransferase type B subunit 2),  :doc:`../../../../../gene/AGAP003229`,  :doc:`../../../../../gene/AGAP003230` (poly (ADP-ribose) polymerase),  :doc:`../../../../../gene/AGAP003231`:sup:`1` (NADH dehydrogenase (ubiquinone) iron-sulfur protein 7, mitochondrial),  :doc:`../../../../../gene/AGAP003232` (splicing factor 4),  :doc:`../../../../../gene/AGAP013304`:sup:`1`,  :doc:`../../../../../gene/AGAP003233`:sup:`1`.



The following 14 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003212` (Adrenodoxin),  :doc:`../../../../../gene/AGAP003213` (nijmegen breakage syndrome protein 1),  :doc:`../../../../../gene/AGAP003214`,  :doc:`../../../../../gene/AGAP003215` (26S proteasome regulatory subunit T2),  :doc:`../../../../../gene/AGAP003216` (26S proteasome regulatory subunit T2),  :doc:`../../../../../gene/AGAP003217` (mRpS6 - 28S ribosomal protein S6, mitochondrial),  :doc:`../../../../../gene/AGAP003218`,  :doc:`../../../../../gene/AGAP003219`,  :doc:`../../../../../gene/AGAP003220`,  :doc:`../../../../../gene/AGAP003221` (ABCC3 - ATP-binding cassette transporter (ABC transporter) family C member 3),  :doc:`../../../../../gene/AGAP003222` (phosphatidylinositol glycan, class N),  :doc:`../../../../../gene/AGAP003224`,  :doc:`../../../../../gene/AGAP003225`,  :doc:`../../../../../gene/AGAP003235` (lachesin).


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
    * - :doc:`../../../../../signal/IHS/AOM/2/3/index`
      - IHS
      - Angola *An. coluzzii*
      - 2R:33,940,000-34,440,000
      - 213
      - 99.8%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/7/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/7/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/2/7/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 397
        # variables        = 4
        chi-square         = 0.064
        reduced chi-square = 0.000
        Akaike info crit   = -3459.820
        Bayesian info crit = -3443.884
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.03626735 +/- 0.002027 (5.59%) (init= 0.5)
        sigma:       1.19266080 +/- 0.094898 (7.96%) (init= 0.5)
        skew:       -0.99999999 +/- 0.022512 (2.25%) (init= 0)
        baseline:    0.02154307 +/- 0.000897 (4.16%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               =  0.472 
        C(sigma, baseline)           = -0.433 
        C(amplitude, baseline)       = -0.319 
        C(amplitude, sigma)          = -0.283 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 7
        # data points      = 396
        # variables        = 1
        chi-square         = 0.111
        reduced chi-square = 0.000
        Akaike info crit   = -3237.452
        Bayesian info crit = -3233.471
    [[Variables]]
        c:   0.02980393 +/- 0.000842 (2.83%) (init= 0.03)



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


