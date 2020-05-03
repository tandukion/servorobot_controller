#!/usr/bin/env python
#
# Copyright (c) 2019, Dwindra Sulistyoutomo
#

import sys
from scripts.ros_controller.scripts.robot_logic_controller import RobotLogicController

try:
    import busio

    from board import SCL, SDA              # import from adafruit_blinka
    from adafruit_pca9685 import PCA9685    # import from adafruit-circuitpython-pca9685

    from scripts.servo_driver.robot_servo import RobotServo
except ImportError:
    print("Not using real board")


class ServoRobot:
    def __init__(self, sim=True, dof=6, home_pos=None):
        # Basic configuration
        self.robot_dof = dof
        self.home_pos = home_pos if home_pos else [0] * self.robot_dof

        # Add servo motor driver
        if not sim:
            i2c = busio.I2C(SCL, SDA)
            pca = PCA9685(i2c)
            pca.frequency = 50

            self.robot_servo = []
            for i in range(self.robot_dof):
                self.robot_servo.append(RobotServo(pca.channels[i]))
        else:
            self.robot_servo = None

        # Start the Robot Logic Controller
        self.robot_controller = RobotLogicController(dof=dof, home_pos=self.home_pos, robot_driver=self.robot_servo)


if __name__ == '__main__':
    sim = False
    # Accept argument for running simulation or real robot
    if len(sys.argv) > 1:
        if sys.argv[1] == "sim":
            sim = True
        else:
            sim = False

    robot = ServoRobot(sim=sim)
    while 1:
        continue
