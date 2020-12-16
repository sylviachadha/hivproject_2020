import sys
import pandas as pd
import json

from helpers import get_db_connection


def get_status_count_recent():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Status,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Status,New_HIV_Diagnosis_and_Recency_Test_taken
            HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Recent'
            ORDER BY Status;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d

ans = get_status_count_recent()

def get_status_count_json1():  # Python Transformations for Data Format
    df_recent = get_status_count_recent()
    # df column to list
    status_list = df_recent['Status'].tolist()
    count_list = df_recent['Count'].tolist()

    # Preparing data for trace1 - keys-value pair as input

    trace1_dic = {
        "x": status_list,
        "y": count_list,
        "name": "Recent",
        "type": "bar"
    }
    return trace1_dic


def get_status_count_LT():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Status,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Status,New_HIV_Diagnosis_and_Recency_Test_taken
            HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Long-term'
            ORDER BY Status;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_status_count_json2():  # Python Transformations for Data Format
    df_LT = get_status_count_LT()
    # df column to list
    status_list = df_LT['Status'].tolist()
    count_list = df_LT['Count'].tolist()

    trace2_dic = {
        "x": status_list,
        "y": count_list,
        "name": "Long-Term",
        "type": "bar"
    }

    return trace2_dic


# A python list as a JSON string
def get_status_count_json():
    json_list = list()
    json_list.append(get_status_count_json1())
    json_list.append(get_status_count_json2())
    print(json_list)
    json_dict = {
        "result": json_list
    }
    data = json.dumps(json_dict)

    return data
