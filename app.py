import pandas as pd
import os

DATA_FILE = "data.csv"
ANSWER_KEY_FILE = "answer_key.csv"

# Create answer key file
if not os.path.exists(ANSWER_KEY_FILE):

    print("========== ENTER ANSWER KEY ==========\n")

    answer_key = {}

    for i in range(1, 6):
        ans = input(f"Enter correct answer for Q{i}: ").upper()
        answer_key[f"Q{i}"] = ans

    answer_df = pd.DataFrame([answer_key])

    answer_df.to_csv(ANSWER_KEY_FILE, index=False)

    print("\nAnswer key saved successfully!\n")

# Create data.csv file
if not os.path.exists(DATA_FILE):

    df = pd.DataFrame(columns=[
        "Name",
        "College",
        "Department",
        "Q1",
        "Q2",
        "Q3",
        "Q4",
        "Q5"
    ])

    df.to_csv(DATA_FILE, index=False)

# Take student inputs
print("========== MCQ QUIZ DATA ENTRY ==========\n")

n = int(input("Enter number of students: "))

students = []

for i in range(n):

    print(f"\nEnter details for Student {i+1}")

    name = input("Enter Name: ")
    college = input("Enter College: ")
    department = input("Enter Department: ")

    student = {
        "Name": name,
        "College": college,
        "Department": department
    }

    for q in range(1, 6):
        ans = input(f"Enter answer for Q{q}: ").upper()
        student[f"Q{q}"] = ans

    students.append(student)

# Save data
student_df = pd.DataFrame(students)

student_df.to_csv(DATA_FILE, mode='a', header=False, index=False)

print("\nStudent data saved successfully in data.csv")
