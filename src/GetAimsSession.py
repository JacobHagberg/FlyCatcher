import requests
import json

def GetAimsSession(username, password, configData):
    try:
        session = requests.Session()
        response = session.get('https://aims-asp.aero.und.edu/aimsweb/', timeout=int(configData['httpRequest']['aimsSessionGetTimeout']))
        response = response.text
        tokenStop = response.find('__RequestVerificationToken')
        tokenStop = response.find('value="', tokenStop)
        startToken = tokenStop + 7
        endToken = response.find('"', startToken + 1)
        #get token
        verificationToken = response[startToken:endToken]

        data = {
            'UserName': username,
            'Password': password,
            'rememberMe': 'false',
            '__RequestVerificationToken': verificationToken,
        }

        response = session.post('https://aims-asp.aero.und.edu/aimsweb/Account/LoginCheck', data=data, timeout=int(configData['httpRequest']['aimsSessionGetTimeout']))
        response = json.loads(response.text)
        if response['status'] != 'SUCCESS': #if password or username not valid
            return False
        response = session.get('https://aims-asp.aero.und.edu/aimsweb/AIMSWeb/UserDashboard', timeout=int(configData['httpRequest']['aimsSessionGetTimeout']))
        if response.text.find('logout'):
            return session
        else:
            print('no logout found')
            return False
    except:
        return False

def IsAimsSessionValid(session, configData):
    response = session.get('https://aims-asp.aero.und.edu/aimsweb/AIMSWeb/UserDashboard', timeout=int(configData['httpRequest']['aimsSessionGetTimeout']))
    if response.text.find('logout'):
        return True
    else:
        return False