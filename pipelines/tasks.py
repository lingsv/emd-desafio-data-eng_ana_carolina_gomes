import datetime
import json
import os
import time

import pandas as pd
import psycopg2
import requests
from prefect import task
from psycopg2 import extras
from utils import log


@task
def get_brt_data(url: str) -> str:
    """Extracts the data from the specific url.

    Args:
        url (str): URL with BRT data.

    Returns:
        str: Request response in JSON format.
    """
    dados_api = []

    for i in range(10):

        try:
            response = requests.get(url)
            json_data = response.json()['veiculos']
            dados_api.extend(json_data)
            time.sleep(60)

        except requests.exceptions.RequestException as error:
            raise error
    log('Data extracted with success!')

    return dados_api


@task
def process_data(data) -> pd.DataFrame:
    """Converts JSON data to a Pandas dataframe.

    Args:
        data (_type_): JSON data.

    Returns:
        pd.DataFrame: Final dataframe.
    """
    data_dict = pd.DataFrame(data)
    data_dict['dataHora'] = data_dict['dataHora'].apply(
        lambda d: datetime.datetime.fromtimestamp(d/1000))

    log('Data has been converted on a dataframe.')

    return data_dict


@task
def save_data_to_csv(dataframe: pd.DataFrame) -> None:
    """Saves the dataframe into a CSV file.
    Args:
        dataframe (pd.DataFrame): The dataframe that will be saved.
    """
    dataframe.to_csv('data/dados_brt.csv', index=False)
    log('Data saved to CSV.')


@task
def load_data_to_postgres(data: pd.DataFrame) -> None:
    """Loads data to a postgres table.

    Args:
        data (pd.DataFrame): Target dataframe.
    """

    with open('credentials.json', 'r') as jsonfile:

        postgres_credentials = json.load(jsonfile)

    log('Loaded postgres credentials.')

    connection_string = psycopg2.connect(
        host=postgres_credentials['host'],
        database=postgres_credentials['database'],
        user=postgres_credentials['user'],
        password=postgres_credentials['password'],
    )

    with connection_string.cursor() as cursor:
        create_table = """
            CREATE TABLE IF NOT EXISTS brt_data(
                codigo VARCHAR,
                placa VARCHAR,
                linha VARCHAR,
                latitude VARCHAR,
                longitude VARCHAR,
                dataHora VARCHAR,
                velocidade VARCHAR,
                id_migracao_trajeto VARCHAR,
                sentido VARCHAR,
                trajeto VARCHAR,
                hodometro VARCHAR,
                direcao VARCHAR              
            )
            """

        cursor.execute(create_table)

        insert_query = "INSERT INTO rio_brt_data VALUES %s"
        extras.execute_values(cursor, insert_query, data.values)

    connection_string.commit()
    connection_string.close()

    log('Loaded data to postgres.')
