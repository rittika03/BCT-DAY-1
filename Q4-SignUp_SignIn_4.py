from prettytable import PrettyTable 
class login:
    def __init__(self):
        self.table=PrettyTable()
        self.l = []
    def signIn(self):
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        n=len(self.l)
        for i in range(n):
            if self.l[i]['email']!=email:
                print(self.l[i])
                print(f"{email} is not registered, please signUp first.")
                return
            elif email.endswith(".com")!=True:
                print(f"Wrong  email entered please Try Again")
                return
            else:
                if(self.l[i]['password']!=password):
                    print("Incorrect password.")
                    return
                else:
                    print("Login successfull.")
                    return
    def signUp(self):
        database = {}
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        database["email"] = email
        database["password"] = password
        if email.endswith(".com")==True:
            self.l.append(database)
            print("Signup successfull.")
        else:
            print(f"Wrong  email entered please Try Again")
    def show(self):
        self.table.field_names=(["EMAIL","PASSWORD"])
        n=len(self.l)
        for i in range(n):
            e=self.l[i]['email']
            p=self.l[i]['password']
            self.table.add_row([e,p])
        print(self.table)


t1=login()
def main():
    while True:
        key=int(input('''\nEnter 1 for signup...
                      \nEnter 2 for signin...
                      \nEnter 3 to exit...
                      \nEnter 4 to show database'''))
        if(key==3):
            break
        elif(key==1):
            t1.signUp()
        elif(key==2):
            t1.signIn()
        elif(key==4):
            t1.show()
        else:
            print("Please enter a valid parameter.")
main()

