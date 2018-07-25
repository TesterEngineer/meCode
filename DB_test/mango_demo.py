import  pymongo

# mongodb服务的地址和端口号
mongo_url = "127.0.0.1:27017"

# 连接到mongodb，如果参数不填，默认为“localhost:27017”
client = pymongo.MongoClient(mongo_url)

#连接到数据库myDatabase
DATABASE = "myDatabase"
db = client[DATABASE]

#连接到集合(表):myDatabase.myCollection
COLLECTION = "myCollection"
db_coll = db[COLLECTION ]

# 在表myCollection中寻找date字段等于2017-08-29的记录，并将结果按照age从大到小排序
queryArgs = {'date':'2017-08-29'}
search_res = db_coll.find(queryArgs).sort('age',-1)
for record in search_res:
      print(f"_id = {record['_id']}, name = {record['name']}, age = {record['age']}")