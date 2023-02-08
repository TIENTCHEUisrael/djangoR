import requests

#endpoint="https://httpbin.org/status/200/"
#endpoint="https://httpbin.org/anything"
#endpoint="http://localhost:8000/"  #http://127.0.0.1:8000/
endpoint="http://localhost:8000/api/"

get_response=requests.get(endpoint,json={"query":"Hello world"}) #HTTP request
print(get_response.text) #print the raw text response
print(get_response.status_code)

#HTTP Request -> HTML
#Rest Api HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dictionnary

print(get_response.json()['message']) 
#print(get_response.status_code)