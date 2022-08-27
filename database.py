import pymongo

passd = "ckZpYU8HGpnc5i9i"
named = "CopySys"

client = pymongo.MongoClient("mongodb+srv://test:"+passd+"@cluster0.3k1xm6o.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database(named)

class user():
    def findacc(collection, message_id):
        collection = db[collection]
        acc = {"message_id":message_id}
        data = collection.find(acc)
        # countacc = collection.count_documents(acc)
        return data

    def findacc1(collection):
        collection = db[collection]
        # data = collection.find(acc)
        data = collection.find_one(sort=[("message_id", pymongo.DESCENDING)])
        # countacc = collection.count_documents(acc)
        return data

    def findacc2(collection, message_id):
            collection = db[collection]
            post1 = {"msg":'^bot%'}
            new = {"$set":{"message_id":message_id}}
            collection.update_one(post1, new)

    def findwords(collection, Owenr, target):
        collection = db[collection]
        words = {"Owenr":Owenr, "target":target}
        data = collection.find_one(words)
        countwords = collection.count_documents(words)
        return data, countwords
        
    def addsession(collection, message_id, msg):
        collection = db[collection]
        newsession = {"message_id":message_id, "msg":msg}
        collection.insert_one(newsession)

    def findpost(collection, Owenr, share):
        collection = db[collection]
        post = {"Owenr":Owenr, "share":share}
        data = collection.find(post)
        countposts = collection.count_documents(post)
        return data, countposts

    def addpost(collection, Owenr, share, post):
        collection = db[collection]
        newspost = {"Owenr":Owenr, "share":share, "post":post}
        collection.insert_one(newspost)

    def editpost(collection, Owenr, share, post):
        collection = db[collection]
        post1 = {"Owenr":Owenr, "share":share}
        new = {"$set":{"post":post}}
        collection.update_one(post1, new)