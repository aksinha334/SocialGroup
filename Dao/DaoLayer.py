from SocialGroup.Dao import MongoDB
class DAO:

    def isUserNameExist(Object):
        #Establishing the connection
        mongodbInstance = MongoDB.MongoDb()
        #Getting the Collection
        mycol = mongodbInstance.CreatingConnectionToMongoDbRetutningCollectionSocialGroup()
        #Finding the particular username
        database_entry = mycol.find_one({"UserName": Object.UserName})
        #Closing the connection
        mongodbInstance.closeConnection()
        if database_entry != None:
            return False
        return True

    def insertIntoDB(Object):
        # Establishing the connection
        mongodbInstance = MongoDB.MongoDb()
        # Getting the Collection
        mycol = mongodbInstance.CreatingConnectionToMongoDbRetutningCollectionSocialGroup()
        # Inserting the data into collection
        mycol.insert_one(vars(Object))
        # Closing the connection
        mongodbInstance.closeConnection()
        return True

    def isUserExists(Object):
        # Establishing the connection
        mongodbInstance = MongoDB.MongoDb()
        # Getting the Collection
        mycol = mongodbInstance.CreatingConnectionToMongoDbRetutningCollectionSocialGroup()
        # Inserting the data into collection
        database_entry = mycol.find_one({"UserName": Object.UserName,'Password':Object.Password})
        # Closing the Connection
        mongodbInstance.closeConnection()
        if database_entry == None:
            return False
        return True

    def availableUsersToFollow(socialGroup):
        mongodbInstance = MongoDB.MongoDb()
        mycol = mongodbInstance.CreatingConnectionToMongoDbRetutningCollectionSocialGroup()
        database_entry = mycol.find_one({"UserName":socialGroup.UserName})
        AlreadyFollowing = database_entry["Following"]
        AllUsers_Cursor = mycol.find()
        AvailableUsers = []
        for each in AllUsers_Cursor:
            if each["UserName"] not in AlreadyFollowing:
                AvailableUsers.append(each["UserName"])
        AvailableUsers.remove(socialGroup.UserName)
        return AvailableUsers





    def following(object,following):
        # Establishing the connection
        mongodbInstance = MongoDB.MongoDb()
        # Getting the Collection
        mycol = mongodbInstance.CreatingConnectionToMongoDbRetutningCollectionSocialGroup()
        # Updating the Following of current user
        ValueInDB = mycol.find_one({"UserName":object.UserName})
        if following not in ValueInDB["Following"]:
            mycol.find_one_and_update({"UserName":object.UserName},{"$push":{"Following":following}})
        ValueInDB = mycol.find_one({"UserName":following})
        if object.UserName not in ValueInDB["Followers"]:
            # Updating the Followers of user who is being Followed
            mycol.find_one_and_update({"UserName":following},{"$push":{"Followers":object.UserName}})

        # Closing the Connection
        mongodbInstance.closeConnection()
