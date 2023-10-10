import sqlite3
import os
import sort

conn = sqlite3.connect('sorting.db')
c = conn.cursor()


while True:
    print("====== Sorting Program ======\n\nYour text will be sorted as [emails, birthdays(mm/dd/yyyy), phone numbers, names]\ntype 0 to end")
    textInput = input("Enter a text: ")
    if textInput == '0': break
    else:
        # sort textInput
        s = sort.TextSort()
        s.validateText(textInput)

# s = sort.TextSort()
# with open('Sample-Inputs.txt', 'r') as f:
#     for text in (f.read().split(',')):
#         print(text)
#         s.validateText(text.strip())