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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def possible_telemarketers(calling_records):
    calling_numbers = []
    for call in calls:
        calling_numbers.append(call[0:2][0])

    telemarketer_numbers = []
    for num in calling_numbers:
        if num[:3] == '140':
            telemarketer_numbers.append(num)

    clean_list = sorted(set(telemarketer_numbers))

    print('"These numbers could be telemarketers: "')
    for num in clean_list:
        print(num)
        
possible_telemarketers(calls)