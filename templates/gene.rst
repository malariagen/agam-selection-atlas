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
    :doc:`/signal/{{ signal.statistic }}/{{ signal.population }}/{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.focus_arm }}:{{ signal.focus_start }}-{{ signal.focus_stop }}",{{ signal.sum_delta_aic|int }}
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

Overlapping signals
-------------------

The following signals have a focus which overlaps this gene:

{{ signals_table(overlapping_signals) }}

Adjacent signals
----------------

The following signals have a focus which occurs within 50 kbp of this gene:

{{ signals_table(adjacent_signals) }}
