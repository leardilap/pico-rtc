#!/usr/bin/python
# -*- coding: utf-8 -*-
from ds3231 import *
from machine import Pin

#led = Pin(25, Pin.OUT)
relay = Pin(19, Pin.OUT)

rtc = ds3231(I2C_PORT,I2C_SCL,I2C_SDA)

#rtc.read_time()

hour = rtc.read_hour()
#minute = rtc.read_minute()

# after 23:30 and before 7 am turn the relay ON to disable the main light and have only the blue light
# 0x23 = 35
# 0x30 = 48
if (hour >= 1 and hour <= 5): 
#    led.on()
    relay.on()
else:
#    led.off()
    relay.off()


