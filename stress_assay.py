import RPi.GPIO as GPIO
import picamera
from time import sleep

ledGpio = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledGpio, GPIO.OUT)

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
    interval_real = interval - duration - 2
    for i inrange(n_times):
        GPIO.output(ledGpio, GPIO.HIGH)
        camera.start_preview()
        sleep(2)
        camera.start_recording(f"{i:02d}.h264")
        sleep(duration)
        camera.stop_recording()
        GPIO.output(ledGpio, GPIO.LOW)
        sleep(interval_real)


stress_assay(2, 20, 30)

GPIO.cleanup()