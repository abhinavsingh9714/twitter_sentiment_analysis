from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

# consumer key, consumer secret, access token, access secret.
ckey = "5FSaDlryhadXnOwYQ9JcQr9uj"
csecret = "I0nIEfD3W9P04wPfHzIHpTJL5picPDfzb2T3GxoBUfuzJrXrYk"
atoken = "246186230-mXiYh3oCCa6ZkSbkX7UT10gjS4PKp5nn3BAFF6DD"
asecret = "vzKkjSanqAWFmjmz0tqRuDopCfGA9vRpOv8sYOK7Xw2cd"


# from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence * 100 >= 80:
            output = open("twitter-out.txt", "a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])
