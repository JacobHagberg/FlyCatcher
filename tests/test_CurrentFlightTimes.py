import sys
#sys.path.append('/Users/jacobhagberg/Documents/PythonCode/AimsFlightSignup/')
from src import CurrentFlightTimes

data = {
    "userSiteNow": "2024-03-03T14:37:02.4052009",
    "availData": {
        "acftType": "ARCH",
        "instIDCode": "",
        "stuOrgID": "1390572",
        "startTime": "2024-03-03T14:37:02.4052009",
        "endTime": "2024-03-09T23:59:59",
        "launchCount": 1,
        "dateAvail": [
            {
                "date": "2024-03-03T00:00:00",
                "slots": [
                    {
                        "bDT": "2024-03-03T14:45:00",
                        "eDT": "2024-03-03T16:45:00",
                        "tCt": 5,
                        "addable": "Y"
                    },
                    {
                        "bDT": "2024-03-03T15:00:00",
                        "eDT": "2024-03-03T17:00:00",
                        "tCt": 6,
                        "addable": "Y"
                    }
                ]
            },
            {
                "date": "2024-03-04T00:00:00",
                "slots": [
                    {
                        "bDT": "2024-03-04T07:00:00",
                        "eDT": "2024-03-04T09:00:00",
                        "tCt": 5,
                        "addable": "Y"
                    }
                ]
            },
            {
                "date": "2024-03-05T00:00:00",
                "slots": []
            },
            {
                "date": "2024-03-06T00:00:00",
                "slots": [
                    {
                        "bDT": "2024-03-06T07:00:00",
                        "eDT": "2024-03-06T09:00:00",
                        "tCt": 5,
                        "addable": "Y"
                    },
                    {
                        "bDT": "2024-03-06T07:15:00",
                        "eDT": "2024-03-06T09:15:00",
                        "tCt": 6,
                        "addable": "Y"
                    }
                ]
            },
            {
                "date": "2024-03-07T00:00:00",
                "slots": [
                    {
                        "bDT": "2024-03-07T07:00:00",
                        "eDT": "2024-03-07T09:00:00",
                        "tCt": 4,
                        "addable": "Y"
                    },
                    {
                        "bDT": "2024-03-07T07:15:00",
                        "eDT": "2024-03-07T09:15:00",
                        "tCt": 6,
                        "addable": "Y"
                    }
                ]
            },
            {
                "date": "2024-03-08T00:00:00",
                "slots": [
                    {
                        "bDT": "2024-03-08T07:00:00",
                        "eDT": "2024-03-08T09:00:00",
                        "tCt": 5,
                        "addable": "Y"
                    }
                ]
            },
            {
                "date": "2024-03-09T00:00:00",
                "slots": []
            }
        ],
        "error": False,
        "errmsg": 0
    },
    "availError": False,
    "availErrMsg": "",
    "schedList": [
        {
            "personID": "6C8D50BB3ED5200850C4BDBB75E859A9AD10F8D15AE0F5FBC45E2CC42D88CCFF99832083010EAE29A4FCE0B7F733815729903F55541062846A521D2C29145D710E8C5B4E2B327B63C56709D913E1C88FBFFF9BED05CD943D04507F6D4A2536739A76795C785143717FF7A16AC7AE5182",
            "stuschedKey": 19003899925,
            "custLastName": "Doe",
            "custFirstName": "John",
            "activityDate": "2024-03-04T14:15:00",
            "schedType": "UA",
            "course": 323,
            "lesson": 0,
            "instLastName": "Doe",
            "instFirstName": "Jane",
            "acftType": "ARCH",
            "observerLastName": 0,
            "observerFirstName": 0,
            "endDate": "2024-03-04T16:15:00",
            "regNum": "N362ND",
            "instID": 12345678,
            "instIDCode": "JDOE",
            "cancelCutoffTime": "2024-03-04T10:15:00",
            "deleteAccess": False,
            "acftID": 15046639,
            "is_unavailable": True,
            "unavailability_reason": "Aircraft in Maintenance"
        },
        {
            "personID": "789718C92B8E10F10125FF65E607FA08DDC3A9F24EF65A28279CC041F5590362AAF69712518FA5FDB423904B7731135E62443128BEA2C91F1B99CCCF6A7FCA3D5D1B3C547FFCF202FD70807187CF6201C60297F7A63277D54A6A37A7D3080EEB7991B206C3EA0492A3D861B51C879AA9",
            "stuschedKey": 19003904001,
            "custLastName": "Doe",
            "custFirstName": "John",
            "activityDate": "2024-03-06T14:15:00",
            "schedType": "UA",
            "course": 323,
            "lesson": 0,
            "instLastName": "Doe",
            "instFirstName": "Jane",
            "acftType": "ARCH",
            "observerLastName": 0,
            "observerFirstName": 0,
            "endDate": "2024-03-06T16:15:00",
            "regNum": "N362ND",
            "instID": 12345678,
            "instIDCode": "JDOE",
            "cancelCutoffTime": "2024-03-06T10:15:00",
            "deleteAccess": False,
            "acftID": 15046639,
            "is_unavailable": True,
            "unavailability_reason": "Aircraft in Maintenance"
        },
        {
            "personID": "A3A977E2D2943574920DAA625073DF2009DFD5ECD48DE0500CF0607529DDF5EE9E5D7A1534689C2E58DD86539A8E402C0DF12127EF89BD94825F6B04B1D247F2931F1E299177EA7B4A922D4AE2DE3BDC9BA059B66634F3F92ECDFD1F1E349625F712146FD11FC10273CA773405560774",
            "stuschedKey": 19003907800,
            "custLastName": "Doe",
            "custFirstName": "John",
            "activityDate": "2024-03-08T14:15:00",
            "schedType": "UA",
            "course": 323,
            "lesson": 0,
            "instLastName": "Doe",
            "instFirstName": "Jane",
            "acftType": "ARCH",
            "observerLastName": 0,
            "observerFirstName": 0,
            "endDate": "2024-03-08T16:15:00",
            "regNum": "N362ND",
            "instID": 12345678,
            "instIDCode": "JDOE",
            "cancelCutoffTime": "2024-03-08T10:15:00",
            "deleteAccess": False,
            "acftID": 15046639,
            "is_unavailable": True,
            "unavailability_reason": "Aircraft in Maintenance"
        }
    ],
    "schedError": False,
    "schedErrMsg": ""
}

