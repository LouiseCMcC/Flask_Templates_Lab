import datetime

class Event():

    def __init__(self, name, date, guest_number, location, description, recurring):
        self.name = name
        self.date = date
        self.guest_number = 0
        self.location = location
        self.description = description
        self.recurring = recurring


