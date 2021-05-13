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

 
 
data = pd.read_csv (r'C:\\Users\\Andrew\\Desktop\\PROGETTO_FINAL\\PROGETTO_MCOLLAB\\file_csv\\INF_Food.csv')   
df = pd.DataFrame(data, columns= ['Screen_name','Name','Number_of_Followers','Location'])
 
print(df)

conn = connect()
cursore = conn.cursor()

cont = 0
sql = "INSERT INTO Influencer(Screen_name, Name, Number_of_Followers, Location_, Category_) VALUES (%s,%s,%s,%s,'Food')"
for row in df.itertuples():
    cursore.execute(sql,
    (str(row.Screen_name), str(row.Name),float(row.Number_of_Followers),str(row.Location)))
    cont += 1
    print("1 record inserted")

print(cont)
conn.commit()
cursore.close()
