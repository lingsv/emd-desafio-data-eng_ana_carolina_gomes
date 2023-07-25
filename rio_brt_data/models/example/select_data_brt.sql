{{ config(materialized='view', schema='public', alias='select_data_brt') }}

SELECT 
    codigo,
    latitude,
    longitude,
    velocidade,
    direcao

FROM {{ ref('rio_brt_data') }}

GROUP BY codigo, latitude, longitude, velocidade, direcao