import pyodbc 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# importDataFromCsv...................................................

def importDataFromCsv(Name= 'combined_csv1.csv'):
    df=pd.read_csv(Name)
    return df

# importDataFromDB...................................................

def importDataFromDB(Driver='{SQL Server}',servername = 'THINKPADAM',DatabaseName = 'AIS'):

    conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=THINKPADAM;'
                         'Database=AIS;'
                         'Trusted_Connection=yes;')
    df = pd.read_sql_query('SELECT * FROM dbo.AIS_Data', conn)
    return df
