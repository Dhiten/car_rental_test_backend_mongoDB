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
        new_person = PersonModel(**person.dict())

        result = self.db["people"].insert_one(new_person.dict())
        person = self.db["people"].find_one({"_id": result.inserted_id})
        print(person)
        return new_person
    
    def update(self, id: int, person: PersonCreate):
        person_db = self.db["people"].update_one({"_id": id}, {"$set": person.dict()})
        return person_db

    def delete(self, id: int):
        person_db = self.db["people"].delete_one({"_id": id})

        return person_db