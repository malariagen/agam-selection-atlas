{{ population.label }}
{% for l in population.label %}={% endfor %}

{% from 'macros.rst' import signals_table, disqus %}

The tables below list signals of recent selection discovered in the
{{ population.label }} population.

{% macro signals_section(seqid) %}
{% if signals[seqid]|length > 0 %}
.. raw:: html
    :file: {{ population.id }}.{{ seqid }}.signals.html

{{ signals_table(signals[seqid], '../') }}
{% else %}
No signals.
{% endif %}
{% endmacro %}

Chromosome arm 2R
-----------------

{{ signals_section('2R') }}

Chromosome arm 2L
-----------------

{{ signals_section('2L') }}

Chromosome arm 3R
-----------------

{{ signals_section('3R') }}

Chromosome arm 3L
-----------------

{{ signals_section('3L') }}

Chromosome X
------------

{{ signals_section('X') }}

Comments
--------

{{ disqus('/population/{{ population.id }}') }}
