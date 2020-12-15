import sys
import pandas as pd
import json

from helpers import get_db_connection


def get_contact_test_count():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Index_Test,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Index_Test
            ORDER BY Index_Test;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_index_count_json1():  # Python Transformations for Data Format
    df_risk = get_contact_test_count()
    # df column to list
    contact_list = df_risk['Index_Test'].tolist()
    count_list = df_risk['Count'].tolist()

    # Preparing data for trace1 - keys-value pair as input

    data_dic = {
        "labels": contact_list,
        "values": count_list,
        "type": "pie"
    }
    return data_dic


# A python dictionary as a JSON string
def get_index_count_json():
    json_list = list()
    json_list.append(get_index_count_json1())
    json_dict = {
        "result": json_list
    }
    data = json.dumps(json_dict)
    return data
