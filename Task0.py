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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def first_text_record(lists_of_texts):
    new_list = []
    for list_ in lists_of_texts:
        for item in list_:
            new_list.append(item)
    
    print('First record of texts, {} texts {} at time {}'
          .format(new_list[0], new_list[1], new_list[2]))

def last_call_record(lists_of_calls):
    new_list = []
    for list_ in lists_of_calls:
        for item in list_:
            new_list.append(item)
    
    print('Last record of calls, {} calls {} at time {}, lasting {} seconds'
          .format(new_list[-4], new_list[-3], new_list[-2], new_list[-1]))
    

first_text_record(texts)
last_call_record(calls)
