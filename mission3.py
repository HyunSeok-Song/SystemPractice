import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.OUT)

time.sleep(2)
GPIO.output(3, GPIO.HIGH)

start = time.time()
def Mycallback(channel):
	print("got it%d"% channel)

GPIO.add_event_detect(5, GPIO.RISING, callback=Mycallback, bouncetime=300)

while True:
	v = GPIO.input(5)
	if(v!=0):
		end = time.time()
		print(end-start)
		GPIO.output(3, GPIO.LOW)
		exit()
	print(v)
	
	time.sleep(1)

GPIO.cleanup()
