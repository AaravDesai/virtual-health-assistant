from flask import Flask

from app_related import create_account

# Create a Flask web application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    create_account()
    return 'Hello, Flask!'

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)