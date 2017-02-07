# api_test.py
import requests_oauthlib, requests

url = \
"https://api.twitter.com/1.1/account/verify_credentials.json"

oauth = requests_oauthlib.OAuth1(
    "nEMzw7wmqWrIWs2uP3rTEJHBy", 
    "tyAfZCcLEOBPFefhYDAfRwsLiqdCXFpqyQs2IMzqQIQmSqDnPN",
    "827216883753512960-NbLd9egmMpStJkpP70JJyb4tplwqSvf",
    "SjI8wCKICwLxeM54xWa61LqoFMrlPBPjivtTt8Wwq7zGa"
)

response = requests.get(url, auth=oauth)

print response.json()