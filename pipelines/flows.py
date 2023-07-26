from prefect import Flow, Parameter
from tasks import (get_brt_data, load_data_to_postgres, process_data,
                   save_data_to_csv)

with Flow('Extracting BRT data') as flow:

    # Parameter
    url = Parameter('url', default='https://dados.mobilidade.rio/gps/brt')

    # Tasks

    data = get_brt_data(url)
    dataframe_brt = process_data(data)
    save_data_to_csv(dataframe_brt)
    load_data_to_postgres(dataframe_brt)

