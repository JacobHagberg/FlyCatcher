#import sys
#sys.path.append('/Users/jacobhagberg/Documents/PythonCode/FlyCatcher/src/')
from src import AimsFlightScheduler

testSettingsData = [
    {
        "AircraftType": "SEMI",
        "InstID": "",
        "StudentID": "123456",
        "Course": 102,
        "Lesson": 30,
        "LaunchCount": 1,
        "ScheduleType": "TA",
        "Station": "D",
        "ObserverID": "",
        "ExcludeTimeBefore": "03:30",
        "ExcludeTimeAfter": "01:30",
        "CurrentTimeBuffer": "04:30",
        "EmailAlerts": [
            "12345@gmail.com"
        ],
        "FlightTimes": [
            [
                "06/03/2024 07:15:00",
                "06/03/2024 13:45:00"
            ],
            [
                "06/03/2024 15:15:00",
                "06/03/2024 17:45:00"
            ]
        ]
    },
    {
        "AircraftType": "ARCH",
        "InstID": "",
        "StudentID": "123456",
        "Course": 102,
        "Lesson": 30,
        "LaunchCount": 2,
        "ScheduleType": "TA",
        "Station": "D",
        "ObserverID": "",
        "ExcludeTimeBefore": "03:30",
        "ExcludeTimeAfter": "01:30",
        "CurrentTimeBuffer": "04:30",
        "EmailAlerts": [
            "12345@gmail.com"
        ],
        "FlightTimes": [
            [
                "06/03/2024 07:15:00",
                "06/03/2024 13:45:00"
            ],
            [
                "06/03/2024 15:15:00",
                "06/03/2024 17:45:00"
            ]
        ]
    },
    {
        "AircraftType": "SEMI",
        "InstID": "",
        "StudentID": "123456",
        "Course": 102,
        "Lesson": 30,
        "LaunchCount": 1,
        "ScheduleType": "TA",
        "Station": "D",
        "ObserverID": "",
        "ExcludeTimeBefore": "03:30",
        "ExcludeTimeAfter": "01:30",
        "CurrentTimeBuffer": "04:30",
        "EmailAlerts": [
            "12345@gmail.com"
        ],
        "FlightTimes": [
            [
                "06/03/2024 07:15:00",
                "06/03/2024 13:45:00"
            ],
            [
                "06/03/2024 15:15:00",
                "06/03/2024 17:45:00"
            ]
        ]
    },
    {
        "AircraftType": "ARCH",
        "InstID": "",
        "StudentID": "123456",
        "Course": 102,
        "Lesson": 30,
        "LaunchCount": 2,
        "ScheduleType": "TA",
        "Station": "D",
        "ObserverID": "",
        "ExcludeTimeBefore": "03:30",
        "ExcludeTimeAfter": "01:30",
        "CurrentTimeBuffer": "04:30",
        "EmailAlerts": [
            "12345@gmail.com"
        ],
        "FlightTimes": [
            [
                "06/03/2024 07:15:00",
                "06/03/2024 13:45:00"
            ],
            [
                "06/03/2024 15:15:00",
                "06/03/2024 17:45:00"
            ]
        ]
    },
    {
        "AircraftType": "ARCH",
        "InstID": "",
        "StudentID": "123456",
        "Course": 102,
        "Lesson": 30,
        "LaunchCount": 1,
        "ScheduleType": "TA",
        "Station": "D",
        "ObserverID": "",
        "ExcludeTimeBefore": "03:30",
        "ExcludeTimeAfter": "01:30",
        "CurrentTimeBuffer": "04:30",
        "EmailAlerts": [
            "12345@gmail.com"
        ],
        "FlightTimes": [
            [
                "06/03/2024 07:15:00",
                "06/03/2024 13:45:00"
            ],
            [
                "06/03/2024 15:15:00",
                "06/03/2024 17:45:00"
            ]
        ]
    },
    {
        "AircraftType": "ARCH",
        "InstID": "",
        "StudentID": "654321",
        "Course": 102,
        "Lesson": 30,
        "LaunchCount": 1,
        "ScheduleType": "TA",
        "Station": "D",
        "ObserverID": "",
        "ExcludeTimeBefore": "03:30",
        "ExcludeTimeAfter": "01:30",
        "CurrentTimeBuffer": "04:30",
        "EmailAlerts": [
            "12345@gmail.com"
        ],
        "FlightTimes": [
            [
                "06/03/2024 07:15:00",
                "06/03/2024 13:45:00"
            ],
            [
                "06/03/2024 15:15:00",
                "06/03/2024 17:45:00"
            ]
        ]
    },
    {
        "AircraftType": "ARCH",
        "InstID": "",
        "StudentID": "654321",
        "Course": 102,
        "Lesson": 30,
        "LaunchCount": 1,
        "ScheduleType": "TA",
        "Station": "D",
        "ObserverID": "",
        "ExcludeTimeBefore": "03:30",
        "ExcludeTimeAfter": "01:30",
        "CurrentTimeBuffer": "04:30",
        "EmailAlerts": [
            "12345@gmail.com"
        ],
        "FlightTimes": [
            [
                "06/03/2024 07:15:00",
                "06/03/2024 13:45:00"
            ],
            [
                "06/03/2024 15:15:00",
                "06/03/2024 17:45:00"
            ]
        ]
    },
    {
        "AircraftType": "ARCH",
        "InstID": "",
        "StudentID": "123456",
        "Course": 102,
        "Lesson": 30,
        "LaunchCount": 1,
        "ScheduleType": "TA",
        "Station": "D",
        "ObserverID": "",
        "ExcludeTimeBefore": "03:30",
        "ExcludeTimeAfter": "01:30",
        "CurrentTimeBuffer": "04:30",
        "EmailAlerts": [
            "12345@gmail.com"
        ],
        "FlightTimes": [
            [
                "06/03/2024 07:15:00",
                "06/03/2024 13:45:00"
            ],
            [
                "06/03/2024 15:15:00",
                "06/03/2024 17:45:00"
            ]
        ]
    }
]


