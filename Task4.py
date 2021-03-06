"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
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

def possible_telemarketers(calls_records, texts_records):
    calling_numbers = []
    for call in calls_records:
        calling_numbers.append(call[0:2][0])
    unique_calling_numbers = set(calling_numbers)

    receiving_numbers = []
    for lst in calls_records:
        receiving_numbers.append(lst[1])

    texts_numbers = []
    for lst in texts_records:
        texts_numbers.append(lst[0])
        texts_numbers.append(lst[1])

    telemarketer_numbers = []
    for num in unique_calling_numbers:
        if num not in receiving_numbers:
            if num not in texts_numbers:
                telemarketer_numbers.append(num)

    sorted_list = sorted(telemarketer_numbers)
    print('These numbers could be telemarketers:')
    for num in sorted_list:
        print(num)
        
possible_telemarketers(calls, texts)
