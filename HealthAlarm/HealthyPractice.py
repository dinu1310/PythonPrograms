import pygame
from datetime import datetime
import time

EyeExercise = 1800  # Seconds --> Eye rest after every 30 minutes
PhyExercise = 2700  # Seconds  --> Body rest after every 45 minutes
TakeWater = 3000  # Seconds  --> Take water after every 50 minutes

""" Below list are created to store the time interval of each alarms and then current
    time will check in list and play alarm accordingly """

EyeL = []
PhyL = []
WatL = []
PreTotal = 9 * 60 * 60
for i in range(PreTotal, 61140, 1800):
    if i / 1800:
        EyeL.append(i)
for j in range(PreTotal, 61140, 2700):
    if j / 2700:
        PhyL.append(j)
for k in range(PreTotal, 61140, 3000):
    if k / 3000:
        WatL.append(k)

try:
    def AlarmM(MP3):
        while True:
            pygame.init()
            pygame.mixer.music.load(MP3)
            sound_obj = pygame.mixer.Sound(MP3)
            pygame.mixer.music.play(0)
            sound_obj.play()
            x = input("Have you done your Exercise Yes/No :")
            if x.lower() == "yes":
                log_time = time.asctime(time.localtime(time.time()))
                sound_obj.stop()
                return log_time
                exit()
            else:
                print("Then do it please.")
                sound_obj.stop()

    def log_report(filename, time_log):  # One can create single log file instead of multiple
        try:
            f = open(filename, "a")
            f.write(time_log)
            f.write("\n")
            f.close()
            return 0
        except:
            print("Please create log file manually")
except:
    print("Something went wrong")

evening = "17:00:00"
morning = "09:00:00"
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
if evening >= current_time >= morning:
    print("Welcome to your office, your personal health alarm at your service:")
    while evening >= current_time >= morning:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        hours = int(now.strftime("%H")) * 60 * 60
        minutes = int(now.strftime("%M")) * 60
        seconds = int(now.strftime("%S"))
        CurrentTotal_Seconds = hours + minutes + seconds

        if CurrentTotal_Seconds in EyeL:
            log = AlarmM("EyeAlarm.mp3")
            log_report("EyeLog.txt",f"Eye Exercise at {log}")

        if CurrentTotal_Seconds in PhyL:
            log = AlarmM("Workout.mp3")
            log_report("ExeLog.txt",f"Physical Exercise at {log}")

        if CurrentTotal_Seconds in WatL:
            log = AlarmM("Water.mp3")
            log_report("waterLog.txt",f"Water drank at {log}")
else:
    print("Currently no office time, Office time is 9 am tp 5 pm \n Thank you")