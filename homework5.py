#PRACTICE EXAMPLES


grade = input("Is your grade either an (A/B/C): ")
sports_team = input("Are you on a sports team? (yes/no): ")
drama_club = input("Are you on a drama club (yes/no): ")

discount = 0

if grade == "A":
    if sports_team == "yes":
        discount = 20
    else:
        discount = 10
elif grade == "B":
    if drama_club == "yes":
        discount = 15

print(f"You are eligible for a {discount}% discount.")
