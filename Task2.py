"""
Read file into texts and calls.
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
def max_duration(call_records):
    
    call_duration = []
    for record in call_records:
        call_duration.append(int(record[3]))
    max_duration = max(call_duration)
    return max_duration

def finding_tel_num(call_records):
    max_time = str(max_duration(call_records))
    for record in call_records:
        if record[3] == max_time:
            print('"{} & {} spent the longest time, {} seconds, on the phone during September 2016."'
                  .format(record[0], record[1], record[3]))
    
finding_tel_num(calls)