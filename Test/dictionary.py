leader = {}
#empty curly brackets assume dictionary

leaders = {"COM411": "Prins", "COM412": "Warren", "COM413": "Darren"}

print(leaders["COM411"])
#Key identifies the value

leaders["COM422"] = "Darren"
#add key pair^

del leaders["COM413"]
#delete from dictionary

print(leaders)

for item in leaders:
    print(item)
#"in" refers to keys

for item1 in leader.values():
    print(item1)
#gets value

for item2 in leader.items():
    print(item2)
#gives both

for code, name in leaders.items():
    print(name)
    print(code)

