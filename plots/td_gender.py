import sys
import pandas as pd
import json

from helpers import get_db_connection

def get_gender_male():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT DATEPART(month, RecencyTest_Date) AS Month,COUNT(New_HIV_Diagnosis_and_Recency_Test_taken) AS Count
            FROM HIV_Sample_tables
            /*WHERE New_HIV_Diagnosis_and_Recency_Test_taken = 'Recent' and Sex = 'Male'*/
            WHERE Sex = 'Male'
            GROUP BY DATEPART(month, RecencyTest_Date)
            order by Month;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d

def get_male_count():
    d = get_gender_male()
    d.replace(1, 'Jan', inplace=True)
    d.replace(2, 'Feb', inplace=True)
    d.replace(3, 'Mar', inplace=True)
    return d


def get_status_count_json1():  # Python Transformations for Data Format
    df_male = get_male_count()
    # df column to list
    month_list = df_male['Month'].tolist()
    count_list = df_male['Count'].tolist()

    # Preparing data for trace1 - keys-value pair as input

    trace1_dic = {
        "x": month_list,
        "y": count_list,
        "type": "scatter",
        "mode": "lines",
        "name": "Male"

    }
    return trace1_dic


def get_gender_female():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT DATEPART(month, RecencyTest_Date) AS Month,COUNT(New_HIV_Diagnosis_and_Recency_Test_taken) AS Count
            FROM HIV_Sample_tables
            WHERE Sex = 'Female'
            GROUP BY DATEPART(month, RecencyTest_Date)
            order by Month;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d

def get_female_count():
    d = get_gender_female()
    d.replace(1, 'Jan', inplace=True)
    d.replace(2, 'Feb', inplace=True)
    d.replace(3, 'Mar', inplace=True)
    return d


def get_status_count_json2():  # Python Transformations for Data Format
    df_female = get_female_count()
    # df column to list
    month_list = df_female['Month'].tolist()
    count_list = df_female['Count'].tolist()

    trace2_dic = {
        "x": month_list,
        "y": count_list,
        "type": "scatter",
        "mode": "lines",
        "name": "Female"
    }

    return trace2_dic


def get_trgender():  # Extract Data from Microsoft SQL Server
    conn = get_db_connection()
    SQL_Query = pd.read_sql_query(
        '''SELECT DATEPART(month, RecencyTest_Date) AS Month,COUNT(New_HIV_Diagnosis_and_Recency_Test_taken) AS Count
            FROM HIV_Sample_tables
            WHERE Sex = 'Trangender'
            GROUP BY DATEPART(month, RecencyTest_Date)
            order by Month;;
            ''', conn)
    d = pd.DataFrame(SQL_Query)
    conn.close()
    return d

def get_trangender_count():
    d = get_trgender()
    d.replace(1, 'Jan', inplace=True)
    d.replace(2, 'Feb', inplace=True)
    d.replace(3, 'Mar', inplace=True)
    return d


def get_status_count_json3():  # Python Transformations for Data Format
    df_tr = get_trangender_count()
    # df column to list
    month_list = df_tr['Month'].tolist()
    count_list = df_tr['Count'].tolist()

    trace3_dic = {
        "x": month_list,
        "y": count_list,
        "type": "scatter",
        "mode": "lines",
        "name": "Transgender"
    }

    return trace3_dic


# A python list as a JSON string
def get_gcount_json():
    json_list = list()
    json_list.append(get_status_count_json1())
    json_list.append(get_status_count_json2())
    json_list.append(get_status_count_json3())

    json_dict = {
        "result": json_list
    }
    data = json.dumps(json_dict)

    return data


