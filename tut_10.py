#Dctionary
d1={"Ajay":"nikita","Rishi":"shreya","Akshu":"sanket" }
print(d1["Ajay"])
d2={"nikita":"purnpoli","ajay":"paneer","rishi":"chikn","akshu":{"nonveg":"fish","veg":"paneer","sweet":"gulabjam"}}
"""
print(d2["akshu"]["veg"])
d2["shreya"]="burger"#or d2.update({"leena":"tofee"})
d2[34]="xyz"
d2["sanket"]="fish"
print(d2)
del d2["sanket"]
del d2[34]
print(d2)
d4=d2.copy()
print(d4)
"""
print(d2.keys())

print(d2.items())