from prettytable import PrettyTable 
table=PrettyTable()
l = []
def signIn():
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    n=len(l)
    for i in range(n):
        if l[i]['email']!=email:
            print(l[i])
            print(f"{email} is not registered, please signUp first.")
            return
        elif email.endswith(".com")!=True:
            print(f"Wrong  email entered please Try Again")
            return
        else:
            if(l[i]['password']!=password):
                print("Incorrect password.")
                return
            else:
                print("Login successfull.")
                return
def signUp():
    database = {}
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    database["email"] = email
    database["password"] = password
    if email.endswith(".com")==True:
        l.append(database)
        print("Signup successfull.")
    else:
        print(f"Wrong  email entered please Try Again")
    return
def show():
    table.field_names=(["EMAIL","PASSWORD"])
    n=len(l)
    for i in range(n):
        e=l[i]['email']
        p=l[i]['password']
        table.add_row([e,p])
    print(table)