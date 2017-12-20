{{ population.label }}
======================

The table below lists signals of recent selection discovered in the
{{ population.label }} population.

{% macro signals_table(signals) -%}
{% if signals|length > 0 -%}
.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score

    {% for signal in signals -%}
    :doc:`/signal/{{ signal.statistic }}/{{ signal.population }}/chr{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.focus_start_arm }}:{{ signal.focus_start }}-{{ signal.focus_stop_arm }}:{{ signal.focus_stop }}",{{ signal.sum_delta_aic|int }}
    {% endfor %}
{% else %}
No signals.
{% endif %}
{%- endmacro %}

Chromosome 2
------------

{{ signals_table(signals['2']) }}

Chromosome 3
------------

{{ signals_table(signals['3']) }}

Chromosome X
------------

{{ signals_table(signals['X']) }}
