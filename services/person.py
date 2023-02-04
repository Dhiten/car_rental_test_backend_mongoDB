from models.person import Person as PersonModel
from schemas.person import PersonCreate

class PersonService():

    def __self__(self, db) -> None:
        self.db = db

    def get(self):
        people = self.db["people"].find()

        return people

    def get_person(self, id: int):
        person = self.db["people"].find_one({"_id": id})

        return person

    def create(self, person: PersonCreate):

        result = self.db["people"].insert_one(person.dict())
        person = self.db["people"].find_one({"_id": result.inserted_id})
        print(person)
        return result
    
    def update(self, id: int, person: PersonCreate):
        person_db = self.db["people"].update_one({"_id": id}, {"$set": person.dict()})
        return person_db

    def delete(self, id: int):
        person_db = self.db["people"].delete_one({"_id": id})

        return person_db