from pymongo import MongoClient


db_client = MongoClient('localhost', 27017)
database = db_client['car_rental_api']