# Project Setup

## Prerequisites
- Python (version 3.6 or higher)
- Django (version 3.2 or higher)
- Django REST Framework (version 3.12 or higher)

## Installation

1. Clone the repository:
````
 git clone https://github.com/SergeyDev1996/StarNaviTest.git
 cd <project_directory>
````
2. Create a virtual environment (optional but recommended):
````
 python3 -m venv env
 source env/bin/activate
````
3. Install the dependencies:
````
pip install -r requirements.txt
````
4. Apply database migrations:
````
python manage.py migrate
````
5. Start the development server:
````
python manage.py runserver

````
6. The API should now be accessible at http://localhost:8000.

# Running the Bot

To run the automated bot, follow these steps:

1. Open a new terminal and navigate to the project directory.

2. Run the bot script:
````
python bot.py
````
4. The bot will read the configuration from the `bot_config.json` file and perform the specified activities, such as user signups, creating posts, and liking posts.
