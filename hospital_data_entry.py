import sqlite3
import os

connection = sqlite3.connect("Patientdata.db")
cursor = connection.cursor()
# cursor.execute("CREATE TABLE Patientdata (name TEXT,age INTEGER,gender TEXT,condition TEXT,city TEXT,phone TEXT)")
# cursor.execute("Insert Into Patientdata Values ('Aun', '25', 'male', 'Normal',' Karachi', '0312456874',) ")
# print(cursor.execute("select * from Patientdata ").fetchall())
# connection.commit()
while True:
    print("\n'Indus Hospital'\n")
    print("1: To add patient:")
    print("2: View patient's Data:")
    print("3: Exit")
    chose = input("Enter your choice:") 
    if chose == '1':
       print("\n'Indus Hospital'\n")
       person_name = input("Enter patient's name: ")
       person_age = int(input("Enter patient's age: "))
       person_gender = input("Enter patient's gender: ")        
       person_condition = input("Enter patient's condition: ")
       person_city =  input("Enter patient's city: ")
       person_phone =int( input("Enter patient's phone number: "))
       cursor.execute(f"Insert into Patientdata Values('{person_name}','{person_age}','{person_gender}','{person_condition}','{person_city}','{person_phone}')")
       connecion.commit()
    if chose == '2':
       rows = cursor.execute("select * from Patientdata").fetchall()
       for i in rows:
           print(*i, sep="\t")
    elif chose == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
      print("Invalid choice. Please enter 1, 2, or 3.")
connection.close()
