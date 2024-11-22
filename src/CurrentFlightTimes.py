import json
from datetime import datetime, timedelta
import pytz

def ParseDateTime(dateString):
    #ex. '2024-03-07T08:30:00'
    year = dateString.find('-')
    month = dateString.find('-', year + 1)
    day = dateString.find('T', month + 1)
    hour = dateString.find(':', day + 1)
    minute = dateString.find(':', hour + 1)
    return {'year' : dateString[0:year], 'month' : dateString[year + 1 : month], 'day' : dateString[month + 1 : day], 'hour' : dateString[day + 1 : hour], 'minute' : dateString[hour + 1 : minute], 'second' : dateString[minute + 1 :]}

def GetOpenSlots(data):
    openSlotStore = []
    try:
        openSlots = data['availData']['dateAvail']
    except:
        return False
    for day in openSlots:
        for slot in day['slots']:
            startDate = ParseDateTime(dateString=slot['bDT'])
            endDate = ParseDateTime(dateString=slot['eDT'])
            tCt = slot['tCt']
            addable = slot['addable']

            openSlotStore.append([startDate, endDate, tCt, addable])
    return openSlotStore

def GetCurrentFlightSpots(data):
    '''
    slot example:
    {
        "personID": "6C8D50BB3ED5200850C4BDBB75E859A9AD10F8D15AE0F5FBC45E2CC42D88CCFF99832083010EAE29A4FCE0B7F733815729903F55541062846A521D2C29145D710E8C5B4E2B327B63C56709D913E1C88FBFFF9BED05CD943D04507F6D4A2536739A76795C785143717FF7A16AC7AE5182",
        "stuschedKey": 19003899925,
        "custLastName": "Doe",
        "custFirstName": "Jane",
        "activityDate": "2024-03-04T14:15:00",
        "schedType": "UA",
        "course": 323,
        "lesson": 0,
        "instLastName": "Doe",
        "instFirstName": "John",
        "acftType": "ARCH",
        "observerLastName": null,
        "observerFirstName": null,
        "endDate": "2024-03-04T16:15:00",
        "regNum": "N362ND",
        "instID": 12345678,
        "instIDCode": "JDOE",
        "cancelCutoffTime": "2024-03-04T10:15:00",
        "deleteAccess": false,
        "acftID": 15046639,
        "is_unavailable": true,
        "unavailability_reason": "Aircraft in Maintenance"
    }
    '''
    currentSlotStore = []
    try:
        currentSlots = data['schedList']
        if currentSlots == None: return False
    except:
        return False
    for slot in currentSlots:
        startDate = ParseDateTime(slot['activityDate'])
        endDate = ParseDateTime(slot['endDate'])
        currentSlotStore.append([startDate, endDate])

    return currentSlotStore

def GetScheduleDates(dayGap=6):
    def formatDate(time):
        if len(time) < 2:
            return '0' + time
        return time
    central_tz = pytz.timezone('US/Central')
    currentDate = datetime.now(central_tz)    
    dateInSixDays = currentDate + timedelta(days=dayGap)
    startTime = formatDate(str(currentDate.month)) + '/' + formatDate(str(currentDate.day)) + '/' + formatDate(str(currentDate.year)) + ' ' + formatDate(str(currentDate.hour)) + ':' + formatDate(str(currentDate.minute)) + ':' + formatDate(str(currentDate.second))
    endTime = formatDate(str(dateInSixDays.month)) + '/' + formatDate(str(dateInSixDays.day)) + '/' + formatDate(str(dateInSixDays.year)) + ' 23:59:59'
    return startTime, endTime

def GetCurrentScheduleData(session, studentID, instID, launchCount, aircraftType, configData):
    #This function calculates the date 6 days from now so that it can send the schedule slot requests for 6 days in the future
    #it then checks if the data was acquired and if true, will return the data, else, returns false
  #  print('GetCurrentScheduleData: ', studentID, instID, launchCount, aircraftType)

    startTime, endTime = GetScheduleDates()
    
    data = {
        'acftType': aircraftType,
        'stuOrgID': studentID,
        'instIDCode' : instID,
        'startTime': startTime,
        'endTime': endTime,
        'launchCount': str(launchCount),
    }
    try:
        response = session.post('https://aims-asp.aero.und.edu/aimsweb/Schedule/SchedSlots', data=data, timeout=int(configData['httpRequest']['flightDataGetRequestTimeout']))
        finalData = json.loads(response.text)
    except:
        return False
    try: #check if cookies have expired
        if finalData['Error'] == 'UnAuthorized':
            return False
    except:
        pass
    return finalData