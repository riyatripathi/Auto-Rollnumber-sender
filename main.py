import pyautogui
import time
from datetime import datetime

# roll -> your Roll Number
roll = "52010003"
# startTime -> Time at which you want to start sending roll number (24-hour notation)
startTime = "16:25:00"  
# delayAfterStart -> After 10sec(delayAfterStart) it will enter in the while loop and wait for the moment when the time will become equal to startTime
delayAfterStart = 10
time.sleep(delayAfterStart)
# spanOf -> want to send roll number in every 20 sec (spanOf)
spanOf = 20
while(1):
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(current_time)
	if current_time >= startTime:
		pyautogui.click(1455,836)
		pyautogui.typewrite(roll,interval = 0.5)
		pyautogui.click(1831,830)
		time.sleep(spanOf)
