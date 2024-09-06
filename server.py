# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

name_lst = []
email_lst = []
password_lst = []

@app.route('/login/<string:name>/<string:email>/<string:password>')
def login(name, email, password):
    # print("debug")
    # name = input()
    # email = input()
    # password = input()

    if email == email_lst[0] and password == password_lst[0]:
        return {'message': 'Logined successfully'}
    else:
        return {"message": "invalid credentials"}
    

@app.route('/signup/<string:name>/<string:email>/<string:password>')
def signup (name, email ,password):
    print (name, email, password)

    name_lst.append(name)
    email_lst.append(email)
    password_lst.append (password)

    print(name_lst, email_lst, password_lst)

    response = {
        "name": name,
         "email": email,
         "password": password

    }

    return response 

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
