# Use the datetime library
from datetime import datetime

# Schedule class that will keep track of all necessary events and their corresponding dates and times.
class Schedule:

    # Inner class for an individual Event, which will keep track of the name, date, time, and description of the event.
    class Event:

        # Constructor for Event class to create attributes, as well as instantiate datetime object.
        def __init__(self, name, desc, day, month, year, hour, minute):
            self.name = name
            self.desc = desc
            self.datetime = datetime(year, month, day, hour, minute, 0, 0)

        # lt, gt, and eq comparison operators so that two instances of the Event object can be compared and sorted.

        def __lt__(self, otherObj):
            return (self.datetime - otherObj.datetime).total_seconds() < 0
        
        def __gt__(self, otherObj):
            return (self.datetime - otherObj.datetime).total_seconds() > 0
        
        def __eq__(self, otherObj):
            return (self.datetime - otherObj.datetime).total_seconds() == 0

        # String function to display the contents of the Event object.
        def __str__(self):
            return f'[{self.datetime.hour:02}:{self.datetime.minute:02}] {self.datetime.day:02}/{self.datetime.month:02}/{self.datetime.year:04} - {self.name}: {self.desc}'

    # Constructor for the Schedule class, which will keep track of all the events for a single instance.
    def __init__(self):
        self.events = []

    # addEvent function to add a new event to the Schedule object, and then sort the events appropriately.
    def addEvent(self, name, desc, year: int, month: int, day: int, hour: int, minute: int):
        event = self.Event(name, desc, year, month, day, hour, minute)
        self.events.append(event)
        self.events.sort()
        return event

    # removeEvent function to remove a pre-existing event from the Schedule object.
    def removeEvent(self, name):
        for index in range(len(self.events)):
            if self.events[index].name == name:
                del self.events[index]
                return

    # checkEvents function to check events taking place at a specific date-time.
    def checkEvents(self, datetime):
        events = []
        for event in self.events:
            if event.datetime == datetime:
                events.append(event)
        return events

    # checkCurrent function checks events taking place at the current time, by invoking checkEvents with datetime.now().
    def checkCurrent(self):
        return self.checkEvents(datetime.now().replace(second = 0, microsecond = 0))

    # String function to display the contents of the Schedule object.
    def __str__(self):
        return "\n".join([str(x) for x in self.events])