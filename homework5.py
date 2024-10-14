#The Range Riddle Task 1
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(len(days_of_week)):
    mood = random.choice(moods)
    print(f"{days_of_week[day]}: {mood}")

#Double Scoop with Nested Loops

import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Relaxed", "Anxious"]
times_of_day = ["morning", "afternoon", "evening"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days_of_week:
    print(f"Mood tracker for {day}:")
    for time in times_of_day:
        mood = random.choice(moods)
        print(f" {time}: {mood}")
