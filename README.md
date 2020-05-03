# servorobot_controller
This repository acts as a controller for servo motors using Raspberry Pi.

## Hardware
The controller controls the servos using PCA9685 servo driver.

I2C setup needs to be enabled on Raspberry Pi.

## Library dependencies
In order to run the program, libraries for using servo with Raspberry Pi are needed.
- RPi.GPIO
- adafruit-blinka
- adafruit-circuitpython-pca9685
- adafruit-circuitpython-motor

For easy install run:
~~~
sudo pip3 install -r requirements.txt
sudo pip3 install -r ros_controller/requirements.txt
~~~
