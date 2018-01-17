{% from 'macros.rst' import gene_doc, disqus, intcomma %}

{{ title }}
{% for c in title %}={% endfor %}

Below is a table of insecticide resistance candidate genes with information about any
overlapping signals of selection.

Please note that the list of genes has been manually
curated and is likely to be incomplete. If you would like to suggest an addition, please
leave a comment at the bottom of the page.

Please also note that the fact that there are any signals of selection overlapping or
adjacent to a given gene **does not** prove that the gene is under selection. Each signal of
selection may span a number of genes, and the true target of selection may be a
different gene nearby. Similarly, if a gene does not have any overlapping or adjacent
signals of selection, that **does not** prove it is selectively neutral. There are a
number of technical reasons why a true signal of selection might not be detected.

.. cssclass:: table-hover
.. list-table::
    :widths: 10, 10, 40, 20, 10, 10
    :header-rows: 1

    * - Gene
      - Name
      - Description
      - Location
      - No. signals (overlapping, adjacent)
      - Known locus
    {% for gene in genes -%}
    * - :doc:`../gene/{{ gene.id }}`
      - {{ gene.name }}
      - {{ gene.description|capitalize }}
      - {{ gene.seqid }}:{{ intcomma(gene.start) }}-{{ intcomma(gene.end) }}
      - {{ gene.n_signals }} ({{ gene.n_signals_overlapping }}, {{ gene.n_signals_adjacent }})
      - {{ gene.known_loci }}
    {% endfor %}

Comments
--------

{{ disqus('/ir-candidate/' + slug) }}
