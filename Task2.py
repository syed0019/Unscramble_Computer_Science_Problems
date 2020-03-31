"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from operator import itemgetter

def number_with_max_duration(calls_records):
    call_duration = 0
    new_dict = {}

    for lst in calls_records:
        for n in lst[0:2]:
            new_dict[n] = call_duration

    for lst in calls_records:
        for n in lst[0:2]:
            if n in new_dict:
                call_duration = int(lst[3])
                new_dict[n] += call_duration

    print('{} spent the longest time, {} seconds, on the phone during September 2016.'
          .format(max(new_dict.items(), key=itemgetter(1))[0], max(new_dict.items(), key=itemgetter(1))[1]))
    
number_with_max_duration(calls)
