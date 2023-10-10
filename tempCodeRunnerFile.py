while True:
    print("====== Sorting Program ======\n\nYour text will be sorted as [emails, birthdays(mm/dd/yyyy), phone numbers, names]\ntype 0 to end")
    textInput = input("Enter a text: ")
    if textInput == '0': break
    else:
        # sort textInput
        s = sort.TextSort()
        s.