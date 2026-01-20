# Taking input from user
total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))

# Calculate attendance percentage
attendance_percentage = (attended_classes / total_classes) * 100

# Check eligibility
if attendance_percentage >= 75:
    print("Attendance Percentage: {:.2f}%".format(attendance_percentage))
    print("Eligible to appear for exam")
else:
    print("Attendance Percentage: {:.2f}%".format(attendance_percentage))
    print("Not eligible to appear for exam")
