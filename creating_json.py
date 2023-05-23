d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

(d["employees"].append({"firstName":"thangu","secondname":"sasi"}))

with open("testjason.json","w") as f:
    f.write(str(d))
    f.close()

print(d)

###############################################################
with open("company1.json", "w") as file:
    json.dump(d, file, indent=4)
