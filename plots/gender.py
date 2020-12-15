import sys
import pandas as pd
import json

from helpers import get_db_connection


def get_sex_count_recent():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Sex,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Sex,New_HIV_Diagnosis_and_Recency_Test_taken
            HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Recent'
            ORDER BY Sex;
;''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_sex_count_json1():  # Python Transformations for Data Format
    df_recent = get_sex_count_recent()
    # df column to list
    gender_list = df_recent['Sex'].tolist()
    count_list = df_recent['Count'].tolist()

    # Preparing data for trace1 - keys-value pair as input

    trace1_dic = {
        "x": gender_list,
        "y": count_list,
        "name": "Recent",
        "type": "bar",
        "marker": {
            "color": '#1e90ff'
        }
    }

    return trace1_dic


def get_sex_count_LT():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT Sex,COUNT(*) AS Count
            FROM HIV_Sample_tables
            GROUP BY Sex,New_HIV_Diagnosis_and_Recency_Test_taken
            HAVING New_HIV_Diagnosis_and_Recency_Test_taken = 'Long-term'
            ORDER BY Sex;
;''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


def get_sex_count_json2():  # Python Transformations for Data Format
    df_LT = get_sex_count_LT()
    # df column to list
    gender_list = df_LT['Sex'].tolist()
    count_list = df_LT['Count'].tolist()

    trace2_dic = {
        "x": gender_list,
        "y": count_list,
        "name": "Long-Term",
        "type": "bar",
        "marker": {
            "color": '#00fa9a'
        }
    }

    return trace2_dic


# A python list as a JSON string
def get_sex_count_json():
    json_list = list()
    json_list.append(get_sex_count_json1())
    json_list.append(get_sex_count_json2())
    print(json_list)
    json_dict = {
        "result": json_list
    }
    data = json.dumps(json_dict)

    return data
