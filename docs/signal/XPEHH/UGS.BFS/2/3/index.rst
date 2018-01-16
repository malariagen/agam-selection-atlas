:orphan:




XPEHH/UGS.BFS/2/3
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/UGS` population
when compared with the :doc:`../../../../../population/BFS` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **57,280,000** and
**57,620,000**.
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


The following 39 genes overlap the focal region: :doc:`../../../../../gene/AGAP004517` (huckebein),  :doc:`../../../../../gene/AGAP004518`,  :doc:`../../../../../gene/AGAP004519` (sideroflexin 1,2,3),  :doc:`../../../../../gene/AGAP004520` (Ran-binding protein 3),  :doc:`../../../../../gene/AGAP004521` (SNW domain-containing protein 1),  :doc:`../../../../../gene/AGAP004522` (TBC1 domain family member 22B),  :doc:`../../../../../gene/AGAP004523`,  :doc:`../../../../../gene/AGAP004524`,  :doc:`../../../../../gene/AGAP004527` (N-acylneuraminate cytidylyltransferase),  :doc:`../../../../../gene/AGAP004528`,  :doc:`../../../../../gene/AGAP004529`,  :doc:`../../../../../gene/AGAP004530`,  :doc:`../../../../../gene/AGAP004531` (cathepsin B precursor),  :doc:`../../../../../gene/AGAP004532` (3-ketoacyl-CoA reductase),  :doc:`../../../../../gene/AGAP004533` (cathepsin B),  :doc:`../../../../../gene/AGAP004534` (cathepsin B precursor),  :doc:`../../../../../gene/AGAP004535` (exportin 7),  :doc:`../../../../../gene/AGAP004537`,  :doc:`../../../../../gene/AGAP004541`,  :doc:`../../../../../gene/AGAP004543`,  :doc:`../../../../../gene/AGAP004544` (solute carrier family 35, member F3/4),  :doc:`../../../../../gene/AGAP028407`,  :doc:`../../../../../gene/AGAP004545`,  :doc:`../../../../../gene/AGAP004546` (RNA-binding protein 25),  :doc:`../../../../../gene/AGAP004548` (LIM domain-containing protein),  :doc:`../../../../../gene/AGAP004549` (Protein yellow),  :doc:`../../../../../gene/AGAP004550` (dolichol-phosphate mannosyltransferase subunit 3),  :doc:`../../../../../gene/AGAP004551` (gamma-interferon-inducible lysosomal thiol reductase),  :doc:`../../../../../gene/AGAP004552`,  :doc:`../../../../../gene/AGAP004553`,  :doc:`../../../../../gene/AGAP004554`,  :doc:`../../../../../gene/AGAP004555`,  :doc:`../../../../../gene/AGAP004556` (ribosome biogenesis protein SSF1/2),  :doc:`../../../../../gene/AGAP004557` (U3 small nucleolar RNA-associated protein 21),  :doc:`../../../../../gene/AGAP004558` (nucleoporin NDC1),  :doc:`../../../../../gene/AGAP004559` (Ras-related protein),  :doc:`../../../../../gene/AGAP004560` (cohesin complex subunit SCC1),  :doc:`../../../../../gene/AGAP004562` (MFS transporter, PCFT/HCP family, solute carrier family 46 (folate transporter)),  :doc:`../../../../../gene/AGAP004563` (ANCE9 - angiotensin-converting enzyme 9).



The following 14 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP004513` (4-hydroxybenzoate hexaprenyltransferase),  :doc:`../../../../../gene/AGAP004514` (nuclear GTP-binding protein),  :doc:`../../../../../gene/AGAP004515`,  :doc:`../../../../../gene/AGAP004516`,  :doc:`../../../../../gene/AGAP004564` (soluble guanylate cyclase 89Da),  :doc:`../../../../../gene/AGAP013164`,  :doc:`../../../../../gene/AGAP013254`,  :doc:`../../../../../gene/AGAP004566` (Clipd1),  :doc:`../../../../../gene/AGAP004567` (Transmembrane protease serine 11B),  :doc:`../../../../../gene/AGAP004568` (Serine protease like protein),  :doc:`../../../../../gene/AGAP004569` (epidermis specific serine protease),  :doc:`../../../../../gene/AGAP004570` (Clipd1),  :doc:`../../../../../gene/AGAP004571` (Oviductin),  :doc:`../../../../../gene/AGAP013278`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/2/3/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/2/3/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/UGS.BFS/2/3/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 58
        # data points      = 281
        # variables        = 4
        chi-square         = 181.687
        reduced chi-square = 0.656
        Akaike info crit   = -114.535
        Bayesian info crit = -99.982
    [[Variables]]
        center:      0 (fixed)
        amplitude:   3.72244470 +/- 0.131779 (3.54%) (init= 3)
        sigma:       1.27679901 +/- 0.061390 (4.81%) (init= 0.5)
        skew:       -0.48151437 +/- 0.051450 (10.69%) (init= 0)
        baseline:    1.57988649 +/- 0.071674 (4.54%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.459 
        C(sigma, baseline)           = -0.459 
        C(amplitude, sigma)          = -0.224 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 11
        # data points      = 280
        # variables        = 1
        chi-square         = 707.697
        reduced chi-square = 2.537
        Akaike info crit   = 261.623
        Bayesian info crit = 265.258
    [[Variables]]
        c:   2.75811159 +/- 0.095177 (3.45%) (init= 1)



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


