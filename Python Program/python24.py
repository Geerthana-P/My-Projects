# Taking input from user
units = float(input("Enter number of electricity units consumed: "))

# Initialize bill
bill = 0

# Calculating bill based on slabs
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# Displaying the result
print("Electricity Bill: ₹", bill)
