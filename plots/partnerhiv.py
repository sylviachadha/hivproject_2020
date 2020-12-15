import sys
import pandas as pd
import json

from helpers import get_db_connection


def get_phiv_count_recent():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Partner_HIV_Result,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Partner_HIV_Result,New_HIV_Diagnosis_and_Recency_Test_taken
            HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Recent'
            ORDER BY Partner_HIV_Result DESC;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_phiv_count_json1():  # Python Transformations for Data Format
    df_recent = get_phiv_count_recent()
    # df column to list
    phiv_list = df_recent['Partner_HIV_Result'].tolist()
    count_list = df_recent['Count'].tolist()

    # Preparing data for trace1 - keys-value pair as input

    trace1_dic = {
        "x": phiv_list,
        "y": count_list,
        "name": "Recent",
        "type": "bar",
        "marker": {
            "color": '#0000cd'
        }
    }
    return trace1_dic


def get_phiv_count_LT():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Partner_HIV_Result,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Partner_HIV_Result,New_HIV_Diagnosis_and_Recency_Test_taken
            HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Long-term'
            ORDER BY Partner_HIV_Result DESC;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_phiv_count_json2():  # Python Transformations for Data Format
    df_LT = get_phiv_count_LT()
    # df column to list
    phiv_list = df_LT['Partner_HIV_Result'].tolist()
    count_list = df_LT['Count'].tolist()

    trace2_dic = {
        "x": phiv_list,
        "y": count_list,
        "name": "Long-Term",
        "type": "bar",
        "marker": {
            "color": '#dc143c'
        }
    }

    return trace2_dic


# A python list as a JSON string
def get_phiv_count_json():
    json_list = list()
    json_list.append(get_phiv_count_json1())
    json_list.append(get_phiv_count_json2())
    print(json_list)
    json_dict = {
        "result": json_list
    }
    data = json.dumps(json_dict)

    return data
