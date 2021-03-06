#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import os
import pygame
GPIO.setmode(GPIO.BCM)

pygame.mixer.init()

def play_sound( theFile ):
	pygame.mixer.music.load( theFile)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy()  == True:
        	time.sleep(.04)


############### DEFINE SOUND SETS ###############
SOUND_SET = 1
NUMBER_OF_SOUND_SETS = 4

# SOUND SET 1
voices = [
     [ "/root/GPIO/DRUM/sounds/drum1.mp3",
            "/root/GPIO/DRUM/sounds/drum2.mp3",
            "/root/GPIO/DRUM/sounds/drum3.mp3",
            "/root/GPIO/DRUM/sounds/drum4.mp3"],
     ["/root/GPIO/DRUM/sounds/Flute1.mp3",
      "/root/GPIO/DRUM/sounds/Flute2.mp3",
      "/root/GPIO/DRUM/sounds/Flute3.mp3",
      "/root/GPIO/DRUM/sounds/Flute4.mp3"],
     ["/root/GPIO/DRUM/sounds/Soprano1.mp3",
      "/root/GPIO/DRUM/sounds/Soprano2.mp3",
      "/root/GPIO/DRUM/sounds/Soprano3.mp3",
      "/root/GPIO/DRUM/sounds/Soprano4.mp3"],
     ["/root/GPIO/DRUM/sounds/Viola1.mp3",
      "/root/GPIO/DRUM/sounds/Viola2.mp3",
      "/root/GPIO/DRUM/sounds/Viola3.mp3",
      "/root/GPIO/DRUM/sounds/Viola4.mp3"]
  ]
voice_bank = 0
# SOUND SET 2
DRUM1_SOUND2 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM2_SOUND2 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM3_SOUND2 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM4_SOUND2 = "/root/GPIO/DRUM/sounds/xxxx.mp3"

# SOUND SET 3
DRUM1_SOUND3 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM2_SOUND3 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM3_SOUND3 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM4_SOUND3 = "/root/GPIO/DRUM/sounds/xxxx.mp3"

# SOUND SET 4
DRUM1_SOUND4 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM2_SOUND4 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM3_SOUND4 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
DRUM4_SOUND4 = "/root/GPIO/DRUM/sounds/xxxx.mp3"
################################################

#### Define GPIO PINS for BUTTONS AND LEDS AND DEFAULT SOUND SET  ####
BUTTON1_PIN = 17
LED1_PIN = 18
#DRUM1_SOUND = DRUM1_SOUND1

BUTTON2_PIN = 22
LED2_PIN = 23
#DRUM2_SOUND = DRUM2_SOUND1

BUTTON3_PIN = 6 
LED3_PIN = 12 
#DRUM3_SOUND = DRUM3_SOUND1

BUTTON4_PIN = 19
LED4_PIN = 16
#DRUM4_SOUND = DRUM4_SOUND1
######################################################################

################## Put GPIO.setup Button / Toggle 5 in here #####################
BUTTON5_PIN = 26
LED5_PIN = 21 
##################################################################################

GPIO.setup(BUTTON1_PIN, GPIO.IN)
GPIO.setup(LED1_PIN, GPIO.OUT)

GPIO.setup(BUTTON2_PIN, GPIO.IN)
GPIO.setup(LED2_PIN, GPIO.OUT)

GPIO.setup(BUTTON3_PIN, GPIO.IN)
GPIO.setup(LED3_PIN, GPIO.OUT)

GPIO.setup(BUTTON4_PIN, GPIO.IN)
GPIO.setup(LED4_PIN, GPIO.OUT)

################## Put GPIO.setup Button / Toggle 5 in here #####################
GPIO.setup(BUTTON5_PIN, GPIO.IN)
GPIO.setup(LED5_PIN, GPIO.OUT)
#################################################################################

def DRUM1(BUTTON1_PIN):
	global voices
	global voice_bank
	print ("Button 1 Pressed!")
	if GPIO.input(BUTTON1_PIN):
    		print('Input was HIGH ')
	else:
    		print('Input was LOW' + str(voice_bank))
		GPIO.output(LED1_PIN, False)
		play_sound( voices[voice_bank][0] )
		GPIO.output(LED1_PIN, True)

