import datetime
from playsound import playsound
import time

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    alarm_hour, alarm_min = map(int, alarm_time.split(':'))
    alarm_am_pm = input("Enter 'am' or 'pm': ")

    if alarm_am_pm == "pm" and alarm_hour != 12:
        alarm_hour += 12
    elif alarm_am_pm == "am" and alarm_hour == 12:
        alarm_hour = 0

    return alarm_hour, alarm_min

def run_alarm_clock():
    alarm_hour, alarm_min = set_alarm()

    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_hour and now.minute == alarm_min:
            print("Alarm Time!")
            playsound("Tone.mp3")  
            break
        time.sleep(1)

run_alarm_clock()