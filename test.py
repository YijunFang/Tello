###################################
# Note: below is using public djitellopy library with python intepretor Python 3.7.3.
# Resources: 
# https://djitellopy.readthedocs.io/en/latest/tello/
# https://github.com/damiafuentes/DJITelloPy
###################################
# Extra Side note: 
# My understanding: Some of the APIs defined in the public interface are only used with a joy stick.

###################################
################################### Preparation ###################################


from djitellopy import *
import cv2
from time import sleep

me = Tello()
me.connect()
print(me.get_battery())
me.takeoff()

################################### Lession 1 ###################################

#Section 2 First flight
# me = Tello()
# me.connect()
# print(me.get_battery())

# me.takeoff()
# print("Tello took off")
# me.land()


# Section 3 Movement
# me = Tello()
# me.connect()
# me.takeoff()

# # Note: send_rc_control(..) accepts a speed change, and the distance changes depending on how long program sleeps. 
# # dist = vel * time
# me.send_rc_control(50, 0, 0, 0) #  Move right 
# sleep(2)

# me.send_rc_control(0, 50, 0, 0) #  Move forward 
# sleep(2)

# me.send_rc_control(0, 0, 50, 0) #  Move up 
# sleep(2)

# me.send_rc_control(0, 0, 0, 30) #  yaw
# sleep(2)

# me.send_rc_control(0, 0, 0, 0)
# me.land()

################################### Lession 2 ###################################

# Section 2: TOF sensor / variable
# result = me.get_distance_tof()
# print("Distance tof: ", result)

# Section 3: TOF sensor / loop
# for i in range(100):
# 	result = me.get_distance_tof()
# 	print(result)

# Section 4: TOF sensor / if statements (some simple ones would be enough)
# if something...:
# 	me.flip_forward()

# Section 5: Activity: Move & Search
# # To be implemented


################################### Extra ###################################

me.streamon()
frame_read = me.get_frame_read()

me.takeoff()
cv2.imwrite("picture.png", frame_read.frame)
################################### Finish ###################################

me.land()




