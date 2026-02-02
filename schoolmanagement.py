import csv
import os
import numpy as np

def register_student():
  roll = input("enter roll no. :")
  name = input("enter name :")
  course = input("enter course :")
  email = input("enter email :")


  with open("FILENAME.txt","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([roll,name,course,email])
    print("student register sucessfully!\n")

def view_students():
  try:
    with open("FILENAME.txt", "r") as file:
      reader = csv.reader(file)
      for row in reader:
        print(row)
  except FileNotFoundError:
    print("No student data found.")


def search_student():
  roll = input("Enter Roll No to Search: ")
  found = False
  try:
    with open("FILENAME.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
           if row[0] == roll: # Fixed np.roll to roll
              print(" Student Found:", row)
              found = True
              break
    if not found: # Fixed FileNotFoundError check
      print(" Student Not Found")
  except FileNotFoundError:
    print("No student data found.")


def update_student():
  roll = input("Enter Roll No to Update: ")
  updated_rows = [] # Initialize updated_rows
  found = False
  try:
    with open("FILENAME.txt", "r", newline="") as file:
      reader = csv.reader(file)
      for row in reader:
        if row[0] == roll: # Fixed np.roll to roll
          print("Old Record:", row)
          name = input("Enter New Name: ")
          course = input("Enter New Course: ")
          email = input("Enter New Email: ")
          updated_rows.append([roll, name, course, email]) # Fixed append call
          found = True
        else:
          updated_rows.append(row)
    if found:
        with open("FILENAME.txt", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("Student Updated Successfully!")
    else:
        print("Student Not Found")
  except FileNotFoundError:
    print("No student data found.")


def delete_student():
  roll = input("Enter Roll No to Delete: ")
  updated_rows = [] # Initialize updated_rows
  found = False
  try:
    with open("FILENAME.txt", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
          if row[0] != roll: # Fixed np.roll to roll
              updated_rows.append(row)
          else:
              found = True
    with open("FILENAME.txt", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)
    if found:
      print(" Student Deleted Successfully!")
    else:
      print("Student Not Found")
  except FileNotFoundError:
    print("No student data found.")


def main():
  while True:
    print("\n=== student Registration System ===")
    print("1. Register student")
    print("2. view all student") # Corrected option description
    print("3. search student")
    print("4. update student")
    print("5. Delete student")
    print("6. EXIT")


    choice = input("enter your choice: ")

    if choice == "1":
      register_student()
    elif choice == "2": # Corrected option
      view_students()
    elif choice =="3":
      search_student()
    elif choice =="4": # Added update student call
      update_student()
    elif choice =="5": # Added delete student call
      delete_student()
    elif choice =="6": # Added exit option
      break
    else:
      print("not avilble")

main() # Added call to main function