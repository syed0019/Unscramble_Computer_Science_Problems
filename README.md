# Investigating Texts and Calls

In this project, I deconstructed a series of open-ended problems into smaller components (e.g. inputs, outputs, series of functions) and completed five tasks based on a fabricated set of calls and texts exchanged during September 2016. Moreover, I used Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, I performed [run-time analysis of my solution](https://github.com/syed0019/Unscramble_Computer_Science_Problems/blob/master/Analysis.txt) and determine its efficiency, time-complexity.

### Steps:

#### Step 1 - Download the Files

Download two csv files [calls.csv](https://github.com/syed0019/Unscramble_Computer_Science_Problems/blob/master/calls.csv) and [texts.csv](https://github.com/syed0019/Unscramble_Computer_Science_Problems/blob/master/texts.csv). The text data (text.csv) has the columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

#### Step 2 - Implement the Code

Complete the five tasks in below files containing the instructions:

- [Task_0.py](https://github.com/syed0019/Unscramble_Computer_Science_Problems/blob/master/Task0.py)
- [Task_1.py](https://github.com/syed0019/Unscramble_Computer_Science_Problems/blob/master/Task1.py)
- [Task_2.py](https://github.com/syed0019/Unscramble_Computer_Science_Problems/blob/master/Task2.py)
- [Task_3.py](https://github.com/syed0019/Unscramble_Computer_Science_Problems/blob/master/Task3.py)
- [Task_4.py](https://github.com/syed0019/Unscramble_Computer_Science_Problems/blob/master/Task4.py)

#### Step 3 - Calculate Big O

Once you have completed your solution for each problem, perform a run time analysis (Worst Case Big-O Notation) of your solution. Document this for each problem and include this in your submission.

#### Step 4 - Check again Rubric and Submit

Use the rubric to check your work before submission. A Udacity Reviewer will give feedback on your work based on this rubric and will leave helpful comments on your code.
