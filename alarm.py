import datetime
import time
import os
import sys
from datetime import datetime, time

moduleName = "Alarm Controller"

swapWords = 'create | make | add | set | delete | remove | next'
commandWords = '$x | alarm'
possibleDays = ['Tomorrow', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times = ['am', 'pm', 'p.m.', 'a.m.']
dayTimes = ['evening', 'morning', 'afternoon', 'night']


def execute(command):
    #print(command)
    command = command.lower()
    #command = "set alarm for 11 o'clock wednesday evening"
    holder = command.split(' ')
    makingAlarm = False
    deletingAlarm = False
    Time = ''
    ampm = ''
    Day = ''
    holdMe = ''

    for word in holder:
        for item in times:
            if word == item.lower():
                if word == 'p.m.':
                    ampm = 'pm'
                elif word == 'a.m.':
                    ampm = 'am'
                else:
                    ampm = item
        for item in dayTimes:
            if word == item.lower():
                if item == 'morning':
                    if ampm == '':
                        ampm = 'am'
                else:
                    if ampm == '':
                        ampm = 'pm'
        for item in possibleDays:
            if word == item.lower():
                Day = item
        if word.isdigit():
            Time = str(holder[int(holder.index(str(word)))])

    if Day == '':
        now = datetime.now()
        holdMe = str(Time)
        if str(ampm) == 'pm':
            holdMe = str(int(Time) + 12)

        if time(int(holdMe)) < now.time():
            Day = 'Tomorrow'
        else:
            Day = 'Today'

def create(Day, Time, AmPm):
    


    return('setting alarm for {0}{1} {2}'.format(Time, ampm, Day))


#execute("set alarm for 11 o'clock wednesday evening")
