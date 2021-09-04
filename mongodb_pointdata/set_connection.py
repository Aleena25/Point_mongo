from pymongo import MongoClient

class Connect(object):
    @staticmethod    
    def get_connection():
        conn = MongoClient("mongodb+srv://Tech27_QtTest:QtTest12345678@cluster0.bajrq.mongodb.net/test")
        db = conn["RadarDatabase"]
        # print("Successfully connected")
        return db
