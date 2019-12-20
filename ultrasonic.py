import rospy
from std_msgs.msg import Int32MultiArray

class Ultrasonic:

	def __init__(self, topic):
		rospy.Subscriber(topic, Int32MultiArray, self.read_distance)
		self.properData = []

	def read_distance(self, data):
		self.properData = data.data

	def get_distance(self):
		print(self.properData)
		return self.properData
