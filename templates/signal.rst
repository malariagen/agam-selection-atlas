
{{ population.label }} | {{ statistic.label }} | Chromosome {{ chromosome }} | Signal #{{ rank }}
================================================================================

{% macro gene(value) -%}
:doc:`/genes/{{ value.id }}`
{%- if value.name or value.description %} (
    {%- if value.name %}{{ value.name|trim }}{% endif -%}
    {%- if value.name and value.description %} - {% endif %}
    {%- if value.description %}{{ value.description|trim }}{% endif -%}
)
{%- endif %}
{%- endmacro %}

This page describes a signal of selection found in the
:doc:`/populations/{{ population.id }}` population using the
:doc:`/methods/{{ statistic.id }}` statistic.
The inferred focus of this signal is on chromosome arm {{ focus.arm }} from
position {{ "{:,}".format(signal.start) }} to {{ "{:,}".format(signal.stop) }}.

{% if overlapping_genes|length == 0 %}
No genes overlap the focal region.
{% endif %}
{% if overlapping_genes|length == 1 %}
Gene {{ gene(overlapping_genes[0]) }} overlaps the focal region.
{% endif %}
{% if overlapping_genes|length > 1 %}
The following {{ overlapping_genes|length }} genes overlap the focal region:
{%- for value in overlapping_genes %} {{ gene(value) }}{{ ", " if not loop.last }}
{%- endfor %}.
{% endif %}
{% if adjacent_genes|length == 0 %}

No genes are within 40 kbp of the focal region.
{% endif %}
{% if adjacent_genes|length == 1 %}
Gene {{ gene(adjacent_genes[0]) }} is within 40 kbp of the focal region.
{% endif %}
{% if adjacent_genes|length > 1 %}
The following {{ adjacent_genes|length }} genes are within 40 kbp of the focal
region:
{%- for value in adjacent_genes %} {{ gene(value) }}{{ ", " if not loop.last }}
{%- endfor %}.
{% endif %}

.. figure:: signal_location.png
    :alt: signal location

    **Figure 1**. Location of the signal of selection. Blue markers show the
    value of the selection statistic in non-overlapping 20 kbp windows. The
    dashed black line shows the fitted peak model. The vertical red bar shows
    the inferred focus of the selection signal. The shaded blue area shows the
    inferred genomic region affected by the selection event.

Related signals
---------------

Overlapping signals
~~~~~~~~~~~~~~~~~~~

The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    {% for signal in overlapping_signals -%}
    :doc:`/signals/{{ signal.statistic }}/{{ signal.population }}/chr{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.signal_arm }}:{{ signal.signal_start }}-{{ signal.signal_stop }}",{{ signal.sum_delta_aic|int }}
    {% endfor %}

Adjacent signals
~~~~~~~~~~~~~~~~

The following selection signals have an inferred focus that is immediately
adjacent to the focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Nearby signals
~~~~~~~~~~~~~~

The following signals affect a genome region that overlaps with the genome region
affected by this signal:

.. cssclass:: table-hover
.. csv-table::
    :header: Signal, Chromosome, Start, Stop, Score, Genes

    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234
    :doc:`/signals/h12/bfs/1/index`, 2L, "2,420,000", "2,460,000", 511.2, AGAP001234

Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/methods/peak_modelling` procedure.

.. figure:: signal_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: signal_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: signal_fit.png

    **Figure 4**. Diagnostics from fitting a peak model to the selection signal.
    **a**, TODO. **b**, TODO. **c**, TODO.

Model fit reports
~~~~~~~~~~~~~~~~~

Left flank, peak model::

    {{ fit_reports.left_peak|indent(4) }}

Right flank, peak model::

    {{ fit_reports.right_peak|indent(4) }}

Left flank, null model::

    {{ fit_reports.left_null|indent(4) }}

Right flank, null model::

    {{ fit_reports.right_null|indent(4) }}

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
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