testGroupSettingsDataAnswer = [
    [
        {
            "AircraftType": "SEMI",
            "InstID": "",
            "StudentID": "123456",
            "Course": 102,
            "Lesson": 30,
            "LaunchCount": 1,
            "ScheduleType": "TA",
            "Station": "D",
            "ObserverID": "",
            "ExcludeTimeBefore": "03:30",
            "ExcludeTimeAfter": "01:30",
            "CurrentTimeBuffer": "04:30",
            "EmailAlerts": [
                "12345@gmail.com"
            ],
            "FlightTimes": [
                [
                    "06/03/2024 07:15:00",
                    "06/03/2024 13:45:00"
                ],
                [
                    "06/03/2024 15:15:00",
                    "06/03/2024 17:45:00"
                ]
            ]
        },
        {
            "AircraftType": "SEMI",
            "InstID": "",
            "StudentID": "123456",
            "Course": 102,
            "Lesson": 30,
            "LaunchCount": 1,
            "ScheduleType": "TA",
            "Station": "D",
            "ObserverID": "",
            "ExcludeTimeBefore": "03:30",
            "ExcludeTimeAfter": "01:30",
            "CurrentTimeBuffer": "04:30",
            "EmailAlerts": [
                "12345@gmail.com"
            ],
            "FlightTimes": [
                [
                    "06/03/2024 07:15:00",
                    "06/03/2024 13:45:00"
                ],
                [
                    "06/03/2024 15:15:00",
                    "06/03/2024 17:45:00"
                ]
            ]
        }
    ],
    [
        {
            "AircraftType": "ARCH",
            "InstID": "",
            "StudentID": "123456",
            "Course": 102,
            "Lesson": 30,
            "LaunchCount": 2,
            "ScheduleType": "TA",
            "Station": "D",
            "ObserverID": "",
            "ExcludeTimeBefore": "03:30",
            "ExcludeTimeAfter": "01:30",
            "CurrentTimeBuffer": "04:30",
            "EmailAlerts": [
                "12345@gmail.com"
            ],
            "FlightTimes": [
                [
                    "06/03/2024 07:15:00",
                    "06/03/2024 13:45:00"
                ],
                [
                    "06/03/2024 15:15:00",
                    "06/03/2024 17:45:00"
                ]
            ]
        },
        {
            "AircraftType": "ARCH",
            "InstID": "",
            "StudentID": "123456",
            "Course": 102,
            "Lesson": 30,
            "LaunchCount": 2,
            "ScheduleType": "TA",
            "Station": "D",
            "ObserverID": "",
            "ExcludeTimeBefore": "03:30",
            "ExcludeTimeAfter": "01:30",
            "CurrentTimeBuffer": "04:30",
            "EmailAlerts": [
                "12345@gmail.com"
            ],
            "FlightTimes": [
                [
                    "06/03/2024 07:15:00",
                    "06/03/2024 13:45:00"
                ],
                [
                    "06/03/2024 15:15:00",
                    "06/03/2024 17:45:00"
                ]
            ]
        }
    ],
    [
        {
            "AircraftType": "ARCH",
            "InstID": "",
            "StudentID": "123456",
            "Course": 102,
            "Lesson": 30,
            "LaunchCount": 1,
            "ScheduleType": "TA",
            "Station": "D",
            "ObserverID": "",
            "ExcludeTimeBefore": "03:30",
            "ExcludeTimeAfter": "01:30",
            "CurrentTimeBuffer": "04:30",
            "EmailAlerts": [
                "12345@gmail.com"
            ],
            "FlightTimes": [
                [
                    "06/03/2024 07:15:00",
                    "06/03/2024 13:45:00"
                ],
                [
                    "06/03/2024 15:15:00",
                    "06/03/2024 17:45:00"
                ]
            ]
        },
        {
            "AircraftType": "ARCH",
            "InstID": "",
            "StudentID": "123456",
            "Course": 102,
            "Lesson": 30,
            "LaunchCount": 1,
            "ScheduleType": "TA",
            "Station": "D",
            "ObserverID": "",
            "ExcludeTimeBefore": "03:30",
            "ExcludeTimeAfter": "01:30",
            "CurrentTimeBuffer": "04:30",
            "EmailAlerts": [
                "12345@gmail.com"
            ],
            "FlightTimes": [
                [
                    "06/03/2024 07:15:00",
                    "06/03/2024 13:45:00"
                ],
                [
                    "06/03/2024 15:15:00",
                    "06/03/2024 17:45:00"
                ]
            ]
        }
    ],
    [
        {
            "AircraftType": "ARCH",
            "InstID": "",
            "StudentID": "654321",
            "Course": 102,
            "Lesson": 30,
            "LaunchCount": 1,
            "ScheduleType": "TA",
            "Station": "D",
            "ObserverID": "",
            "ExcludeTimeBefore": "03:30",
            "ExcludeTimeAfter": "01:30",
            "CurrentTimeBuffer": "04:30",
            "EmailAlerts": [
                "12345@gmail.com"
            ],
            "FlightTimes": [
                [
                    "06/03/2024 07:15:00",
                    "06/03/2024 13:45:00"
                ],
                [
                    "06/03/2024 15:15:00",
                    "06/03/2024 17:45:00"
                ]
            ]
        },
        {
            "AircraftType": "ARCH",
            "InstID": "",
            "StudentID": "654321",
            "Course": 102,
            "Lesson": 30,
            "LaunchCount": 1,
            "ScheduleType": "TA",
            "Station": "D",
            "ObserverID": "",
            "ExcludeTimeBefore": "03:30",
            "ExcludeTimeAfter": "01:30",
            "CurrentTimeBuffer": "04:30",
            "EmailAlerts": [
                "12345@gmail.com"
            ],
            "FlightTimes": [
                [
                    "06/03/2024 07:15:00",
                    "06/03/2024 13:45:00"
                ],
                [
                    "06/03/2024 15:15:00",
                    "06/03/2024 17:45:00"
                ]
            ]
        }
    ]
]



