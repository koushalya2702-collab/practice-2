#Dictionaries in Python
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
print(karnataka_food["Mysuru"])
print(karnataka_food.get("shimogga","Not Found"))

#Adding and Updating Dictionary Elements
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
karnataka_food["Bengaluru"]="kadubu"
print(karnataka_food)

karnataka_food["shimogga"]="panneer"
print(karnataka_food)

#Removing Elements from a Dictionary
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
karnataka_food.pop("Mysuru")
print(karnataka_food)  
  

# Dictionary Methods
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
print(karnataka_food.keys())
print(karnataka_food.values())
print(karnataka_food.items())


#Nested Dictionary Practice
friends={
    "Rahul":{
        "subject":"Math",
        "food":"pizza"
    },
    "Anita":{
        "subject":"science",
        "food":"dosa"
    }
}
print(friends["Rahul"]["food"])