import json
from email.message import EmailMessage
import smtplib


#replace keys: [FlightType] = The kind of flight that has been signed up for (archer, seminole, SEATD, etc.)
#              [Date] = the date of the flight
#              [Time] = the time of the flight
#              [Course] = the flight course number of the lesson
#              [Lesson] = the flight lesson number

def MakeEmail(emailAddress, flightType, date, time, course, lesson, configData):
    #takes in info for creation of an email along with configData, and returns an email message, or False if an error is encountered.
    try:
        emailAddressLower = emailAddress.lower()
        subjects = json.loads(configData['email']['emailSubject'])
        subjects = {k.lower(): v for k, v in subjects.items()}
        if emailAddressLower in subjects.keys():
            emailSubject = subjects[emailAddressLower]
        else:
            emailSubject = subjects['default']

        texts = json.loads(configData['email']['emailText'])
        texts = {k.lower(): v for k, v in texts.items()}
        if emailAddressLower in texts.keys():
            text = texts[emailAddressLower]
        else:
            text = texts['default']
        senderEmailAddress = configData['email']['senderEmailAddress']
    except Exception as e:
        print(e)
        return False

    msg = EmailMessage()
    msg['Subject'] = emailSubject
    msg['To'] = emailAddressLower
    msg['From'] = senderEmailAddress#make real email
    text = text.replace('&FlightType&', flightType)
    text = text.replace('&Date&', date)
    text = text.replace('&Time&', time)
    text = text.replace('&Course&', str(course))
    text = text.replace('&Lesson&', str(lesson))
    msg.set_content(text)
    return msg

def SendEmail(craftedEmail, configData):
    try:
        s = smtplib.SMTP(configData['email']['senderEmailServer'], int(configData['email']['senderEmailServerPort']))
        s.starttls()
        s.login(configData['email']['senderEmailAddress'], password=configData['email']['senderEmailPassword'])
        s.sendmail(configData['email']['senderEmailAddress'], craftedEmail['To'], craftedEmail.as_string())
        s.quit()
        return True
    except:
        print('Error in sending email.')
        return False

if __name__ == '__main__':
    import configparser
    configData = configparser.ConfigParser()
    #configData.read('src/FlightSchedulerConfig.ini')
    configData.read('tests/FlightSchedulerConfigTest.ini')
   # email = MakeEmail(emailAddress='JohnDoe1@gmail.com', flightType='flight', date='today', time='00:00', course=111, lesson=222, configData=configData)
    email = MakeEmail(emailAddress='johnDoe@gmail.com', flightType='ARCH', date='1/2/2024', time='12:00', course=102, lesson=30, configData=configData)
    assert email['to'] == 'johndoe@gmail.com'
    assert email['from'] == 'john.doe1@gmail.com'
    assert email['subject'] == 'UND Flight Lesson2'
    print(email['to'])
    print(email['from'])
    print(email['subject'])
  #  result = SendEmail(email, config)
  #  print(result)