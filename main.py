# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD ----------------
import sqlalchemy as sa
from sqlalchemy import create_engine, update
import requests

#Alternative for direct db connection
# my_conn = create_engine("mysql+pymysql://root:@localhost/jio_demo") 

# DEFINE THE DATABASE CREDENTIALS ----------------
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'jio_demo'

LIST = []

#Updates the Status in DB ----------------
def status_updater(op, id):
    metadata = sa.MetaData()
    urls = sa.Table('urlvalidation', metadata, autoload=True, autoload_with=engine)
    upd = update(urls)
    
    if op == 1:
        val = upd.values ({"status":"valid"})
        cod = val.where(urls.columns.id == id)
        engine.execute(cod)
    elif op == 2:
        val = upd.values({"status":"invalid"})
        cod = val.where (urls.columns.id == id)
        engine.execute(cod)

#VALIDATION OF URL ----------------
def url_checker(url, id):
    try:
        #Get Url
        get = requests.get(url)
        # if the request succeeds 
        if get.status_code == 200:
            print("Valid")
            # return(f"{url}: is reachable")
            status_updater(1,id)
        else:
            print("Invalid")
            # return(f"{url}: is Not reachable, status_code: {get.status_code}")
            status_updater(1,id)
    #Exception
    except requests.exceptions.RequestException as e:
        # print URL with Errs
        print("Not Found")
        status_updater(2, id)
        # raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

#GET THE LIST OF URLS FROM DB ----------------
def listurl():
    metadata = sa.MetaData()
    urls = sa.Table('urlvalidation', metadata, autoload=True, autoload_with=engine)
    query = sa.select(urls.columns.id,urls.columns.url)
    result = engine.execute(query).fetchall()
                                                       
    
    for record in result:
        LIST.append(record)
    
    for i in LIST:
        print(i[1])
        url_checker(i[1], i[0])
            
#List of URLS 
# q="SELECT id,url FROM urlvalidation"
# rs=my_conn.execute(q)
# urls=[]

# for row in rs:
#         urls.append(row)



# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND ----------------
# RETURN THE SQLACHEMY ENGINE OBJECT ----------------
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
if __name__ == '__main__':
    
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(f"Connection to the {host} for user {user} created successfully.")
        listurl()
            
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)




