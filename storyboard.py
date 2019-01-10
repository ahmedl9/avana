#Variables
name = ""        #Users name //CREATE CONSTRUCTORS FOR NAME AND AGE 
age  = 0         #User age
creditLog = []   #Credit Log, updated throughout the game 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

class StoryBoard:
    creditDebit = ""
    def scene1(self):
        # gather the input
        # "while" is the loop statement, checking the condition and executing the code in the body of loop while the condition holds true
        # obviously, "while True" will execute its body forever until "break" statement executes or you press Ctrl+C on keyboard
        while True:
            d1a = input ("Do you want to: \nA) Credit Card. \nB) Debit Card. \n[A/B]? : ")
            # check if d1a is equal to one of the strings, specified in the list
            if d1a in ['A', 'B']:
                # if it was equal - break from the while loop
                break
    # process the input
        self.creditDebit = d1a
        if d1a == "A": 
            print ("You pay for coffee with it") 
        elif d1a == "B": 
            print ("GAME ENDED: Game was about credit cards fool.")
    
    def scene2(self, creditDebit):
        if creditDebit == "A":
            print("this func is working")
        elif creditDebit == "B":
            print("B")



#Gathering Information
# name = input("Hello, what is your name? ")
# age  = input("What is your age? ")
# p1 = Person(name, age)



#Opening Story 
# print("Hello deliquent, welcome to the real world, where everything isn't rainbows and lollipops and you are constantly letting down your parents (just kidding," + 
#       " but if you don't have financial literacy than that will come true).")
# print()
# print("Lets set the scene, you and you're friend are at a cafe and you have run out of cash and want a credit card!")
# print()

storyBoard = StoryBoard()
storyBoard.scene1()
storyBoard.scene2(storyBoard.creditDebit)