currentFlightSpots = [
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


openFlightSpots = [
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
            "hour": "12",
            "minute": "15",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "06",
            "hour": "14",
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
            "hour": "16",
            "minute": "15",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "08",
            "hour": "18",
            "minute": "15",
            "second": "00"
        },
        5,
        "Y"
    ],
    [
        {
            "year": "2024",
            "month": "03",
            "day": "08",
            "hour": "17",
            "minute": "15",
            "second": "00"
        },
        {
            "year": "2024",
            "month": "03",
            "day": "08",
            "hour": "19",
            "minute": "15",
            "second": "00"
        },
        5,
        "Y"
    ],
]




def test_GroupSettingsDict():
    result = AimsFlightScheduler.GroupSettingsDict(settings=testSettingsData)
    assert result == testGroupSettingsDataAnswer

def test_ParseSettingsDateTime():
    result = AimsFlightScheduler.ParseSettingsDateTime(dateTimeStr='05/09/2024 04:05:09')
    assert result == {'year': '2024', 'month': '05', 'day': '09', 'hour': '04', 'minute': '05', 'second': '09'}
    result = AimsFlightScheduler.ParseSettingsDateTime(dateTimeStr='11/12/2024 14:15:39')
    assert result == {'year': '2024', 'month': '11', 'day': '12', 'hour': '14', 'minute': '15', 'second': '39'}
    
def test_StrTimeToIntTime():
    result = AimsFlightScheduler.StrTimeToIntTime(time={'year': '2024', 'month': '05', 'day': '09', 'hour': '04', 'minute': '05', 'second': '09'})
    assert result == {'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9}

def test_IsTimeGreaterOrEqualToTime():
    #equal time check
    result = AimsFlightScheduler.IsTimeGreaterOrEqualToTime(checkTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9}, compareTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9})
    assert result == True
    #greater than time check
    result = AimsFlightScheduler.IsTimeGreaterOrEqualToTime(checkTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 6, 'second': 9}, compareTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9})
    assert result == True
    #less than time check
    result = AimsFlightScheduler.IsTimeGreaterOrEqualToTime(checkTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 3, 'second': 9}, compareTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9})
    assert result == False

