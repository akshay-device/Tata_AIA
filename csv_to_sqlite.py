import pandas
import sqlite3

try:
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)

    df = pandas.read_csv(r'E:\PYCHARM NEW PROJECTS\Tatat_AIA_Task\task1.csv')
    df.columns = df.columns.str.replace(' ', '_')
    df.to_sql('tata_api_tata_rec', sqliteConnection, if_exists='append',index=False)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")



