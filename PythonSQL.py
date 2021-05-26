import pymssql 
import pandas as pd
 
def connect():
    server = "213.140.22.237"
    user = "MARASIGAN.JOSHUA"
    password = "AWWWWR6R+"
    database = "MARASIGAN.JOSHUA"
    try:
        conn = pymssql.connect (server, user, password, database)
        print("------CONNECTED--------")
        return conn
    except:
        print("------NOT__CONNECTED--------")

 
 
data = pd.read_csv (r'C:\\Users\\Jana\\Desktop\\prog\\PROGETTO_MCOLLAB\\file_csv\\AllInfluencer.csv')   
df = pd.DataFrame(data, columns= ['Screen_name','Name','Number_of_Followers','Location','Url','description','profile_image','Category'])
 
print(df)

conn = connect()
cursore = conn.cursor()

cont = 0
for row in df.itertuples():
    if row.Category == "Art":
        cursore.execute("INSERT INTO Influencer(Screen_name, Name_, Number_of_Followers, Location_, Category_, Url_, Profile_image,Description) VALUES (%s,%s,%s,%s,'Art',%s,%s,%s)",
        (str(row.Screen_name), str(row.Name),float(row.Number_of_Followers),str(row.Location),str(row.Url),str(row.profile_image),str(row.description)))
        cont += 1
        print("1 record inserted")
    if row.Category == "Sport":
        cursore.execute("INSERT INTO Influencer(Screen_name, Name_, Number_of_Followers, Location_, Category_, Url_, Profile_image,Description) VALUES (%s,%s,%s,%s,'Sport',%s,%s,%s)",
        (str(row.Screen_name), str(row.Name),float(row.Number_of_Followers),str(row.Location),str(row.Url),str(row.profile_image),str(row.description)))
        cont += 1
        print("1 record inserted")
    if row.Category == "Tech":
        cursore.execute("INSERT INTO Influencer(Screen_name, Name_, Number_of_Followers, Location_, Category_, Url_, Profile_image,Description) VALUES (%s,%s,%s,%s,'Tech',%s,%s,%s)",
        (str(row.Screen_name), str(row.Name),float(row.Number_of_Followers),str(row.Location),str(row.Url),str(row.profile_image),str(row.description)))
        cont += 1
        print("1 record inserted")
    if row.Category == "Food":
        cursore.execute("INSERT INTO Influencer(Screen_name, Name_, Number_of_Followers, Location_, Category_, Url_, Profile_image,Description) VALUES (%s,%s,%s,%s,'Food',%s,%s,%s)",
        (str(row.Screen_name), str(row.Name),float(row.Number_of_Followers),str(row.Location),str(row.Url),str(row.profile_image),str(row.description)))
        cont += 1
        print("1 record inserted")
    if row.Category == "Music":
        cursore.execute("INSERT INTO Influencer(Screen_name, Name_, Number_of_Followers, Location_, Category_, Url_, Profile_image,Description) VALUES (%s,%s,%s,%s,'Music',%s,%s,%s)",
        (str(row.Screen_name), str(row.Name),float(row.Number_of_Followers),str(row.Location),str(row.Url),str(row.profile_image),str(row.description)))
        cont += 1
        print("1 record inserted")

print(cont)
conn.commit()
cursore.close()
