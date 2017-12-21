:orphan:

{{ gene.id }}
=============

{% macro signals_table(signals) %}
{% if signals|length > 0 %}
.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score

    {% for signal in signals -%}
    :doc:`../signal/{{ signal.statistic }}/{{ signal.population }}/{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.focus_start_arm }}:{{ "{:,}".format(signal.focus_start|int) }}-{% if signal.focus_start_arm != signal.focus_stop_arm %}{{ signal.focus_stop_arm }}:{% endif %}{{ "{:,}".format(signal.focus_stop|int) }}",{{ signal.sum_delta_aic|int }} ({{ signal.delta_aic_left|int }} | {{ signal.delta_aic_right|int }})
    {% endfor %}
{% else %}
No signals.
{% endif %}
{% endmacro %}

{% if gene.name %}Name: **{{ gene.name }}**{% endif %}

{% if gene.description -%}
Description: {{ gene.description|capitalize }}.
{%- endif %}

External links:
`VectorBase <https://www.vectorbase.org/Anopheles_gambiae/Gene/Summary?g={{ gene.id }}>`_ |
`Ag1000G genome browser <https://www.malariagen.net/apps/ag1000g/phase1-AR3/index.html?genome_region={{ gene.seqid }}:{{ gene.start }}-{{ gene.end }}#genomebrowser>`_

{% if overlapping_signals|length > 0 -%}
Overlapping signals
-------------------

The following signals have a focus which overlaps this gene:

{{ signals_table(overlapping_signals) }}

{% endif %}

{% if adjacent_signals|length > 0 -%}
Adjacent signals
----------------

The following signals have a focus which occurs within 50 kbp of this gene:

{{ signals_table(adjacent_signals) }}

{% endif %}
