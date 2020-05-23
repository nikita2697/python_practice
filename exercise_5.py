# client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
# lock_list = {1: "Exercise", 2: "Diet"}
#
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
# try:
#     print("Select Client Name:")
#     for key, value in client_list.items():
#         print("Press", key, "for", value, "\n", end="")
#     client_name = int(input())
#
#     print("Selected Client : ", client_list[client_name], "\n", end="")
#
#     print("Press 1 for Lock")
#     print("Press 2 for Retrieve")
#     op = int(input())
#
#     if op is 1:
#         for key, value in lock_list.items():
#             print("Press", key, "to lock", value, "\n", end="")
#         lock_name = int(input())
#         print("Selected Job : ", lock_list[lock_name])
#         f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
#         k = 'y'
#         while (k is not "n"):
#             print("Enter", lock_list[lock_name], "\n", end="")
#             mytext = input()
#             f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
#             k = input("ADD MORE ? y/n:")
#             continue
#         f.close()
#     elif op is 2:
#         for key, value in lock_list.items():
#             print("Press", key, "to retrieve", value, "\n", end="")
#         lock_name = int(input())
#         print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
#         f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
#         contents = f.readlines()
#         for line in contents:
#             print(line, end="")
#         f.close()
#     else:
#         print("Invalid Input !!!")
# except Exception as e:
#     print("Wrong Input !!!")
def getdate():
    import datetime
    return datetime.datetime.now()


def write_file(a,b):
    if b==1:
        z1='y'

        data=input("enter food name:")
        with open(clients[a]+"_food.txt","a") as f:
                #f.write("[" +str(getdate()) +"]:" + data))
            f.write("[ " + str(getdate()) + " ] : " + data + "\n")
    else:
        data = input("enter exercise name:")
        with open(clients[a] + "_exercise.txt", "a") as f:
            # f.write("[" +str(getdate()) +"]:" + data))
            f.write("[ " + str(getdate()) + " ] : " + data + "\n")
    print("added successfully!!!")

def read_file(a,b):
    if b==1:
        z1='y'
        while(z1!='n'):
            with open(clients[a]+"_food.txt") as f:
                content=f.readlines()
                for i in content:
                    print(i)
            z1=input("do you want to add more[y/n]?")
    else:
        with open(clients[a]+"_exercise.txt") as f:
            content=f.readlines()
            for i in content:
                print(i)


try:
    clients = {1: "Harry", 2: "Rohan", 3: "Nikita"}
    z='y'
    while(z != 'n'):
        print("Enter name of client")
        for i,j in clients.items():
            print("Press", i, "for", j, "\n", end="")
        clientname=int(input())
        print("What you want to do read or write?\npress 1 for write \npress 2 for read")
        k=int(input())
        print("Select file type:\npress 1 for Food \npress 2 for Exercise:")
        x = int(input())
        if k==1:
            write_file(clientname,x)
        else:
            read_file(clientname,x)
        z=input("do you want to continue[y/n]:\n")

except Exception as e:
    print(e)



