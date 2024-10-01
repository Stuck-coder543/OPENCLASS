#Task 1 (decis
# 
# 
number = int(input("Enter a number: (0-50) "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")




#Task 2
    
a = int(input("Enter First Number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))

greatest = a
if greatest < b:
    greatest = b
if greatest < c:
    greatest = c

print("Greatest of Three Numbers is : ", greatest)