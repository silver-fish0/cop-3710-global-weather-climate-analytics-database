import os
import shutil

os.makedirs("data", exist_ok=True)

files_to_copy = [
    "locations.csv",
    "weather_stations.csv",
    "station_metadata.csv",
    "measurement_type.csv",
    "daily_measurement.csv",
    "users.csv",
    "user_queries.csv"
]

copied = []
missing = []

for file_name in files_to_copy:
    if os.path.exists(file_name):
        destination = os.path.join("data", file_name)
        shutil.copy(file_name, destination)
        copied.append(file_name)
    else:
        missing.append(file_name)

print("Preprocessing complete.")
print("Copied files:")
for f in copied:
    print(f" - {f}")

if missing:
    print("\nMissing files:")
    for f in missing:
        print(f" - {f}")