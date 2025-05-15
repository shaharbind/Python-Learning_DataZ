'''Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. '''

import random

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

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

