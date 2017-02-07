# app.py
import flask
import os
import random
import tweepy
import requests, json
from tweepy import OAuthHandler

url = \
"https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best&phrase=Batman"


my_headers = {
    "Api-Key": os.getenv("my_headers")
    #"Api-Key": "23t97kvfqr25rj4annzk3mwr"
}



consumer_key =  os.getenv("consumer_key")
consumer_secret =  os.getenv("consumer_secret")
access_token =  os.getenv("access_token")
access_secret =  os.getenv("access_secret")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

app = flask.Flask(__name__)

response = requests.get(url, headers=my_headers)
json_body = response.json()
num = random.randrange(11)
print json_body["images"][num]["display_sizes"][0]["uri"]

tester=json_body["images"][num]["display_sizes"][0]["uri"]
print tester

@app.route('/') 
def index():
    
    temp= " --TheBatman"
    api.user_timeline(id="dog_rates")
    num = random.randrange(11)
    tester=json_body["images"][num+1]["display_sizes"][0]["uri"]
    if num < 6:
        for status in tweepy.Cursor(api.user_timeline, id="TheBatman").items(num):
            temp= "--NotTheBatman"
        # Process a single status
            print(status.text)
    if num > 5:
        for status in tweepy.Cursor(api.user_timeline, id="TheBatman").items(num):
        # Process a single status
            temp= " --TheBatman"
            print(status.text)
    
        #uri=json_body["images"][status.num]["display_sizes"][status.num]["uri"]#not actually doing anything good find the image URI and them use it in HTM so it will always print it it will be in the index.html
    #return flask.render_template("index.html",image_uri=uri) 
    #json_body["images"][0]["display_sizes"][0]["uri"]
    return flask.render_template("index.html",tweet=status.text+temp, tester=tester)
    #return flask.render_template("index.html",tweet=status.text)
    
@app.route('/random')
def index2():
	a = str(random.randrange(11))
	return str(a)
app.run(

    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    #debug=True
)