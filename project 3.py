# Ask the user for total number of class days
total_days = int(input("Enter total number of working days: "))
# Ask how many days the student was absent
absent_days = int(input("Enter number of days the student was absent: "))
# Find out how many days the student was present
present_days = total_days - absent_days
# Now calculate attendance percentage
attendance = (present_days / total_days) * 100
# Show the attendance percentage
print("Attendance percentage is:", attendance, "%")
# Check if the student is allowed to sit in the exam
if attendance < 75:
    print("Student is NOT allowed to sit in the exam.")
else:
    print("Student is ALLOWED to sit in the exam.")