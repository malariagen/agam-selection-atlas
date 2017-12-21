{{ population.label }}
======================

The tables below list signals of recent selection discovered in the
{{ population.label }} population.

{% macro signals_table(signals) -%}
{% if signals|length > 0 -%}
.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score (Left | Right)

    {% for signal in signals -%}
    :doc:`../signal/{{ signal.statistic }}/{{ signal.population }}/{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.focus_start_arm }}:{{ "{:,}".format(signal.focus_start|int) }}-{% if signal.focus_start_arm != signal.focus_stop_arm %}{{ signal.focus_stop_arm }}:{% endif %}{{ "{:,}".format(signal.focus_stop|int) }}",{{ signal.sum_delta_aic|int }} ({{ signal.delta_aic_left|int }} | {{ signal.delta_aic_right|int }})
    {% endfor %}
{% else %}
No signals.
{% endif %}
{%- endmacro %}

Chromosome arm 2R
-----------------

{{ signals_table(signals['2R']) }}

Chromosome arm 2L
-----------------

{{ signals_table(signals['2L']) }}

Chromosome arm 3R
-----------------

{{ signals_table(signals['3R']) }}

Chromosome arm 3L
-----------------

{{ signals_table(signals['3L']) }}

Chromosome X
------------

{{ signals_table(signals['X']) }}
