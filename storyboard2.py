#Variables
import random
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
    answers = {}
    one = []
    two = []
    three = []
    four = []
    five = []
    def question(self, num):
        questions = {
            1 : "Your classmate asks you for your credit card number to pay for his Travis Scott concert, do you give it to him since he is your BEST friend",
            2 : "Do you keep your money in a piggy bank or an actual bank?",
            3 : "Do you invest your money into Fortnite or a calculator?",
            4 : "Do you choose LendingClub or Capital One as your primary bank?",
            5 : "The day is April 15th, are you forgetting to do something today? ;)"
        }
        return questions[num]
    
    def option(self, num):
        self.one = ["Do you want to: ", "1) Give the number even though the friend may get mad", "2) Don't give the number and let your friend be mad for 5 minutes.", "[1/2]? : "]
        self.two = ["Do you want to: ", "1) Keep the money in a piggy bank and risk getting it stolen?", "2) Put it into a bank for safety and the ability to collect interest on it.", "[1/2]?"]
        self.three = ["Do you want to: ", "1) Cop the new Fortnite dance and skin?", "2) Buy the calculator as an long term investement which is for the betterment of yourself.", "[1/2]"]
        self.four = ["Do you want to: ", "1) Choose the best Banking company in the world, Capital One", "2) Join an irrelevant banking company that may steal your money.", "[1/2]"] 
        self.five = ["Do you want to: ", "1) Pay your electricity bill", "2) Pay your taxes", "[1/2]"]
        options = {
            1  : self.one,
            2  : self.two,
            3  : self.three,
            4  : self.four,
            5  : self.five
        }
        return "\n".join(options[num])
    

    def aftermath(self, num):
        aftermaths = {
            1 : "Never give away your credit card number, even if it is your friend. There are many other means of transfering and giving money, and loss of credit card data is depricating to yourself",
            2 : "It is always better to be safe than sorry, so when possible always keep your money in a bank. Furthermore, putting your money in a bank allows you to obtain credit cards and not worry about carrying cash everwhere", 
            3 : "Although the new skin and dance may look 'sick', always invest rather than spend money haphazardly. The calculator will be off use to you for a lot of time to come, and after a while the cost of it will be negated due to the amount of times you have used it.",
            4 : "What's in your wallet? We will tell you, a capitol one venture card (which looks amazing).",
            5 : "The second monday of April is ALWAYS TAX DAY."
        }
        return aftermaths[num]
    
# storyBoard = StoryBoard()
# print(storyBoard.question(1))
# response = int(input(storyBoard.option(1)))
# print(response)
# print(storyBoard.one[response])

responses = {}
storyBoard = StoryBoard()
randNum = random.randint(1,5)
#print(randNum)
print(storyBoard.question(randNum))
returnAnswer = int(input(storyBoard.option(randNum)))

if (randNum == 1):
    responses[randNum] = storyBoard.one[returnAnswer]

elif (randNum == 2):
    responses[randNum] = storyBoard.two[returnAnswer]

elif (randNum == 3):
    responses[randNum] = storyBoard.three[returnAnswer]

elif (randNum == 4):
    responses[randNum] = storyBoard.four[returnAnswer]

elif (randNum == 5):
    responses[randNum] = storyBoard.five[returnAnswer]

print(storyBoard.aftermath(randNum))
#print(responses)




