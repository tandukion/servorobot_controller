#!/usr/bin/env python
#
# Copyright (c) 2019, Dwindra Sulistyoutomo
#

import unittest
import time
import busio

from board import SCL, SDA
# https://github.com/adafruit/Adafruit_CircuitPython_Motor
from adafruit_motor import servo
# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685


class TestPCA6985(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        i2c = busio.I2C(SCL, SDA)

        # Create a simple PCA9685 class instance.
        cls.pca = PCA9685(i2c)
        cls.pca.frequency = 50

        cls.servo = servo.Servo(cls.pca.channels[0], min_pulse=500, max_pulse=2500)

    def test_pca_6985(self):
        for i in range(180):
            self.servo.angle = i

        time.sleep(2)
        for i in range(180):
            self.servo.angle = 180 - i

        self.pca.deinit()


if __name__ == '__main__':
    unittest.main()



