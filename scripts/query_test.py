#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import State, StateCapital

#State.objects.all()
#print State.objects.filter(name__startswith= 'T')
#state=State.objects.get(pk=158)
#print state.abbrev

#pop = small to great, -pop = great to small
# states=State.objects.all().order_by('pop')
# print states

# for state in states:
#     print state.name

#icontains is not case sensitive, contains is,
#same thing for istartswith and startswith

#states = State.objects.all().exclude(name__contains='Ala')
# states = State.objects.all().exclude(name__icontains='N')

# for state in states:
#         print state.name

#returns list of dictionaries
# states = State.objects.all().values('name', 'pop')
# print states

# for state in states:
#     print state

#list of lists
# states = State.objects.all().values_list('name', 'abbrev', 'pk')


# for state in states:
#     print "State name: %s, State Abbreviation: %s" % (state[0], state[1])

#states = State.objects.all().values_list('name', 'abbrev', 'pop')

# for name, abbrev, pop in states:
#     print "Name: {0}, Abbrev: {1}, Pop: {2}".format(name, abbrev, pop)

#states = State.objects.all().exclude(name__startswith='N').filter(pop__gte=500000).order_by('-pop').values_list('name', 'pop')

#print states

#for state in states:
    #good for objects
    #print "State name: %s, Pop: %s" % (state.name, state.pop)
    
    #good for dictionaries using values
    #print "%s %s" % (state['name'], state['pop'])

    #good for list of list using values_list('name', 'pop')
    #print "%s %s" % (state[0], state[1])

# states_list = ['Texas', 'California', 'Nevada', 'Alaska']

# states = State.objects.filter(name__in=states_list)
# print states

# state = State.objects.get(name='Alabama')
# print state.name
# print state.abbrev
# print state.statecapital_set.all()

# state= State.objects.get(pk=155)
# state2 = State.objects.get(pk=166)
# state3 = State.objects.get(pk=157)
# state4 = State.objects.get(pk=170)

# cap = StateCapital.objects.get(pk=1)
# cap2 = StateCapital.objects.get(pk=2)
# cap3 = StateCapital.objects.get(pk=3)

# #print state.name
# #print cap.name

# state.statecapital_set.remove(cap)
# cap.state.add(state)
# cap.state.add(state2)
# cap.state.add(state3)
# cap.state.add(state4)


# state.statecapital_set.add(cap)
# state.statecapital_set.add(cap2)
# state.statecapital_set.add(cap3)

# print cap.state.all()
# print '-' * 10
# print state.statecapital_set.all()

# states = State.objects.all()

# for state in states:
#     print "State: %s, Capital: %s" % (state.name, state.statecapital.name)

states_list = ['Texas', 'Alabama', 'Alaska', 'Mars']

for state in states_list:
    try:
        get_state = State.objects.get(name = state)
        print "State found! %s" % get_state
    except Exception, e:
        print "State missing %s" % e


