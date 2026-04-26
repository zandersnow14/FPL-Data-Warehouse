{% macro extract_json(column, key) %}
    {% if target.type == 'duckdb' %}
        JSON_EXTRACT_STRING({{ column }}, '$.{{ key }}')
    {% elif target.type == 'bigquery' %}
        json_extract_scalar({{ column }}, '$.{{ key }}')
    {% endif %}
{% endmacro %}