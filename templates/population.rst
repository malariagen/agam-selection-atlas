{{ population.label }}
======================

The table below lists signals of recent selection discovered in the
{{ population.label }} population.

Chromosome 2
------------

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score

    {% for signal in signals -%}
    {% if signal.chromosome == "2" -%}
    :doc:`/signals/{{ signal.statistic }}/{{ signal.population }}/chr{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.signal_arm }}:{{ signal.signal_start }}-{{ signal.signal_stop }}",{{ signal.sum_delta_aic|int }}
    {% endif %}
    {%- endfor %}

Chromosome 3
------------

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score

    {% for signal in signals -%}
    {% if signal.chromosome == "3" -%}
    :doc:`/signals/{{ signal.statistic }}/{{ signal.population }}/chr{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.signal_arm }}:{{ signal.signal_start }}-{{ signal.signal_stop }}",{{ signal.sum_delta_aic|int }}
    {% endif %}
    {%- endfor %}

Chromosome X
------------

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score

    {% for signal in signals -%}
    {% if signal.chromosome == "X" -%}
    :doc:`/signals/{{ signal.statistic }}/{{ signal.population }}/chr{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.signal_arm }}:{{ signal.signal_start }}-{{ signal.signal_stop }}",{{ signal.sum_delta_aic|int }}
    {% endif %}
    {%- endfor %}
