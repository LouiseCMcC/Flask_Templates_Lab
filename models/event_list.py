from models.event import *

event1 = Event("Party", (datetime.date(2022,11,1)), 9, "Nice Bar", "Petes Birthday", False)
event2 = Event("Dinner Out", (datetime.date(2022,9,22)), 4, "Italian Restaurant", "Catch Up", True)
event3 = Event("Concert", (datetime.date(2022,10,6)), 5, "Barrowlands", "Mezingers", False)
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)
    

