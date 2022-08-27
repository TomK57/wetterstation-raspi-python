#!/usr/bin/python3

import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()
from time import sleep

# address = 0x77 # Adafruit BMP180 address.

def read all():
    print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    print('Pressure = {0:0.2f} hPa'.format(sensor.read_pressure()/100))
    print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    sea_level_calc = ((sensor.read_pressure()/(1-(sensor.read_altitude()/44330))**5.255)/100)
    print('Sealevel Pressure = {0:0.2f} hPa'.format(sea_level_calc))
    sleep(1)
