import RPi.GPIO as GPIO
import time

PIN = 11
PIN2 = 13
freq = 523

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)

voice = GPIO.PWM(PIN2, freq)

SOS = [1, 1, 1, 3, 3, 3, 1, 1, 1]

try:
    while True:
        for i in SOS:
            GPIO.output(PIN, GPIO.HIGH)
            voice.start(50)

            time.sleep(i * 0.1)

            voice.stop()
            GPIO.output(PIN, GPIO.LOW)

            time.sleep(0.2)

        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    voice.stop()
    GPIO.cleanup()