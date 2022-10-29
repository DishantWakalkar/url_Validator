# import sqlalchemy as sa
# from sqlalchemy import create_engine
# import requests


# db_conn = create_engine("mysql+pymysql://root:@localhost/jio_demo") 

# metadata = sa.MetaData()
# urls = sa.Table('urlvalidation', metadata, autoload=True, autoload_with=db_conn)
# query = sa.select(urls.columns.id,urls.columns.url)
# result = db_conn.execute(query).fetchall()
# print(result)

# # #List of URLS 
# q="SELECT id,url FROM urlvalidation"
# rs=my_conn.execute(q)
# urls=[]

# for row in rs:
#         urls.append(row)

#URL checker
# def url_checker(url):
#     try:
#         #Get Url
#         get = requests.get(url)
#         # if the request succeeds 
#         if get.status_code == 200:
#             return(f"{url}: is reachable")
#             status_updater(valid)
#         else:
#             return(f"{url}: is Not reachable, status_code: {get.status_code}")
#             status_updater(invalid)
#     #Exception
#     except requests.exceptions.RequestException as e:
#         # print URL with Errs
#         raise SystemExit(f"{url}: is Not reachable \nErr: {e}")


# #Update States
# def status_updater():
#     if op == valid
#         q=""
#         rs=my_conn.execute(q)
#     elif op == invalid
#         q=""
#         rs=my_conn.execute(q)