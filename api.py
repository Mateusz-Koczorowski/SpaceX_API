import csv
import sys
import requests

url = "https://api.spacexdata.com/v3/launches"


class OpenFile():
    head_line = ['flight_number', 'mission_name', 'rocket_id', 'rocket_name', 'launch_date_utc', 'video_link']

    def __init__(self, url):
        self.url = url

    def fetch_spacex(self):
        try:
            result = requests.get(url)
            result.raise_for_status()
        except requests.exceptions.HTTPError:
            raise print("Fail to fetch data!!")
        return result.json()

    def __enter__(self):
        self.spacex_file = open('flights_spacex.csv', mode='w', newline='')
        print("Opening file!")

    def run(self):
        self.data = self.fetch_spacex()
        self.csv_write = csv.writer(self.spacex_file)
        if len(sys.argv) > 1:
            start_arg = sys.argv[1]
            if start_arg == "-h":
                self.csv_write.writerow(self.head_line)
        for row in self.data:
            flight_number = row.get('flight_number')
            mission_name = row.get('mission_name')
            rocket_id = row.get('rocket').get('rocket_id')
            rocket_name = row.get('rocket').get('rocket_name')
            launch_date_utc = row.get('launch_date_utc')
            video_link = row.get('links').get('video_link', None)
            list_to_write = [flight_number, mission_name, rocket_id, rocket_name, launch_date_utc, video_link]
            print(list_to_write)
            self.csv_write.writerow(list_to_write)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spacex_file.close()
        print("Closing file!")


spacex = OpenFile(url)

with spacex:
    spacex.run()
