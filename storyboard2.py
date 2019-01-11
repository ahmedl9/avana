#Variables
import random
name = ""        #Users name //CREATE CONSTRUCTORS FOR NAME AND AGE 
age  = 0         #User age
creditLog = []   #Credit Log, updated throughout the game 
arr = [1, 2, 3, 4, 5] #Find out which number to show

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

class StoryBoard:
    answers = {}
    one = []
    two = []
    three = []
    four = []
    five = []

    #Questions to ask takes in a num and returns the value to that key
    def question(self, num):
        questions = {
            1 : "Your classmate asks you for your credit card number to pay for his Travis Scott concert, do you give it to him since he is your BEST friend",
            2 : "Do you keep your money in a piggy bank or an actual bank?",
            3 : "Do you invest your money into Fortnite or a calculator?",
            4 : "Do you choose LendingClub or Capital One as your primary bank?",
            5 : "The day is April 15th, are you forgetting to do something today? ;)"
        }
        return questions[num]
    
    #Options the user can have, takes in num and returns the value to that key
    def option(self, num):
        self.one = ["1) Give number", "2) Heck No!"]
        self.two = ["1) Piggy Bank", "2) Actual Bank"]
        self.three = ["1) Ofc Fortnite", "2) Calculator"]
        self.four = ["1) Capital One", "2) Irrelevant Bank"]
        self.five = ["1) Electricity Bill", "2) Pay taxes"]
        options = {
            1  : self.one,
            2  : self.two,
            3  : self.three,
            4  : self.four,
            5  : self.five
        }
    
        return options[num]
    
    #The concluding sentence, takes in num and return the value to that key 
    def aftermath(self, num):
        aftermaths = {
            1 : "Never give away your credit card number, even if it is your friend. There are many other means of transfering and giving money, and loss of credit card data is depricating to yourself",
            2 : "It is always better to be safe than sorry, so when possible always keep your money in a bank. Furthermore, putting your money in a bank allows you to obtain credit cards and not worry about carrying cash everwhere", 
            3 : "Although the new skin and dance may look 'sick', always invest rather than spend money haphazardly. The calculator will be off use to you for a lot of time to come, and after a while the cost of it will be negated due to the amount of times you have used it.",
            4 : "What's in your wallet? We will tell you, a capitol one venture card (which looks amazing).",
            5 : "The second monday of April is ALWAYS TAX DAY."
        }
        return aftermaths[num]
    

responses = {} #Dict that keeps track of user responses
rightAnswers = {} #Dict that keeps track of right answers

"""
while len(arr) != 0:

    
    storyBoard = StoryBoard()
    randNum = random.randint(1,5)
    #print(randNum)
    if randNum in arr:
        #print(storyBoard.question(randNum))
        returnAnswer = int(input(storyBoard.option(randNum)))

        if (randNum == 1):
            responses.update({randNum : storyBoard.one[returnAnswer]})
            rightAnswers.update({randNum : storyBoard.one[2]})

        elif (randNum == 2):
            responses.update({randNum : storyBoard.two[returnAnswer]})
            rightAnswers.update({randNum : storyBoard.two[2]})

        elif (randNum == 3):
            responses.update({randNum : storyBoard.three[returnAnswer]})
            rightAnswers.update({randNum : storyBoard.three[2]})

        elif (randNum == 4):
            responses.update({randNum : storyBoard.four[returnAnswer]})
            rightAnswers.update({randNum : storyBoard.four[1]})

        elif (randNum == 5):
            responses.update({randNum : storyBoard.five[returnAnswer]})
            rightAnswers.update({randNum : storyBoard.five[2]})

        #print(storyBoard.aftermath(randNum))
        #print(responses)
        arr.remove(randNum)
    else:
        continue
    
    #print(responses)

print(responses)
print(rightAnswers)

"""



