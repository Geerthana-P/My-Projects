days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_num = int(input("Enter day number (1-7): "))

if 1 <= day_num <= 7:
    print("Day:", days[day_num - 1])
else:
    print("Invalid day number")
