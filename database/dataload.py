import sqlite3
import csv
import os

if os.path.exists("weather.db"):
    os.remove("weather.db")

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

with open("create_db.sql", "r", encoding="utf-8") as f:
    sql_script = f.read()

cursor.executescript(sql_script)

def load_csv(file_path, table_name):
    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if not row or all(cell.strip() == "" for cell in row):
                continue
            placeholders = ",".join(["?"] * len(row))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(query, row)

load_csv("locations.csv", "Location")
load_csv("weather_stations.csv", "WeatherStation")
load_csv("station_metadata.csv", "StationMetadata")
load_csv("measurement_type.csv", "MeasurementType")
load_csv("users.csv", "Users")
load_csv("daily_measurement.csv", "DailyMeasurement")
load_csv("user_queries.csv", "UserQuery")

conn.commit()
conn.close()

print("Database setup complete. All data has been loaded into weather.db.")
