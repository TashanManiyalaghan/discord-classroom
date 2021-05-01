# Use the datetime library
from datetime import datetime

# Schedule class that will keep track of all necessary events and their corresponding dates and times.
class Schedule:

    # Inner class for an individual Event, which will keep track of the name, date, time, and description of the event.
    class Event:

        # Constructor for Event class to create attributes, as well as instantiate datetime object.
        def __init__(self, name, year, month, day, hour, minute, desc):
            self.name = name
            self.datetime = datetime(year, month, day, hour, minute, 0, 0)
            self.desc = desc

        # lt, gt, and eq comparison operators so that two instances of the Event object can be compared and sorted.

        def __lt__(self, otherObj):
            return (self.datetime - otherObj.datetime).total_seconds() < 0
        
        def __gt__(self, otherObj):
            return (self.datetime - otherObj.datetime).total_seconds() > 0
        
        def __eq__(self, otherObj):
            return (self.datetime - otherObj.datetime).total_seconds() == 0

        # String function to display the contents of the Event object.
        def __str__(self):
            return f'{self.datetime.day:02}/{self.datetime.month:02}/{self.datetime.year:04} {self.datetime.hour:02}:{self.datetime.minute:02} {self.name}: {self.desc}'

    # Constructor for the Schedule class, which will keep track of all the events for a single instance.
    def __init__(self):
        self.events = []

    # addEvent function to add a new event to the Schedule object, and then sort the events appropriately.
    def addEvent(self, name, year: int, month: int, day: int, hour: int, minute: int, desc = None):
        event = self.Event(name, year, month, day, hour, minute, desc)
        self.events.append(event)
        self.events.sort()
        return event

    # removeEvent function to remove a pre-existing event from the Schedule object.
    def removeEvent(self, name):
        for index in range(len(self.events)):
            if self.events[index].name == name:
                del self.events[index]
                return

    def checkEvents(self, datetime):
        events = []
        
        for event in self.events:
            if event.datetime == datetime:
                events.append(event)

        return events

    def checkCurrent(self):
        return self.checkEvents(datetime.now().replace(second = 0, microsecond = 0))

    # String function to display the contents of the Schedule object.
    def __str__(self):
        return "\n".join([str(x) for x in self.events])

# Testing goes here.
if __name__ == '__main__':

    schedule = Schedule()
    schedule.addEvent('Hackathon', 2021, 4, 30, 19, 0, 'Hacking begins!')
    schedule.addEvent('Discord bot hosting', 2021, 5, 1, 21, 0, 'Workshop for hosting discord bots.')
    schedule.addEvent('Relationship advice', 2021, 5, 1, 17, 0, 'A relationship advice panel from single people.')
    schedule.addEvent('Dinnertime', 2021, 4, 30, 19, 0, 'Time to eat')

    print(schedule, end = '\n\n')

    datetime = datetime(2021, 5, 1, 17, 0, 0, 0)
    print('Check what events are happening on', datetime)
    for event in schedule.checkEvents(datetime):
        print(event)

    current = datetime.now().replace(second = 0, microsecond = 0)
    print('\nCheck what events are happening now', current)
    for event in schedule.checkEvents(current):
        print(event)