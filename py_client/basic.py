import requests

endpoint="https://httpbin.org/status/200/"
endpoint="https://httpbin.org/anything"

get_response=requests.get(endpoint) #HTTP request
print(get_response.text) #print the raw text response

#HTTP Request -> HTML
#Rest Api HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dictionnary

print(get_response.json)