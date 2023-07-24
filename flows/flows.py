from prefect import Flow, Parameter

from tasks import (get_brt_data, 
                   process_data, 
                   save_data_to_csv,
                   load_data_to_postgres)
                   

with Flow('Extracting BRT data') as flow:

    # Parameter
    url = Parameter('url', default='https://dados.mobilidade.rio/gps/brt')

    # Tasks

    data = get_brt_data(url)
    dataframe_brt = process_data(data)
    save_data_to_csv(dataframe_brt)
    load_data_to_postgres(dataframe_brt)

#with Flow('Load databse to DBT') as flow:
#    load_to_dbt()