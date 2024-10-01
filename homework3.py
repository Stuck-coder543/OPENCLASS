 
#MODULE 2 LESSON 2: NESTED IFS

#Nested Decisions: The adventure Game

place = input("Choose a place forest or cave?: ")

if place == "forest":
    action = input("Do you want to climb a tree or cross a river?")
    if action == "climb a tree":  
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    
else:       
    
    action = input("Do you want to light a torch or proceed in the dark?: ")       
    if action == "light a torch":
      print("Hooray!!")
    elif action == "proceed in the dark":
        print("Be Careful")


#Where would I insert the pass function here?

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


      print("testing")