import f1
t1=f1.login()
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