All signals
===========

The table below lists all the signals of recent selection discovered.

.. cssclass:: table-hover
.. csv-table::
    :widths: auto
    :header: Signal,Focus,Score

    {% for signal in signals -%}
    :doc:`./signal/{{ signal.statistic }}/{{ signal.population }}/{{ signal.chromosome }}/{{ signal.rank }}/index`,"{{ signal.focus_start_arm }}:{{ "{:,}".format(signal.focus_start|int) }}-{% if signal.focus_stop_arm != signal.focus_start_arm %}{{ signal.focus_stop_arm }}{% endif %}{{ "{:,}".format(signal.focus_stop|int) }}",{{ signal.sum_delta_aic|int }}
    {% endfor %}
