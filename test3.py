#!/usr/bin/env python3

from quick2wire.gpio import pins, In, Out, Both
from quick2wire.selector import Selector, Timer

button = pins.pin(0, direction=In, interrupt=Both)
led = pins.pin(1, direction=Out)

with button, led, \
     Timer(interval=0.5) as timer, \
     Selector() as selector:
    
    selector.add(button)
    selector.add(timer)
    
    print("ready")
    
    while True:
        selector.wait()
        
        if selector.ready == button:
            if button.value:
                led.value = 1
                timer.start()
            else:
                led.value = 0
                timer.stop()
        
        elif selector.ready == timer:
            timer.wait()
            led.value = not led.value