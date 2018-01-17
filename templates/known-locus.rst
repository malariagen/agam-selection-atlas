{{ locus.short_name }} locus
{% for l in locus.short_name %}={% endfor %}======

{% from 'macros.rst' import signals_table, disqus, intcomma, gene_doc %}
{% set root_path = '../' %}

This page provides information about the **{{ locus.long_name }}**, a locus for which there is prior
evidence of recent positive selection and/or an association with insecticide resistance in
*Anopheles* mosquitoes.

The locus occurs on chromosome {% if locus.seqid|length > 1 %}arm{% endif %} **{{ locus.seqid }}**
from position **{{ intcomma(locus.start_coord) }}** to **{{ intcomma(locus.end_coord) }}**.

{% if genes|length == 0 %}
The locus does not contain any genes.
{% elif genes|length == 1 %}
The locus contains gene {{ gene_doc(genes[0], root_path) }}.
{% elif genes|length > 1 %}
The locus contains the following {{ genes|length }} genes:
{%- for value in genes %} {{ gene_doc(value, root_path) }}{{ ", " if not loop.last }}
{%- endfor %}.
{% endif %}

References
----------

{% for ref in locus.references %}
- `{{ ref.author }} ({{ ref.year }}) <{{ ref.url }}>`_ {{ ref.title }}
{% endfor %}

Selection signals
-----------------

{% if signals|length > 0 %}
The table below lists signals of recent selection found in this study that are overlapping or
within 50 kbp of this locus.

{{ signals_table(signals, '../') }}
{% else %}
No selection signals at this locus.
{% endif %}

Comments
--------

{{ disqus('/known-locus/' + locus.short_name|lower) }}
