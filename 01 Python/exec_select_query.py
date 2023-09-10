import pandas as pd
import pyodbc


def main():

    server = 'DESKTOP-EHI4MET\DEV2019'
    db_name = 'AdventureWorksDW2019'

    print('Execution started')
    cursor = conn_sql(server, db_name)
    query = ' SELECT  *   FROM [dbo].[DimDate] '
    df, schema = exec_select(cursor, query)
    print(df.shape)
    print(schema)


# connect to sql server database
def conn_sql(server, db_name):

    driver = "Driver={SQL Server Native Client 11.0};"
    conn_str = (driver + "Server=" + server + ";Database=" + db_name + ';Trusted_Connection=yes;')
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    return cursor


# execute select query and returns data in dataframe and schema. Also closes the sql connection
def exec_select(cursor, query):

    cursor.execute(query)
    df = pd.DataFrame.from_records(cursor, columns=[i[0] for i in cursor.description])  # description gives column names
    schema = list(df.columns)
    cursor.close()
    return df, schema


main()