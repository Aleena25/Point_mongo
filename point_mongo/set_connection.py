from pymongo import MongoClient

class Connect(object):
    @staticmethod    
    def get_connection():
        conn = MongoClient("link for connection")
        db = conn["RadarDatabase"]
        # print("Successfully connected")
        return db