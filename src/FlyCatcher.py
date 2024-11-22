import json
import time
import AimsFlightScheduler
import SignUpForFlight
import CurrentFlightTimes
import GetAimsSession
import SendEmail
import requests
import configparser

previousPrintNumber, previousPrintNumbers = -1, 0

def main():
    global previousPrintNumber, previousPrintNumbers
    try:
        configData = configparser.ConfigParser()
        configData.read('src/FlightSchedulerConfig.ini')
        aimsUser, aimsPass = configData['aimsAccount']['aimsUsername'], configData['aimsAccount']['aimsPassword']
        
        if configData['email']['enableEmailSending'].lower() == 'true':
            sendEmails = True
        else:
            sendEmails = False
    except Exception as e:
        print('Error in loading FlightSchedulerConfig.ini file: ', e)
        return
    session = GetAimsSession.GetAimsSession(username=aimsUser, password=aimsPass, configData=configData)
    newSessionNeeded = False
    while True:
        #get settings dict and group the dict
        if newSessionNeeded:
            try:
                result = requests.get('https://aims-asp.aero.und.edu/', timeout=4)
                if result.text.find('This is aims') == -1:
                    previousPrintNumber, previousPrintNumbers = AimsFlightScheduler.PrintOutHandling(printNumber=0, previousPrintNumber=previousPrintNumber, previousPrintNumbers=previousPrintNumbers)
                    continue
            except:
                previousPrintNumber, previousPrintNumbers = AimsFlightScheduler.PrintOutHandling(printNumber=0, previousPrintNumber=previousPrintNumber, previousPrintNumbers=previousPrintNumbers)
                continue
            
            session = GetAimsSession.GetAimsSession(username=aimsUser, password=aimsPass, configData=configData)
            if session != False:
                print('Got New Session')
                newSessionNeeded = False
            else:
                previousPrintNumber, previousPrintNumbers = AimsFlightScheduler.PrintOutHandling(printNumber=4, previousPrintNumber=previousPrintNumber, previousPrintNumbers=previousPrintNumbers)
                continue
        try:
            with open(configData['settingsDict']['flightSchedulerSettingsDictPath'], 'r') as f:
                settingsDict = json.load(f)
        except:
            previousPrintNumber, previousPrintNumbers = AimsFlightScheduler.PrintOutHandling(printNumber=1, previousPrintNumber=previousPrintNumber, previousPrintNumbers=previousPrintNumbers)
            continue
        groups = AimsFlightScheduler.GroupSettingsDict(settings=settingsDict)
        if groups == False: 
            previousPrintNumber, previousPrintNumbers = AimsFlightScheduler.PrintOutHandling(printNumber=1, previousPrintNumber=previousPrintNumber, previousPrintNumbers=previousPrintNumbers)
            continue
        for i in range(len(groups)):
            group = groups[i][0]
            data = CurrentFlightTimes.GetCurrentScheduleData(session, studentID=group['StudentID'], instID=group['InstID'], launchCount=group['LaunchCount'], aircraftType=group['AircraftType'], configData=configData)
            if data == False:
                newSessionNeeded == True
                break

            flightSpots = CurrentFlightTimes.GetCurrentFlightSpots(data)
            openSpots = CurrentFlightTimes.GetOpenSlots(data)
            if flightSpots == False or openSpots == False:
                newSessionNeeded == True
                break

            chosenFlightTime = -1
            for o in range(len(groups[i])):
                validFlightSpot = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openSpots, validTimes=groups[i][o]['FlightTimes'], currentTimeSlots=flightSpots, excludeTimeBefore=groups[i][o]['ExcludeTimeBefore'], excludeTimeAfter=groups[i][o]['ExcludeTimeAfter'], currentTimeBuffer=groups[i][o]['CurrentTimeBuffer'])
                if validFlightSpot:
                    chosenFlightTime = o
                    break

            if validFlightSpot != False:
                #sign up for flight
                signUpTime = validFlightSpot[0]['month'] + '/' + validFlightSpot[0]['day'] + '/' + validFlightSpot[0]['year'] + ' ' + validFlightSpot[0]['hour'] + ':' + validFlightSpot[0]['minute'] + ':' + validFlightSpot[0]['second']
                result = SignUpForFlight.SignUpForFlight(session=session, studentID=groups[i][chosenFlightTime]['StudentID'], instIDCode=groups[i][chosenFlightTime]['InstID'], startTime=signUpTime, course=groups[i][chosenFlightTime]['Course'], lesson=groups[i][chosenFlightTime]['Lesson'], configData=configData, aircraftType=groups[i][chosenFlightTime]['AircraftType'], launchCount=groups[i][chosenFlightTime]['LaunchCount'], schedType=groups[i][chosenFlightTime]['ScheduleType'], station=groups[i][chosenFlightTime]['Station'], observerID=groups[i][chosenFlightTime]['ObserverID'])
                if result == True:
                    time.sleep(0.5)
                    AimsFlightScheduler.FlightSignUpSettingsDictProcess(flightDetails=groups[i][chosenFlightTime], signUpTime=signUpTime, configData=configData)

                    if sendEmails:
                        for emailAddress in group['EmailAlerts']:
                            flightDate = validFlightSpot[0]['month'] + '/' + validFlightSpot[0]['day'] + '/' + validFlightSpot[0]['year']
                            flightTime = validFlightSpot[0]['hour'] + ':' + validFlightSpot[0]['minute']
                            email = SendEmail.MakeEmail(emailAddress=emailAddress, flightType=group['AircraftType'], date=flightDate, time=flightTime, course=group['Course'], lesson=group['Lesson'], configData=configData)
                            SendEmail.SendEmail(email, configData=configData)
                    
                    print('Flight Sign Up Successful: ', groups[i][chosenFlightTime])

                    previousPrintNumber, previousPrintNumbers = -1, 0
                else:
                    print(result)
                    previousPrintNumber, previousPrintNumbers = AimsFlightScheduler.PrintOutHandling(printNumber=3, previousPrintNumber=previousPrintNumber, previousPrintNumbers=previousPrintNumbers)
            else:
                previousPrintNumber, previousPrintNumbers = AimsFlightScheduler.PrintOutHandling(printNumber=2, previousPrintNumber=previousPrintNumber, previousPrintNumbers=previousPrintNumbers)

if __name__ == '__main__':
    main()