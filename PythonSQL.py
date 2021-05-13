import pymssql 
import pandas as pd
 
def connect():
    server = "213.140.22.237\\SQLEXPRESS"
    user = "LUO.HANG"
    password = "SSSSNN5N+"
    database = "LUO.HANG"
    try:
        conn = pymssql.connect (server, user, password, database)
        print("------CONNECTED--------")
        return conn
    except:
        print("------NOT__CONNECTED--------")

 
 
 
data = pd.read_csv (r'C:\Users\Andrew\Desktop\Multicollab\file_csv\Inf_Tech.csv')   
df = pd.DataFrame(data, columns= ['Name','Screen_name','Number_of_Followers','Location'])
 
print(df)

conn = connect()
cursore=conn.cursor()

cont = 0
query = "INSERT INTO Influencer(Screen_name, Name_, Number_of_Followers, Location_, Category_) VALUES(%s,%s,%s,%s,'Tech')"
for row in df.itertuples():
    cursore.execute(query,
    (str(row.Screen_name), str(row.Name),float(row.Number_of_Followers),str(row.Location)))
    cont += 1
    print("1 record inserted")



print(cont)
conn.commit()
cursore.close()

