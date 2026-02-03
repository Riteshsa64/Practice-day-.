import random

# 1. List of random subjects
subjects = [
    "Virat Kohli",
    "MS Dhoni",
    "Modi Ji",
    "Salman Khan",
    "Rohit Sharma",
    "Anushka Sharma",
    "Ronaldo",
    "Amitabh Bachchan"
]


# 2. List of actions
actions = [
    "eats",
    "runs",
    "dances",
    "shouts",
    "buys chai",
    "falls asleep",
    "gets confused",
    "laughs loudly"
]


# 3. List of places or things
places_or_things = [
    "at India Gate",
    "in Mumbai local train",
    "at a pani puri stall",
    "near a school canteen",
    "at Ganga Ghat",
    "in a small barber shop",
    "in a crowded market",
    "at a bus stop"
]


# 4. Start generating headlines
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

# Goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day!")

