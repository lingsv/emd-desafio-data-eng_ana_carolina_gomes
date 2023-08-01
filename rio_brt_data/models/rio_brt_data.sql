
{{ config(materialized='table', schema='public', alias='rio_brt_data') }}

SELECT
    codigo,
    placa,
    linha,
    latitude,
    longitude,
    dataHora,
    velocidade,
    id_migracao_trajeto,
    sentido,
    trajeto,
    hodometro,
    direcao

FROM {{ source('rio_brt_data', 'rio_brt_data') }}

