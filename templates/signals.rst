All signals
===========

The table below lists all the signals of recent selection discovered.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score

    {% for signal in signals -%}
    :doc:`/signal/{{ signal.statistic }}/{{ signal.population }}/chr{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.signal_arm }}:{{ signal.signal_start }}-{{ signal.signal_stop }}",{{ signal.sum_delta_aic|int }}
    {% endfor %}
