# RowdyHacks23

**Must be using Git Bash or anything else that runs Python commands**  
Virtual env are being used to run the programs, so make sure to always activate an env before running or trying to work on anything

Basic command to create a venv: $ python -m venv /path/to/new/virtual/environment  
Example: `python -m venv basic` creates a venv called basic

Basic command to activate an env: $ source /Scripts/activate  
Example: `source ./basic/Scripts/activate`

REMEMBER: Add the venv into the .gitignore file or else it will be pushed into the repo the outlined venv name is currently

IMPORTING VENV: Allows the user to install the basic venv that I used for the project `pip install -r requirements.txt`

UPDATING VENV: When new packages are installed, update the import file $ python -m pip freeze > requirements.txt