def DRUM2(BUTTON2_PIN):
	print ("Button 2 Pressed!")
	if GPIO.input(BUTTON2_PIN):
    		print('Input was HIGH')
	else:
    		print('Input was LOW')
		GPIO.output(LED2_PIN, False)
		play_sound( voices[voice_bank][1] )
		GPIO.output(LED2_PIN, True)

def DRUM3(BUTTON3_PIN):
	print ("Button 3 Pressed!")
	if GPIO.input(BUTTON3_PIN):
    		print('Input was HIGH')
	else:
    		print('Input was LOW')
                GPIO.output(LED3_PIN, False)
                play_sound( voices[voice_bank][2] )
		GPIO.output(LED3_PIN, True)

def DRUM4(BUTTON4_PIN):
	print ("Button 4 Pressed!")
	if GPIO.input(BUTTON4_PIN):
    		print('Input was HIGH')
	else:
    		print('Input was LOW')

	GPIO.output(LED4_PIN, False)
	play_sound( voices[voice_bank][3] )
	GPIO.output(LED4_PIN, True)

################## Put Button / Toggle 5 main code in here #####################
def DRUM5(BUTTON5_PIN):
        global voice_bank
	print ("Button 5 Pressed!")
	print ("SOUND_SET: " + str( voice_bank + 1) )
	print ("NUMBER_OF_SOUND_SETS: " + str(NUMBER_OF_SOUND_SETS))

	if voice_bank == NUMBER_OF_SOUND_SETS-1:
		voice_bank = 0
	else:
		voice_bank = voice_bank + 1

#	DRUM1_SOUND = "DRUM1_SOUND" + str(SOUND_SET)
#	DRUM2_SOUND = "DRUM2_SOUND" + str(SOUND_SET)
#	DRUM3_SOUND = "DRUM3_SOUND" + str(SOUND_SET)
#	DRUM4_SOUND = "DRUM4_SOUND" + str(SOUND_SET)

#	print("SOUND SET: " + SOUND_SET)
#	print("DRUM1_SOUND: " + DRUM1_SOUND)
#	print("DRUM2_SOUND: " + DRUM1_SOUND)
#	print("DRUM3_SOUND: " + DRUM1_SOUND)
#	print("DRUM4_SOUND: " + DRUM1_SOUND)

#################################################################################

print "Drum Module Test (CTRL+C to exit)"

time.sleep(2)

GPIO.output(LED1_PIN, False)
time.sleep(0.2)
GPIO.output(LED2_PIN, False)
time.sleep(0.2)
GPIO.output(LED3_PIN, False)
time.sleep(0.2)
GPIO.output(LED4_PIN, False)
time.sleep(0.5)

################## Put GPIO.output LED 5 in here #####################
GPIO.output(LED5_PIN, False)
time.sleep(0.5)
#################################################################################

################## Put GPIO.output LED 5 in here #####################
GPIO.output(LED5_PIN, True)
time.sleep(0.2)
#################################################################################

GPIO.output(LED4_PIN, True)
time.sleep(0.2)
GPIO.output(LED3_PIN, True)
time.sleep(0.2)
GPIO.output(LED5_PIN, False)
time.sleep(0.5)
GPIO.output(LED2_PIN, True)
time.sleep(0.2)
GPIO.output(LED1_PIN, True)
time.sleep(0.5)


print "Ready"

try:
	GPIO.add_event_detect(BUTTON1_PIN, GPIO.FALLING, callback=DRUM1)
	GPIO.add_event_detect(BUTTON2_PIN, GPIO.FALLING, callback=DRUM2)
	GPIO.add_event_detect(BUTTON3_PIN, GPIO.FALLING, callback=DRUM3)
	GPIO.add_event_detect(BUTTON4_PIN, GPIO.FALLING, callback=DRUM4)

################## Put GPIO Event handling butoon 5 in here #####################
	GPIO.add_event_detect(BUTTON5_PIN, GPIO.FALLING, callback=DRUM5)
#################################################################################

	while 1:
		time.sleep(100)

except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()

