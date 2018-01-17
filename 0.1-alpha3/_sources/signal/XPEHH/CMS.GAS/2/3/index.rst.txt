:orphan:




XPEHH/CMS.GAS/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` population
when compared with the :doc:`../../../../../population/GAS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **28,560,000** and
**28,800,000**.
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


The following 12 genes overlap the focal region: :doc:`../../../../../gene/AGAP002875` (protein HEXIM1/2),  :doc:`../../../../../gene/AGAP013244` (adenosine deaminase, tRNA-specific 2, TAD2 homolog),  :doc:`../../../../../gene/AGAP002876` (single-strand selective monofunctional uracil DNA glycosylase),  :doc:`../../../../../gene/AGAP002877` (Tetratricopeptide repeat protein 30 homolog),  :doc:`../../../../../gene/AGAP002878` (Cystatin-like protein),  :doc:`../../../../../gene/AGAP002879` (cathepsin F),  :doc:`../../../../../gene/AGAP002880` (COP9 signalosome complex subunit 5),  :doc:`../../../../../gene/AGAP002881` (GPRNPR1 - putative neuropeptide receptor 1),  :doc:`../../../../../gene/AGAP002883`:sup:`1`,  :doc:`../../../../../gene/AGAP013115`,  :doc:`../../../../../gene/AGAP002884` (V-type H -transporting ATPase subunit B),  :doc:`../../../../../gene/AGAP002885`.



The following 9 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP002859` (solute carrier family 8 (sodium/calcium exchanger)),  :doc:`../../../../../gene/AGAP013202`,  :doc:`../../../../../gene/AGAP000586`,  :doc:`../../../../../gene/AGAP002872` (lipase),  :doc:`../../../../../gene/AGAP002873`,  :doc:`../../../../../gene/AGAP013069`,  :doc:`../../../../../gene/AGAP002874`,  :doc:`../../../../../gene/AGAP002886` (GPRNNA2 - putative GPCR class a orphan receptor 2),  :doc:`../../../../../gene/AGAP002888` (GPRNNA3 - putative GPCR class a orphan receptor 3).


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
    * - :doc:`../../../../../signal/IHS/UGS/2/1/index`
      - IHS
      - Uganda *An. gambiae*
      - 2R:28,280,000-28,700,000
      - 1,661
      - 100.0%
      - Cyp6p
    * - :doc:`../../../../../signal/IHS/CMS/2/1/index`
      - IHS
      - Cameroon *An. gambiae*
      - 2R:28,240,000-28,560,000
      - 1,249
      - 100.0%
      - Cyp6p
    * - :doc:`../../../../../signal/IHS/GNS/2/1/index`
      - IHS
      - Guinea *An. gambiae*
      - 2R:28,440,000-28,700,000
      - 1,134
      - 99.8%
      - Cyp6p
    * - :doc:`../../../../../signal/H12/CMS/2/1/index`
      - H12
      - Cameroon *An. gambiae*
      - 2R:28,460,000-28,560,000
      - 1,124
      - 100.0%
      - Cyp6p
    * - :doc:`../../../../../signal/XPEHH/UGS.GWA/2/1/index`
      - XPEHH
      - Uganda *An. gambiae*
      - 2R:28,460,000-28,600,000
      - 758
      - 99.7%
      - Cyp6p
    * - :doc:`../../../../../signal/XPEHH/CMS.GWA/2/2/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 2R:28,420,000-28,620,000
      - 578
      - 98.7%
      - Cyp6p
    * - :doc:`../../../../../signal/IHS/BFM/2/1/index`
      - IHS
      - Burkina Faso *An. coluzzii*
      - 2R:28,700,000-29,020,000
      - 468
      - 99.8%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/CMS.GAS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 48
        # data points      = 518
        # variables        = 4
        chi-square         = 187.839
        reduced chi-square = 0.365
        Akaike info crit   = -517.455
        Bayesian info crit = -500.455
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.03391137 +/- 0.146743 (7.21%) (init= 3)
        sigma:       0.23282177 +/- 0.021241 (9.12%) (init= 0.5)
        skew:       -0.58081249 +/- 0.107541 (18.52%) (init= 0)
        baseline:    1.62486893 +/- 0.028543 (1.76%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, sigma)          = -0.505 
        C(sigma, skew)               =  0.289 
        C(sigma, baseline)           = -0.198 
        C(amplitude, baseline)       = -0.152 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 517
        # variables        = 1
        chi-square         = 274.163
        reduced chi-square = 0.531
        Akaike info crit   = -325.943
        Bayesian info crit = -321.695
    [[Variables]]
        c:   1.76148225 +/- 0.032057 (1.82%) (init= 1)



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


