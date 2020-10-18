import random
import webbrowser
from googlesearch import search
def greet():
    greetings = ["Hi buddy! I am pharmabot.I can help you in knowing details about any medicine.May I know your name?","Wonderful.It is so nice to be in touch with you.I am a pharmabot.May I know your name?"]
    print(random.choice(greetings))
    return 0
def welcome(name):
    welcome_message = ["Nice to meet you","Lets have some good time together"]
    print()
    print("{0} {1}".format(random.choice(welcome_message),name))
    return 0
def menu():
    print()
    print("1.Get info about medicine")
    print("2.End this chat.")
    print("-------------------------")
    print()
    choice=int(input("Enter your choice: "))
    if 1<=choice<=2:
        return choice
    else:
        return 0
def details_medicine():
    print()
    query=input("Enter name of the medicine: ")
    query=query+ "medicine"
    for j in search(query,tld="com",num=1,stop=1,pause=0):
        webbrowser.open(j)
    return 0
def pharmabot():
    greet()
    name=input("Your name: ")
    welcome(name)
    option = menu()
    while option != 2:
        if option == 1:
            details_medicine()
        else:
            print()
            print("Enter choice between 1 and 2.")
            print()
        option = menu()
    if option==2:
        print()
        print("Thanks for interacting with me,bye...")
    return 0 
pharmabot()


