
Known loci
==========

The following genome regions contain one or more genes with prior evidence of a role in insecticide
resistance and/or of recent selection in *Anopheles* populations.

.. toctree::
    :maxdepth: 1

    {% for locus in loci -%}
    known-locus/{{ locus.short_name|lower }}
    {% endfor %}
