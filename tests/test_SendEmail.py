import configparser
from src import SendEmail

def test_EmailCreation():
    configData = configparser.ConfigParser()
    configData.read('tests/FlightSchedulerConfigTest.ini')
    email = SendEmail.MakeEmail(emailAddress='12345@gmail.com', flightType='ARCH', date='1/2/2024', time='12:00', course=102, lesson=30, configData=configData)
    assert email['to'] == '12345@gmail.com'
    assert email['from'] == 'john.doe1@gmail.com'
    assert email['subject'] == 'UND Flight Lesson'

    email = SendEmail.MakeEmail(emailAddress='johnDoe@gmail.com', flightType='ARCH', date='1/2/2024', time='12:00', course=102, lesson=30, configData=configData)
    assert email['to'] == 'johndoe@gmail.com'
    assert email['from'] == 'john.doe1@gmail.com'
    assert email['subject'] == 'UND Flight Lesson2'