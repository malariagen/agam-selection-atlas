:orphan:

{{ population.label }} | {{ statistic.label }} | Chromosome {{ chromosome }} | Signal #{{ rank }}
================================================================================

{% macro gene(value) -%}
:doc:`/gene/{{ value.id }}`
{%- if value.name or value.description %} (
    {%- if value.name %}{{ value.name|trim }}{% endif -%}
    {%- if value.name and value.description %} - {% endif %}
    {%- if value.description %}{{ value.description|trim }}{% endif -%}
)
{%- endif %}
{%- endmacro %}

This page describes a signal of selection found in the
:doc:`/population/{{ population.id }}` population using the
:doc:`/method/{{ statistic.id }}` statistic.
{%- if focus.start[0] == focus.stop[0] -%}
The inferred focus of this signal is on chromosome arm
**{{ focus.start[0] }}** between positions **{{ "{:,}".format(focus.start[1]) }}** and
**{{ "{:,}".format(focus.stop[1]) }}**.
{%- else -%}
The inferred focus of this signal is between
**{{ focus.start[0] }}:{{ "{:,}".format(focus.start[1]) }}** and
**{{ focus.stop[0] }}:{{ "{:,}".format(focus.stop[1]) }}**.
{%- endif %}
The evidence supporting this signal is
{% if minor_delta_aic >= 100 -%}
**strong** (:math:`\Delta_{i}` >= 100 on both flanks)
{%- elif minor_delta_aic > 50 -%}
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks)
{%- else -%}
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks)
{%- endif -%}.

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Figure 1</strong>. Location of the signal of selection. Blue markers
    show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area
    shows the focus of the selection signal. The shaded blue area shows
    the genomic region in linkage with the selection event. Use the
    mouse wheel or the controls at the right of the plot to zoom in, and hover
    over genes to see gene names and descriptions.
    </p></div>

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

No genes are within 50 kbp of the focal region.
{% endif %}
{% if adjacent_genes|length == 1 %}
Gene {{ gene(adjacent_genes[0]) }} is within 50 kbp of the focal region.
{% endif %}
{% if adjacent_genes|length > 1 %}
The following {{ adjacent_genes|length }} genes are within 50 kbp of the focal
region:
{%- for value in adjacent_genes %} {{ gene(value) }}{{ ", " if not loop.last }}
{%- endfor %}.
{% endif %}

Overlapping signals
-------------------

{% if overlapping_signals|length > 0 %}

The following selection signals have an inferred focus which overlaps with the
focus of this signal:

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal, Focus, Score

    {% for signal in overlapping_signals -%}
    :doc:`/signal/{{ signal.statistic }}/{{ signal.population }}/chr{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.focus_start_arm }}:{{ "{:,}".format(signal.focus_start|int) }}-{% if signal.focus_stop_arm != signal.focus_start_arm%}{{ signal.focus_stop_arm }}:{% endif %}{{ "{:,}".format(signal.focus_stop|int) }}",{{ signal.sum_delta_aic|int }}
    {% endfor %}

{% else %}
No overlapping signals.
{% endif %}

Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`/method/peak_modelling` algorithm.

.. figure:: peak_context.png

    **Figure 2**. Chromosome-wide selection statistic and results from peak
    modelling. **a**, TODO. **b**, TODO.

.. figure:: peak_targetting.png

    **Figure 3**. Diagnostics from targetting the selection signal to a focal
    region. TODO.

.. figure:: peak_fit.png

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
