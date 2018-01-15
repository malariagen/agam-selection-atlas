
{% macro intcomma(v) %}{{ "{:,}".format(v) }}{% endmacro %}


{% macro signal_doc(signal, root_path) -%}
:doc:`{{ root_path }}signal/{{ signal.uid }}/index`
{%- endmacro %}


{% macro signal_focus(signal) -%}
{{ signal.focus_start_seqid }}:{{ intcomma(signal.focus_start_coord|int) }}-
{%- if signal.focus_end_seqid != signal.focus_start_seqid -%}
{{ signal.focus_end_seqid }}:
{%- endif -%}
{{ intcomma(signal.focus_end_coord|int) }}
{%- endmacro %}


{% macro signal_score(signal) -%}
{{ intcomma(signal.delta_aic|int) }}
{%- endmacro %}


{% macro signals_table(signals, root_path) -%}
{% if signals|length > 0 -%}
.. cssclass:: table-hover
.. list-table::
    :widths: auto
    :header-rows: 1

    * - Signal
      - Statistic
      - Population
      - Focus
      - Peak Model :math:`\Delta_{i}`
      - Max Percentile
    {% for signal in signals -%}
    * - {{ signal_doc(signal, root_path) }}
      - {{ signal.statistic }}
      - {{ signal.focal_population_label }}
      - {{ signal_focus(signal) }}
      - {{ signal_score(signal) }}
      - {{ "{:.1f}%".format(signal.max_percentile|float * 100) }}
    {% endfor %}

{% else %}
No signals.
{% endif %}
{%- endmacro %}


{% macro gene_doc(value, root_path, ir_candidates, describe=True) -%}
:doc:`{{ root_path }}gene/{{ value.id }}`
{%- if value.id in ir_candidates.metabolic %}:sup:`1`
{%- elif value.id in ir_candidates.target_site %}:sup:`2`
{%- elif value.id in ir_candidates.behavioural %}:sup:`3`
{%- elif value.id in ir_candidates.cuticular %}:sup:`4`
{%- endif %}
{%- if value.name or (value.description and describe) %} (
    {%- if value.name %}{{ value.name|trim }}{% endif -%}
    {%- if value.name and value.description and describe %} - {% endif %}
    {%- if value.description and describe %}{{ value.description|trim }}{% endif -%}
)
{%- endif %}
{%- endmacro %}


{% macro disqus(identifier='') %}
.. raw:: html

    <div id="disqus_thread"></div>
    <script>
    {% if identifier|length > 0 %}
    var disqus_config = function () {
        this.page.identifier = '{{ identifier }}';
    };
    {% endif %}
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://agam-selection-atlas.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments.</a></noscript>

{% endmacro %}
