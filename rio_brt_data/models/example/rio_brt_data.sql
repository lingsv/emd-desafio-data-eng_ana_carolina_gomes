
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/


{{ config(materialized='table', schema='public', alias='rio_brt_data') }}

-- Defina a estrutura da tabela resultante
-- Certifique-se de ajustar os tipos de dados conforme necessário
-- O DBT criará a tabela automaticamente com base na consulta SELECT
SELECT
    codigo,
    latitude,
    longitude,
    velocidade 
FROM {{ source('rio_brt_data', 'rio_brt_data') }}
GROUP BY codigo,latitude, longitude, velocidade
/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