testOpenSlotsAnswer = [
    [
        {
            "year": "2024",
            "month": "03",
            "day": "03",
            "hour": "14",
            "minute": "45",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "03",
            "hour": "16",
            "minute": "45",
            "second": "00"
        },
        5,
        "Y"
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "03",
            "hour": "15",
            "minute": "00",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "03",
            "hour": "17",
            "minute": "00",
            "second": "00"
        },
        6,
        "Y"
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "04",
            "hour": "07",
            "minute": "00",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "04",
            "hour": "09",
            "minute": "00",
            "second": "00"
        },
        5,
        "Y"
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "06",
            "hour": "07",
            "minute": "00",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "06",
            "hour": "09",
            "minute": "00",
            "second": "00"
        },
        5,
        "Y"
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "06",
            "hour": "07",
            "minute": "15",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "06",
            "hour": "09",
            "minute": "15",
            "second": "00"
        },
        6,
        "Y"
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "07",
            "hour": "07",
            "minute": "00",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "07",
            "hour": "09",
            "minute": "00",
            "second": "00"
        },
        4,
        "Y"
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "07",
            "hour": "07",
            "minute": "15",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "07",
            "hour": "09",
            "minute": "15",
            "second": "00"
        },
        6,
        "Y"
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "08",
            "hour": "07",
            "minute": "00",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "08",
            "hour": "09",
            "minute": "00",
            "second": "00"
        },
        5,
        "Y"
    ]
]

testCurrentFLightSpotsAnswer = [
    [
        {
            "year": "2024",
            "month": "03",
            "day": "04",
            "hour": "14",
            "minute": "15",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "04",
            "hour": "16",
            "minute": "15",
            "second": "00"
        }
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "06",
            "hour": "14",
            "minute": "15",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "06",
            "hour": "16",
            "minute": "15",
            "second": "00"
        }
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "08",
            "hour": "14",
            "minute": "15",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "08",
            "hour": "16",
            "minute": "15",
            "second": "00"
        }
    ]
]

def test_ParseDateTime():
    parsedDate = CurrentFlightTimes.ParseDateTime(dateString='2024-03-07T08:30:01')
    assert parsedDate == {'year' : '2024', 'month' : '03', 'day' : '07', 'hour' : '08', 'minute' : '30', 'second' : '01'}

def test_GetOpenSlots():
    openSlots = CurrentFlightTimes.GetOpenSlots(data=data)
    assert openSlots == testOpenSlotsAnswer

def test_GetCurrentFlightSpots():
    currentFLightSpots = CurrentFlightTimes.GetCurrentFlightSpots(data=data)
    assert currentFLightSpots == testCurrentFLightSpotsAnswer


'''
test_ParseDateTime()
test_GetOpenSlots()
test_GetCurrentFlightSpots()
'''