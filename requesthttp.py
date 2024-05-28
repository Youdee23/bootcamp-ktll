"""
HTTP AND API
-------------------------------------------------------
HTTTP - Hypertext Transfer Protocol

It is a set of rules that the network uses to fetch 
a resouce over the internet.
Any time you type a website address into a browser you
are making an HTTP request.
A browser is simply an agent.

https://www.facbook.com - this is a URI. The URI has different components

HTTP Verbs
-------------------------------------------------------
GET - with this the HTTP makes a get request, where the
resource is sent over the URI.
POST - with this the HTTP makes a post request, where the
resource is part of the the request body.
PUT - with this the HTTP makes a update request, where the
resource is part of the request body and it will only make
and update.
PATCH -
DELETE - with this the HTTP makes a delete request, where the
resource is part of the request body but it will delete
the resouce.


API - Application Progamming Interface
---------------------------------------------------------------
An API is simple an interface or an end-point that a user uses
to interact with a resource on the internet. JSON Object

JSON - JavaScript Object Notation
"""
import requests

{
    'userId': 1,
    'name': 'Paul',
    'age': 57,
    'vaccinated': True
}

"""
To install a package into your system, you will use
python -m pip install requests json
"""

r = requests.get("https://jsonplaceholder.typicode.com/todos")
# we can access the response of the request that we made
# we can do something like checking the status of the request to know if it was successful or not
# there are plenty HTTP status code with their respective meaning
# they are usually grouped into families
# for example 200 are for request status. So 200 is when a request was successful
r.status_code

# to view the string version of your response
r.text

# to view a json version of your response
r.json()

completed_user = {}
todos = r.json() # this will give us a list
for todo in todos:
    if todo['completed']:
        # add the user to completed_user dictionary
        try:
            completed_user[todo['userId']] += 1
        except KeyError:
            # the userId does not exist
            completed_user[todo['userId']] = 1
