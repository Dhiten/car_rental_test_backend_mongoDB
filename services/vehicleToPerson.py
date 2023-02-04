from models.vehicleToPerson import VehicleToPerson as VehiclePersonModel
from schemas.vehicleToPerson import VehiclePerson

class VehicleToPerson():

    def __self__(self, db) -> None:
        self.db = db

    def get(self):
        vehicle_persons = self.db["vehicleToPerson"].find()

        self.db.close()
        return vehicle_persons

    def get_People_by_vehicle(self, vehicle_id: int):
        vehicle_person = self.db["vehicleToPerson"].find({"vehicle_id": vehicle_id})

        self.db.close()
        return vehicle_person

    def get_vehicles_by_person(self, person_id: int):
        vehicle_person = self.db["vehicleToPerson"].find({"person_id": person_id})

        self.db.close()
        return vehicle_person

    def get_vehicleToPerson(self, vehicle_id: int, person_id: int):
        vehicle_person = self.db["vehicleToPerson"].find_one({"person_id": person_id, "vehicle_id": vehicle_id})

        self.db.close()
        return vehicle_person

    def create(self, vehicle_person: VehiclePerson):

        vehicle_person = self.db["vehicleToPerson"].insert_one(vehicle_person.dict())
        return vehicle_person

    def update(self, vehicle_person: VehiclePerson):
        vehicle_person = self.db["vehicleToPerson"].update_one({"person_id": vehicle_person.person_id, "vehicle_id": vehicle_person.vehicle_id}, {"$set": vehicle_person.dict()})
        return vehicle_person

    def delete(self, vehicle_id: int, person_id: int):
        vehicle_person = self.db["vehicleToPerson"].delete_one({"person_id": person_id, "vehicle_id": vehicle_id})
        
        return vehicle_person