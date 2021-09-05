#!/usr/bin/env python3
import RPi.GPIO as GPIO
import dht22
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# 14番ピンをセット
instance = dht22.DHT22(pin=14)

# 値の取得に失敗することがあるので、2秒インターバルで5回ループする
count = 0
while count < 5:
    result = instance.read()
    if result.is_valid():
        msg = u"{0:0.1f}℃ {1:0.1f}％".format(result.temperature, result.humidity)
        count = 9999
    else:
        msg = "err"
        count += 1
        time.sleep(2)

# make html
f = open('index.html', 'w')
f.write('<!DOCTYPE html><html><meta charset="UTF-8"><body>\n')
f.write(msg + "\n")
f.write(str(datetime.datetime.now()) + "\n")
f.write("</body></html>\n")
f.close()

# cleanup GPIO
GPIO.cleanup()
