Chromosome {% if seqid|length > 1 %}arm{% endif %} {{ seqid }}
==============================================================

This page provides information about signals of recent selection on
chromosome{% if seqid|length > 1 %} arm{% endif %} {{ seqid }}.

{% from 'macros.rst' import signals_table %}

.. raw:: html
    :file: {{ seqid }}.signals.html

{{ signals_table(signals, '../') }}
