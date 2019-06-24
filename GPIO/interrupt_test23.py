#!/usr/bin/python3

# Test interrupts.

import select, time, sys

pin_base = '/sys/class/gpio/gpio23/'

def write_once(path, value):
    f = open(path, 'w')
    f.write(value)
    f.close()
    return


f = open(pin_base + 'value', 'r')

write_once(pin_base + 'direction', 'in')
write_once(pin_base + 'edge', 'both')

po = select.poll()
po.register(f, select.POLLPRI)

state_last = f.read(1)
t1 = time.time()
sys.stdout.write('Initial pin value = {}\n'.format(repr(state_last)))

while 1:
    events = po.poll(60000)
    t2 = time.time()
    f.seek(0)
    state_last = f.read(1)
    if len(events) == 0:
        sys.stdout.write('  timeout  delta = {:8.4f} seconds\n'.format(t2 - t1))
    else:
        sys.stdout.write('value = {}  delta ={:8.4f}\n'.format(state_last, t2 - t1))
        t1 = t2
