import gpiozero
import time
import gpio_assignments


def wait_for_dog():
    if gpio_assignments.actuator_reversal.value == 0:
        gpio_assignments.power_supply.off()
        time.sleep(2)
        gpio_assignments.power_supply.on()


def close():
    gpio_assignments.power_supply.on()
    for waiting in range(120):
        gpio_assignments.pir_sensor.when_motion = wait_for_dog
        gpio_assignments.pir_sensor.when_motion = wait_for_dog
        time.sleep(0.1)
    gpio_assignments.power_supply.off()
    


def open():
    gpio_assignments.actuator_reversal.on()
    gpio_assignments.power_supply.on()
    time.sleep(10)
    gpio_assignments.power_supply.off()
    gpio_assignments.actuator_reversal.off()
    time.sleep(2)
    close()
