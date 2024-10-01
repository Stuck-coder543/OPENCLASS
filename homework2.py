#Quick Decisions: The Event Planner

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

if venue == "large hall":
    print("You should add an audio system")
elif venue == "conference room":
        print("You should get a projector")

user = input("Would you like vergetarian food? (yes/no): ")

if user == "yes":
      print("That's great!")
elif user == "no":
      print("Not a problem!")
else:
      print("It seems like you didn't answer with yes or no. Try again!")


