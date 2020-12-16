import sys
import pandas as pd
import json

from helpers import get_db_connection


def get_date_recent():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT RecencyTest_Date,COUNT(New_HIV_Diagnosis_and_Recency_Test_taken) AS Count
            FROM HIV_Sample_tables
            WHERE New_HIV_Diagnosis_and_Recency_Test_taken = 'Recent'
            GROUP BY RecencyTest_Date;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d


ans = get_date_recent()


# def get_date_recent_month():
#     d = get_date_recent()
#     d.replace(1, 'Jan', inplace=True)
#     d.replace(2, 'Feb', inplace=True)
#     d.replace(3, 'Mar', inplace=True)
#     return d


def get_status_count_json1():  # Python Transformations for Data Format
    df_recent = get_date_recent()
    # df column to list

    date_list = df_recent['RecencyTest_Date'].apply(lambda x: x.strftime('%Y-%m-%d')).tolist()
    count_list = df_recent['Count'].tolist()

    # Preparing data for trace1 - keys-value pair as input

    trace1_dic = {
        "x": date_list,
        "y": count_list,
        "type": "scatter",
        "mode": "lines",
        "name": "Recent",
        "line": {"color": "#17BECF"}

    }
    return trace1_dic


ans1 = get_status_count_json1()


def get_date_LT():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT RecencyTest_Date,COUNT(New_HIV_Diagnosis_and_Recency_Test_taken) AS Count
            FROM HIV_Sample_tables
            WHERE New_HIV_Diagnosis_and_Recency_Test_taken = 'Long-Term'
            GROUP BY RecencyTest_Date;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d

ans = get_date_LT()
# def get_date_LT_month():
#     d = get_date_LT()
#     d.replace(1, 'Jan', inplace=True)
#     d.replace(2, 'Feb', inplace=True)
#     d.replace(3, 'Mar', inplace=True)
#     return d


def get_status_count_json2():  # Python Transformations for Data Format
    df_LT = get_date_LT()
    # df column to list - This column is datetime so convert to
    # string cz Javascript expects string value
    date_list = df_LT['RecencyTest_Date'].apply(lambda x: x.strftime('%Y-%m-%d')).tolist()
    print(date_list)
    #date_list = df_LT['RecencyTest_Date'].tolist()
    count_list = df_LT['Count'].tolist()

    trace2_dic = {
        "x": date_list,
        "y": count_list,
        "type": "scatter",
        "mode": "lines",
        "name": "Long-term",
        "line": {"color": "#7F7F7F"}
    }

    return trace2_dic


ans2 = get_status_count_json2()
ans2


# A python list as a JSON string
def get_RLcount_json():
    json_list = list()
    json_list.append(get_status_count_json1())
    json_list.append(get_status_count_json2())
    json_dict = {
        "result": json_list
    }
    data = json.dumps(json_dict)

    return data


ans = get_RLcount_json()
ans