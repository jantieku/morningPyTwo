# TUPLES
cars = ("Mercedes","Toyota","BMW","AUDI","Range")
print(cars[1])
print(cars[4])
print(cars[0:3])
for gari in cars:
    print (gari)
# LIST
students = ["Dennis","Leah","Glory","Elsy","Walter","Jared"]
students.append("Michelle")
students.append("Quiton")
students.append("Donald")
students[3] = "Wairimu"
print(students[1])
print(students[3])
print(students[2:3])
for std in students:
    print(std)
# DICTIONARIES
Vehicles = {"V1":"BMW","V2":"Ford","V3":"Mitsubushi","V4":"Probox"}
print(Vehicles["V4"])
for key in Vehicles.keys():
    print(key)

# printing all the values of a dictionary
for values in Vehicles.values():
    print(values)

# PYTHON DICTIONARY KEYS
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)
