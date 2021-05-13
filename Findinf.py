import tweepy
import time
import pandas as pd
from time import localtime, strftime, sleep

consumer_key='JWdPxO0jPLt2WWlKMXcC2YyHB'
consumer_secret='ZkkealjKf7tLsjbWrAJdn72CHqw4YqsQM9IaGZJsp4fNUnIMkC'
access_token_key='1381861844038643714-cPKd2WptqVYx83U8qU0gxBoRrcfD7B'
access_token_secret='CwIuQx5v3GfRLltTiLp1oEasFzrTEjiW9kdZAXpJeafHU'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api = tweepy.API(auth,  wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


Category = {
        'Sport': 'Football OR Basketball OR Golf OR Racing OR Soccer OR Tennis',
        'Art': 'Design OR Architecture OR Illustrator OR Drawing OR Draw',
        'Music': 'Song OR Music',
	'Tech': 'Tech OR Hardware OR Computer OR Pc OR MasterRace',
        'Food' : 'Cooking OR Chef OR Vegan OR Food OR Recipes OR Beers',
        'Fashion' : 'Fashion OR Luxury OR Styling OR Shoes OR Beauty OR Accessories OR Jewelry',
        }

def data_org(path_):
        data = {
                'Name': [],
                'Screen_name': [],
                'Number_of_Followers': [],
                #'Number of tweets' : [],
                'Location' : [],
                #'reach_score' : [],
                #'popularity_score' : [],
                #'relevance_score' : [],
        }	

        df_marks = pd.DataFrame(data)
        for tweet in tweets:
                reach_score = tweet.user.followers_count - tweet.user.friends_count
                #popularity_score = tweet.retweet_count + tweet.favorite_count
                #relevance_score = tweet.reply_count + tweet.quote_count
                if tweet.user.followers_count > 5000 and reach_score > 0: #tweet.user.verified is True:
                        new_row = {
                                'Name':tweet.user.name,
                                'Screen_name':"@" + tweet.user.screen_name,
                                'Number_of_Followers':tweet.user.followers_count,
                                #'Number of tweets':tweet.user.statuses_count,
                                'Location':tweet.user.location,
                                #'reach_score':reach_score,
                                #'popularity_score':popularity_score,
                                #'relevance_score':relevance_score,
                                }
                        df_marks = df_marks.append(new_row, ignore_index=True)

        df_marks.drop_duplicates(subset = ['Screen_name', 'Number_of_Followers'], keep='last', inplace = True)

        print('Lista degli "Influencer" di Twitter')
        print('-' * 200)
        print(df_marks.sort_values(by=['Number_of_Followers'], ascending = False))
        print('-' * 200)
        


        df_marks.to_csv(path_)

print("Scelte: Art, Food, Music, Sport, Tech, Fashion")
scelta = input("scelta:")
for t, q in Category.items():
        if scelta == t:
                tweets = tweepy.Cursor(api.search,q).items(1000)
                path_ = "C:\\Users\\Andrew\\Desktop\\Multicollab\\file_csv\\"+"INF_"+scelta+".csv"
                data_org(path_)