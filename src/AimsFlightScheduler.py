import json
import time
import copy
from datetime import datetime, timedelta
import pytz

printoutDict = {
    0 : [5, 30, 'Cant get data from AIMS website.'], #number of seconds to wait, number of errors in a row to give error, string to print out when this happens
    1 : [5, 30, 'Settings Dict Error.'],
    2 : [5, 50, 'Looking for valid time slots.'],
    3 : [1, 5, 'Flight Sign Up Unsuccessful.'],
    4 : [1, 5, 'Get Aims Session Failed.']
}

def PrintOutHandling(printNumber, previousPrintNumber, previousPrintNumbers):
    global printoutDict

    if printNumber == previousPrintNumber:
        previousPrintNumbers += 1
    else:
        previousPrintNumbers = 1
    
    try:
        if previousPrintNumbers >= printoutDict[printNumber][1] or previousPrintNumber != printNumber:
            print(printoutDict[printNumber][2], round(time.time()))
            previousPrintNumbers = 1
        previousPrintNumber = printNumber
        
        time.sleep(printoutDict[printNumber][0])
    except:
        print('Print Out Handling Error.')
        time.sleep(1)
    
    return previousPrintNumber, previousPrintNumbers
        
def GroupSettingsDict(settings): #settings= the result of the settings dict
    #Tested, works
    #this function takes in the settings dict and then groups the settings for each individual flight and groups them into flights that can be looked up at the same time
    #for example, if we have two flights that are both the archer, but one flight that is in the Semi, we will group the 2 archer flights into a list, and the one semi flight into a list
    #this allows the code to more quickly check for valid flights
    if len(settings) == 0: return []
    if len(settings) == 1: return [settings]
    try:
        groupedSettings = []
        if len(settings) != 0:
            groupedSettings.append([settings[0]])
            for i in range(1, len(settings)):
                for o in range(len(groupedSettings)):
                    if groupedSettings[o][0]['AircraftType'] == settings[i]['AircraftType'] and groupedSettings[o][0]['StudentID'] == settings[i]['StudentID'] and groupedSettings[o][0]['LaunchCount'] == settings[i]['LaunchCount']:
                        groupedSettings[o].append(settings[i])
                        break
                else: #no break
                    groupedSettings.append([settings[i]])
        return groupedSettings
    except: #probably an error with the settings dict
        return False

def ParseSettingsDateTime(dateTimeStr): #tested works
    #ex. "03/07/2024 13:15:00"
    month = dateTimeStr.find('/')
    day = dateTimeStr.find('/', month + 1)
    year = dateTimeStr.find(' ', day + 1)
    hour = dateTimeStr.find(':', year + 1)
    minute = dateTimeStr.find(':', hour + 1)
    return {'year' : dateTimeStr[day + 1 : year], 'month' : dateTimeStr[: month], 'day' : dateTimeStr[month + 1 : day], 'hour' : dateTimeStr[year + 1 : hour], 'minute' : dateTimeStr[hour + 1 : minute], 'second' : dateTimeStr[minute + 1 :]}

def StrTimeToIntTime(time): #done, tested
    intTime = {}
    
    for key in time.keys():
        intTime[key] = int(time[key])
    return intTime

def IsTimeGreaterOrEqualToTime(checkTime, compareTime): #done, tested
    #returns true if checkTime is later or equal to compare time
    keyList = ['year', 'month', 'day', 'hour', 'minute', 'second']
    for key in keyList:
        if checkTime[key] > compareTime[key]:
            return True
        if checkTime[key] < compareTime[key]:
            return False
    return True

def IsTimeLessOrEqualToTime(checkTime, compareTime): #done, tested
    #returns true if check time is earlier or equal to compare time
    keyList = ['year', 'month', 'day', 'hour', 'minute', 'second']
    for key in keyList:
        if checkTime[key] < compareTime[key]:
            return True
        if checkTime[key] > compareTime[key]:
            return False
    return True

def IsTimeLessThanTime(checkTime, compareTime):
    #returns true if check time is earlier to compare time
    keyList = ['year', 'month', 'day', 'hour', 'minute', 'second']
    for key in keyList:
        if checkTime[key] < compareTime[key]:
            return True
        if checkTime[key] > compareTime[key]:
            return False
    return False

