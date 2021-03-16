from djitellopy import tello
import KeyPressModule as kp
from time import sleep, time
import cv2

kp.init()

me = tello.Tello()

me.connect()

print(me.get_battery())

# global img

me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 20
    updated = False

    if kp.getKey('LEFT'): 
        lr = -speed
        updated = True
    elif kp.getKey('RIGHT'): 
        lr = speed
        updated = True

    if kp.getKey('UP'): 
        fb = speed
        updated = True

    elif kp.getKey('DOWN'): 
        fb = -speed
        updated = True

    if kp.getKey('w'):
        ud = speed
        updated = True
    elif kp.getKey('s'): 
        ud = -speed
        updated = True

    if kp.getKey('a'):
        yv = -speed
        updated = True
    elif kp.getKey('d'): 
        yv = speed
        updated = True

    if kp.getKey('q'): 
        me.land()
        sleep(3)
        updated = True

    if kp.getKey('e'): 
        me.takeoff()
        updated = True

    if kp.getKey('z'):
        img = me.get_frame_read().frame
        cv2.imwrite(f'{time()}.jpg', img)
        sleep(0.3)
        updated = True

    return ([lr, fb, ud, yv], updated)

while True:

    (vals, updated) = getKeyboardInput()

    if updated:
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    # img = me.get_frame_read().frame

    # img = cv2.resize(img, (360, 240))
    # sleep(0.05)
    # sleep(0.2)