import re
from story_api_request import generate_bedtime_story
from database import StoryDatabase 

def start():
    print("Welcome to Bedtime Story")
    print("Create your story")
    user_name = get_valid_name()
    user_role = choose_role()
    user_location = choose_location()
    story = generate_bedtime_story(user_name, user_role, user_location)
    print("\nHere is your bedtime story:\n")
    print(story)
    db = StoryDatabase()
    db.save_story(user_name, user_role, user_location, story)
    db.close()

   
def get_valid_name():
    while True:
        user_name = input("Please enter your name -> ").strip()
        if not user_name:
            print("Name cannot be empty. Please try again.")
        elif not re.match(r"^[A-Za-zА-Яа-яёЁ\s-]+$", user_name):
            print("Invalid name. Use only letters, spaces, or hyphens.")
        elif len(user_name) < 2:
            print("Name must be at least 2 characters long.")
        else:
            return user_name

def choose_role():
    roles = {
        "1": "Wizard",
        "2": "Knight",
        "3": "Thief"
    }

    while True:
        print("\nPlease choose a role:")
        for key, role in roles.items():
            print(f"{key} - {role}")

        choice = input("Enter the number of your role -> ").strip()

        if choice in roles:
            return roles[choice]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def choose_location():
    locations = {
        "1": "Enchanted Forest",
        "2": "Abandoned Castle",
        "3": "Misty Mountains"
    }

    while True:
        print("\nPlease choose a location:")
        for key, location in locations.items():
            print(f"{key} - {location}")
        choice = input("Enter the number of your location -> ").strip()
        if choice in locations:
            return locations[choice]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

start()
