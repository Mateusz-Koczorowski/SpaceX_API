import requests
import csv
import json
import sys

class OpenFile:
    url = "https://api.spacexdata.com/v3/launches"
    result = requests.get(url)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError:
            print("No connection!")
    result = result.json()
    head_line = ['flight_number', 'mission_name', 'rocket_id', 'rocket_name', 'launch_date_utc', 'video_link']
    def __enter__(self):
        self.spacex_file = open('flights_spacex.csv', mode='w', newline='')
        print("Opening file!")

    def run(self):
        self.csv_write = csv.writer(self.spacex_file)
        if len(sys.argv) > 1:
            start_arg = sys.argv[1]
            if start_arg == "-h":
                self.csv_write.writerow(self.head_line)
        for row in self.result:
            flight_number = row.get('flight_number')
            mission_name = row.get('mission_name')
            rocket_id = row.get('rocket').get('rocket_id')
            rocket_name = row.get('rocket').get('rocket_name')
            launch_date_utc = row.get('launch_date_utc')
            video_link = row.get('links').get('video_link')
            list_to_write = [flight_number, mission_name, rocket_id, rocket_name, launch_date_utc, video_link]
            print(list_to_write)
            self.csv_write.writerow(list_to_write)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spacex_file.close()
        print("Closing file!")

spacex = OpenFile()

with spacex:
    spacex.run()