import requests
import csv
import json

url = "https://api.spacexdata.com/v3/launches"
result = requests.get(url)
result = result.json()
with open("flights_spacex.csv", mode="w") as spacex_file:
    csv_write = csv.writer(spacex_file)
    for row in result:
        flight_number = row['flight_number']
        mission_name = row['mission_name']
        rocket_id = row['rocket']['rocket_id']
        rocket_name = row['rocket']['rocket_name']
        launch_date_utc = row['launch_date_utc']
        video_link = row['links']['video_link']
        list_to_write = [flight_number, mission_name, rocket_id, rocket_name, launch_date_utc, video_link]
        print(list_to_write)
        csv_write.writerow(list_to_write)
