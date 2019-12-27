import time
import datetime
import RPi.GPIO as GPIO

m=0
n=-1
def sensorCallback(channel):
    timestamp=time.time()
    stamp=datetime.datetime.fromtimestamp(timestamp).strftime('%M:%H:%S')
    global n
    if GPIO.input(channel):
        print("Sensor HIGH"+stamp)
        n=n+1
        m=n*21.9915/5
        print(m)
    else:
        print("Sensor LOW"+stamp)
        n=n+1
        m=n*21.9915/5
        print(m)

def main():
    sensorCallback(17)
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17,GPIO.BOTH,callback=sensorCallback,bouncetime=200)

if __name__=='__main__':
    main()
