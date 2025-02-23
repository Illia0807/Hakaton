Bedtime Story Generator

Description

Bedtime Story Generator is a Python application that allows users to create personalized bedtime stories. The user enters their name, selects a role and a location, and the application generates a unique story using an AI model. The generated stories are saved in a PostgreSQL database for future viewing.

Features

User input validation (name, role, location).

Story generation based on user input.

Saving stories in a PostgreSQL database.

Graphical user interface (GUI) using Tkinter.

Background image and interactive elements.

Installation

Required Dependencies

Python 3.x

PostgreSQL

Python Libraries:

psycopg2

python-dotenv

requests

tkinter

PIL (pillow)

Setup

Clone the repository:

git clone https://github.com/your-repository/bedtime-story-generator.git
cd bedtime-story-generator

Install dependencies:

pip install -r requirements.txt

Create a .env file and add database credentials and API tokens:

DB_TOKEN=your_database_connection_string
TOKEN_AI=your_huggingface_api_key

Ensure that PostgreSQL is running and accessible.

Usage

Running the Application

Run the command:

python main.py

Functionality

Enter Name: The user enters their name.

Select Role: Predefined roles are available (e.g., Wizard, Knight, Thief).

Select Location: Choose a location (e.g., Enchanted Forest, Abandoned Castle).

Generate Story: AI creates a story based on user input.

Display Story: The story is shown in a new window.

Save Story: The story is recorded in the PostgreSQL database.

Project Structure

- bedtime-story-generator/
  - main.py                 # Main executable file
  - database.py             # Database management
  - story_api_request.py    # API request for story generation
  - gui.py                  # Tkinter GUI interface
  - requirements.txt        # Dependency file
  - .env                    # Environment variables (not included in the repository)
  - stars.jpg               # Background image for GUI

Installing Dependencies

Make sure all required libraries are installed:

pip install psycopg2 python-dotenv requests pillow

License

This project is distributed under the MIT License.

Author

[Your Name] - [Your Contact Information]