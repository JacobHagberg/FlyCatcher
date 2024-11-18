# FlyCatcher
 UND AIMS Flight Reservation Tool

## Description
FlyCatcher is a python program used to simplify the flight slot acquisition process for the UND Aviation's AIMS (Aviation Information Management System).
FlyCatcher will constantly scrape the open flight stop data from AIMS, and check if there is an open flight slot. If a valid flight slot is found, the program will reserver the flight spot. 

## Table Of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#Features-and-Function)
- [KnownIssues](#known-issues)

## Installation

To use FlyCatcher, you will need to download python3 and download the src folder, and install necessary libraries. 

Dependencies: <br>
pytz: Time library for current time and timezone <br>
Install: pip3 install pytz <br>
secure-smtplib: Used for authentication and utilization of an SMTP mail server. <br>
Install: pip3 install secure-smtplib<br>

## Usage

To use FlyCatcher, you need to configure both the FlightScheduleSettings.json json file, and the FlightSchedulerConfig.ini configuration file. 
The FlightScheduleSettings.json specifies the desired flights to be reserved, and the FlightSchedulerConfig.ini file holds email info, AIMS account info, and path and timeouts. 

To configure the config file, simply read the comments for each entry and follow their directions. 

To specify what flight slots the program should sign up for, you need to edit the FlightScheduleSettings.json file. The structure of this json file is a list of dictionaries, where each dict is one flight to schedule. If you want to add a new flight, simply add a new dictionary to the list. 
Here is an example dictionary entry:

```json
{
    "AircraftType": "ARCH",
    "InstID": "",
    "StudentID": "1234567",
    "Course": 102,
    "Lesson": 30,
    "LaunchCount": 1,
    "ScheduleType": "TA",
    "Station": "D",
    "ObserverID": "",
    "ExcludeTimeBefore": "04:30",
    "ExcludeTimeAfter": "08:30",
    "CurrentTimeBuffer": "08:30",
    "EmailAlerts": [
        "john.doe@gmail.com"
    ],
    "FlightTimes": [
        [
            "11/18/2024 14:00:00",
            "11/18/2024 15:00:00"
        ],
        [
            "11/19/2024 11:00:00",
            "11/19/2024 13:30:00"
        ],
        [
            "11/20/2024 14:30:00",
            "11/20/2024 15:00:00"
        ],
        [
            "11/22/2024 08:00:00",
            "11/22/2024 14:30:00"
        ]
    ]
}
```

To set the details for the flight, you need to set the Aircraft type, course, lesson, launch count, ScheduleType, Station, ExcludeTimeBefore, ExcludeTimeAfter, CurrentTimeBuffer, and add a range of valid times for the flight. 
If this is a student account you are using, you need to add your student ID, and if it is a CFI account, you need to include your Instructor ID, and optionally the student ID should you want to assign the launch to a student. 
The EmailAlerts list is a list of strings, each one being an email address to send an email to should the program sign up for a flight. The settings for emails can be found in the FlightSchedulerConfig.ini file. 

ExcludeTimeBefore is the time in HH:MM preceding any activity on your AIMS schedule that will be viewed by the program as an invalid time for an open time slot. For example, if you have an activity at 12:00, with ExcludeTimeBefore set to 04:00, an open flight slot at 10:00 would not be reserved because it is within the exclusion time. 
ExcludeTimeAfter is very similar to ExcludeTimeBefore, except it is the time in HH:MM after an AIMS activity that will be excluded from the reservation of an open time slot. This ExcludeTimeBefore time is calculated at the end of the scheduled activity, where ExcludeTimeBefore is calculated from the start of the activity. 
With both ExcludeTimeBefore and ExcludeTimeAfter, this time range only will exclude an open flight slot if the start of it falls within the time exclusion range. 

CurrentTimeBuffer is used to exclude flights from being reserved that are too close to the current time. The time of CurrentTimeBuffer is added to the current time, and any open slot within that range is not considered valid, and will therefore be ignored.

One thing to note for ExcludeTimeBefore, ExcludeTimeAfter, and CurrentTimeBuffer, is that these times do not carry over to the next day, because the timing system, as of right now, doesn't account for that. 
For example, if CurrentTimeBuffer is set to 20:00, for 20 hours, and the current time is 18:00, a flight slot at 08:00 would be valid because it is on the following day, even through it is within 20 hours of the current time. This system also applies to ExcludeTimeBefore and ExcludeTimeAfter. 

To set time ranges for the flight, you must add a list to the list of flight times. Each sub list contains 2 strings, the first is the date and time for the start of the time range, and the second string is the date and time of the end of the time range.
The format for the time range is as follows: "MM/DD/YYYY HH:MM:SS". Every entry needs to be completed. You can add as many valid time slots as desired by simply adding another sub list. 

To configure FlyCatcher to be on the lookout for multiple flights, just add another flight dictionary to the list in the FlightScheduleSettings.json file. 

Once you have configured both the FlightScheduleSettings.json and the FlightSchedulerConfig.ini files, you can run the program by running the command python3 AimsFlightScheduler.py 

You are able to modify the FlightScheduleSettings.json file after starting the program. If you make a syntax mistake, it will inform you with the printout "Settings Dict Error." which will be replaced by "Looking for valid time slots." once the issue is resolved. 
Changes made to the FlightSchedulerConfig.ini will not take effect until the program is restarted. 

When a valid flight slot is found and reserved by FlyCatcher, a printout will be made with the slot details, and the flight will be removed from FlightScheduleSettings.json, and placed in AimsSignUpSuccessLog.json along with data about the chosen slot. 
This will create a log for the flights reserved by FlyCatcher.

Each flight must have the acftType, schedType, and station. These options are the same as they are in AIMS, and a full list can be found in Examples/AIMSFlightOptions.json.

Program Printouts:

"Looking for valid time slots."
Once running, you should see the printout, "Looking for valid time slots." along with a time stamp. This will be regularly printed to the terminal to show that the program is still running. 

"Cant get data from AIMS website."
This will be print out if FlyCatcher is unable to reach the AIMS website. If this happens, it is advisable to check your internet connection. 

"Get Aims Session Failed."
This prints if FlyCatcher attempts to get a logged in session in aims, and it fails. This can happen because of incorrect username or password, or because of faulty internet connection. 

"Flight Sign Up Unsuccessful."
If FlyCatcher finds a valid flight slot givin the rules set in the flight dict, and it attempts to reserve the flight but aims returns an error, this printout is made, and the program continues. 
This can occur if you have reached your maximum allowed flight slots for your account, or if the flight slot was taken in the time between FlyCatcher downloading the schedule data and sending the signup packet to the server. 

"Settings Dict Error."
If there is an issue in reading the FlightScheduleSettings.json file, FlyCatcher will print this and not proceed until the issue is resolved. 
Some issues may include improper use of json syntax, or improper formatting. Remember to close all [] and {}, and Remember that the JSON parser only views "" as a valid string, and not ''.


## Features and Function

Features:
1. Can reserve flights using the AIMS website.
2. Can filter out slots too close to other flights or slots that are too close to the current time.
3. Can send customizable email alerts to a list of emails, using an email account provided by the user to send the emails.
4. Will provide regular printouts to keep the user informed of the status of FlyCatcher.
5. Will keep a log of successful flight reservations. 

The Basic loop of FlyCatcher is as follows:

1. Make sure the AIMS session is valid.
2. Read the FlightScheduleSettings.json file.
3. Group the flights from FlightScheduleSettings.json into compatible groups to minimize data requests per loop. 
4. Go in order for each group, and get the flight slot data from AIMS, if a valid slot is found, proceed to signup.
5. If a slot is found, the necessary data is packaged into an http post packet, and sent to the AIMS website.
6. If the signup was successful, the flight slot is removed from the FlightScheduleSettings.json file, and placed in the AimsSignUpSuccessLog.json file. 
7. Emails are then crafted and sent using the email account provided. 
8. Regardless if a flight slot is reserved or not, the program loops back to step 1.


## Known issues:

1. ExcludeTimeBefore, ExcludeTimeAfter, and CurrentTimeBuffer do not carry over to the next day due to the time calculation method being used. This means that a time slot the following day will not be invalidated even if it is within the time of, for example: ExcludeTimeAfter.
2. If FlyCatcher finds a flight slot that it thinks is valid, but one that aims will not allow it to reserve, it will fall into a rut, and will keep trying to sign up for the flight slot it is unable to reserve. 
3. If you have an AIMS account that supports the sched-add-bypass feature, this feature is currently unsupported by FlyCatcher.