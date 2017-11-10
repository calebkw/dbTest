from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://localhost:27017/bme590")

class User(MongoModel):
    name = fields.CharField()
    age = fields.IntegerField()
    bmi = fields.FloatField()

u = User('user1@email.com', last_name='Ross', first_name='Bob')
u2 = User('user2@email.com', last_name='Ross', first_name='Rob')

u.save()
u2.save()

# for user in User.objects.raw({"first_name":"Rob"}):
# 	print(user.first_name)
# 	print(user.last_name)