'''Can you change the self-parameter inside a class to something else (say 
“arbind”). Try changing self to “slf” or “arbind” and see the effects.'''

# ans:- Nothing will happen

import random

class Train:

    def __init__(arbind, trainNo):
        arbind.trainNo = trainNo

    def book(self, froms, to):
        print(f"Tickets is booked in train no: {self.trainNo} from {froms} to {to}")

    def getStatus(self):
        print(f"The train no: {self.trainNo} is on time")

    def getFare(self, froms, to):
        print(f"The ticket fare in train no : {self.trainNo} from {froms} to {to} is {random.randint(500,2500)}")



t = Train(1222)
t.getStatus()
t.book("Janakpur", "Bihar")
t.getFare("Biratnagar","Dharan")



