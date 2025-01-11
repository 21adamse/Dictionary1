list=["hello",1,True,0.1]

#creating a dictionary
sampledictionary={
    "name":"Ewan",
    "age":14,
    "school":"Harrogate Grammer",
    "pass":True,
    "grade":10
}
print(sampledictionary)
print(sampledictionary["name"],sampledictionary["school"])

#updating existing values
sampledictionary["age"]=15
print(sampledictionary["age"])

#adding a new key
sampledictionary["teacher"]="Mrs Teacher"
print(sampledictionary["teacher"])

#getting all of the keys
keys=sampledictionary.keys()
print(keys)

#getting all of the values
values=sampledictionary.values()
print(values)

#printing keys and values 1 by 1 using a for loop
for key in sampledictionary:
    print(key,sampledictionary[key])

#check if there is a key in a dictionary
if "mark" in sampledictionary:
    print("Mark is in the sample dictionary")
else:
    print("Mark is not in the sample dictionary")

if "name" in sampledictionary:
    print("Name is in the sample dictionary")
else:
    print("Name is not in the sample dictionary")

#deleting a key and value pair
del sampledictionary["age"]
print(sampledictionary)

#adding a list into the dictionary
sampledictionary["marks"]=[45,30,26,63,41]
print(sampledictionary)
print(sampledictionary["marks"])
print(sampledictionary["marks"][3])

#creating nested dictionaries
classroom={
    "Ewan":{
        "age":14,
        "marks":[60,36,75,50,42]
    },
    "Bob":{
        "age":13,
        "marks":[50,34,67,44,56]
    }
}
print(classroom)
print(classroom["Ewan"])
print(classroom["Bob"]["marks"][4])