SELECT
    CAST({{ extract_json('payload', 'id') }} AS INT) AS team_id,
    {{ extract_json('payload', 'name') }} AS full_name,
    {{ extract_json('payload', 'short_name') }} AS short_name
FROM {{ source('bronze', 'teams') }}
WHERE ingested_at = (SELECT MAX(ingested_at) FROM {{ source('bronze', 'teams') }})