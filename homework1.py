#Task 1 (decisions at the crossroad)

number = int(input("Enter a number: (0-50) "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")




#Task 1 and 2 (greatest showdown)
    
a = int(input("Enter First Number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))

smallest = a
if smallest > b:
    smallest = b
if smallest > c:
    smallest = c

greatest = a
if greatest < b:
    greatest = b
if greatest < c:
    greatest = c

print("Smallest of Three Numbers is : ", smallest)
print("Greatest of Three Numbers is : ", greatest)


#Task 1 (leap year explorer)

year = int(input("Enter a year: "))

if(year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year. ")
else:
    print(f"{year} is not a leap year. ")

