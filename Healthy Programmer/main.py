# Code From Mayur Pawar
# make programmer healthy throgh giving them remainder after several time
# take time from system
# play a music via pygame
# music not stop until user enter specific word (e.g Drunk water)
# after entering word timer will be restart
#  their are 3 activity for remaider
# 1.Drink Water - 40 min
# 2.Eye exercise - 25 min
# 3. Short Break  - 55 min
# Every Entry Save as a log file


from datetime import datetime
from pygame import mixer
from time import time

def playMusic(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while(1):
        userInput = input()
        if (userInput == stopper):
            mixer.music.stop()
            break

def logFile(msg):
    with open("record.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == "__main__":
    # playMusic("abc.mp3","STOP")
    initEye = time()
    initDrink = time()
    initExercise = time()

    timeEye = 1500
    timeDrink = 2400
    timeBreak = 3300

    while(1):
        if time() - initDrink > timeDrink:
            print("Alarm for Drink Water\tEnter 'stop' for Stop alarm")
            playMusic("abc.mp3","stop")
            initDrink = time()
            logFile("Drunk Water at : ")

        if time() - initExercise > timeBreak:
            print("Alarm for Short Break\tEnter 'stop' for Stop alarm")
            playMusic("abc.mp3","stop")
            initExercise = time()
            logFile("Short Break taken at : ")

        if time() - initEye > timeEye:
            print("Alarm for Eye Exercise\tEnter 'stop' for Stop alarm")
            playMusic("abc.mp3","stop")
            initEye = time()
            logFile("Eye Exercise done at : ")



