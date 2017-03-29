import os
import glob
import time
import urllib2
import RPi.GPIO as GPIO

GREEN=13
RED=11

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

GPIO.output(GREEN, GPIO.LOW)
GPIO.output(RED, GPIO.LOW)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
	
while True:
	temp_c, temp_f = read_temp()
	if(24<= int(temp_c) and int(temp_c) < 28):
		GPIO.output(GREEN, GPIO.HIGH)
	elif(int(temp_c) >= 28):
		GPIO.output(GREEN, GPIO.LOW)
		GPIO.output(RED, GPIO.HIGH)
	print(read_temp())	
	time.sleep(10)

GPIO.cleanup()
