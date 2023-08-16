#!/usr/bin/python3
'''
MODULE NAME:
------------
    100-hbnb

MODULE DESCRIPTION:
-------------------
    That return a HTML with the states, cities and amenities

MODULE ATTRUBUTES:
------------------
    None

ROUTES:
-------
    '/hbnb' Return a HTML
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City

dict_instances = {"State": State, "Amenity": Amenity,
                  "Place": Place,"City": City}

app = Flask(__name__)

@app.route('/hbnb/<inst>/<id>', strict_slashes=False)
@app.route('/hbnb', strict_slashes=False)
def state_list(inst=None, id=None):
    places = storage.all(Place)
    states = storage.all(State)
    amenities = storage.all(Amenity)
    cities = storage.all(City)

    if inst == 'State' and id:
        state = states["State." + id]
        if state:
            places = {key: place for key, place in places.items()\
                      if place.cities.state_id == id}
    elif inst == 'City' and id:
        city = cities["City." + id]
        if city:
            places = {key: place for key, place in places.items()\
                      if place.city_id == id}
    elif inst == "Amenity":
        amty = amenities["Amenity." + id]
        if amty:
            places = {key: place for key, place in places.items()\
                      if any(amenity.id == id for amenity in place.amenities)}

    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
