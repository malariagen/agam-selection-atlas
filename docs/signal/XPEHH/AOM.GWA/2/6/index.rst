:orphan:




XPEHH/AOM.GWA/2/6
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/GWA` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2L** between positions **25,254,895** and
**25,414,895**.
The evidence supporting this signal is
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks).


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


The following 2 genes overlap the focal region: :doc:`../../../../../gene/AGAP006027`:sup:`2` (glutamate receptor, ionotropic , AMPA),  :doc:`../../../../../gene/AGAP006028`:sup:`2` (Rdl - GABA-gated chloride channel subunit).



The following 4 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006029`,  :doc:`../../../../../gene/AGAP006030` (mfrn - mitoferrin),  :doc:`../../../../../gene/AGAP006031` (nuclear pore complex protein Nup54),  :doc:`../../../../../gene/AGAP006032`.


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
    * - :doc:`../../../../../signal/H12/AOM/2/3/index`
      - H12
      - Angola *An. coluzzii*
      - 2L:25,214,895-25,334,895
      - 398
      - 95.7%
      - Rdl
    * - :doc:`../../../../../signal/IHS/BFM/2/3/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 2L:24,754,895-25,434,895
      - 304
      - 99.9%
      - Rdl
    * - :doc:`../../../../../signal/XPEHH/CMS.UGS/2/2/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 2L:25,414,895-25,454,895
      - 291
      - 90.3%
      - Rdl
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/6/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/6/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.GWA/2/6/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 60
        # data points      = 142
        # variables        = 4
        chi-square         = 16.603
        reduced chi-square = 0.120
        Akaike info crit   = -296.762
        Bayesian info crit = -284.939
    [[Variables]]
        center:      0 (fixed)
        amplitude:   1.23747441 +/- 0.112154 (9.06%) (init= 3)
        decay:       0.95216575 +/- 0.210834 (22.14%) (init= 0.5)
        skew:       -1          +/- 6.04e-06 (0.00%) (init= 0)
        baseline:    1.27441424 +/- 0.051260 (4.02%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, baseline)           = -0.589 
        C(decay, skew)               = -0.457 
        C(amplitude, decay)          = -0.380 
        C(amplitude, baseline)       = -0.192 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 141
        # variables        = 1
        chi-square         = 32.686
        reduced chi-square = 0.233
        Akaike info crit   = -204.117
        Bayesian info crit = -201.168
    [[Variables]]
        c:   1.59693008 +/- 0.040691 (2.55%) (init= 1)



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


