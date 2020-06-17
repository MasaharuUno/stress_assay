# Import libraries
import RPi.GPIO as GPIO
import picamera
from time import sleep
from datetime import datetime

# Setup 
GPIO.setmode(GPIO.BCM)    # Set the GPIO pin name
ledGpio = 21    # GPIO pin for use
GPIO.setup(ledGpio, GPIO.OUT)    # Se the ledGpio in use

camera = picamera.PiCamera()

def stress_assay(n_times=10, duration=60, interval=60*60):
    """
    Shoot 'duratioin' seconds movies for 'n_times' times every 'interval' seconds
    and save every movie.

    Parameters:
    n_times -- int: number of times to shoot
    duration -- int: duration seconds of shooting
    interval -- int: interval seconds between shooting
    """
    interval_real = interval - duration - 2    # calculate real interval time
    for i in range(n_times):    # iterate for n_times
        now = datetime.now()    # get yime
        filename = strftime("%Y%m%d_%H:%M")    # make filename
        GPIO.output(ledGpio, GPIO.HIGH)    # Led on
        camera.start_preview()    # camera on for adjustment
        sleep(2)    # camera adjustment time
        camera.start_recording(f"{filename}_{i:02d}.h264")    # start shooting
        sleep(duration)    # shoot for 'duration' time
        camera.stop_recording()    # stop shooting
        camera.stop_preview()    # stop preview
        GPIO.output(ledGpio, GPIO.LOW)    # Led off
        sleep(interval_real)    # wait for interval time


stress_assay(2, 20, 30)

GPIO.cleanup()