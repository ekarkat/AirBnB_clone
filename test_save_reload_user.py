#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)


print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)




print("-- Create a new place and save it")

my_place = Place()
my_place.name = "Moulay rachid"
my_place.number_rooms = 12
my_place.save()


print("-- Create a new State  and save it")
state1 = State()
state1.name = "Laayuoune sakia el hemra"
state1.save()


print("-- Create a new Amenity and save it")

amen = Amenity()
amen.name = "Homeland"
amen.save()

print("-- Create a new place and save it")

my_place = Place()
my_place.name = "Moulay rachid"
my_place.number_rooms = 12
my_place.save()


print("-- Create a new Review and save it")

review1 = Review()
review1.text = "hahahahaahaha"
review1.save()
