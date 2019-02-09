import tweepy
import csv
import pandas as pd
import re
####input your credentials here

consumer_key=''  # aka API KEY
consumer_secret=''  # aka API SECRET
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

numberOfTweets = 100
total_no_of_tweets_per_hastag = 500

category = "Sports"
all_hash_tags = ["#superbowl","#nba", "#cricket", "#olympics", "#ManU"]
#all_hash_tags = ["ManU"]

output = open(category+".csv","w") 
output.write("Tweet"+",Category"+"\n")


for i in range(len(all_hash_tags)):
	tweets = []
	#new_tweets = api.user_timeline(screen_name = user_names[i],count=100)
	new_tweets = api.search(q=all_hash_tags[i]+" -filter:retweets", lang="en", count=numberOfTweets, tweet_mode='extended')
	tweets.extend(new_tweets)
	previous = tweets[-1].id-1
	while len(tweets) < total_no_of_tweets_per_hastag:
	    # max_id param to prevent duplicates
	    new_tweets = api.search(q=all_hash_tags[i]+" -filter:retweets", lang="en", count=numberOfTweets, tweet_mode='extended' , max_id = previous)
	    tweets.extend(new_tweets)
	    previous = tweets[-1].id-1
	    print str(len(tweets)) + " Tweets done for "+all_hash_tags[i]

	tweet_text = []
	for j in tweets:
		text_lower = j.full_text.lower()
		text_no_comma = text_lower.replace(",","")
		tweet_text.append(text_no_comma)

	final_tweet_texts = list(set(tweet_text))	
	print "******"+str(len(final_tweet_texts))

	for k in final_tweet_texts:
		k = k.encode('utf-8')
		k = re.sub('\n+','', k)
		output.write(k)
		output.write(",")
		output.write(category)  
		output.write("\n") 

output.close()
