#!/usr/bin/env python

import rospy, time

from properAngle import GetAngleSpeed
from motordrive import MotorDriver
from ultrasonic import Ultrasonic

class Main:

	def __init__(self):
		rospy.init_node('xycar_AD')
		self.ultrasonic = Ultrasonic('/ultrasonic')
		self.driver = MotorDriver('/xycar_motor_msg')
		self.saveSpeed = 90

	def runAway(self):
		angleSpeed = GetAngleSpeed(self.ultrasonic.get_distance())
		angle = angleSpeed["angle"]
		speed = angleSpeed["speed"]
		if angle == -1 and speed == -1:
			angle = 90
			speed = 90
			self.driver.drive(angle, speed)
			time.sleep(3)
			return
		if speed < 90 and self.saveSpeed >= 90:
			self.beforeStop()
		self.driver.drive(angle, speed)
		self.saveSpeed = speed

	def beforeStop(self):
		for _ in range(2):
			self.driver.drive(90, 90)
			time.sleep(0.1)
			self.driver.drive(90, 60)
			time.sleep(0.1)

if __name__ == "__main__":
	cat = Main()
	time.sleep(3)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		cat.runAway()
		rate.sleep()	