def ParseBeforeAfterTime(time): #time = 'HH:MM"
    #done, tested
    try:
        start = time.find(':')
        if start == -1: return False
        hour = int(time[0:start])
        minute = int(time[start + 1:])
        return {'hour' : hour, 'minute' : minute}
    except:
        return False

def GetUpdatedCurrentTimeSlots(currentTimeSlots, excludeTimeBefore, excludeTimeAfter): #currentTimeSlots = [[{'year': '2024', 'month': '03', 'day': '04', 'hour': '14', 'minute': '15', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '04', 'hour': '16', 'minute': '15', 'second': '00'}], [...]], excludeTimeBefore = 'HH:MM', excludeTimeAfter = 'HH:MM'
    #updates the time slot to account for excludeTimeBefore and excludeTimeAfter
    #this function will take in the current time slots that you are signed up for, and then add the before time and subtract the after time from the current time, so that we can just check if the time is within the updated time slot
    #tested works
    newTimeSlots = copy.deepcopy(currentTimeSlots)
    for i in range(len(newTimeSlots)):
        if type(newTimeSlots[i][0]['year']) == str:
            newTimeSlots[i][0] = StrTimeToIntTime(newTimeSlots[i][0])
            newTimeSlots[i][1] = StrTimeToIntTime(newTimeSlots[i][1])
    parsedBeforeTime = ParseBeforeAfterTime(excludeTimeBefore)
    parsedAfterTime = ParseBeforeAfterTime(excludeTimeAfter)

    for i in range(len(newTimeSlots)):
        if newTimeSlots[i][0]['minute'] - parsedBeforeTime['minute'] < 0:
     #       parsedBeforeTime['hour'] += 1
            newTimeSlots[i][0]['hour'] -= 1
            newTimeSlots[i][0]['minute'] = 60 + (newTimeSlots[i][0]['minute'] - parsedBeforeTime['minute'])
        else:
            newTimeSlots[i][0]['minute'] -= parsedBeforeTime['minute']

        if newTimeSlots[i][1]['minute'] + parsedAfterTime['minute'] >= 60:
            newTimeSlots[i][1]['hour'] += 1
           # parsedAfterTime['hour'] += 1
            newTimeSlots[i][1]['minute'] = (newTimeSlots[i][1]['minute'] + parsedAfterTime['minute']) - 60
        else:
            newTimeSlots[i][1]['minute'] += parsedAfterTime['minute']

        if newTimeSlots[i][0]['hour'] - parsedBeforeTime['hour'] < 0:
            newTimeSlots[i][0]['hour'] = 0
            newTimeSlots[i][0]['minute'] = 0
        else:
            newTimeSlots[i][0]['hour'] -= parsedBeforeTime['hour']

        if newTimeSlots[i][1]['hour'] + parsedAfterTime['hour'] > 24:
            newTimeSlots[i][1]['hour'] = 24
            newTimeSlots[i][1]['minute'] = 0
        else:
            newTimeSlots[i][1]['hour'] += parsedAfterTime['hour']
    return newTimeSlots

def IsTimeInATimeSlot(time, timeSlots, includeEnd=True): #done, tested works
    #time = the individual time you are going to check, in parsed format
    #timeSLots = the list of time options in unparsed format: [["03/07/2024 13:15:00", "03/09/2024 14:45:00"], ["03/07/2024 15:15:00", "03/07/2024 16:45:00"]]
    if len(timeSlots) == 0: return False
    for i in range(len(timeSlots)):
        if type(timeSlots[i][0]) == str:
            timeSlots[i][0] = ParseSettingsDateTime(timeSlots[i][0])
            timeSlots[i][1] = ParseSettingsDateTime(timeSlots[i][1])
    intTime = StrTimeToIntTime(time=time)
    for timeRange in timeSlots:
        timeRange[0] = StrTimeToIntTime(timeRange[0])
        timeRange[1] = StrTimeToIntTime(timeRange[1])
        if includeEnd:
            if IsTimeGreaterOrEqualToTime(checkTime=intTime, compareTime=timeRange[0]) and IsTimeLessOrEqualToTime(checkTime=intTime, compareTime=timeRange[1]):
                return True
        else:
            if IsTimeGreaterOrEqualToTime(checkTime=intTime, compareTime=timeRange[0]) and IsTimeLessThanTime(checkTime=intTime, compareTime=timeRange[1]):
                return True
    return False

