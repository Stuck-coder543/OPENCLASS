#Lesson 3: Assignments: Python Lists

#Task 1: Python List Transformation

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)

print(grades)

#Task 2:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

average =sum(grades) / len(grades)
print(f"The average grade is: {average:.2f}")


#Advanced List Methods and Identity Operators 

#Task 1:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted the assignment and attended class.")
else:
    print("Alice did not either submit the assignment or attend class")

#Advanced Slicing Techniques

#Task 1

my_temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print(my_temperatures[7:14])

#Task 2
my_temperatures = [100, 101, 102, 103, 104, 105, 106]

print(my_temperatures[1:7])

