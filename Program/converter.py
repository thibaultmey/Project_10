import sqlite3
import pandas

conn = sqlite3.connect('locations.db')

df = pandas.read_csv('locations.csv')

df.to_sql('locations', conn, if_exists='append', index=False)