import tweepy
from textblob import TextBlob;
from pandas import DataFrame;

df = DataFrame(columns=['text', 'retweetcount','sentiment']) ;
#consumer_key = Enter consumer key
#consumer_secret = Enter consumer secret
#access_token = Enter access token
#access_token_secret = Enter access token secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

no_pos=0
no_neg=0

public_tweets = api.user_timeline(screen_name='@amazonIN');
for tweet in public_tweets:
	t1 = TextBlob(tweet.text);	
	if (t1.polarity > 0 ):
			no_pos+=1
	else:
		if (t1.polarity < 0):
			no_neg+=1

print('Total number of positive tweets :' + str(no_pos))
print('Total number of negative tweets :' + str(no_neg))
