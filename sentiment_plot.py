import tweepy
from textblob import TextBlob;
from pandas import DataFrame;
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


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
no_neu=0

public_tweets = api.user_timeline(screen_name='@amazonIN');
for tweet in public_tweets:
	t1 = TextBlob(tweet.text);
	if (t1.polarity > 0 ):
			no_pos+=1;
	else:
		if (t1.polarity < 0):
			no_neg+=1;
		else:
			no_neu+=1;



objects = ('Positive tweets', 'Negative tweets', 'Neutral tweets')
y_pos = np.arange(len(objects))
performance = [no_pos, no_neg, no_neu]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of tweets')

plt.show()
