import requests
from requests.exceptions import HTTPError


# CLASS ACTIVITY
try:
    requests.get('https://api.github.com')
    try:
        requests.get('https://api.github.com/invalid')
    except HTTPError:
        print('An HTTP error occured')
    except Exception:
        print('Some other error ocurred')
finally:
    print('Me, I will still print no matter what')


result = requests.get('https://jsonplaceholder.typicode.com/todos')
res = result.status_code
print(res)
outcome = result.json()
print(outcome)

