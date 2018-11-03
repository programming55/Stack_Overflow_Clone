from flask import Flask

# Creates the application object 
app = Flask(__name__)

# Import Views from the app module. (DO NOT Confuse with app variable)
from app import views

# Import is at the end to avoid circular reference