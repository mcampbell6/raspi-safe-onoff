import RPi.GPIO as GPIO
import time
import subprocess

pin = 29
cur_state = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    new_state = GPIO.input(pin)
    if new_state != cur_state and new_state == False:
        subprocess.call("init 0", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cur_state = new_state
    time.sleep(0.1)

#terminal:
#sudo crontab -e
#@reboot sh /home/pi/shutdown.sh >/home/pi/shutdown-logs/cronlog 2>&1
