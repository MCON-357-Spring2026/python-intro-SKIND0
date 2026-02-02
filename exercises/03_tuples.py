"""
TODO:
Create and unpack a tuple
Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
Unpack the tuple into three separate variables: lat, lon, and alt.
Create a tuple with mixed data types
Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
Unpack the tuple into three separate variables: name, age, and height.
Demonstrate tuple immutability
Create a tuple named 'immutable_tuple' with three integer values.
Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""

coordinates = (40.87, 34.345, 20.5)
lat, lon, alt = coordinates
print(f"Latitude: {lat}, Longitude: {lon}, Altitude: {alt}")

person_info = ("Sarah", 19, 5.3)
name, age, height = person_info
print(f"{name} is {age} years old and {height} feet tall")

immutable_tuple = (6, 7, 8)
try:
    immutable_tuple[0] = 99
except TypeError as e:
    print(f"Error: {e}")


