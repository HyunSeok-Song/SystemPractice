import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.LOW)

while(True):
	mode = int(input('Please Input Number : '))
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	if mode==0:
		GPIO.cleanup()
		exit()
	if mode==1:
		GPIO.output(13, GPIO.HIGH)
	if mode==2:
		GPIO.output(11, GPIO.HIGH)
	if mode==3:
		GPIO.output(15, GPIO.HIGH)
