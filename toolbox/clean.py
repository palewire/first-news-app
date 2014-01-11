"""
A quick clean up of the CSV I downloaded from OpenBaltimore.

https://data.baltimorecity.gov/Crime/CCTV-Locations/hdyb-27ak

The only thing I did was split the 'Location 1' field into a separate
latitude and longitude fields to save the students this drudgery during class.
"""
import os
import csv

def clean():
    csv_path = os.path.join("static", "baltimore-cctv-locations.csv")
    reader = csv.DictReader(open(csv_path, 'r'))
    out_path = os.path.join("static", "baltimore-cctv-locations-clean.csv")
    outfile = csv.writer(open(out_path, 'w'))
    outfile.writerow(['location', 'number', 'project', 'x', 'y'])
    for row in reader:
        y, x = row['Location 1'][1:-1].split(", ")
        outrow = [
            row['cameraLocation'],
            row['cameraNumber'],
            row['cameraProject'],
            x,
            y,
        ]
        outfile.writerow(outrow)


if __name__ == '__main__':
    clean()
