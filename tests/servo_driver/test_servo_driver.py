#!/usr/bin/env python
#
# Copyright (c) 2019, Dwindra Sulistyoutomo
#

import unittest
import time
import busio

from board import SCL, SDA              # import from adafruit_blinka
from adafruit_pca9685 import PCA9685    # import from adafruit-circuitpython-pca9685

from ...scripts.servo_driver.robot_servo import RobotServo


class TestRobotServo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        i2c = busio.I2C(SCL, SDA)

        # Create a simple PCA9685 class instance.
        pca = PCA9685(i2c)
        pca.frequency = 50

        # Test RobotServoclass
        cls.servo = RobotServo(pca.channels[0])

    def test_run(self):
        angle = 0
        for i in range(4):
            angle = angle + 22.5
            self.servo.setAngle(angle)
            print(self.servo.getAngle())

        time.sleep(2)
        for i in range(8):
            angle = angle - 22.5
            self.servo.setAngle(angle)
            print(self.servo.getAngle())

        time.sleep(2)
        for i in range(4):
            angle = angle + 22.5
            self.servo.setAngle(angle)
            print(self.servo.getAngle())


if __name__ == '__main__':
    unittest.main()
