"""
HTTP AND API
-------------------------------------------------------
HTTTP - Hypertext Transfer Protocol

It is a set of rules that the network uses to fetch 
a resouce over the internet. It also enables the communication
between a server and a client.
Any time you type a website address into a browser you
are making an HTTP request. Here the browser is the client
making request a server somewhere else and getting a response
that it translates into webpage(s).
HTTP works in a request - response cycle.
A browser is simply an agent.

https://www.facbook.com - this is a URI. The URI has different components

HTTP Verbs
-------------------------------------------------------
GET Method - is used to make request, where the
resource is sent over the URI.
POST Method - with this the HTTP makes a send a request/data, where the
request/data is stored in the body of the HTTP request.
PUT Method - used to send data to a server to update a record on the server..
PATCH Method - used to send data/request that makes a partial update in the server.
DELETE - with this the HTTP makes a delete request.


API - Application Progamming Interface
---------------------------------------------------------------
An API is simple an interface or an end-point that a user uses
to interact with a resource on the internet. JSON Object

JSON - JavaScript Object Notation
"""
import requests
from requests.exceptions import HTTPError

{
    'userId': 1,
    'name': 'Paul',
    'age': 57,
    'vaccinated': True
}

"""
To install a package into your system, you will use
python -m pip install requests
"""

# Making Request to a server using the GET Method
response = requests.get("https://jsonplaceholder.typicode.com/todos")
# we can access the response of the request that we made
# we can do something like checking the status of the request to know if it was successful or not
# there are plenty HTTP status code with their respective meaning
# they are usually grouped into families
# for example 200 are for request status. So 200 is when a request was successful
response.status_code

if response.status_code == 200:
    print("Successful")
elif response.status_code == 404:
    print("Not Found")


if response:
    print("Ok")
else:
    raise Exception(f"Request was not successful {response.status_code}")


urls = ["https://api.github.com", "https://api.github.com/invalid"]
"""
# CLASSWORK
-------------------------------------------------------------------------------
Write a program that visits both of the urls. Since you have a list of urls, 
you can use a loop here. Make use of the try-except
block in the program. Catch an exception called HTTPError and print the following
"An HTTP error occured" and also catch any other exception and print
"Some other error occured", then handle the situation where even if the error occurs
or not you will print "Me I will still print no matter what"
"""
def sanbox_test():
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as err:
            print(f"An HTTP error occured: {err}")
        except Exception as e:
            print(f"Some other error occured: {e}")
        finally:
            print("Me I will still print no matter what")

# to view the string version of your response
response.text

# give you the content in bytes
response.content

# to view a json version of your response
response.json()

# you can inspect the headers sent with the response
response.headers

completed_user = {}
todos = response.json() # this will give us a list
for todo in todos:
    if todo['completed']:
        # add the user to completed_user dictionary
        try:
            completed_user[todo['userId']] += 1
        except KeyError:
            # the userId does not exist
            completed_user[todo['userId']] = 1
