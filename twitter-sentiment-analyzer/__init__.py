#import all needed packages
import tweepy #twitter and python integration
from textblob import TextBlob #text analyzer
import nltk #natural language tool kit
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#keys to authenticate with twitter
consumer_key='fOM3vYq9UPU5ppS9GbziKMQ1r'
consumer_secret='22SmoAYndvuQhOF4VIJdZEs2uv5gz5oLFKMp9MO16hiaKuQc3w'

access_token='1013191582130925568-GYyw3bGQRNk4jchsGbCZoGqhosnaml'
acess_token_secret='NTUSeTDbDO9gyEtzuBULl4MhmziYmpT62grEpwXqcnTVA'

#logging into twitter with code
auth=tweepy.OAuthHandler(consumer_key, consumer_secret) #function call

#second part of authentication
auth.set_access_token(access_token, acess_token_secret)

#accesses the api
api = tweepy.API(auth)

#stores a list of tweets related to specified topic
public_tweets=api.search('Pineapple on Pizza')

#increments through all the tweets and prints them
for tweet in public_tweets:
    print(tweet.text) #.text turns it into a string
    analysis=TextBlob(tweet.text) #analyzes the string
    print(analysis.sentiment)