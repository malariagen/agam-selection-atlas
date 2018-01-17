:orphan:
{% from 'macros.rst' import signals_table, disqus, intcomma %}
{% set root_path = '../' %}

{{ gene.id }}
{% for c in gene.id %}={% endfor %}

Location: **{{ gene.seqid }}:{{ intcomma(gene.start) }}-{{ intcomma(gene.end) }}**

{% if gene.name|length > 0 %}Name: **{{ gene.name }}**{% endif %}

{% if gene.description|length > 0 -%}
Description: **{{ gene.description|capitalize }}**.
{%- endif %}

External links:
`VectorBase <https://www.vectorbase.org/Anopheles_gambiae/Gene/Summary?g={{ gene.id }}>`_ |
`Ag1000G genome browser <https://www.malariagen.net/apps/ag1000g/phase1-AR3/index.html?genome_region={{ gene.seqid }}:{{ gene.start }}-{{ gene.end }}#genomebrowser>`_

{% for locus in overlapping_loci %}
This gene is within the :doc:`{{ root_path }}known-locus/{{ locus.short_name|lower }}`, a genome
region with prior evidence of an association with insecticide resistance and/or recent positive selection in
*Anopheles* mosquitoes.
{% endfor %}

{% for locus in adjacent_loci %}
This gene occurs within 50 kbp of the :doc:`{{ root_path }}known-locus/{{ locus.short_name|lower }}`,
a genome region with prior evidence of an association with insecticide resistance and/or recent positive
selection in *Anopheles* mosquitoes.
{% endfor %}

{% if overlapping_signals|length > 0 -%}
Overlapping selection signals
-----------------------------

The following signals have a focus which overlaps this gene.

{{ signals_table(overlapping_signals, root_path) }}
{% endif %}

{% if adjacent_signals|length > 0 -%}
Adjacent selection signals
--------------------------

The following signals have a focus which occurs within 50 kbp of this gene.

{{ signals_table(adjacent_signals, root_path) }}
{% endif %}

Comments
--------

{{ disqus('/gene/' + gene.id) }}