def test_IsTimeLessOrEqualToTime():
    #equal time check
    result = AimsFlightScheduler.IsTimeLessOrEqualToTime(checkTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9}, compareTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9})
    assert result == True
    #greater than time check
    result = AimsFlightScheduler.IsTimeLessOrEqualToTime(checkTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 6, 'second': 9}, compareTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9})
    assert result == False
    #less than time check
    result = AimsFlightScheduler.IsTimeLessOrEqualToTime(checkTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 3, 'second': 9}, compareTime={'year': 2024, 'month': 5, 'day': 9, 'hour': 4, 'minute': 5, 'second': 9})
    assert result == True

def test_ParseBeforeAfterTime():
    result = AimsFlightScheduler.ParseBeforeAfterTime(time='12:11')
    assert result =={'hour': 12, 'minute': 11}
    result = AimsFlightScheduler.ParseBeforeAfterTime(time='03:09')
    assert result =={'hour': 3, 'minute': 9}
    result = AimsFlightScheduler.ParseBeforeAfterTime(time='1211')
    assert result == False
    

def test_GetUpdatedCurrentTimeSlots(): #add more edge cases
    timeSlots = [[{'year': '2024', 'month': '03', 'day': '04', 'hour': '14', 'minute': '15', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '04', 'hour': '16', 'minute': '15', 'second': '00'}], [{'year': '2024', 'month': '03', 'day': '04', 'hour': '12', 'minute': '00', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '04', 'hour': '14', 'minute': '00', 'second': '00'}]]
    result = AimsFlightScheduler.GetUpdatedCurrentTimeSlots(currentTimeSlots=timeSlots, excludeTimeBefore='03:30', excludeTimeAfter='01:56')
    assert result == [[{'year': 2024, 'month': 3, 'day': 4, 'hour': 10, 'minute': 45, 'second': 0}, {'year': 2024, 'month': 3, 'day': 4, 'hour': 18, 'minute': 11, 'second': 0}], [{'year': 2024, 'month': 3, 'day': 4, 'hour': 8, 'minute': 30, 'second': 0}, {'year': 2024, 'month': 3, 'day': 4, 'hour': 15, 'minute': 56, 'second': 0}]]    

def test_IsTimeInATimeSlot():
    result = AimsFlightScheduler.IsTimeInATimeSlot(time={'year': '2024', 'month': '03', 'day': '08', 'hour': '14', 'minute': '15', 'second': '00'}, timeSlots=[["03/07/2024 13:15:00", "03/09/2024 14:45:00"], ["03/010/2024 15:15:00", "03/12/2024 16:45:00"]])
    assert result == True
    result = AimsFlightScheduler.IsTimeInATimeSlot(time={'year': '2024', 'month': '03', 'day': '07', 'hour': '14', 'minute': '15', 'second': '00'}, timeSlots=[["03/07/2024 13:15:00", "03/09/2024 14:45:00"], ["03/010/2024 15:15:00", "03/12/2024 16:45:00"]])
    assert result == True
    result = AimsFlightScheduler.IsTimeInATimeSlot(time={'year': '2024', 'month': '03', 'day': '07', 'hour': '13', 'minute': '15', 'second': '00'}, timeSlots=[["03/07/2024 13:15:00", "03/09/2024 14:45:00"], ["03/010/2024 15:15:00", "03/12/2024 16:45:00"]])
    assert result == True
    result = AimsFlightScheduler.IsTimeInATimeSlot(time={'year': '2024', 'month': '03', 'day': '07', 'hour': '14', 'minute': '45', 'second': '00'}, timeSlots=[["03/07/2024 13:15:00", "03/09/2024 14:45:00"], ["03/010/2024 15:15:00", "03/12/2024 16:45:00"]])
    assert result == True
    result = AimsFlightScheduler.IsTimeInATimeSlot(time={'year': '2024', 'month': '03', 'day': '10', 'hour': '15', 'minute': '14', 'second': '00'}, timeSlots=[["03/07/2024 13:15:00", "03/09/2024 14:45:00"], ["03/010/2024 15:15:00", "03/12/2024 16:45:00"]])
    assert result == False
    result = AimsFlightScheduler.IsTimeInATimeSlot(time={'year': '2024', 'month': '03', 'day': '12', 'hour': '16', 'minute': '45', 'second': '01'}, timeSlots=[["03/07/2024 13:15:00", "03/09/2024 14:45:00"], ["03/010/2024 15:15:00", "03/12/2024 16:45:00"]])
    assert result == False

