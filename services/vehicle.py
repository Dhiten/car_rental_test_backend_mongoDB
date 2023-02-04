from models.vehicle import Vehicle as VehicleModel
from schemas.vehicle import Vehicle

class VehicleService():

    def __init__(self, db) -> None:
        self.db = db
    
    def get(self):
        vehicles = self.db["vehicles"].find()

        self.db.close()
        return vehicles

    def get_vehicle(self, id: int):
        vehicle = self.db["vehicles"].find_one({"_id": id})

        self.db.close()
        return vehicle

    def create(self, vehicle: Vehicle):
        result = self.db["vehicles"].insert_one(vehicle.dict())
        return result

    def update(self, id: int, vehicle: Vehicle):
        vehicle_db = self.db["vehicles"].update_one({"_id": id}, {"$set": vehicle.dict()})
        return vehicle_db

    def delete(self, id: int):
        vehicle_db = self.db["vehicles"].delete_one({"_id": id})
        
        return vehicle_db

