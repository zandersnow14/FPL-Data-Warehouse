SELECT
    CAST({{ extract_json('payload', 'id') }} AS INT) AS player_id,
    {{ extract_json('payload', 'first_name') }} AS first_name,
    {{ extract_json('payload', 'second_name') }} AS second_name,
    {{ extract_json('payload', 'web_name') }} AS web_name,
    CAST({{ extract_json('payload', 'team') }} AS INT) AS team_id,
    CAST({{ extract_json('payload', 'element_type') }} AS INT) AS position_id,
    CAST({{ extract_json('payload', 'now_cost') }} AS INT) / 10 AS price,
    {{ extract_json('payload', 'status') }} AS status,
    CAST({{ extract_json('payload', 'code') }} AS INT) AS code
FROM {{ source('bronze', 'players') }}
WHERE ingested_at = (SELECT MAX(ingested_at) FROM {{ source('bronze', 'players') }})