def test_FindFirstValidFlightSpot():
    validTimes = [["03/03/2024 07:15:00", "03/03/2024 13:45:00"], ["03/04/2024 15:15:00", "03/04/2024 17:45:00"], ["03/05/2024 15:15:00", "03/07/2024 17:45:00"]]
    result = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openFlightSpots, validTimes=validTimes, currentTimeSlots=currentFlightSpots, excludeTimeBefore='02:30', excludeTimeAfter='01:15', currentTimeBuffer='00:00')
    assert result == [{'year': '2024', 'month': '03', 'day': '06', 'hour': '07', 'minute': '00', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '06', 'hour': '09', 'minute': '00', 'second': '00'}, 5, 'Y']

    validTimes = [["03/03/2024 12:15:00", "03/03/2024 15:45:00"]]
    result = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openFlightSpots, validTimes=validTimes, currentTimeSlots=currentFlightSpots, excludeTimeBefore='01:30', excludeTimeAfter='01:15', currentTimeBuffer='00:00')
    assert result == [{'year': '2024', 'month': '03', 'day': '03', 'hour': '14', 'minute': '45', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '03', 'hour': '16', 'minute': '45', 'second': '00'}, 5, 'Y']

    validTimes = [["03/04/2024 12:15:00", "03/04/2024 15:45:00"]]#
    result = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openFlightSpots, validTimes=validTimes, currentTimeSlots=currentFlightSpots, excludeTimeBefore='01:30', excludeTimeAfter='01:15', currentTimeBuffer='00:00')
    assert result == False

    validTimes = [["03/06/2024 12:15:00", "03/06/2024 15:45:00"]]#
    result = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openFlightSpots, validTimes=validTimes, currentTimeSlots=currentFlightSpots, excludeTimeBefore='02:00', excludeTimeAfter='01:15', currentTimeBuffer='00:00')
    assert result == False

    validTimes = [["03/06/2024 12:15:00", "03/06/2024 15:45:00"]]#
    result = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openFlightSpots, validTimes=validTimes, currentTimeSlots=currentFlightSpots, excludeTimeBefore='01:59', excludeTimeAfter='01:15', currentTimeBuffer='00:00')
    assert result == [{'year': '2024', 'month': '03', 'day': '06', 'hour': '12', 'minute': '15', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '06', 'hour': '14', 'minute': '15', 'second': '00'}, 6, 'Y']

    validTimes = [["03/08/2024 12:15:00", "03/08/2024 16:45:00"]]#tests the exclude after time allowing for flight spots that are right after a flight
    result = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openFlightSpots, validTimes=validTimes, currentTimeSlots=currentFlightSpots, excludeTimeBefore='01:30', excludeTimeAfter='00:00', currentTimeBuffer='00:00')
    assert result == [{'year': '2024', 'month': '03', 'day': '08', 'hour': '16', 'minute': '15', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '08', 'hour': '18', 'minute': '15', 'second': '00'}, 5, 'Y']

    validTimes = [["03/08/2024 12:15:00", "03/08/2024 16:45:00"]] #tests the exclude after time 
    result = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openFlightSpots, validTimes=validTimes, currentTimeSlots=currentFlightSpots, excludeTimeBefore='01:30', excludeTimeAfter='00:01', currentTimeBuffer='00:00')
    assert result == False

    validTimes = [["03/08/2024 12:15:00", "03/08/2024 17:45:00"]] #tests the exclude after time 
    result = AimsFlightScheduler.FindFirstValidFlightSpot(openSlots=openFlightSpots, validTimes=validTimes, currentTimeSlots=currentFlightSpots, excludeTimeBefore='01:30', excludeTimeAfter='01:00', currentTimeBuffer='00:00')
    assert result == [{'year': '2024', 'month': '03', 'day': '08', 'hour': '17', 'minute': '15', 'second': '00'}, {'year': '2024', 'month': '03', 'day': '08', 'hour': '19', 'minute': '15', 'second': '00'}, 5, 'Y']


'''
test_GroupSettingsDict()
test_ParseSettingsDateTime()
test_StrTimeToIntTime()
test_IsTimeGreaterOrEqualToTime()
test_IsTimeLessOrEqualToTime()
test_ParseBeforeAfterTime()
test_GetUpdatedCurrentTimeSlots()
test_IsTimeInATimeSlot()
test_FindFirstValidFlightSpot()
'''