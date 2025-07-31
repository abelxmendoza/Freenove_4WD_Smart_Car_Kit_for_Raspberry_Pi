# File: servo2.py

from PCA9685 import PCA9685
import time

class Servo:
    def __init__(self):
        self.PwmServo = PCA9685(0x40, debug=True)
        self.PwmServo.setPWMFreq(50)
        self.PwmServo.setServoPulse(8, 1500)
        self.PwmServo.setServoPulse(9, 1500)

    def setServoPwm(self, channel, angle, error=10):
        angle = int(angle)
        if channel == '0':
            self.PwmServo.setServoPulse(8, 2500 - int((angle + error) / 0.09))
        elif channel == '1':
            self.PwmServo.setServoPulse(9, 500 + int((angle + error) / 0.09))

if __name__ == '__main__':
    print("Sweeping servos on channels 0 and 1 from 0° to 180° and back.")
    pwm = Servo()
    try:
        while True:
            # Sweep from 0° to 180°
            for angle in range(0, 181, 5):
                pwm.setServoPwm('0', angle)
                pwm.setServoPwm('1', angle)
                time.sleep(0.03)
            # Sweep from 180° back to 0°
            for angle in range(180, -1, -5):
                pwm.setServoPwm('0', angle)
                pwm.setServoPwm('1', angle)
                time.sleep(0.03)
    except KeyboardInterrupt:
        print("\nEnd of sweep program.")
