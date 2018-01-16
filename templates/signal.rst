:orphan:
{% from 'macros.rst' import signals_table, gene_doc, disqus, intcomma %}
{% set root_path = '../../../../../' %}
{% set title = uid %}

{{ title }}
{% for c in title %}={% endfor %}

This page describes a signal of selection found in the
:doc:`{{ root_path }}population/{{ focal_population.id }}` population
{%- if reference_population is not none %}
when compared with the :doc:`{{ root_path }}population/{{ reference_population.id }}` population
{% endif -%}
using the :doc:`{{ root_path }}method/{{ statistic.id }}` statistic.
{%- if focus_start_seqid == focus_end_seqid -%}
The focus of this signal is on chromosome arm
**{{ focus_start_seqid }}** between positions **{{ intcomma(focus_start_coord) }}** and
**{{ intcomma(focus_end_coord) }}**.
{%- else -%}
The focus of this signal is between
**{{ focus_start_seqid }}:{{ intcomma(focus_start_coord) }}** and
**{{ focus_end_seqid }}:{{ intcomma(focus_end_coord) }}**.
{%- endif %}
The evidence supporting this signal is
{% if min_flank_delta_aic >= 100 -%}
**strong** (:math:`\Delta_{i}` >= 100 on both flanks)
{%- elif min_flank_delta_aic > 50 -%}
**moderate** (:math:`\Delta_{i}` >= 50 on both flanks)
{%- else -%}
**weak** (:math:`\Delta_{i}` < 50 on one or both flanks)
{%- endif -%}.

{% for locus in overlapping_loci %}
This signal overlaps the :doc:`{{ root_path }}known-locus/{{ locus.short_name|lower }}`, a genome
region with prior evidence of an association with insecticide resistance and/or recent positive selection in
*Anopheles* mosquitoes.
{% endfor %}

{% for locus in adjacent_loci %}
This signal occurs within 50 kbp of the :doc:`{{ root_path }}known-locus/{{ locus.short_name|lower }}`,
a genome region with prior evidence of an association with insecticide resistance and/or recent positive
selection in *Anopheles* mosquitoes.
{% endfor %}

.. raw:: html
    :file: peak_location.html

.. raw:: html

    <div class='bokeh-figure figure'><p class='caption'>
    <strong>Signal location</strong>. Blue markers show the values of the selection statistic.
    The dashed black line shows the fitted peak model. The shaded red area shows the focus of the
    selection signal. The shaded blue area shows the genomic region in linkage with the
    selection event. Use the mouse wheel or the controls at the top right of the plot to zoom
    in, and hover over genes to see gene names and descriptions.
    </p></div>

Genes
-----

{% if overlapping_genes|length == 0 %}
No genes overlap the focal region.
{% elif overlapping_genes|length == 1 %}
Gene {{ gene_doc(overlapping_genes[0], root_path, ir_candidates) }} overlaps the focal region.
{% elif overlapping_genes|length > 1 %}
The following {{ overlapping_genes|length }} genes overlap the focal region:
{%- for value in overlapping_genes %} {{ gene_doc(value, root_path, ir_candidates) }}{{ ", " if not loop.last }}
{%- endfor %}.
{% endif %}

{% if adjacent_genes|length == 0 %}
No genes are within 50 kbp of the focal region.
{% elif adjacent_genes|length == 1 %}
Gene {{ gene_doc(adjacent_genes[0], root_path, ir_candidates) }} is within 50 kbp of the focal region.
{% elif adjacent_genes|length > 1 %}
The following {{ adjacent_genes|length }} genes are within 50 kbp of the focal
region:
{%- for value in adjacent_genes %} {{ gene_doc(value, root_path, ir_candidates) }}{{ ", " if not loop.last }}
{%- endfor %}.
{% endif %}

Key to insecticide resistance candidate gene types: :sup:`1` metabolic;
:sup:`2` target-site; :sup:`3` behavioural; :sup:`4` cuticular.

{% if overlapping_signals|length > 0 -%}
Overlapping selection signals
-----------------------------

The following selection signals have a focus which overlaps with the
focus of this signal.

{{ signals_table(overlapping_signals, root_path) }}
{% endif %}

Diagnostics
-----------

The information below provides some diagnostics from the
:doc:`{{ root_path }}method/peak_modelling` algorithm.

.. raw:: html

    <div class="figure">
    <img src="{{ root_path }}_static/data/signal/{{ uid }}/peak_finding.png"/>
    <p class="caption"><strong>Selection signal in context</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="{{ root_path }}_static/data/signal/{{ uid }}/peak_targetting.png"/>
    <p class="caption"><strong>Peak targetting</strong>. @@TODO</p>
    </div>

.. raw:: html

    <div class="figure">
    <img src="{{ root_path }}_static/data/signal/{{ uid }}/peak_fit.png"/>
    <p class="caption"><strong>Peak fitting diagnostics</strong>. @@TODO</p>
    </div>

Model fit reports
~~~~~~~~~~~~~~~~~

Peak model::

    {{ fit_reports.peak|indent(4) }}

Null model::

    {{ fit_reports.null|indent(4) }}


Comments
--------

{{ disqus() }}
