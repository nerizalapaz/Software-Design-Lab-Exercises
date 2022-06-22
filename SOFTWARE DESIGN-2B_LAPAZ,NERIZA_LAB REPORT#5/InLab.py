#Create a SQLite database connection to a memory-based database by writing a Python program.
import sqlite3

try:
   sqlite_Connection = sqlite3.connect('temp.db')
   conn = sqlite3.connect(':memory:')
   print("\nCreating and connecting a memory database to SQLite.")
   sqlite_select_Query = "select sqlite_version();"
   conn.execute(sqlite_select_Query)
   print("\nSQLite Database Version is: ", sqlite3.version)
   conn.close()
except sqlite3.Error as error:
   print("\nError while connecting to sqlite", error)
finally:
   if (sqlite_Connection):
       sqlite_Connection.close()
       print("\nThe SQLite connection is closed.")