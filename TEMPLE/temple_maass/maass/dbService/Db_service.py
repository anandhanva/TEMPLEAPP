# from pymongo import MongoClient
# import pymongo
# from pymongo.errors import CollectionInvalid,ConnectionFailure
# from maass.constants import config


# class DbServiceImpl:

#     URI = config.MONGODB_SERVER
#     USER = config.MONGO_USER
#     PASS = config.MONGO_PASS
#     DATABASE = None

#     @staticmethod
#     def initialize_maass():
#         try:
#             client = pymongo.MongoClient(DbServiceImpl.URI)
#             client.admin.authenticate(DbServiceImpl.USER, DbServiceImpl.PASS)
#             DbServiceImpl.DATABASE = client['buildd']
#         except pymongo.errors.PyMongoError as e:
#             print("error mongo", e)
#         except pymongo.errors.ConnectionFailure as e:
#             print("Connection Error ", e)
#         except pymongo.errors.ServerSelectionTimeoutError as e:
#             print("Server Selection Error ", e)
#         except Exception as e:
#             # traceback.print_exc()
#             print(e)
#             raise(e)
    

#     @staticmethod
#     def getOneData(tableName, query):
#         print("TABLE NAME, QUERY =====>",tableName,query)
#         resultJson = DbServiceImpl.DATABASE[tableName].find_one(query)
#         return resultJson

#     @staticmethod
#     def insertOneData(tableName,data,):
#         inserted = DbServiceImpl.DATABASE[tableName].insert_one(data)
#         inserted_cur = pymongo.results.InsertOneResult.acknowledged
#         print("INSERT:::::::::::",inserted_cur)
#         return inserted_cur
            
            

    


