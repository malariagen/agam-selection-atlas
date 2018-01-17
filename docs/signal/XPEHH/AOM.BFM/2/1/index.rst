:orphan:




XPEHH/AOM.BFM/2/1
=================

This page describes a signal of selection found in the
:doc:`../../../../../population/AOM` population
when compared with the :doc:`../../../../../population/BFM` population
using the :doc:`../../../../../method/XPEHH` statistic.The focus of this signal is on chromosome arm
**2R** between positions **56,520,000** and
**56,920,000**.
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


The following 40 genes overlap the focal region: :doc:`../../../../../gene/AGAP004453` (GPRDOP3 - GPCR Dopamine Family 3),  :doc:`../../../../../gene/AGAP004454`,  :doc:`../../../../../gene/AGAP004455` (GNBPB1 - 3-glucan binding protein),  :doc:`../../../../../gene/AGAP004456` (GNBPB5 - 3-glucan binding protein),  :doc:`../../../../../gene/AGAP004457` (Sugar transporter ERD6-like 4),  :doc:`../../../../../gene/AGAP004458` (Leucine-rich repeat-containing protein 58),  :doc:`../../../../../gene/AGAP004459` (ubiquitin-like 1-activating enzyme E1 A),  :doc:`../../../../../gene/AGAP004460` (sialic acid synthase),  :doc:`../../../../../gene/AGAP004461` (solute carrier family 30 (zinc transporter), member 5/7),  :doc:`../../../../../gene/AGAP004462` (RpS25 - 40S ribosomal protein S25),  :doc:`../../../../../gene/AGAP004463` (ribosomal RNA-processing protein 17),  :doc:`../../../../../gene/AGAP004464`,  :doc:`../../../../../gene/AGAP004465` (18S rRNA (adenine1779-N6/adenine1780-N6)-dimethyltransferase),  :doc:`../../../../../gene/AGAP004466`,  :doc:`../../../../../gene/AGAP004467` (centromere/kinetochore protein ZW10),  :doc:`../../../../../gene/AGAP004468` (Phosducin-like protein),  :doc:`../../../../../gene/AGAP004469` (phosphatidylinositol transfer protein, beta like),  :doc:`../../../../../gene/AGAP004470` (STE24 endopeptidase),  :doc:`../../../../../gene/AGAP004471`,  :doc:`../../../../../gene/AGAP004472`,  :doc:`../../../../../gene/AGAP004473`,  :doc:`../../../../../gene/AGAP013052`,  :doc:`../../../../../gene/AGAP004474`,  :doc:`../../../../../gene/AGAP004475` (IR100i - ionotropic receptor IR100i),  :doc:`../../../../../gene/AGAP004476` (solute carrier family 18 (vesicular monoamine), member 2),  :doc:`../../../../../gene/AGAP004477` (Polyphosphoinositide phosphatase),  :doc:`../../../../../gene/AGAP004478` (ATP synthase subunit s, mitochondrial precursor),  :doc:`../../../../../gene/AGAP004479` (reduction in cnn dots 1),  :doc:`../../../../../gene/AGAP004480` (DNA-directed RNA polymerase III subunit RPC4),  :doc:`../../../../../gene/AGAP004481` (mRpS26 - 28S ribosomal protein S26, mitochondrial),  :doc:`../../../../../gene/AGAP004483` (Lethal giant larvae),  :doc:`../../../../../gene/AGAP004484` (CDGSH iron sulfur domain-containing protein 2 homolog),  :doc:`../../../../../gene/AGAP004485`,  :doc:`../../../../../gene/AGAP004486` (adiponectin receptor),  :doc:`../../../../../gene/AGAP004487` (SNX5 protein),  :doc:`../../../../../gene/AGAP004488` (actin-related protein 5),  :doc:`../../../../../gene/AGAP004489`,  :doc:`../../../../../gene/AGAP004490`,  :doc:`../../../../../gene/AGAP004491` (exonuclease 1),  :doc:`../../../../../gene/AGAP004492` (upstream activation factor subunit UAF30).



No genes are within 50 kbp of the focal region.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/XPEHH/AOM.BFM/2/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_gaussian)
    [[Fit Statistics]]
        # function evals   = 83
        # data points      = 395
        # variables        = 4
        chi-square         = 180.247
        reduced chi-square = 0.461
        Akaike info crit   = -301.901
        Bayesian info crit = -285.985
    [[Variables]]
        center:      0 (fixed)
        amplitude:   2.07285347 +/- 0.087371 (4.22%) (init= 3)
        sigma:       2.47378308 +/- 0.158131 (6.39%) (init= 0.5)
        skew:       -0.99999540 +/- 0.068793 (6.88%) (init= 0)
        baseline:    2.22945297 +/- 0.058532 (2.63%) (init= 1)
        ceiling:     100 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, baseline)       = -0.598 
        C(sigma, baseline)           = -0.468 
        C(amplitude, skew)           =  0.224 
        C(sigma, skew)               = -0.144 
        C(amplitude, sigma)          = -0.124 
        C(skew, baseline)            = -0.119 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 12
        # data points      = 394
        # variables        = 1
        chi-square         = 448.223
        reduced chi-square = 1.141
        Akaike info crit   = 52.802
        Bayesian info crit = 56.779
    [[Variables]]
        c:   3.13284006 +/- 0.053802 (1.72%) (init= 1)



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


