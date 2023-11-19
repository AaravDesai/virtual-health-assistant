from flask import Flask, request
from flask_cors import CORS

from app_related import create_account,login,fetch_data,update_data,getAiResponse,initializeUserRec

# Create a Flask web application
app = Flask(__name__)
CORS(app)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/login')
def loginRoute():
    return login.login_api(request.args)

@app.route('/signup')
def signupRoute():
    return create_account.create_account_api(request.args)

@app.route('/fetchdata')
def fetchDataRoute():
    return fetch_data.fetch_data_api(request.args.get("cookie"),request.args.get("isHome"))

@app.route('/updatedata')
def updateDataRoute():
    return update_data.update_data_api(request.args.to_dict())

@app.route('/getAiResponse')
def getAiResponseRoute():
    return getAiResponse.getAiResponse_api(request.args.to_dict())

@app.route('/initializeUserRec')
def initializeUserRecRoute():
    return initializeUserRec.initializeUserRec_api(request.args.get("cookie"))

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)