:orphan:




H12/CMS/3/1
===========

This page describes a signal of selection found in the
:doc:`../../../../../population/CMS` populationusing the :doc:`../../../../../method/H12` statistic.The focus of this signal is on chromosome arm
**3R** between positions **28,580,000** and
**28,620,000**.
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




The following 12 genes overlap the focal region: :doc:`../../../../../gene/AGAP009189`,  :doc:`../../../../../gene/AGAP009190`:sup:`1` (GSTE8 - glutathione S-transferase epsilon class 8),  :doc:`../../../../../gene/AGAP009191`:sup:`1` (GSTE6 - glutathione S-transferase epsilon class 6),  :doc:`../../../../../gene/AGAP009192`:sup:`1` (GSTE5 - glutathione S-transferase epsilon class 5),  :doc:`../../../../../gene/AGAP009193`:sup:`1` (GSTE4 - glutathione S-transferase epsilon class 4),  :doc:`../../../../../gene/AGAP009194`:sup:`1` (GSTE2 - glutathione S-transferase epsilon class 2),  :doc:`../../../../../gene/AGAP009195`:sup:`1` (GSTE1 - glutathione S-transferase epsilon class 1),  :doc:`../../../../../gene/AGAP009196`:sup:`1` (GSTE7 - glutathione S-transferase epsilon class 7),  :doc:`../../../../../gene/AGAP009197`:sup:`1` (GSTE3 - glutathione S-transferase epsilon class 3),  :doc:`../../../../../gene/AGAP009198`,  :doc:`../../../../../gene/AGAP009199` (palmitoyltransferase ZDHHC24),  :doc:`../../../../../gene/AGAP009200` (collagen type IV alpha).




The following 7 genes are within 50 kbp of the focal
region: :doc:`../../../../../gene/AGAP009185`,  :doc:`../../../../../gene/AGAP009187`:sup:`1` (Indanol dehydrogenase),  :doc:`../../../../../gene/AGAP009188` (solute carrier family 39 (zinc transporter), member 9),  :doc:`../../../../../gene/AGAP009201` (collagen type IV alpha),  :doc:`../../../../../gene/AGAP009202` (selenoprotein T),  :doc:`../../../../../gene/AGAP028058`,  :doc:`../../../../../gene/AGAP009203` (SPRY domain-containing SOCS box protein 3).


Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

Overlapping signals
-------------------

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
    * - :doc:`../../../../../signal/XPEHH/BFS.GWA/3/1/index`
      - XPEHH
      - Burkina Faso *An. gambiae*
      - 3R:28,500,000-28,620,000
      - 1,181
      - 100.0%
    * - :doc:`../../../../../signal/H12/BFS/3/1/index`
      - H12
      - Burkina Faso *An. gambiae*
      - 3R:28,520,000-28,580,000
      - 995
      - 98.4%
    * - :doc:`../../../../../signal/H12/UGS/3/1/index`
      - H12
      - Uganda *An. gambiae*
      - 3R:28,560,000-28,600,000
      - 876
      - 97.3%
    * - :doc:`../../../../../signal/H12/BFM/3/1/index`
      - H12
      - Burkina Faso *An. coluzzii*
      - 3R:28,560,000-28,620,000
      - 747
      - 98.0%
    




Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`../../../../../method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/1/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/1/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="../../../../../_static/data/signal/H12/CMS/3/1/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    [[Model]]
        Model(skewed_exponential_peak)
    [[Fit Statistics]]
        # function evals   = 23
        # data points      = 362
        # variables        = 4
        chi-square         = 0.041
        reduced chi-square = 0.000
        Akaike info crit   = -3283.635
        Bayesian info crit = -3268.068
    [[Variables]]
        center:      0 (fixed)
        amplitude:   0.48440501 +/- 0.004688 (0.97%) (init= 0.5)
        decay:       0.41270821 +/- 0.006057 (1.47%) (init= 0.5)
        skew:        0.20509592 +/- 0.014068 (6.86%) (init= 0)
        baseline:    0.01323736 +/- 0.000636 (4.80%) (init= 0.03)
        ceiling:     1 (fixed)
        floor:       0 (fixed)
    [[Correlations]] (unreported correlations are <  0.100)
        C(amplitude, decay)          = -0.659 
        C(decay, baseline)           = -0.348 


Null model::

    [[Model]]
        Model(constant)
    [[Fit Statistics]]
        # function evals   = 9
        # data points      = 361
        # variables        = 1
        chi-square         = 2.005
        reduced chi-square = 0.006
        Akaike info crit   = -1872.729
        Bayesian info crit = -1868.840
    [[Variables]]
        c:   0.03980864 +/- 0.003927 (9.87%) (init= 0.03)



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


