import os
import csv
from datetime import datetime
from states.models import Week, State, ActivityLevel
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Loads flu activity data from a CSV file into the database'
    
    def handle(self, *args, **options):
        path = os.path.join("./states/data/week44.csv")
        data = csv.DictReader(open(path, 'r'))
        for row in data:
            if row.get("STATENAME") == 'New York City':
                continue
            print "Loading %s" % (row.get("STATENAME"))
            state, state_created = State.objects.get_or_create(
                name = row.get("STATENAME"),
                website_name = row.get("WEBSITE"),
                website_url = row.get("URL"),
            )
            week, week_created = Week.objects.get_or_create(
                number = int(row.get("WEEK ")),
                end_date = datetime.strptime(row.get("WEEKENDING"), '%b-%d-%Y')
            )
            level, level_created = ActivityLevel.objects.get_or_create(
                state = state,
                week = week,
                activity_level = int(row.get("ACTIVITY_LEVEL").split(" ")[-1])
            )

