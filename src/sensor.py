import RPi.GPIO as GPIO


class GPIOSensor:
    def __init__(self, name: str, pin: int, out_mode: bool = False):
        self.pin = pin
        self.name = name
        self.prev_value = 0
        self.out_mode = out_mode
        self.setup_gpio()

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        if self.out_mode:
            GPIO.setup(self.pin, GPIO.OUT)
        else:
            GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.prev_value = GPIO.input(self.pin)

    def update_value(self, value):
        self.prev_value = self.get_value()
        GPIO.output(self.pin, value)

    def get_value(self):
        return GPIO.input(self.pin)
