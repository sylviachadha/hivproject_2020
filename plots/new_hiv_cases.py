import sys
import pandas as pd
import json

from helpers import get_db_connection


def new_hiv_count():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT New_HIV_Diagnosis_and_Recency_Test_taken,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY New_HIV_Diagnosis_and_Recency_Test_taken
            ORDER BY New_HIV_Diagnosis_and_Recency_Test_taken;;;;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_hiv_count_json1():  # Python Transformations for Data Format
    df_hiv = new_hiv_count()
    # df column to list
    infection_list = df_hiv['New_HIV_Diagnosis_and_Recency_Test_taken'].tolist()
    count_list = df_hiv['Count'].tolist()

    # Preparing data for trace1 - keys-value pair as input

    data_dic = {
        "labels": infection_list,
        "values": count_list,
        "type": "pie"
    }
    return data_dic


# A python dictionary as a JSON string
# First we put result in list cz plotly expects result to be in a list
def get_hiv_count_json():
    json_list = list()
    json_list.append(get_hiv_count_json1())
    json_dict = {
        "result": json_list
    }
    data = json.dumps(json_dict)
    return data
