import pandas as pd
from import_DB import importDataFromDB,importDataFromCsv
from DBscan import AIS_DBscan as adb

df = importDataFromDB()

adb.Describe_DB(df)

# print(df)
# print(type(df))


