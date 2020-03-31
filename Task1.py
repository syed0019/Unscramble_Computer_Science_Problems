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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def unique_tel_numbers(lists_of_texts, lists_of_calls):
    records = lists_of_texts + lists_of_calls
    
    total_numbers = []
    for lst in records:
        total_numbers.append(lst[0])
        total_numbers.append(lst[1])

    unique_numbers = set(total_numbers)
    
    count = len(unique_numbers)
    
    print('There are {} different telephone numbers in the records.'.format(count))

unique_tel_numbers(texts, calls)
