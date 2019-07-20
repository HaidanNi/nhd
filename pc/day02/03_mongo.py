import pymongo

#创建对象
conn=pymongo.MongoClient('localhost',27017)
db=conn['maoyandb']
myset=db['filmset']

#执行插入语句
# myset.insert_one({'name':'Tiechui'})
# myset.insert_many([{'name':"huahua"},{'name':'tiantain'}])

