
from flask import Flask, request, jsonify

from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://vcm-1866.vm.duke.edu:27017/bme590_2")


class User(MongoModel):
    name = fields.CharField()
    age = fields.IntegerField()
    bmi = fields.FloatField()

# for user in User.objects.raw({"first_name":"Rob"}):
# 	print(user.first_name)
# 	print(user.last_name)

app = Flask(__name__)

@app.route("/average_bmi", methods=['GET'])
def avg_bmi():
    """
    :return: the total number of requests the service has served since its
    most recent reboot as JSON
    """
    # return bmi info


@app.route("/new_patient", methods=['POST'])
def new_pt():

    name = request.json['name']
    age = request.json['age']
    bmi = request.json['bmi']
    print(bmi)

    u = User(name=name, age=age, bmi=bmi)

    u.save()
    return 'yay'





