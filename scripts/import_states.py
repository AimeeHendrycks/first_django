#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


from main.models import State, StateCapital, City

print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "states.csv"
file_name2 = "zip_codes_states.csv"

#print "%s%s" % (dir_name, file_name)
#print "{0}/{1}".format(dir_name, file_name)

states_csv = os.path.join(dir_name, file_name)

zip_code_csv = os.path.join(dir_name, file_name2)

print zip_code_csv
csv_file = open(states_csv, 'r')
csv_file2 = open(zip_code_csv, 'r')

reader = csv.DictReader(csv_file)
reader2 = csv.DictReader(csv_file2)

for row in reader:
    new_state, created = State.objects.get_or_create(name=row['state'])
    print new_state.name
    print created
    new_state.abbrev = row['abbrev']
    new_state.save()
    
    new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
    new_capital.lat = row['latitude']
    new_capital.lon = row['longitude']
    new_capital.pop = row['population']
    new_capital.state = new_state
    new_capital.save()

for row in reader2:

    new_city, created = City.objects.get_or_create(zip_code=row['zip_code'])
    print new_city.zip_code
    # print created
    new_city.lat = row['latitude']
    new_city.lon = row['longitude']
    new_city.name = row['city']
    new_city.county = row['county']
    try:
        new_city.state = State.objects.get(abbrev=row['state'])
    except Exception, e:
        print row['state'], "State missing! %s" % e
    try:
        new_city.save()
    except:
        print e
        print new_city.county
        print new_city.lat
        print new_city.lon

csv_file.close()
csv_file2.close()