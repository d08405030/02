from flask import Flask
from resources.user import Users,User
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
api.add_resource(Users,'/users')
api.add_resource(User,'/user/<id>')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/star/burst/stream")
def star_burst_stream():
    return 'Ten second!'
    
@app.route('/<int:userID>')
def hello(userID):
    return 'The user ID is : {}'.format(userID)



if __name__ == "__main__":
    app.debug = True
    app.run(debug = True,host = '0.0.0.0',port = 5030)