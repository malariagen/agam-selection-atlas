:orphan:




IHS/BFM/2/2
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/BFM` populationusing the :doc:`../../../../../method/IHS` statistic.The focus of this signal is on chromosome arm
**2R** between positions **40,880,000** and
**41,160,000**.
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


The following 20 genes overlap the focal region: :doc:`../../../../../gene/AGAP003639` (Prolylcarboxypeptidase),  :doc:`../../../../../gene/AGAP003640`:sup:`1` (SP8905),  :doc:`../../../../../gene/AGAP003641`:sup:`1` (SP8907),  :doc:`../../../../../gene/AGAP003642`:sup:`1` (SP8898),  :doc:`../../../../../gene/AGAP003643` (ubiquitin carboxyl-terminal hydrolase 34),  :doc:`../../../../../gene/AGAP003644` (mRpS11 - 28S ribosomal protein S11, mitochondrial),  :doc:`../../../../../gene/AGAP003645` (kelch-like protein 19),  :doc:`../../../../../gene/AGAP013307`,  :doc:`../../../../../gene/AGAP003646`,  :doc:`../../../../../gene/AGAP003647`,  :doc:`../../../../../gene/AGAP003648` (DNA-directed RNA polymerase II subunit RPB2),  :doc:`../../../../../gene/AGAP003649`,  :doc:`../../../../../gene/AGAP003650` (translation initiation factor eIF-2B subunit alpha),  :doc:`../../../../../gene/AGAP003651` (Tyrosine-protein kinase Fes/Fps),  :doc:`../../../../../gene/AGAP012992`,  :doc:`../../../../../gene/AGAP013502`,  :doc:`../../../../../gene/AGAP003652`:sup:`1` (aldehyde dehydrogenase (NAD )),  :doc:`../../../../../gene/AGAP003654` (GPRCAL3 - putative calcitonin receptor 3),  :doc:`../../../../../gene/AGAP003655` (RNA methyltransferase like 1),  :doc:`../../../../../gene/AGAP013179`.



The following 2 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP003638`,  :doc:`../../../../../gene/AGAP003656` (Terribly reduced optic lobes, isoform B).


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
    * - :doc:`../../../../../signal/XPEHH/BFS.UGS/2/2/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 2R:40,880,000-40,940,000
      - 1,181
      - 99.6%
      - nan
    * - :doc:`../../../../../signal/XPEHH/CMS.UGS/2/1/index`
      - XPEHH
      - Cameroon *An. gambiae*
      - 2R:41,020,000-41,400,000
      - 943
      - 99.7%
      - nan
    * - :doc:`../../../../../signal/H12/BFM/2/3/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 2R:40,920,000-40,960,000
      - 512
      - 97.6%
      - nan
    * - :doc:`../../../../../signal/H12/BFS/2/4/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 2R:40,640,000-41,060,000
      - 384
      - 95.9%
      - nan
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/2/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/2/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/IHS/BFM/2/2/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 42
        # data points      = 530
        # variables        = 4
        chi-square         = 245.952
        reduced chi-square = 0.468
        Akaike info crit   = -398.903
        Bayesian info crit = -381.812
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.73005639 +/- 0.156535 (5.73%) (init= 3)
        sigma:       0.47670524 +/- 0.037670 (7.90%) (init= 0.5)
        skew:        0.99999989 +/- 0.095591 (9.56%) (init= 0)
        baseline:    3.20142879 +/- 0.033769 (1.05%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(sigma, skew)               = -0.665 
        C(amplitude, sigma)          = -0.465 
        C(sigma, baseline)           = -0.224 
        C(amplitude, baseline)       = -0.133 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 529
        # variables        = 1
        chi-square         = 447.893
        reduced chi-square = 0.848
        Akaike info crit   = -86.044
        Bayesian info crit = -81.773
    [[Variables]]
        c:   3.46271854 +/- 0.040044 (1.16%) (init= 1)



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


