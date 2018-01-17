:orphan:




H12/AOM/X/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**X** between positions **14,500,000** and
**14,600,000**.
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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP000795`,  :doc:`../../../../../gene/AGAP000797` (E3 ubiquitin-protein ligase HECW2).



The following 3 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP013289`,  :doc:`../../../../../gene/AGAP000798`:sup:`2` (GLURIIc - ionotropic receptor GLURIIc),  :doc:`../../../../../gene/AGAP000801`:sup:`2` (GLURIIb - ionotropic receptor GLURIIb).


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
    * - :doc:`../../../../../signal/XPEHH/GAS.GWA/X/1/index`
      - XPEHH
      - Gabon *An. gambiae*
      - X:14,460,000-14,860,000
      - 301
      - 98.5%
      - nan
    * - :doc:`../../../../../signal/XPEHH/AOM.GWA/X/2/index`
      - XPEHH
      - Angola *An. coluzzii*
      - X:14,500,000-15,180,000
      - 228
      - 98.5%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/AOM/X/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 210
        # data points      = 390
        # variables        = 4
        chi-square         = 0.104
        reduced chi-square = 0.000
        Akaike info crit   = -3203.146
        Bayesian info crit = -3187.282
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.05782970 +/- 0.003249 (5.62%) (init= 0.5)
        decay:       2.15349257 +/- 0.258947 (12.02%) (init= 0.5)
        skew:       -0.99999999 +/- 0.205505 (20.55%) (init= 0)
        baseline:    0.02691357 +/- 0.001654 (6.15%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.690 
        C(decay, skew)               = -0.354 
        C(amplitude, baseline)       = -0.289 
        C(amplitude, decay)          = -0.274 
        C(skew, baseline)            =  0.224 
        C(amplitude, skew)           = -0.147 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 10
        # data points      = 389
        # variables        = 1
        chi-square         = 0.192
        reduced chi-square = 0.000
        Akaike info crit   = -2959.783
        Bayesian info crit = -2955.819
    [[Variables]]
        c:   0.04327335 +/- 0.001127 (2.61%) (init= 0.03)



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


