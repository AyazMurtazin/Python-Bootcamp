from random import randint
from time import sleep


def emit_gel(step):
    pressure = 50
    while True:
        sign = yield pressure
        pressure += sign * randint(0, step)
        pressure = 100 if pressure > 100 else pressure


def valve(gen: emit_gel):
    sign = 1
    pressure = next(gen)
    while True:
        pressure = gen.send(sign)
        if pressure < 10 or pressure > 90:
            print("!EMERGENCY BREAK!")
            gen.close()
            exit(0)
        elif pressure < 20 or pressure > 80:
            sign = -sign
        print(pressure)
        sleep(0.01)


gen = emit_gel(1)
valve(gen)
