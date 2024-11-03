import pyautogui
import keyboard
import time
import datetime
import threading

press = False


def monitor_key_press():
    global press
    count = 0
    while press:
        if keyboard.is_pressed('space'):
            # press = False
            count+=1
            if count == 2:
                press = False
                print("Space bar pressed! Stopping the loop.")
        time.sleep(0.1)  # Small delay to avoid excessive CPU usage


def ClickNow(interval, lst):
    global press
    while not keyboard.is_pressed('space'):
        time.sleep(0.1)
        press = True
    if press:
        print("Started the Program")
        thread = threading.Thread(target=monitor_key_press)
        thread.start()
        while press:
            for j in lst:
                pyautogui.write(str(j), interval=0)
                pyautogui.press('enter')


def ClickWithStartStopTime(StartTime, StopTime, interval, lst):
    press = True
    current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    while current_time < StartTime:
        current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
        print(f"Waiting... Current time: {current_time}")
        time.sleep(0.5)
    # time.sleep(1)
    # current_time = StartTime
    if current_time == StartTime:
        pyautogui.click()
        while press:
            for j in lst:
                pyautogui.write(str(j))
                pyautogui.press('enter')
                current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
            if current_time == StopTime:
                press = False

    print("Current time equal Start Time")

def getCurrentTime():
    current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    return current_time




# datetime.time
# print(datetime.time(11,12,10))
# date_time = datetime.datetime.now()
# current_time = date_time.strftime("%H:%M:%S")
# print(current_time)


lst = [11,12,13,14,15]
startTime = datetime.time(20,29,50).strftime("%H:%M:%S")
stopTime = datetime.time(20,29,58).strftime("%H:%M:%S")
interval = 10
ClickWithStartStopTime(startTime, stopTime, interval, lst)

# current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
# print(current_time)

# lst = [6,7,8,9]
# interval = 10
# ClickNow(interval, lst)