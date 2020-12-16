import pigpio
import time

# set Trigger and Echo pin
TRIG_PIN = 17
ECHO_PIN = 27

# initialze Pi with pins
pi = pigpio.pi()
pi.set_mode(TRIG_PIN, pigpio.OUTPUT)
pi.set_mode(ECHO_PIN, pigpio.INPUT)

def distance():
    # this functions returns the distance from the ultrasonic sensor

    # send trigger pulse
    pi.write(TRIG_PIN, 1)
    time.sleep(0.00001)
    pi.write(TRIG_PIN, 0)

    start = time.time()
    stop = time.time()

    # listen for echo
    while pi.read(ECHO_PIN) == 0:
        pass
    start = time.time()
    while pi.read(ECHO_PIN) == 1:
        pass
    stop = time.time()
 
    distance = (stop - start) * 17150 # delta_t * speed of sound in air = 343 m/s, /2 two ways
    # TODO: why this offset?
    distance = round(distance - 515)
    return distance

