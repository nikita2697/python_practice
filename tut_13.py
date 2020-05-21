#for loop
"""
list1=["harry","marry","carry","larry",["hi",1]]
print(list1)
for i  in list1:
    print(i)

list2=[["harry",1],["marry",2],["carry",5]]
print(list2)
for i, i1 in list2:
    print(i, ":",i1)

dict1=dict(list2)#type cast list to dict
print(dict1)
for i,i2 in dict1.items():#if only dict1 then it gives error have to write .items to acess key vlue both
    print(i,i2)


for i in dict1: #print only key
    print(i)
"""
#quize:make a list and print only numbers from list which are greater than 6
data=["harry",6,"nikita",9,5,"ajay",11,15]
for i in data:
    if(str(i).isnumeric() and i > 6):# we have to cnvert i to string vlue bcz isnumeric can applied to string aand i is int
        print(i)