def FindFirstValidFlightSpot(openSlots, validTimes, currentTimeSlots, excludeTimeBefore, excludeTimeAfter, currentTimeBuffer): # excludeTimeBefore = 'HH:MM', excludeTimeAfter = 'HH:MM" MM range is 0-59
    copiedTimes = copy.deepcopy(validTimes)
    updatedCurrentTimeSlots = GetUpdatedCurrentTimeSlots(currentTimeSlots, excludeTimeBefore, excludeTimeAfter)

    bufferHour, bufferMinute = int(currentTimeBuffer[0:2]), int(currentTimeBuffer[3:5])
    if bufferHour != 0 or bufferMinute != 0:
        central_tz = pytz.timezone('US/Central')
        currentDate = datetime.now(central_tz)
        endOfTimeExclusion = currentDate + timedelta(hours=bufferHour, minutes=bufferMinute)
        currentTimeExclusionTime = [{'year': currentDate.year, 'month': currentDate.month, 'day': currentDate.day, 'hour': currentDate.hour, 'minute': currentDate.minute, 'second': 0}, {'year': endOfTimeExclusion.year, 'month': endOfTimeExclusion.month, 'day': endOfTimeExclusion.day, 'hour': endOfTimeExclusion.hour, 'minute': endOfTimeExclusion.minute, 'second': 0}]
        updatedCurrentTimeSlots.append(currentTimeExclusionTime)
    for i in range(len(openSlots)):
        #this if statement needs to check if the flight is in one of the valid time ranges that a flight can be scheduled in, this needs to be end inclusive, this should be right
        if IsTimeInATimeSlot(openSlots[i][0], timeSlots=copiedTimes): #is the slot we are checking within one of our time ranges for when the flight should be
            #this if statement needs to check if the flight is not in a range of a current flight, this cant be end inclusive, for example, if we have a flight ending at 14:00, we need to be able to sign up for a flight spot at 14:00
            if not IsTimeInATimeSlot(openSlots[i][0], timeSlots=updatedCurrentTimeSlots, includeEnd=False) and openSlots[i][3] != 'N': #is the flight spot we are checking not within the range of time that our current flight spots are in
                return openSlots[i]
    return False
            #if minus the ExcludeTimeBefore time from the start of activity, and add the ExcludeTimeAfter time to end of each activity, and check if that new open spot is in the updated current activitys, if not, schedule it, if so, keep searching
               # [{'year': '2024', 'month': '03', 'day': '04', 'hour': '14', 'minute': '15', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '04', 'hour': '16', 'minute': '15', 'second': '00'}]

def FlightSignUpSettingsDictProcess(flightDetails, signUpTime, configData):
    #flightDetails = the full dict for the specifics of the flight, from the settings dict. 
    #signUpTime = the time of the flight that is signed up for
    #This function will remove the flight that was just signed up for from the settings JSON file, and then write that launch data to the success JSON file
    pathToJsonSetting = configData['settingsDict']['flightSchedulerSettingsDictPath']
    pathToSuccessfulSignup = configData['settingsDict']['flightSchedulerSuccessDictPath']

    try:
        with open(pathToJsonSetting, 'r') as f:
            settingsDict = json.load(f)
    except:
        print('Settings dict error')
        return False
    successfulSignedUpSpot = {}
    for o in range(len(settingsDict)):
        if settingsDict[o] == flightDetails:
            successfulSignedUpSpot = copy.deepcopy(settingsDict[o])
            settingsDict.pop(o)
            break
    with open(pathToJsonSetting, 'w') as f:
        json.dump(settingsDict, f, indent=4)
    try:
        with open(pathToSuccessfulSignup, 'r') as f:
            signupOut = json.load(f)
    except:
        with open(pathToSuccessfulSignup, 'w') as f:
            json.dump([], f, indent=4)
        signupOut = []
    signupOut.append([round(time.time(), 1), signUpTime, successfulSignedUpSpot])
    with open(pathToSuccessfulSignup, 'w') as f:
        json.dump(signupOut, f, indent=4)