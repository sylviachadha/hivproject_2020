import sys
import pandas as pd
import json

from helpers import get_db_connection


def get_site_count_recent():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Site_ID,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Site_ID,New_HIV_Diagnosis_and_Recency_Test_taken
            HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Recent'
            ORDER BY Site_ID;''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_site_count_json1():  # Python Transformations for Data Format
    df_recent = get_site_count_recent()
    # df column to list
    site_list = df_recent['Site_ID'].tolist()
    count_list = df_recent['Count'].tolist()

    # Preparing data for trace1 - keys-value pair as input

    trace1_dic = {
        "type": "bar",
        "x": count_list,
        "y": site_list,
        "orientation": 'h',
        "name": "Recent",
        "marker": {
            "color": '#a52a2a'
        }
    }

    return trace1_dic


def get_site_count_LT():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Site_ID,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Site_ID,New_HIV_Diagnosis_and_Recency_Test_taken
            HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Long-term'
            ORDER BY Site_ID;''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_site_count_json2():  # Python Transformations for Data Format
    df_LT = get_site_count_LT()
    # df column to list
    site_list = df_LT['Site_ID'].tolist()
    count_list = df_LT['Count'].tolist()

    trace2_dic = {
        "type": "bar",
        "x": count_list,
        "y": site_list,
        "orientation": 'h',
        "name": "Long-Term",
        "marker": {
            "color": '#c0c0c0'
        }
    }

    return trace2_dic


# A python list as a JSON string
def get_site_count_json():
    json_list = list()
    json_list.append(get_site_count_json1())
    json_list.append(get_site_count_json2())
    print(json_list)
    json_dict = {
        "result": json_list
    }
    data = json.dumps(json_dict)

    return data
