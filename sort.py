import re
import sqlite3

conn = sqlite3.connect('sorting.db')
c = conn.cursor()
class TextSort:
    
  
    def __init__(self):
        pass
    
    def is_valid_email(self, email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def is_valid_phone_number(self, phone_number):
        regex = r'^[+63][\d]{10}|09[\d]{9}$'
        return re.match(regex, phone_number) is not None

    def is_valid_name(self, name):
        regex = r'^[a-z A-Z.]+$'
        return re.match(regex, name) is not None

    def is_valid_date(self, date):
        regex = r'^\d{2}/\d{2}/\d{4}$'
        return re.match(regex, date) is not None
    
    def validateText(self, textInput):
        if self.is_valid_email(textInput):
            c.execute("CREATE TABLE IF NOT EXISTS emails (email text)")
            conn.commit()
            c.execute("INSERT INTO emails VALUES (?)", (textInput,))
            conn.commit()
            print("Text input is an email.")

        elif self.is_valid_date(textInput):
            c.execute("CREATE TABLE IF NOT EXISTS birthdays (birthday text)")
            conn.commit()
            c.execute("INSERT INTO birthdays VALUES (?)", (textInput,))
            conn.commit()
            print("Text input is a birthday/date.")

        elif self.is_valid_phone_number(textInput):
            c.execute("CREATE TABLE IF NOT EXISTS phone_numbers (phone_number text)")
            conn.commit()
            c.execute("INSERT INTO phone_numbers VALUES (?)", (textInput,))
            conn.commit()
            print("Text input is a phone number.")

        elif self.is_valid_name(textInput):
            c.execute("CREATE TABLE IF NOT EXISTS names (name text)")
            conn.commit()
            c.execute("INSERT INTO names VALUES (?)", (textInput,))
            conn.commit()
            print("Text input is a name.")

        else:
            print("Text input is not valid.")

