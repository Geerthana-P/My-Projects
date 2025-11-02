student_grades = {"Alice": [88,92,78],
                  "Bob": [75,80,85],
                  "Charlie": [95,89,90]
                  }
average_grades = {}
for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    average_grades[student] = average
    highest_avg_student = max(average_grades, key=average_grades.get)
highest_avg = average_grades[highest_avg_student]
lowest_avg_student = min(average_grades, key=average_grades.get)
lowest_avg = average_grades[lowest_avg_student]
print("Average Grades of Students:")
for student, avg in average_grades.items():
    print(f"{student}: {avg:}")
print(f"\nHighest average grade: {highest_avg_student} with {highest_avg:}")
print(f"Lowest average grade: {lowest_avg_student} with {lowest_avg:}")