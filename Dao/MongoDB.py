from pymongo import MongoClient

class MongoDb:
    connection = MongoClient('localhost', 27017)
    def CreatingConnectionToMongoDbRetutningCollectionSocialGroup(self):
        #print(connection)
        #printing the databases
        #print(connection.list_database_names())
        #choosing one of the database
        mydb = MongoDb.connection["test"]
        #printing the collection name
        #print(mydb.list_collection_names())
        #choosing one of the collection
        mycol = mydb["SocialGroup"]
        return mycol


    def closeConnection(self):
        MongoDb.connection.close()
