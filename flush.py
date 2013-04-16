from quick2wire.gpio import pins, Out

pins = [pins.pin(i, Out) for i in range(8)]

for p in pins:
    p.close()