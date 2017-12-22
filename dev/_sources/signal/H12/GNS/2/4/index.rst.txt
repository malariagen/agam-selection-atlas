:orphan:




H12 / Guinea *An. gambiae* / Chromosome 2 / #4
==============================================

This page describes a signal of selection found in the
:doc:`../../../../../population/GNS` population using the
:doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**2L** between positions **25,660,001** and
**25,760,000**.
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




The following 7 genes overlap the focal region: :doc:`../../../../../gene/AGAP006052` (protein phosphatase 1, regulatory (inhibitor) subunit 3),  :doc:`../../../../../gene/AGAP006053`,  :doc:`../../../../../gene/AGAP006054`,  :doc:`../../../../../gene/AGAP006055` (NF-kappa-B inhibitor-like protein 2),  :doc:`../../../../../gene/AGAP006056`,  :doc:`../../../../../gene/AGAP006057` (multiple coagulation factor deficiency 2),  :doc:`../../../../../gene/AGAP006058` (heparan sulfate 2-o-sulfotransferase).




The following 8 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP006045` (protein yorkie),  :doc:`../../../../../gene/AGAP006046` (Med23 - mediator of RNA polymerase II transcription subunit 23),  :doc:`../../../../../gene/AGAP006047`:sup:`1` (CYP4J9 - cytochrome P450),  :doc:`../../../../../gene/AGAP006048`:sup:`1` (CYP4J5 - cytochrome P450),  :doc:`../../../../../gene/AGAP006049`:sup:`1` (CYP4J10 - cytochrome P450),  :doc:`../../../../../gene/AGAP006050` (AarF domain containing kinase 5),  :doc:`../../../../../gene/AGAP006051` (pentatricopeptide repeat domain 1),  :doc:`../../../../../gene/AGAP006059`.


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.



Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/4/peak_context.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/4/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/GNS/2/4/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 51
        # data points      = 151
        # variables        = 3
        chi-square         = 0.055
        reduced chi-square = 0.000
        Akaike info crit   = -1190.763
        Bayesian info crit = -1181.711
    [[Variables]]
        amplitude:   0.17692286 +/- 0.008345 (4.72%) (init= 0.5)
        decay:       0.76517577 +/- 0.064104 (8.38%) (init= 0.5)
        c:           0.05999999 +/- 0.002231 (3.72%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(decay, c)                  = -0.577 
        C(amplitude, decay)          = -0.543 


Right flank, peak model::

    [[Model]]
        Model(exponential)
    [[Fit Statistics]]
        # function evals   = 43
        # data points      = 150
        # variables        = 3
        chi-square         = 0.276
        reduced chi-square = 0.002
        Akaike info crit   = -938.889
        Bayesian info crit = -929.858
    [[Variables]]
        amplitude:   0.15950485 +/- 0.021499 (13.48%) (init= 0.5)
        decay:       0.72685933 +/- 0.162885 (22.41%) (init= 0.5)
        c:           0.05559313 +/- 0.004913 (8.84%) (init= 0.03)
        cap:         1 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.614 
        C(decay, c)                  = -0.563 


Left flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 150
        # variables        = 1
        chi-square         = 0.249
        reduced chi-square = 0.002
        Akaike info crit   = -958.054
        Bayesian info crit = -955.043
    [[Variables]]
        c:   0.08328130 +/- 0.003338 (4.01%) (init= 0.03)


Right flank, null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 6
        # data points      = 149
        # variables        = 1
        chi-square         = 0.420
        reduced chi-square = 0.003
        Akaike info crit   = -872.827
        Bayesian info crit = -869.823
    [[Variables]]
        c:   0.07340815 +/- 0.004364 (5.95%) (init= 0.03)


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


