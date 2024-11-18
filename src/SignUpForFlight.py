def SignUpForFlight(session, studentID, instIDCode, startTime, course, lesson, configData, aircraftType='ARCH', launchCount=1, schedType='TA', station='D', observerID=''):
    #add current cookies to this function
    #start time format (string): '03/08/2024 17:00:00'
    #course and lesson and studentID all strings
    data = {
        'acftType': aircraftType,
        'instIDCode': instIDCode,
        'stuOrgID': studentID,
        'startTime': startTime,
        'launchCount': launchCount,
        'schedType': schedType,
        'station': station,
        'course': course,
        'lesson': lesson,
        'retake': '',
        'observerOrgID': observerID,
        'options': '',
        'bypass': 'false',
    }
    try:
        response = session.post(
            'https://aims-asp.aero.und.edu/aimsweb/Schedule/AddToSched',
            data=data,
            timeout=int(configData['httpRequest']['flightSignupTimeout'])
        )
        response = response.text
        if response.find('Success') >= 0:
            return True
        else:
            return response
    except:
        return False