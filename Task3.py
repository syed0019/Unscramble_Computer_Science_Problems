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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def list_of_codes(calls_records):
    # creating lists of calling and receiving numbers
    calling_numbers = []
    receiving_numbers = []
    for call in calls:
        calling_numbers.append(call[0:2][0])
        receiving_numbers.append(call[0:2][1])
    
    global fixed_line_num
    fixed_line_num = []
    fixed_num = '(080)'
    for num in calling_numbers:
        if num[0:5] == fixed_num:
            fixed_line_num.append(num)
            
    global new_list
    new_list = []
    for record in calls:
        for num in fixed_line_num:
            if num in record[0]:
                new_list.append(record[1])
    
    codes = []
    for num in new_list:
        if num[0] == '(':
            codes.append(num[1:4])
        else:
            codes.append(num[:4])
    clean_list = sorted(list(set(codes)))
    
    print('"The numbers called by people in Bangalore have codes:"')
    for code in clean_list:
        print(code)

def percentage_of_fixed_calls():
    count_fixed_calling_numbers = len(fixed_line_num)
    
    count_fixed_receiving_numbers = 0
    for num in new_list:
        if num[0:5] == '(080)':
            count_fixed_receiving_numbers += 1
    percentage = (count_fixed_calling_numbers / count_fixed_receiving_numbers) * 100
    print('"{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."'
          .format(percentage))

list_of_codes(calls)
percentage_of_fixed_calls()
