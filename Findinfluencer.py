import tweepy
import pandas as pd
import os
import glob
import seaborn as sns
from matplotlib import pyplot as plt

os.chdir("C:\\Users\\Andrew\\Desktop\\elaborato\\PROGETTO_MCOLLAB\\file_csv")

consumer_key='JWdPxO0jPLt2WWlKMXcC2YyHB'
consumer_secret='ZkkealjKf7tLsjbWrAJdn72CHqw4YqsQM9IaGZJsp4fNUnIMkC'
access_token_key='1381861844038643714-cPKd2WptqVYx83U8qU0gxBoRrcfD7B'
access_token_secret='CwIuQx5v3GfRLltTiLp1oEasFzrTEjiW9kdZAXpJeafHU'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api = tweepy.API(auth,  wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


Category = {
        'Sport': '#Football OR #Basketball OR #Golf OR #Racing OR #Soccer OR #Tennis OR #NFL OR #Race OR #WORLDCUP',
        'Art': '#Design OR #Architecture OR #Illustrator OR #Drawing OR #Draw',
        'Music': '#Song OR #Music OR #Tone OR #Guitar OR #Piano ',
	'Tech': '#Tech OR #Hardware OR #Computer OR #Pc OR #MasterRace OR #Gaming',
        'Food' : '#Cooking OR #Chef OR #Vegan OR #Food OR #Recipes OR #Beers',
        'Fashion' : '#Fashion OR #Luxury OR #Styling OR #Shoes OR #Beauty OR #Accessories OR #Jewelry',
        }

def data_org(path_,cat):
        data = {
                'Screen_name': [],
                'Name': [],
                'Number_of_Followers': [],
                'Location' : [],
                'Url':[],
                'description':[],
                'profile_image':[],
                'Category':[],
                'reach_score' : [],
                'popularity_score' : []
                #'relevance_score' : []
        }	

        df_marks = pd.DataFrame(data)
        for tweet in tweets:
                reach_score = tweet.user.followers_count - tweet.user.friends_count
                popularity_score = tweet.user.statuses_count + tweet.user.favourites_count
                #relevance_score = tweet.reply_count + tweet.quote_count
                if reach_score > 1000:
                        new_row = {
                                'Screen_name':"@" + tweet.user.screen_name,
                                'Name':tweet.user.name,
                                'Number_of_Followers':tweet.user.followers_count,
                                'Location':tweet.user.location,
                                'Url':tweet.user.url,
                                'description':tweet.user.description,
                                'profile_image':tweet.user.profile_image_url_https,
                                'Category':cat,
                                'reach_score':reach_score,
                                'popularity_score':popularity_score,
                                #'relevance_score':relevance_score,
                                }
                        df_marks = df_marks.append(new_row, ignore_index=True)

        df_marks.drop_duplicates(subset = ['Screen_name', 'Name'], keep='last', inplace = True)

        print('Lista degli "Influencer" di Twitter')
        print('-' * 200)
        print(df_marks.sort_values(by=['reach_score'], ascending = False))
        print('-' * 200)


        data_visual(df_marks, cat)


        ans = input("Vuoi salvarlo in un fle csv? si/no: ")
        if ans == "si":
                df_marks.to_csv(path_)
        else:
                print("Dataframe non salvata")

def data_visual(influencer_df, cat_):
        #bar plot - reach score
        plt.figure(figsize=(20,10))
        sns.set(style="darkgrid")
        ax = sns.barplot(x='Screen_name', y='reach_score', palette="Blues_d",
                        data=influencer_df.sort_values(by='reach_score', ascending=False)[0:10]
                        )
        for p in ax.patches:
                ax.annotate(format(p.get_height()), (p.get_x() + p.get_width() / 2.,
                p.get_height()), ha = 'center', va = 'center', 
                xytext = (0, 10), textcoords = 'offset points')


        ax.set_title("Reach Score for Top " + cat_ , size=40, weight='bold')
        ax.set_xlabel("Twitter Screen Names", size=20, weight='bold')
        ax.set_ylabel("Reach Score(Followers-Following)", size=20, weight='bold')
        for item in ax.get_xticklabels():
                item.set_rotation(45)
                
        plt.savefig('reach.png') 
        plt.show()

        #bar plot - popularity score
        plt.figure(figsize=(20,10)) #customizing the size of the plot
        sns.set(style="darkgrid") #customizing the style of the plot
        #visualizing the data using bar plot
        ax = sns.barplot(x='Screen_name', y='popularity_score', palette="Blues_d",
                        data=influencer_df.sort_values(by='popularity_score', ascending=False)[0:10]
                        )
        #getting the values of the data
        for p in ax.patches:
                ax.annotate(format(p.get_height()), (p.get_x() + p.get_width() / 2.,
                p.get_height()), ha = 'center', va = 'center', 
                xytext = (0, 10), textcoords = 'offset points')


        #setting the parameters for the title, x and y labels of the plot
        ax.set_title("Popularity Score for Top " + cat_ , size=40, weight='bold')
        ax.set_xlabel("Twitter Screen Names", size=20, weight='bold')
        ax.set_ylabel("Popularity_score(retweets+likes)", size=20, weight='bold')
        #changing the rotation of the x axis tick labels 
        for item in ax.get_xticklabels():
                item.set_rotation(45)
                
        plt.savefig('popular.png') #saving the figure
        plt.show()




print("Scelte: Art, Food, Music, Sport, Tech, Fashion")
scelta = input("scelta:")
for t, q in Category.items():
        if scelta == t:
                tweets = tweepy.Cursor(api.search,q).items(500)
                path_ = "C:\\Users\\Andrew\\Desktop\\elaborato\\PROGETTO_MCOLLAB\\file_csv\\"+"INF_"+scelta+".csv"
                data_org(path_,scelta)


def combinecsv():
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

        #combine all files in the list
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
        #duplicate eliminate
        combined_csv.drop_duplicates(subset = ['Screen_name'], keep='last', inplace = True)
        #export to csv
        combined_csv.to_csv( "AllInfluencer.csv", index=False, encoding='utf-8-sig')

print("Vuoi Unire tutti Unire tutti i csv File")
sc = input("Inserisci si se vuoi")
if sc == "si":
        combinecsv()
