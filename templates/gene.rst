
{{ gene.id }}
=============

{% if gene.name %}Name: **{{ gene.name }}**{% endif %}

{% if gene.description -%}
Description: {{ gene.description|capitalize }}.
{%- endif %}

External links: `VectorBase <https://www.vectorbase.org/Anopheles_gambiae/Gene/Summary?g={{ gene.id }}>`_

TODO
