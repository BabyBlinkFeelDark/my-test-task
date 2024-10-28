import pandas as pd
import mysql.connector

from .config import DATABASE_CONFIG


def get_data(query):
    """
    Выполняет SQL-запрос к базе данных и возвращает результаты в виде DataFrame.

    Подключается к базе данных, выполняет указанный SQL-запрос, загружает результаты
    в объект pandas DataFrame и закрывает соединение.

    :param query: SQL-запрос, который необходимо выполнить.
    :return: DataFrame, содержащий результаты выполнения запроса.
    """
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

