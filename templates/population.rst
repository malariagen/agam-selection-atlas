{{ population.label }}
{% for l in population.label %}={% endfor %}

{% from 'macros.rst' import signals_table, disqus %}

The tables below list signals of recent selection discovered in the
{{ population.label }} population.

Chromosome arm 2R
-----------------

{{ signals_table(signals['2R'], '../') }}

Chromosome arm 2L
-----------------

{{ signals_table(signals['2L'], '../') }}

Chromosome arm 3R
-----------------

{{ signals_table(signals['3R'], '../') }}

Chromosome arm 3L
-----------------

{{ signals_table(signals['3L'], '../') }}

Chromosome X
------------

{{ signals_table(signals['X'], '../') }}

Comments
--------

{{ disqus('/population/{{ population.id }}') }}
