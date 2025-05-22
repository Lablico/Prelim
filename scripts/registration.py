import csv
from datetime import datetime

name = input("Enter your Name: ")
email = input("Enter your Email: ")
student_id = input("Enter your Student ID: ")

subjects = ["Math", "English", "Science", "History", "Computer"]
print("\nAvailable Subjects:")
for i, subject in enumerate(subjects, 1):
    print(f"{i}. {subject}")

choices = input("Select 3 subjects by number (e.g., 1,3,5): ").split(",")
selected_subjects = [subjects[int(choice.strip()) - 1] for choice in choices if choice.strip().isdigit()]

paid = input("Have you paid the fee? (Y/N): ").strip().lower()
if paid != 'y':
    print("Please complete your payment first.")
    exit()

csv_path = "../data/students.csv"
with open(csv_path, "a", newline='') as csvfile:
   writer = csv.writer(csvfile)
   writer.writerow([name, email, student_id, ", ".join(selected_subjects)])

log_path = "../logs/registrations.log"
with open(log_path, "a") as logfile:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logfile.write(f"[{timestamp}] {name} ({student_id}) registered for: {', '.join(selected_subjects)}\n")

print("Registration successful!")
