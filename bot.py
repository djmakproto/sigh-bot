import tweepy, time, sys, random
from os import environ

def tweet(api):
  f = open("adj.txt", "r", encoding="utf-8")
  adjList = list(f)
  adj = random.choice(adjList)[:-1]
  f.close()
  f = open("sighs.txt", "r", encoding="utf-8")
  sighList = list(f)
  sigh = random.choice(sighList)[:-1]
  f.close()
  print("adj: " + adj)
  print("sigh: " + sigh)
  coinFlip = random.randrange(101)
  if(coinFlip%2 == 0):
    tweet = adj + " " + sigh
  else:
    tweet = sigh + " " + adj
  try:
    api.update_status(tweet)
  except tweepy.TweepError:
    tweet(api)
  

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
while True:
  print("tweeting...")
  tweet(api)
  print("tweeted...")
  time.sleep(60*60*1) #tweet every hour

'''
try:
  err = api.update_status("test")
except tweepy.TweepError:
  print("Dupe tweet!")
  #make a new one
'''