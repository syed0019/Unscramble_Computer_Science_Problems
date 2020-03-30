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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def unique_tel_numbers(lists_of_texts, lists_of_calls):
    check_1 = []
    for ls in texts:
        check_1.append(ls[0:2])
    check_one = []
    for lst in check_1:
        for item in lst:
            check_one.append(item)
    new_one = set(check_one)
    
    check_2 = []
    for ls in calls:
        check_2.append(ls[0:2])
    check_two = []
    for lst in check_2:
        for item in lst:
            check_two.append(item)
    new_two = set(check_two)
    count = len(new_one) + len(new_two)
    
    print('"There are {} different telephone numbers in the records."'.format(count))

unique_tel_numbers(texts, calls)